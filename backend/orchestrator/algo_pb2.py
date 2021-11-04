# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: algo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='algo.proto',
  package='orchestrator',
  syntax='proto3',
  serialized_options=b'Z\'github.com/owkin/orchestrator/lib/asset',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nalgo.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\x84\x03\n\x04\x41lgo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x1a.orchestrator.AlgoCategory\x12.\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x19.orchestrator.Addressable\x12,\n\talgorithm\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12.\n\x0bpermissions\x18\x06 \x01(\x0b\x32\x19.orchestrator.Permissions\x12\r\n\x05owner\x18\x07 \x01(\t\x12\x31\n\rcreation_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x08metadata\x18\x10 \x03(\x0b\x32 .orchestrator.Algo.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcf\x02\n\x07NewAlgo\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12,\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x1a.orchestrator.AlgoCategory\x12.\n\x0b\x64\x65scription\x18\x04 \x01(\x0b\x32\x19.orchestrator.Addressable\x12,\n\talgorithm\x18\x05 \x01(\x0b\x32\x19.orchestrator.Addressable\x12\x35\n\x0fnew_permissions\x18\x06 \x01(\x0b\x32\x1c.orchestrator.NewPermissions\x12\x35\n\x08metadata\x18\x11 \x03(\x0b\x32#.orchestrator.NewAlgo.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1b\n\x0cGetAlgoParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"P\n\x12QueryAlgosResponse\x12!\n\x05\x41lgos\x18\x01 \x03(\x0b\x32\x12.orchestrator.Algo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"Y\n\x0f\x41lgoQueryFilter\x12,\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x1a.orchestrator.AlgoCategory\x12\x18\n\x10\x63ompute_plan_key\x18\x02 \x01(\t\"g\n\x0fQueryAlgosParam\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r\x12-\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x1d.orchestrator.AlgoQueryFilter*Y\n\x0c\x41lgoCategory\x12\x10\n\x0c\x41LGO_UNKNOWN\x10\x00\x12\x0f\n\x0b\x41LGO_SIMPLE\x10\x01\x12\x12\n\x0e\x41LGO_AGGREGATE\x10\x02\x12\x12\n\x0e\x41LGO_COMPOSITE\x10\x03\x32\xd2\x01\n\x0b\x41lgoService\x12\x39\n\x0cRegisterAlgo\x12\x15.orchestrator.NewAlgo\x1a\x12.orchestrator.Algo\x12\x39\n\x07GetAlgo\x12\x1a.orchestrator.GetAlgoParam\x1a\x12.orchestrator.Algo\x12M\n\nQueryAlgos\x12\x1d.orchestrator.QueryAlgosParam\x1a .orchestrator.QueryAlgosResponseB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])

_ALGOCATEGORY = _descriptor.EnumDescriptor(
  name='AlgoCategory',
  full_name='orchestrator.AlgoCategory',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALGO_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALGO_SIMPLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALGO_AGGREGATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALGO_COMPOSITE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1111,
  serialized_end=1200,
)
_sym_db.RegisterEnumDescriptor(_ALGOCATEGORY)

AlgoCategory = enum_type_wrapper.EnumTypeWrapper(_ALGOCATEGORY)
ALGO_UNKNOWN = 0
ALGO_SIMPLE = 1
ALGO_AGGREGATE = 2
ALGO_COMPOSITE = 3



_ALGO_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='orchestrator.Algo.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.Algo.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='orchestrator.Algo.MetadataEntry.value', index=1,
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
  serialized_start=417,
  serialized_end=464,
)

_ALGO = _descriptor.Descriptor(
  name='Algo',
  full_name='orchestrator.Algo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.Algo.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='orchestrator.Algo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='orchestrator.Algo.category', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='orchestrator.Algo.description', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='orchestrator.Algo.algorithm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='orchestrator.Algo.permissions', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='orchestrator.Algo.owner', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='orchestrator.Algo.creation_date', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='orchestrator.Algo.metadata', index=8,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ALGO_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=464,
)


_NEWALGO_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='orchestrator.NewAlgo.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewAlgo.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='orchestrator.NewAlgo.MetadataEntry.value', index=1,
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
  serialized_start=417,
  serialized_end=464,
)

_NEWALGO = _descriptor.Descriptor(
  name='NewAlgo',
  full_name='orchestrator.NewAlgo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewAlgo.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='orchestrator.NewAlgo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='orchestrator.NewAlgo.category', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='orchestrator.NewAlgo.description', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='orchestrator.NewAlgo.algorithm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_permissions', full_name='orchestrator.NewAlgo.new_permissions', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='orchestrator.NewAlgo.metadata', index=6,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NEWALGO_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=802,
)


_GETALGOPARAM = _descriptor.Descriptor(
  name='GetAlgoParam',
  full_name='orchestrator.GetAlgoParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.GetAlgoParam.key', index=0,
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
  serialized_start=804,
  serialized_end=831,
)


_QUERYALGOSRESPONSE = _descriptor.Descriptor(
  name='QueryAlgosResponse',
  full_name='orchestrator.QueryAlgosResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Algos', full_name='orchestrator.QueryAlgosResponse.Algos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='orchestrator.QueryAlgosResponse.next_page_token', index=1,
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
  serialized_start=833,
  serialized_end=913,
)


_ALGOQUERYFILTER = _descriptor.Descriptor(
  name='AlgoQueryFilter',
  full_name='orchestrator.AlgoQueryFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='orchestrator.AlgoQueryFilter.category', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compute_plan_key', full_name='orchestrator.AlgoQueryFilter.compute_plan_key', index=1,
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
  serialized_start=915,
  serialized_end=1004,
)


_QUERYALGOSPARAM = _descriptor.Descriptor(
  name='QueryAlgosParam',
  full_name='orchestrator.QueryAlgosParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_token', full_name='orchestrator.QueryAlgosParam.page_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='orchestrator.QueryAlgosParam.page_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='orchestrator.QueryAlgosParam.filter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1006,
  serialized_end=1109,
)

_ALGO_METADATAENTRY.containing_type = _ALGO
_ALGO.fields_by_name['category'].enum_type = _ALGOCATEGORY
_ALGO.fields_by_name['description'].message_type = common__pb2._ADDRESSABLE
_ALGO.fields_by_name['algorithm'].message_type = common__pb2._ADDRESSABLE
_ALGO.fields_by_name['permissions'].message_type = common__pb2._PERMISSIONS
_ALGO.fields_by_name['creation_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ALGO.fields_by_name['metadata'].message_type = _ALGO_METADATAENTRY
_NEWALGO_METADATAENTRY.containing_type = _NEWALGO
_NEWALGO.fields_by_name['category'].enum_type = _ALGOCATEGORY
_NEWALGO.fields_by_name['description'].message_type = common__pb2._ADDRESSABLE
_NEWALGO.fields_by_name['algorithm'].message_type = common__pb2._ADDRESSABLE
_NEWALGO.fields_by_name['new_permissions'].message_type = common__pb2._NEWPERMISSIONS
_NEWALGO.fields_by_name['metadata'].message_type = _NEWALGO_METADATAENTRY
_QUERYALGOSRESPONSE.fields_by_name['Algos'].message_type = _ALGO
_ALGOQUERYFILTER.fields_by_name['category'].enum_type = _ALGOCATEGORY
_QUERYALGOSPARAM.fields_by_name['filter'].message_type = _ALGOQUERYFILTER
DESCRIPTOR.message_types_by_name['Algo'] = _ALGO
DESCRIPTOR.message_types_by_name['NewAlgo'] = _NEWALGO
DESCRIPTOR.message_types_by_name['GetAlgoParam'] = _GETALGOPARAM
DESCRIPTOR.message_types_by_name['QueryAlgosResponse'] = _QUERYALGOSRESPONSE
DESCRIPTOR.message_types_by_name['AlgoQueryFilter'] = _ALGOQUERYFILTER
DESCRIPTOR.message_types_by_name['QueryAlgosParam'] = _QUERYALGOSPARAM
DESCRIPTOR.enum_types_by_name['AlgoCategory'] = _ALGOCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Algo = _reflection.GeneratedProtocolMessageType('Algo', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ALGO_METADATAENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.Algo.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _ALGO,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.Algo)
  })
_sym_db.RegisterMessage(Algo)
_sym_db.RegisterMessage(Algo.MetadataEntry)

NewAlgo = _reflection.GeneratedProtocolMessageType('NewAlgo', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWALGO_METADATAENTRY,
    '__module__' : 'algo_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewAlgo.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _NEWALGO,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewAlgo)
  })
_sym_db.RegisterMessage(NewAlgo)
_sym_db.RegisterMessage(NewAlgo.MetadataEntry)

GetAlgoParam = _reflection.GeneratedProtocolMessageType('GetAlgoParam', (_message.Message,), {
  'DESCRIPTOR' : _GETALGOPARAM,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetAlgoParam)
  })
_sym_db.RegisterMessage(GetAlgoParam)

QueryAlgosResponse = _reflection.GeneratedProtocolMessageType('QueryAlgosResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALGOSRESPONSE,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryAlgosResponse)
  })
_sym_db.RegisterMessage(QueryAlgosResponse)

AlgoQueryFilter = _reflection.GeneratedProtocolMessageType('AlgoQueryFilter', (_message.Message,), {
  'DESCRIPTOR' : _ALGOQUERYFILTER,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.AlgoQueryFilter)
  })
