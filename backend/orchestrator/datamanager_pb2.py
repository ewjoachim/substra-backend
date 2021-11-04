# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datamanager.proto
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
  name='datamanager.proto',
  package='orchestrator',
  syntax='proto3',
  serialized_options=b'Z\'github.com/owkin/orchestrator/lib/asset',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x64\x61tamanager.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\xef\x02\n\x0b\x44\x61taManager\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12.\n\x0bpermissions\x18\x04 \x01(\x0b\x32\x19.orchestrator.Permissions\x12.\n\x0b\x64\x65scription\x18\x06 \x01(\x0b\x32\x19.orchestrator.Addressable\x12)\n\x06opener\x18\x07 \x01(\x0b\x32\x19.orchestrator.Addressable\x12\x0c\n\x04type\x18\x08 \x01(\t\x12\x31\n\rcreation_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x08metadata\x18\x10 \x03(\x0b\x32\'.orchestrator.DataManager.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x02\n\x0eNewDataManager\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x35\n\x0fnew_permissions\x18\x03 \x01(\x0b\x32\x1c.orchestrator.NewPermissions\x12.\n\x0b\x64\x65scription\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12)\n\x06opener\x18\x06 \x01(\x0b\x32\x19.orchestrator.Addressable\x12\x0c\n\x04type\x18\x07 \x01(\t\x12<\n\x08metadata\x18\x10 \x03(\x0b\x32*.orchestrator.NewDataManager.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\"\n\x13GetDataManagerParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"?\n\x16QueryDataManagersParam\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r\"f\n\x19QueryDataManagersResponse\x12\x30\n\rdata_managers\x18\x01 \x03(\x0b\x32\x19.orchestrator.DataManager\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x98\x02\n\x12\x44\x61taManagerService\x12N\n\x13RegisterDataManager\x12\x1c.orchestrator.NewDataManager\x1a\x19.orchestrator.DataManager\x12N\n\x0eGetDataManager\x12!.orchestrator.GetDataManagerParam\x1a\x19.orchestrator.DataManager\x12\x62\n\x11QueryDataManagers\x12$.orchestrator.QueryDataManagersParam\x1a\'.orchestrator.QueryDataManagersResponseB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])




_DATAMANAGER_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='orchestrator.DataManager.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.DataManager.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='orchestrator.DataManager.MetadataEntry.value', index=1,
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
  serialized_start=403,
  serialized_end=450,
)

_DATAMANAGER = _descriptor.Descriptor(
  name='DataManager',
  full_name='orchestrator.DataManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.DataManager.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='orchestrator.DataManager.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='orchestrator.DataManager.owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='orchestrator.DataManager.permissions', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='orchestrator.DataManager.description', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opener', full_name='orchestrator.DataManager.opener', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='orchestrator.DataManager.type', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='orchestrator.DataManager.creation_date', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='orchestrator.DataManager.metadata', index=8,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATAMANAGER_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=450,
)


_NEWDATAMANAGER_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='orchestrator.NewDataManager.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewDataManager.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='orchestrator.NewDataManager.MetadataEntry.value', index=1,
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
  serialized_start=403,
  serialized_end=450,
)

_NEWDATAMANAGER = _descriptor.Descriptor(
  name='NewDataManager',
  full_name='orchestrator.NewDataManager',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewDataManager.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='orchestrator.NewDataManager.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_permissions', full_name='orchestrator.NewDataManager.new_permissions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='orchestrator.NewDataManager.description', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opener', full_name='orchestrator.NewDataManager.opener', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='orchestrator.NewDataManager.type', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='orchestrator.NewDataManager.metadata', index=6,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NEWDATAMANAGER_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=767,
)


_GETDATAMANAGERPARAM = _descriptor.Descriptor(
  name='GetDataManagerParam',
  full_name='orchestrator.GetDataManagerParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.GetDataManagerParam.key', index=0,
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
  serialized_start=769,
  serialized_end=803,
)


_QUERYDATAMANAGERSPARAM = _descriptor.Descriptor(
  name='QueryDataManagersParam',
  full_name='orchestrator.QueryDataManagersParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_token', full_name='orchestrator.QueryDataManagersParam.page_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='orchestrator.QueryDataManagersParam.page_size', index=1,
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
  serialized_start=805,
  serialized_end=868,
)


_QUERYDATAMANAGERSRESPONSE = _descriptor.Descriptor(
  name='QueryDataManagersResponse',
  full_name='orchestrator.QueryDataManagersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_managers', full_name='orchestrator.QueryDataManagersResponse.data_managers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='orchestrator.QueryDataManagersResponse.next_page_token', index=1,
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
  serialized_start=870,
  serialized_end=972,
)

_DATAMANAGER_METADATAENTRY.containing_type = _DATAMANAGER
_DATAMANAGER.fields_by_name['permissions'].message_type = common__pb2._PERMISSIONS
_DATAMANAGER.fields_by_name['description'].message_type = common__pb2._ADDRESSABLE
_DATAMANAGER.fields_by_name['opener'].message_type = common__pb2._ADDRESSABLE
_DATAMANAGER.fields_by_name['creation_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATAMANAGER.fields_by_name['metadata'].message_type = _DATAMANAGER_METADATAENTRY
_NEWDATAMANAGER_METADATAENTRY.containing_type = _NEWDATAMANAGER
_NEWDATAMANAGER.fields_by_name['new_permissions'].message_type = common__pb2._NEWPERMISSIONS
_NEWDATAMANAGER.fields_by_name['description'].message_type = common__pb2._ADDRESSABLE
_NEWDATAMANAGER.fields_by_name['opener'].message_type = common__pb2._ADDRESSABLE
_NEWDATAMANAGER.fields_by_name['metadata'].message_type = _NEWDATAMANAGER_METADATAENTRY
_QUERYDATAMANAGERSRESPONSE.fields_by_name['data_managers'].message_type = _DATAMANAGER
DESCRIPTOR.message_types_by_name['DataManager'] = _DATAMANAGER
DESCRIPTOR.message_types_by_name['NewDataManager'] = _NEWDATAMANAGER
DESCRIPTOR.message_types_by_name['GetDataManagerParam'] = _GETDATAMANAGERPARAM
DESCRIPTOR.message_types_by_name['QueryDataManagersParam'] = _QUERYDATAMANAGERSPARAM
DESCRIPTOR.message_types_by_name['QueryDataManagersResponse'] = _QUERYDATAMANAGERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataManager = _reflection.GeneratedProtocolMessageType('DataManager', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATAMANAGER_METADATAENTRY,
    '__module__' : 'datamanager_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.DataManager.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _DATAMANAGER,
  '__module__' : 'datamanager_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.DataManager)
  })
_sym_db.RegisterMessage(DataManager)
_sym_db.RegisterMessage(DataManager.MetadataEntry)

NewDataManager = _reflection.GeneratedProtocolMessageType('NewDataManager', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWDATAMANAGER_METADATAENTRY,
    '__module__' : 'datamanager_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewDataManager.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _NEWDATAMANAGER,
  '__module__' : 'datamanager_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewDataManager)
  })
_sym_db.RegisterMessage(NewDataManager)
_sym_db.RegisterMessage(NewDataManager.MetadataEntry)

GetDataManagerParam = _reflection.GeneratedProtocolMessageType('GetDataManagerParam', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAMANAGERPARAM,
  '__module__' : 'datamanager_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetDataManagerParam)
  })
