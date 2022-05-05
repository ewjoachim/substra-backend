import json
from collections import defaultdict
from urllib.parse import unquote

import structlog
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

from substrapp import exceptions

logger = structlog.get_logger(__name__)


def get_filters(query_params):
    """
    Transform user request search param in filters.
        - Logical AND is represented by a comma `,`
        - Logical OR is represented by `-OR-`
        - But comma used for the same field is equivalent to `IN`

    >>> get_filters("algo:name:algo1")
    [
        {
            "algo": {
                "name": ["algo1"],
            },
        },
    ]

    >>> get_filters("algo:name:algo1,algo:owner:owner1")
    [
        {
            "algo": {
                "name": ["algo1"],
                "owner": ["owner1"],
            },
        },
    ]

    >>> get_filters("algo:name:algo1,algo:name:algo2")
    [
        {
            "algo": {
                "name": ["algo1", "algo2"],
            },
        },
    ]

    >>> get_filters("algo:name:algo1-OR-algo:owner:owner1")
    [
        {
            "algo": {
                "name": ["algo1"],
            },
        },
        {
            "algo": {
                "owner": ["owner1"],
            },
        },
    ]

    """
    filters = []
    for or_params in query_params.split("-OR-"):
        or_filters = {}
        for and_params in or_params.split(","):
            asset, field, value = unquote(and_params).split(":")
            if asset not in or_filters:
                or_filters[asset] = defaultdict(list)
            or_filters[asset][field].append(value)
        filters.append(or_filters)
    return json.loads(json.dumps(filters))  # convert default dict to dict


def filter_queryset(object_type, queryset, query_params, mapping_callback=None):
    """
    Filter django model queryset by user request search param.
    Provide a `mapping_callback` to customize filter key and/or values.

    >>> filter_queryset("algo", Algo.objects, "algo:name:algo1")
    Algo.objects.filter(Q(name="algo1"))

    >>> filter_queryset("algo", Algo.objects, "algo:name:algo1,algo:owner:owner1")
    Algo.objects.filter(Q(name="algo1") & Q(owner="owner1"))

    >>> filter_queryset("algo", Algo.objects, "algo:name:algo1,algo:name:algo2")
    Algo.objects.filter(name__in=[algo1", "algo_2"])

    >>> filter_queryset("algo", Algo.objects, "algo:name:algo1-OR-algo:owner:owner1")
    Algo.objects.filter(Q(name="algo1") | Q(owner="owner1"))

    >>> def map_category(key, values):
    ...     if key == "category":
    ...         values = [algo_pb2.AlgoCategory.Value(value) for value in values]
    ...     return key, values

    >>> filter_queryset("algo", Algo.objects, "algo:category:ALGO_SIMPLE", map_category)
    Algo.objects.filter(Q(category=1))

    """
    try:
        filters = get_filters(query_params)
    except Exception:
        raise exceptions.BadRequestError(f"Malformed search filters: invalid syntax: {query_params}")

    or_params = None
    for or_filter in filters:
        and_params = None
        if set(or_filter.keys()) != {object_type}:
            raise exceptions.BadRequestError(f"Malformed search filters: invalid syntax: {query_params}")
        for key, values in or_filter[object_type].items():
            if mapping_callback is not None:
                key, values = mapping_callback(key, values)
            # handle multi-values
            if len(values) == 1:
                param = Q(**{key: values[0]})
            else:
                param = Q(**{f"{key}__in": values})
            and_params = param if and_params is None else and_params & param
        or_params = and_params if or_params is None else or_params | and_params

    try:
        return queryset.filter(or_params)
    except ValidationError:
        raise exceptions.BadRequestError(f"Malformed search filters: invalid syntax: {query_params}")


class CustomSearchFilter(BaseFilterBackend):
    """Bridge to use our custom filtering system with django_filters.

    You must set the custom_search_object_type attr or a get_custom_search_object_type method on the view that uses it.

    You can set a custom_search_mapping_callback attr on the view that uses it.

    It should be removed soon when we abandon them for the default filter implementation
    """

    def filter_queryset(self, request, queryset, view):
        # object type
        if hasattr(view, "custom_search_object_type"):
            object_type = view.custom_search_object_type
        elif hasattr(view, "get_custom_search_object_type"):
            object_type = view.get_custom_search_object_type()
        else:
            raise Exception("Missing configuration")

        # mapping callback
        mapping_callback = getattr(view, "custom_search_mapping_callback", None)
        if mapping_callback:
            # filter_queryset expects a callback with signature (key: str, values: str[]) -> (str, str[])
            # However mapping_callback is a bound method instance.
            # It wraps the function underneath and automatically injects the class instance as first argument (self)
            # What we need to pass to filter_queryset is therefore the function underneath itself, without the wrapping
            mapping_callback = mapping_callback.__func__

        # apply filters to queryset
        query_params = request.query_params.get("search")
        if query_params is not None:
            queryset = filter_queryset(object_type, queryset, query_params, mapping_callback)
        return queryset


class PermissionFilter(BaseFilterBackend):
    """Filter assets who can be used by a given set of nodes"""

    def get_param(self):
        try:
            return self.param
        except AttributeError:
            raise NotImplementedError("Missing param definition")

    def get_field(self):
        try:
            return self.field
        except AttributeError:
            raise NotImplementedError("Missing field definition")

    def get_node_ids(self, request):
        params = request.query_params.get(self.get_param())
        if params:
            node_ids = [param.strip() for param in params.split(",")]
            return node_ids
        return []

    def filter_queryset(self, request, queryset, view):
        node_ids = self.get_node_ids(request)
        if node_ids:
            is_public = Q(**{f"{self.get_field()}_public": True})
            is_authorized = Q(**{f"{self.get_field()}_authorized_ids__contains": node_ids})
            queryset = queryset.filter(is_public | is_authorized)
        return queryset


class ProcessPermissionFilter(PermissionFilter):
    param = "can_process"
    field = "permissions_process"


class LogsPermissionFilter(PermissionFilter):
    param = "can_access_logs"
    field = "logs_permission"