_sym_db.RegisterMessage(AlgoQueryFilter)

QueryAlgosParam = _reflection.GeneratedProtocolMessageType('QueryAlgosParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALGOSPARAM,
  '__module__' : 'algo_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryAlgosParam)
  })
_sym_db.RegisterMessage(QueryAlgosParam)


DESCRIPTOR._options = None
_ALGO_METADATAENTRY._options = None
_NEWALGO_METADATAENTRY._options = None

_ALGOSERVICE = _descriptor.ServiceDescriptor(
  name='AlgoService',
  full_name='orchestrator.AlgoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1203,
  serialized_end=1413,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterAlgo',
    full_name='orchestrator.AlgoService.RegisterAlgo',
    index=0,
    containing_service=None,
    input_type=_NEWALGO,
    output_type=_ALGO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAlgo',
    full_name='orchestrator.AlgoService.GetAlgo',
    index=1,
    containing_service=None,
    input_type=_GETALGOPARAM,
    output_type=_ALGO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryAlgos',
    full_name='orchestrator.AlgoService.QueryAlgos',
    index=2,
    containing_service=None,
    input_type=_QUERYALGOSPARAM,
    output_type=_QUERYALGOSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ALGOSERVICE)

DESCRIPTOR.services_by_name['AlgoService'] = _ALGOSERVICE

# @@protoc_insertion_point(module_scope)