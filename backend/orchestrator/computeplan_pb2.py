# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: computeplan.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='computeplan.proto',
  package='orchestrator',
  syntax='proto3',
  serialized_options=b'Z\'github.com/owkin/orchestrator/lib/asset',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x63omputeplan.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc0\x03\n\x0b\x43omputePlan\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x15\n\rwaiting_count\x18\x08 \x01(\r\x12\x12\n\ntodo_count\x18\t \x01(\r\x12\x13\n\x0b\x64oing_count\x18\n \x01(\r\x12\x16\n\x0e\x63\x61nceled_count\x18\x0b \x01(\r\x12\x14\n\x0c\x66\x61iled_count\x18\x0c \x01(\r\x12\x12\n\ndone_count\x18\x03 \x01(\r\x12\x12\n\ntask_count\x18\x04 \x01(\r\x12/\n\x06status\x18\x05 \x01(\x0e\x32\x1f.orchestrator.ComputePlanStatus\x12\"\n\x1a\x64\x65lete_intermediary_models\x18\x06 \x01(\x08\x12\x31\n\rcreation_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0b\n\x03tag\x18\x10 \x01(\t\x12\x39\n\x08metadata\x18\x11 \x03(\x0b\x32\'.orchestrator.ComputePlan.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbd\x01\n\x0eNewComputePlan\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x10 \x01(\t\x12<\n\x08metadata\x18\x11 \x03(\x0b\x32*.orchestrator.NewComputePlan.MetadataEntry\x12\"\n\x1a\x64\x65lete_intermediary_models\x18\x12 \x01(\x08\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\"\n\x13GetComputePlanParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"T\n\x14\x41pplyPlanActionParam\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x1f.orchestrator.ComputePlanAction\"\x19\n\x17\x41pplyPlanActionResponse\"8\n\x0fQueryPlansParam\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r\"W\n\x12QueryPlansResponse\x12(\n\x05plans\x18\x01 \x03(\x0b\x32\x19.orchestrator.ComputePlan\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\xba\x01\n\x11\x43omputePlanStatus\x12\x17\n\x13PLAN_STATUS_UNKNOWN\x10\x00\x12\x17\n\x13PLAN_STATUS_WAITING\x10\x01\x12\x14\n\x10PLAN_STATUS_TODO\x10\x02\x12\x15\n\x11PLAN_STATUS_DOING\x10\x03\x12\x14\n\x10PLAN_STATUS_DONE\x10\x04\x12\x18\n\x14PLAN_STATUS_CANCELED\x10\x05\x12\x16\n\x12PLAN_STATUS_FAILED\x10\x06*F\n\x11\x43omputePlanAction\x12\x17\n\x13PLAN_ACTION_UNKNOWN\x10\x00\x12\x18\n\x14PLAN_ACTION_CANCELED\x10\x01\x32\xd3\x02\n\x12\x43omputePlanService\x12G\n\x0cRegisterPlan\x12\x1c.orchestrator.NewComputePlan\x1a\x19.orchestrator.ComputePlan\x12G\n\x07GetPlan\x12!.orchestrator.GetComputePlanParam\x1a\x19.orchestrator.ComputePlan\x12\\\n\x0f\x41pplyPlanAction\x12\".orchestrator.ApplyPlanActionParam\x1a%.orchestrator.ApplyPlanActionResponse\x12M\n\nQueryPlans\x12\x1d.orchestrator.QueryPlansParam\x1a .orchestrator.QueryPlansResponseB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_COMPUTEPLANSTATUS = _descriptor.EnumDescriptor(
  name='ComputePlanStatus',
  full_name='orchestrator.ComputePlanStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAN_STATUS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAN_STATUS_WAITING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAN_STATUS_TODO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAN_STATUS_DOING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAN_STATUS_DONE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAN_STATUS_CANCELED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAN_STATUS_FAILED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1008,
  serialized_end=1194,
)
_sym_db.RegisterEnumDescriptor(_COMPUTEPLANSTATUS)

ComputePlanStatus = enum_type_wrapper.EnumTypeWrapper(_COMPUTEPLANSTATUS)
_COMPUTEPLANACTION = _descriptor.EnumDescriptor(
  name='ComputePlanAction',
  full_name='orchestrator.ComputePlanAction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAN_ACTION_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAN_ACTION_CANCELED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1196,
  serialized_end=1266,
)
_sym_db.RegisterEnumDescriptor(_COMPUTEPLANACTION)

ComputePlanAction = enum_type_wrapper.EnumTypeWrapper(_COMPUTEPLANACTION)
PLAN_STATUS_UNKNOWN = 0
PLAN_STATUS_WAITING = 1
PLAN_STATUS_TODO = 2
PLAN_STATUS_DOING = 3
PLAN_STATUS_DONE = 4
PLAN_STATUS_CANCELED = 5
PLAN_STATUS_FAILED = 6
PLAN_ACTION_UNKNOWN = 0
PLAN_ACTION_CANCELED = 1



_COMPUTEPLAN_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='orchestrator.ComputePlan.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.ComputePlan.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='orchestrator.ComputePlan.MetadataEntry.value', index=1,
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
  serialized_start=470,
  serialized_end=517,
)

_COMPUTEPLAN = _descriptor.Descriptor(
  name='ComputePlan',
  full_name='orchestrator.ComputePlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.ComputePlan.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='orchestrator.ComputePlan.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='waiting_count', full_name='orchestrator.ComputePlan.waiting_count', index=2,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='todo_count', full_name='orchestrator.ComputePlan.todo_count', index=3,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doing_count', full_name='orchestrator.ComputePlan.doing_count', index=4,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='canceled_count', full_name='orchestrator.ComputePlan.canceled_count', index=5,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failed_count', full_name='orchestrator.ComputePlan.failed_count', index=6,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='done_count', full_name='orchestrator.ComputePlan.done_count', index=7,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_count', full_name='orchestrator.ComputePlan.task_count', index=8,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='orchestrator.ComputePlan.status', index=9,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delete_intermediary_models', full_name='orchestrator.ComputePlan.delete_intermediary_models', index=10,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='orchestrator.ComputePlan.creation_date', index=11,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='orchestrator.ComputePlan.tag', index=12,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='orchestrator.ComputePlan.metadata', index=13,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COMPUTEPLAN_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=517,
)


_NEWCOMPUTEPLAN_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='orchestrator.NewComputePlan.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewComputePlan.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='orchestrator.NewComputePlan.MetadataEntry.value', index=1,
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
  serialized_start=470,
  serialized_end=517,
)

_NEWCOMPUTEPLAN = _descriptor.Descriptor(
  name='NewComputePlan',
  full_name='orchestrator.NewComputePlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.NewComputePlan.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='orchestrator.NewComputePlan.tag', index=1,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='orchestrator.NewComputePlan.metadata', index=2,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delete_intermediary_models', full_name='orchestrator.NewComputePlan.delete_intermediary_models', index=3,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_NEWCOMPUTEPLAN_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=520,
  serialized_end=709,
)


_GETCOMPUTEPLANPARAM = _descriptor.Descriptor(
  name='GetComputePlanParam',
  full_name='orchestrator.GetComputePlanParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.GetComputePlanParam.key', index=0,
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
  serialized_start=711,
  serialized_end=745,
)


_APPLYPLANACTIONPARAM = _descriptor.Descriptor(
  name='ApplyPlanActionParam',
  full_name='orchestrator.ApplyPlanActionParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='orchestrator.ApplyPlanActionParam.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='orchestrator.ApplyPlanActionParam.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=747,
  serialized_end=831,
)


_APPLYPLANACTIONRESPONSE = _descriptor.Descriptor(
  name='ApplyPlanActionResponse',
  full_name='orchestrator.ApplyPlanActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_end=858,
)


_QUERYPLANSPARAM = _descriptor.Descriptor(
  name='QueryPlansParam',
  full_name='orchestrator.QueryPlansParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_token', full_name='orchestrator.QueryPlansParam.page_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='orchestrator.QueryPlansParam.page_size', index=1,
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
  serialized_start=860,
  serialized_end=916,
)


_QUERYPLANSRESPONSE = _descriptor.Descriptor(
  name='QueryPlansResponse',
  full_name='orchestrator.QueryPlansResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plans', full_name='orchestrator.QueryPlansResponse.plans', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='orchestrator.QueryPlansResponse.next_page_token', index=1,
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
  serialized_start=918,
  serialized_end=1005,
)

_COMPUTEPLAN_METADATAENTRY.containing_type = _COMPUTEPLAN
_COMPUTEPLAN.fields_by_name['status'].enum_type = _COMPUTEPLANSTATUS
_COMPUTEPLAN.fields_by_name['creation_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_COMPUTEPLAN.fields_by_name['metadata'].message_type = _COMPUTEPLAN_METADATAENTRY
_NEWCOMPUTEPLAN_METADATAENTRY.containing_type = _NEWCOMPUTEPLAN
_NEWCOMPUTEPLAN.fields_by_name['metadata'].message_type = _NEWCOMPUTEPLAN_METADATAENTRY
_APPLYPLANACTIONPARAM.fields_by_name['action'].enum_type = _COMPUTEPLANACTION
_QUERYPLANSRESPONSE.fields_by_name['plans'].message_type = _COMPUTEPLAN
DESCRIPTOR.message_types_by_name['ComputePlan'] = _COMPUTEPLAN
DESCRIPTOR.message_types_by_name['NewComputePlan'] = _NEWCOMPUTEPLAN
DESCRIPTOR.message_types_by_name['GetComputePlanParam'] = _GETCOMPUTEPLANPARAM
DESCRIPTOR.message_types_by_name['ApplyPlanActionParam'] = _APPLYPLANACTIONPARAM
DESCRIPTOR.message_types_by_name['ApplyPlanActionResponse'] = _APPLYPLANACTIONRESPONSE
DESCRIPTOR.message_types_by_name['QueryPlansParam'] = _QUERYPLANSPARAM
DESCRIPTOR.message_types_by_name['QueryPlansResponse'] = _QUERYPLANSRESPONSE
DESCRIPTOR.enum_types_by_name['ComputePlanStatus'] = _COMPUTEPLANSTATUS
DESCRIPTOR.enum_types_by_name['ComputePlanAction'] = _COMPUTEPLANACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComputePlan = _reflection.GeneratedProtocolMessageType('ComputePlan', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _COMPUTEPLAN_METADATAENTRY,
    '__module__' : 'computeplan_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.ComputePlan.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _COMPUTEPLAN,
  '__module__' : 'computeplan_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ComputePlan)
  })
_sym_db.RegisterMessage(ComputePlan)
_sym_db.RegisterMessage(ComputePlan.MetadataEntry)

NewComputePlan = _reflection.GeneratedProtocolMessageType('NewComputePlan', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWCOMPUTEPLAN_METADATAENTRY,
    '__module__' : 'computeplan_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewComputePlan.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _NEWCOMPUTEPLAN,
  '__module__' : 'computeplan_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewComputePlan)
  })
_sym_db.RegisterMessage(NewComputePlan)
_sym_db.RegisterMessage(NewComputePlan.MetadataEntry)

GetComputePlanParam = _reflection.GeneratedProtocolMessageType('GetComputePlanParam', (_message.Message,), {
  'DESCRIPTOR' : _GETCOMPUTEPLANPARAM,
  '__module__' : 'computeplan_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetComputePlanParam)
  })
_sym_db.RegisterMessage(GetComputePlanParam)

ApplyPlanActionParam = _reflection.GeneratedProtocolMessageType('ApplyPlanActionParam', (_message.Message,), {
  'DESCRIPTOR' : _APPLYPLANACTIONPARAM,
  '__module__' : 'computeplan_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ApplyPlanActionParam)
  })
_sym_db.RegisterMessage(ApplyPlanActionParam)

ApplyPlanActionResponse = _reflection.GeneratedProtocolMessageType('ApplyPlanActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYPLANACTIONRESPONSE,
  '__module__' : 'computeplan_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ApplyPlanActionResponse)
  })
_sym_db.RegisterMessage(ApplyPlanActionResponse)

QueryPlansParam = _reflection.GeneratedProtocolMessageType('QueryPlansParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPLANSPARAM,
  '__module__' : 'computeplan_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryPlansParam)
  })
_sym_db.RegisterMessage(QueryPlansParam)

QueryPlansResponse = _reflection.GeneratedProtocolMessageType('QueryPlansResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPLANSRESPONSE,
  '__module__' : 'computeplan_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryPlansResponse)
  })
_sym_db.RegisterMessage(QueryPlansResponse)


DESCRIPTOR._options = None
_COMPUTEPLAN_METADATAENTRY._options = None
_NEWCOMPUTEPLAN_METADATAENTRY._options = None

_COMPUTEPLANSERVICE = _descriptor.ServiceDescriptor(
  name='ComputePlanService',
  full_name='orchestrator.ComputePlanService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1269,
  serialized_end=1608,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterPlan',
    full_name='orchestrator.ComputePlanService.RegisterPlan',
    index=0,
    containing_service=None,
    input_type=_NEWCOMPUTEPLAN,
    output_type=_COMPUTEPLAN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPlan',
    full_name='orchestrator.ComputePlanService.GetPlan',
    index=1,
    containing_service=None,
    input_type=_GETCOMPUTEPLANPARAM,
    output_type=_COMPUTEPLAN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ApplyPlanAction',
    full_name='orchestrator.ComputePlanService.ApplyPlanAction',
    index=2,
    containing_service=None,
    input_type=_APPLYPLANACTIONPARAM,
    output_type=_APPLYPLANACTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryPlans',
    full_name='orchestrator.ComputePlanService.QueryPlans',
    index=3,
    containing_service=None,
    input_type=_QUERYPLANSPARAM,
    output_type=_QUERYPLANSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMPUTEPLANSERVICE)

DESCRIPTOR.services_by_name['ComputePlanService'] = _COMPUTEPLANSERVICE

# @@protoc_insertion_point(module_scope)