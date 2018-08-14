from django.db import IntegrityError
from django.http import Http404
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from substrapp.conf import conf
from substrapp.models import Model
from substrapp.serializers import ModelSerializer, LedgerChallengeSerializer

# from hfc.fabric import Client
# cli = Client(net_profile="../network.json")
from substrapp.utils import queryLedger
from substrapp.views.utils import get_filters


class ModelViewSet(mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        # can modify result by interrogating `request.version`

        # using chu-nantes as in our testing owkin has been revoked
        org = conf['orgs']['chu-nantes']
        peer = org['peers'][0]

        data, st = queryLedger({
            'org': org,
            'peer': peer,
            'args': '{"Args":["queryModels"]}'
        })

        # parse filters
        query_params = request.query_params.get('search', None)
        l = [data]
        if query_params is not None:
            try:
                filters = get_filters(query_params)
            except Exception as exc:
                raise Response(
                    {'message': 'Malformed search filters %(query_params)s' % {'query_params': query_params}},
                    status=status.HTTP_400_BAD_REQUEST)
            else:
                # filtering, reinit l to empty array
                l = []
                for idx, filter in enumerate(filters):
                    # init each list iteration to data
                    l.append(data)
                    for k, subfilters in filter.items():
                        if k == 'model':  # filter by own key
                            for key, val in subfilters.items():
                                l[idx] = [x for x in l[idx] if x['endModel']['hash'] in val]

        return Response(l, status=st)


    # TODO create traintuples list related to model