_sym_db.RegisterMessage(GetDataManagerParam)

QueryDataManagersParam = _reflection.GeneratedProtocolMessageType('QueryDataManagersParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDATAMANAGERSPARAM,
  '__module__' : 'datamanager_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryDataManagersParam)
  })
_sym_db.RegisterMessage(QueryDataManagersParam)

QueryDataManagersResponse = _reflection.GeneratedProtocolMessageType('QueryDataManagersResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDATAMANAGERSRESPONSE,
  '__module__' : 'datamanager_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryDataManagersResponse)
  })
_sym_db.RegisterMessage(QueryDataManagersResponse)


DESCRIPTOR._options = None
_DATAMANAGER_METADATAENTRY._options = None
_NEWDATAMANAGER_METADATAENTRY._options = None

_DATAMANAGERSERVICE = _descriptor.ServiceDescriptor(
  name='DataManagerService',
  full_name='orchestrator.DataManagerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=975,
  serialized_end=1255,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterDataManager',
    full_name='orchestrator.DataManagerService.RegisterDataManager',
    index=0,
    containing_service=None,
    input_type=_NEWDATAMANAGER,
    output_type=_DATAMANAGER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDataManager',
    full_name='orchestrator.DataManagerService.GetDataManager',
    index=1,
    containing_service=None,
    input_type=_GETDATAMANAGERPARAM,
    output_type=_DATAMANAGER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryDataManagers',
    full_name='orchestrator.DataManagerService.QueryDataManagers',
    index=2,
    containing_service=None,
    input_type=_QUERYDATAMANAGERSPARAM,
    output_type=_QUERYDATAMANAGERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAMANAGERSERVICE)

DESCRIPTOR.services_by_name['DataManagerService'] = _DATAMANAGERSERVICE

# @@protoc_insertion_point(module_scope)