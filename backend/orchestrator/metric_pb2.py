# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metric.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metric.proto',
  package='orchestrator',
  syntax='proto3',
  serialized_options=b'Z\'github.com/owkin/orchestrator/lib/asset',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmetric.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\xd8\x02\n\x06Metric\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x19.orchestrator.Addressable\x12*\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12.\n\x0bpermissions\x18\x06 \x01(\x0b\x32\x19.orchestrator.Permissions\x12\r\n\x05owner\x18\x07 \x01(\t\x12\x31\n\rcreation_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x08metadata\x18\x12 \x03(\x0b\x32\".orchestrator.Metric.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa3\x02\n\tNewMetric\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x19.orchestrator.Addressable\x12*\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12\x35\n\x0fnew_permissions\x18\x06 \x01(\x0b\x32\x1c.orchestrator.NewPermissions\x12\x37\n\x08metadata\x18\x12 \x03(\x0b\x32%.orchestrator.NewMetric.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1d\n\x0eGetMetricParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"V\n\x14QueryMetricsResponse\x12%\n\x07metrics\x18\x01 \x03(\x0b\x32\x14.orchestrator.Metric\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\":\n\x11QueryMetricsParam\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r2\xe6\x01\n\rMetricService\x12?\n\x0eRegisterMetric\x12\x17.orchestrator.NewMetric\x1a\x14.orchestrator.Metric\x12?\n\tGetMetric\x12\x1c.orchestrator.GetMetricParam\x1a\x14.orchestrator.Metric\x12S\n\x0cQueryMetrics\x12\x1f.orchestrator.QueryMetricsParam\x1a\".orchestrator.QueryMetricsResponseB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])




_METRIC_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='orchestrator.Metric.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.Metric.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='orchestrator.Metric.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=422,
)

_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='orchestrator.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.Metric.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='orchestrator.Metric.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='orchestrator.Metric.description', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='orchestrator.Metric.address', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='orchestrator.Metric.permissions', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='orchestrator.Metric.owner', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='orchestrator.Metric.creation_date', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='orchestrator.Metric.metadata', index=7,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_METRIC_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=422,
)


_NEWMETRIC_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='orchestrator.NewMetric.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewMetric.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='orchestrator.NewMetric.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=422,
)

_NEWMETRIC = _descriptor.Descriptor(
  name='NewMetric',
  full_name='orchestrator.NewMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewMetric.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='orchestrator.NewMetric.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='orchestrator.NewMetric.description', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='orchestrator.NewMetric.address', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_permissions', full_name='orchestrator.NewMetric.new_permissions', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='orchestrator.NewMetric.metadata', index=5,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NEWMETRIC_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=716,
)


_GETMETRICPARAM = _descriptor.Descriptor(
  name='GetMetricParam',
  full_name='orchestrator.GetMetricParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.GetMetricParam.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=747,
)


_QUERYMETRICSRESPONSE = _descriptor.Descriptor(
  name='QueryMetricsResponse',
  full_name='orchestrator.QueryMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='orchestrator.QueryMetricsResponse.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='orchestrator.QueryMetricsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=749,
  serialized_end=835,
)


_QUERYMETRICSPARAM = _descriptor.Descriptor(
  name='QueryMetricsParam',
  full_name='orchestrator.QueryMetricsParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_token', full_name='orchestrator.QueryMetricsParam.page_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='orchestrator.QueryMetricsParam.page_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=837,
  serialized_end=895,
)

_METRIC_METADATAENTRY.containing_type = _METRIC
_METRIC.fields_by_name['description'].message_type = common__pb2._ADDRESSABLE
_METRIC.fields_by_name['address'].message_type = common__pb2._ADDRESSABLE
_METRIC.fields_by_name['permissions'].message_type = common__pb2._PERMISSIONS
_METRIC.fields_by_name['creation_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METRIC.fields_by_name['metadata'].message_type = _METRIC_METADATAENTRY
_NEWMETRIC_METADATAENTRY.containing_type = _NEWMETRIC
_NEWMETRIC.fields_by_name['description'].message_type = common__pb2._ADDRESSABLE
_NEWMETRIC.fields_by_name['address'].message_type = common__pb2._ADDRESSABLE
_NEWMETRIC.fields_by_name['new_permissions'].message_type = common__pb2._NEWPERMISSIONS
_NEWMETRIC.fields_by_name['metadata'].message_type = _NEWMETRIC_METADATAENTRY
_QUERYMETRICSRESPONSE.fields_by_name['metrics'].message_type = _METRIC
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['NewMetric'] = _NEWMETRIC
DESCRIPTOR.message_types_by_name['GetMetricParam'] = _GETMETRICPARAM
DESCRIPTOR.message_types_by_name['QueryMetricsResponse'] = _QUERYMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['QueryMetricsParam'] = _QUERYMETRICSPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _METRIC_METADATAENTRY,
    '__module__' : 'metric_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.Metric.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'metric_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.Metric)
  })
_sym_db.RegisterMessage(Metric)
_sym_db.RegisterMessage(Metric.MetadataEntry)

NewMetric = _reflection.GeneratedProtocolMessageType('NewMetric', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWMETRIC_METADATAENTRY,
    '__module__' : 'metric_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewMetric.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _NEWMETRIC,
  '__module__' : 'metric_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewMetric)
  })
_sym_db.RegisterMessage(NewMetric)
_sym_db.RegisterMessage(NewMetric.MetadataEntry)

GetMetricParam = _reflection.GeneratedProtocolMessageType('GetMetricParam', (_message.Message,), {
  'DESCRIPTOR' : _GETMETRICPARAM,
  '__module__' : 'metric_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetMetricParam)
  })
_sym_db.RegisterMessage(GetMetricParam)

QueryMetricsResponse = _reflection.GeneratedProtocolMessageType('QueryMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMETRICSRESPONSE,
  '__module__' : 'metric_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryMetricsResponse)
  })
_sym_db.RegisterMessage(QueryMetricsResponse)

QueryMetricsParam = _reflection.GeneratedProtocolMessageType('QueryMetricsParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYMETRICSPARAM,
  '__module__' : 'metric_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryMetricsParam)
  })
_sym_db.RegisterMessage(QueryMetricsParam)


DESCRIPTOR._options = None
_METRIC_METADATAENTRY._options = None
_NEWMETRIC_METADATAENTRY._options = None

_METRICSERVICE = _descriptor.ServiceDescriptor(
  name='MetricService',
  full_name='orchestrator.MetricService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=898,
  serialized_end=1128,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterMetric',
    full_name='orchestrator.MetricService.RegisterMetric',
    index=0,
    containing_service=None,
    input_type=_NEWMETRIC,
    output_type=_METRIC,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMetric',
    full_name='orchestrator.MetricService.GetMetric',
    index=1,
    containing_service=None,
    input_type=_GETMETRICPARAM,
    output_type=_METRIC,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryMetrics',
    full_name='orchestrator.MetricService.QueryMetrics',
    index=2,
    containing_service=None,
    input_type=_QUERYMETRICSPARAM,
    output_type=_QUERYMETRICSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_METRICSERVICE)

DESCRIPTOR.services_by_name['MetricService'] = _METRICSERVICE

# @@protoc_insertion_point(module_scope)