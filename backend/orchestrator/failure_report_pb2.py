# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: failure_report.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x66\x61ilure_report.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\xc9\x01\n\rFailureReport\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t\x12+\n\nerror_type\x18\x02 \x01(\x0e\x32\x17.orchestrator.ErrorType\x12/\n\x0clogs_address\x18\x03 \x01(\x0b\x32\x19.orchestrator.Addressable\x12\x31\n\rcreation_date\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05owner\x18\x05 \x01(\t\"\x8a\x01\n\x10NewFailureReport\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t\x12+\n\nerror_type\x18\x02 \x01(\x0e\x32\x17.orchestrator.ErrorType\x12/\n\x0clogs_address\x18\x03 \x01(\x0b\x32\x19.orchestrator.Addressable\"1\n\x15GetFailureReportParam\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t*p\n\tErrorType\x12\x1a\n\x16\x45RROR_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x45RROR_TYPE_BUILD\x10\x01\x12\x18\n\x14\x45RROR_TYPE_EXECUTION\x10\x02\x12\x17\n\x13\x45RROR_TYPE_INTERNAL\x10\x03\x32\xc2\x01\n\x14\x46\x61ilureReportService\x12T\n\x15RegisterFailureReport\x12\x1e.orchestrator.NewFailureReport\x1a\x1b.orchestrator.FailureReport\x12T\n\x10GetFailureReport\x12#.orchestrator.GetFailureReportParam\x1a\x1b.orchestrator.FailureReportB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3')

_ERRORTYPE = DESCRIPTOR.enum_types_by_name['ErrorType']
ErrorType = enum_type_wrapper.EnumTypeWrapper(_ERRORTYPE)
ERROR_TYPE_UNSPECIFIED = 0
ERROR_TYPE_BUILD = 1
ERROR_TYPE_EXECUTION = 2
ERROR_TYPE_INTERNAL = 3


_FAILUREREPORT = DESCRIPTOR.message_types_by_name['FailureReport']
_NEWFAILUREREPORT = DESCRIPTOR.message_types_by_name['NewFailureReport']
_GETFAILUREREPORTPARAM = DESCRIPTOR.message_types_by_name['GetFailureReportParam']
FailureReport = _reflection.GeneratedProtocolMessageType('FailureReport', (_message.Message,), {
  'DESCRIPTOR' : _FAILUREREPORT,
  '__module__' : 'failure_report_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.FailureReport)
  })
_sym_db.RegisterMessage(FailureReport)

NewFailureReport = _reflection.GeneratedProtocolMessageType('NewFailureReport', (_message.Message,), {
  'DESCRIPTOR' : _NEWFAILUREREPORT,
  '__module__' : 'failure_report_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewFailureReport)
  })
_sym_db.RegisterMessage(NewFailureReport)

GetFailureReportParam = _reflection.GeneratedProtocolMessageType('GetFailureReportParam', (_message.Message,), {
  'DESCRIPTOR' : _GETFAILUREREPORTPARAM,
  '__module__' : 'failure_report_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetFailureReportParam)
  })
_sym_db.RegisterMessage(GetFailureReportParam)

_FAILUREREPORTSERVICE = DESCRIPTOR.services_by_name['FailureReportService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'github.com/owkin/orchestrator/lib/asset'
  _ERRORTYPE._serialized_start=481
  _ERRORTYPE._serialized_end=593
  _FAILUREREPORT._serialized_start=86
  _FAILUREREPORT._serialized_end=287
  _NEWFAILUREREPORT._serialized_start=290
  _NEWFAILUREREPORT._serialized_end=428
  _GETFAILUREREPORTPARAM._serialized_start=430
  _GETFAILUREREPORTPARAM._serialized_end=479
  _FAILUREREPORTSERVICE._serialized_start=596
  _FAILUREREPORTSERVICE._serialized_end=790
# @@protoc_insertion_point(module_scope)
