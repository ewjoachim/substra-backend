"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _EventKind:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _EventKindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EventKind.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    EVENT_UNKNOWN: EventKind.ValueType = ...  # 0
    EVENT_ASSET_CREATED: EventKind.ValueType = ...  # 1
    EVENT_ASSET_UPDATED: EventKind.ValueType = ...  # 2
    EVENT_ASSET_DISABLED: EventKind.ValueType = ...  # 3
class EventKind(_EventKind, metaclass=_EventKindEnumTypeWrapper):
    pass

EVENT_UNKNOWN: EventKind.ValueType = ...  # 0
EVENT_ASSET_CREATED: EventKind.ValueType = ...  # 1
EVENT_ASSET_UPDATED: EventKind.ValueType = ...  # 2
EVENT_ASSET_DISABLED: EventKind.ValueType = ...  # 3
global___EventKind = EventKind


class Event(google.protobuf.message.Message):
    """Event is an occurence of an orchestration event.
    It is triggered during orchestration and allows a consumer to react to the orchestration process.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    ASSET_KEY_FIELD_NUMBER: builtins.int
    ASSET_KIND_FIELD_NUMBER: builtins.int
    EVENT_KIND_FIELD_NUMBER: builtins.int
    CHANNEL_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    asset_key: typing.Text = ...
    asset_kind: common_pb2.AssetKind.ValueType = ...
    event_kind: global___EventKind.ValueType = ...
    channel: typing.Text = ...
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        asset_key : typing.Text = ...,
        asset_kind : common_pb2.AssetKind.ValueType = ...,
        event_kind : global___EventKind.ValueType = ...,
        channel : typing.Text = ...,
        timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        metadata : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp",b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_key",b"asset_key","asset_kind",b"asset_kind","channel",b"channel","event_kind",b"event_kind","id",b"id","metadata",b"metadata","timestamp",b"timestamp"]) -> None: ...
global___Event = Event

class QueryEventsParam(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    SORT_FIELD_NUMBER: builtins.int
    page_token: typing.Text = ...
    page_size: builtins.int = ...
    @property
    def filter(self) -> global___EventQueryFilter: ...
    sort: common_pb2.SortOrder.ValueType = ...
    def __init__(self,
        *,
        page_token : typing.Text = ...,
        page_size : builtins.int = ...,
        filter : typing.Optional[global___EventQueryFilter] = ...,
        sort : common_pb2.SortOrder.ValueType = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["filter",b"filter"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["filter",b"filter","page_size",b"page_size","page_token",b"page_token","sort",b"sort"]) -> None: ...
global___QueryEventsParam = QueryEventsParam

class EventQueryFilter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    ASSET_KEY_FIELD_NUMBER: builtins.int
    ASSET_KIND_FIELD_NUMBER: builtins.int
    EVENT_KIND_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    asset_key: typing.Text = ...
    asset_kind: common_pb2.AssetKind.ValueType = ...
    event_kind: global___EventKind.ValueType = ...
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    @property
    def start(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """timestamp inclusive lower bound"""
        pass
    @property
    def end(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """timestamp inclusive upper bound"""
        pass
    def __init__(self,
        *,
        asset_key : typing.Text = ...,
        asset_kind : common_pb2.AssetKind.ValueType = ...,
        event_kind : global___EventKind.ValueType = ...,
        metadata : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        start : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end",b"end","start",b"start"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_key",b"asset_key","asset_kind",b"asset_kind","end",b"end","event_kind",b"event_kind","metadata",b"metadata","start",b"start"]) -> None: ...
global___EventQueryFilter = EventQueryFilter

class QueryEventsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EVENTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Event]: ...
    next_page_token: typing.Text = ...
    def __init__(self,
        *,
        events : typing.Optional[typing.Iterable[global___Event]] = ...,
        next_page_token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["events",b"events","next_page_token",b"next_page_token"]) -> None: ...
global___QueryEventsResponse = QueryEventsResponse