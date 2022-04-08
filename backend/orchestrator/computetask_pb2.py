# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: computetask.proto
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
from . import algo_pb2 as algo__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63omputetask.proto\x12\x0corchestrator\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\nalgo.proto\x1a\x0c\x63ommon.proto\"\xad\x05\n\x0b\x43omputeTask\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32!.orchestrator.ComputeTaskCategory\x12 \n\x04\x61lgo\x18\x03 \x01(\x0b\x32\x12.orchestrator.Algo\x12\r\n\x05owner\x18\x04 \x01(\t\x12\x18\n\x10\x63ompute_plan_key\x18\x05 \x01(\t\x12\x18\n\x10parent_task_keys\x18\x06 \x03(\t\x12\x0c\n\x04rank\x18\x07 \x01(\x05\x12/\n\x06status\x18\x08 \x01(\x0e\x32\x1f.orchestrator.ComputeTaskStatus\x12\x0e\n\x06worker\x18\t \x01(\t\x12\x31\n\rcreation_date\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x0flogs_permission\x18\x0b \x01(\x0b\x32\x18.orchestrator.Permission\x12*\n\x04test\x18\x0c \x01(\x0b\x32\x1a.orchestrator.TestTaskDataH\x00\x12,\n\x05train\x18\r \x01(\x0b\x32\x1b.orchestrator.TrainTaskDataH\x00\x12\x39\n\tcomposite\x18\x0e \x01(\x0b\x32$.orchestrator.CompositeTrainTaskDataH\x00\x12\x39\n\taggregate\x18\x0f \x01(\x0b\x32$.orchestrator.AggregateTrainTaskDataH\x00\x12\x39\n\x08metadata\x18\x10 \x03(\x0b\x32\'.orchestrator.ComputeTask.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x06\n\x04\x64\x61ta\"\xeb\x03\n\x0eNewComputeTask\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32!.orchestrator.ComputeTaskCategory\x12\x10\n\x08\x61lgo_key\x18\x03 \x01(\t\x12\x18\n\x10\x63ompute_plan_key\x18\x04 \x01(\t\x12\x18\n\x10parent_task_keys\x18\x05 \x03(\t\x12-\n\x04test\x18\x0c \x01(\x0b\x32\x1d.orchestrator.NewTestTaskDataH\x00\x12/\n\x05train\x18\r \x01(\x0b\x32\x1e.orchestrator.NewTrainTaskDataH\x00\x12<\n\tcomposite\x18\x0e \x01(\x0b\x32\'.orchestrator.NewCompositeTrainTaskDataH\x00\x12<\n\taggregate\x18\x0f \x01(\x0b\x32\'.orchestrator.NewAggregateTrainTaskDataH\x00\x12<\n\x08metadata\x18\x10 \x03(\x0b\x32*.orchestrator.NewComputeTask.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x06\n\x04\x64\x61ta\"y\n\rTrainTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\t\x12\x34\n\x11model_permissions\x18\x04 \x01(\x0b\x32\x19.orchestrator.Permissions\"F\n\x10NewTrainTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\t\"W\n\x0cTestTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\t\x12\x13\n\x0bmetric_keys\x18\x03 \x03(\t\"Z\n\x0fNewTestTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\t\x12\x13\n\x0bmetric_keys\x18\x03 \x03(\t\"\xb7\x01\n\x16\x43ompositeTrainTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\t\x12\x33\n\x10head_permissions\x18\x05 \x01(\x0b\x32\x19.orchestrator.Permissions\x12\x34\n\x11trunk_permissions\x18\x06 \x01(\x0b\x32\x19.orchestrator.Permissions\"\x88\x01\n\x19NewCompositeTrainTaskData\x12\x18\n\x10\x64\x61ta_manager_key\x18\x01 \x01(\t\x12\x18\n\x10\x64\x61ta_sample_keys\x18\x02 \x03(\t\x12\x37\n\x11trunk_permissions\x18\x04 \x01(\x0b\x32\x1c.orchestrator.NewPermissions\"N\n\x16\x41ggregateTrainTaskData\x12\x34\n\x11model_permissions\x18\x02 \x01(\x0b\x32\x19.orchestrator.Permissions\"+\n\x19NewAggregateTrainTaskData\x12\x0e\n\x06worker\x18\x02 \x01(\t\"A\n\x12RegisterTasksParam\x12+\n\x05tasks\x18\x01 \x03(\x0b\x32\x1c.orchestrator.NewComputeTask\"A\n\x15RegisterTasksResponse\x12(\n\x05tasks\x18\x01 \x03(\x0b\x32\x19.orchestrator.ComputeTask\"\xb3\x01\n\x0fTaskQueryFilter\x12\x0e\n\x06worker\x18\x01 \x01(\t\x12/\n\x06status\x18\x02 \x01(\x0e\x32\x1f.orchestrator.ComputeTaskStatus\x12\x33\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32!.orchestrator.ComputeTaskCategory\x12\x18\n\x10\x63ompute_plan_key\x18\x04 \x01(\t\x12\x10\n\x08\x61lgo_key\x18\x05 \x01(\t\"g\n\x0fQueryTasksParam\x12\x12\n\npage_token\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\r\x12-\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x1d.orchestrator.TaskQueryFilter\"W\n\x12QueryTasksResponse\x12(\n\x05tasks\x18\x01 \x03(\x0b\x32\x19.orchestrator.ComputeTask\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x1b\n\x0cGetTaskParam\x12\x0b\n\x03key\x18\x01 \x01(\t\"n\n\x14\x41pplyTaskActionParam\x12\x18\n\x10\x63ompute_task_key\x18\x01 \x01(\t\x12/\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x1f.orchestrator.ComputeTaskAction\x12\x0b\n\x03log\x18\x03 \x01(\t\"\x19\n\x17\x41pplyTaskActionResponse*n\n\x13\x43omputeTaskCategory\x12\x10\n\x0cTASK_UNKNOWN\x10\x00\x12\x0e\n\nTASK_TRAIN\x10\x01\x12\x12\n\x0eTASK_AGGREGATE\x10\x02\x12\x12\n\x0eTASK_COMPOSITE\x10\x03\x12\r\n\tTASK_TEST\x10\x04*\x97\x01\n\x11\x43omputeTaskStatus\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x12\n\x0eSTATUS_WAITING\x10\x01\x12\x0f\n\x0bSTATUS_TODO\x10\x02\x12\x10\n\x0cSTATUS_DOING\x10\x03\x12\x0f\n\x0bSTATUS_DONE\x10\x04\x12\x13\n\x0fSTATUS_CANCELED\x10\x05\x12\x11\n\rSTATUS_FAILED\x10\x06*u\n\x11\x43omputeTaskAction\x12\x17\n\x13TASK_ACTION_UNKNOWN\x10\x00\x12\x15\n\x11TASK_ACTION_DOING\x10\x01\x12\x18\n\x14TASK_ACTION_CANCELED\x10\x02\x12\x16\n\x12TASK_ACTION_FAILED\x10\x03\x32\xdb\x02\n\x12\x43omputeTaskService\x12V\n\rRegisterTasks\x12 .orchestrator.RegisterTasksParam\x1a#.orchestrator.RegisterTasksResponse\x12M\n\nQueryTasks\x12\x1d.orchestrator.QueryTasksParam\x1a .orchestrator.QueryTasksResponse\x12@\n\x07GetTask\x12\x1a.orchestrator.GetTaskParam\x1a\x19.orchestrator.ComputeTask\x12\\\n\x0f\x41pplyTaskAction\x12\".orchestrator.ApplyTaskActionParam\x1a%.orchestrator.ApplyTaskActionResponseB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3')

_COMPUTETASKCATEGORY = DESCRIPTOR.enum_types_by_name['ComputeTaskCategory']
ComputeTaskCategory = enum_type_wrapper.EnumTypeWrapper(_COMPUTETASKCATEGORY)
_COMPUTETASKSTATUS = DESCRIPTOR.enum_types_by_name['ComputeTaskStatus']
ComputeTaskStatus = enum_type_wrapper.EnumTypeWrapper(_COMPUTETASKSTATUS)
_COMPUTETASKACTION = DESCRIPTOR.enum_types_by_name['ComputeTaskAction']
ComputeTaskAction = enum_type_wrapper.EnumTypeWrapper(_COMPUTETASKACTION)
TASK_UNKNOWN = 0
TASK_TRAIN = 1
TASK_AGGREGATE = 2
TASK_COMPOSITE = 3
TASK_TEST = 4
STATUS_UNKNOWN = 0
STATUS_WAITING = 1
STATUS_TODO = 2
STATUS_DOING = 3
STATUS_DONE = 4
STATUS_CANCELED = 5
STATUS_FAILED = 6
TASK_ACTION_UNKNOWN = 0
TASK_ACTION_DOING = 1
TASK_ACTION_CANCELED = 2
TASK_ACTION_FAILED = 3


_COMPUTETASK = DESCRIPTOR.message_types_by_name['ComputeTask']
_COMPUTETASK_METADATAENTRY = _COMPUTETASK.nested_types_by_name['MetadataEntry']
_NEWCOMPUTETASK = DESCRIPTOR.message_types_by_name['NewComputeTask']
_NEWCOMPUTETASK_METADATAENTRY = _NEWCOMPUTETASK.nested_types_by_name['MetadataEntry']
_TRAINTASKDATA = DESCRIPTOR.message_types_by_name['TrainTaskData']
_NEWTRAINTASKDATA = DESCRIPTOR.message_types_by_name['NewTrainTaskData']
_TESTTASKDATA = DESCRIPTOR.message_types_by_name['TestTaskData']
_NEWTESTTASKDATA = DESCRIPTOR.message_types_by_name['NewTestTaskData']
_COMPOSITETRAINTASKDATA = DESCRIPTOR.message_types_by_name['CompositeTrainTaskData']
_NEWCOMPOSITETRAINTASKDATA = DESCRIPTOR.message_types_by_name['NewCompositeTrainTaskData']
_AGGREGATETRAINTASKDATA = DESCRIPTOR.message_types_by_name['AggregateTrainTaskData']
_NEWAGGREGATETRAINTASKDATA = DESCRIPTOR.message_types_by_name['NewAggregateTrainTaskData']
_REGISTERTASKSPARAM = DESCRIPTOR.message_types_by_name['RegisterTasksParam']
_REGISTERTASKSRESPONSE = DESCRIPTOR.message_types_by_name['RegisterTasksResponse']
_TASKQUERYFILTER = DESCRIPTOR.message_types_by_name['TaskQueryFilter']
_QUERYTASKSPARAM = DESCRIPTOR.message_types_by_name['QueryTasksParam']
_QUERYTASKSRESPONSE = DESCRIPTOR.message_types_by_name['QueryTasksResponse']
_GETTASKPARAM = DESCRIPTOR.message_types_by_name['GetTaskParam']
_APPLYTASKACTIONPARAM = DESCRIPTOR.message_types_by_name['ApplyTaskActionParam']
_APPLYTASKACTIONRESPONSE = DESCRIPTOR.message_types_by_name['ApplyTaskActionResponse']
ComputeTask = _reflection.GeneratedProtocolMessageType('ComputeTask', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _COMPUTETASK_METADATAENTRY,
    '__module__' : 'computetask_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.ComputeTask.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _COMPUTETASK,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ComputeTask)
  })
_sym_db.RegisterMessage(ComputeTask)
_sym_db.RegisterMessage(ComputeTask.MetadataEntry)

NewComputeTask = _reflection.GeneratedProtocolMessageType('NewComputeTask', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _NEWCOMPUTETASK_METADATAENTRY,
    '__module__' : 'computetask_pb2'
    # @@protoc_insertion_point(class_scope:orchestrator.NewComputeTask.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _NEWCOMPUTETASK,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewComputeTask)
  })
_sym_db.RegisterMessage(NewComputeTask)
_sym_db.RegisterMessage(NewComputeTask.MetadataEntry)

TrainTaskData = _reflection.GeneratedProtocolMessageType('TrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _TRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.TrainTaskData)
  })
_sym_db.RegisterMessage(TrainTaskData)

NewTrainTaskData = _reflection.GeneratedProtocolMessageType('NewTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWTRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewTrainTaskData)
  })
_sym_db.RegisterMessage(NewTrainTaskData)

TestTaskData = _reflection.GeneratedProtocolMessageType('TestTaskData', (_message.Message,), {
  'DESCRIPTOR' : _TESTTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.TestTaskData)
  })
_sym_db.RegisterMessage(TestTaskData)

NewTestTaskData = _reflection.GeneratedProtocolMessageType('NewTestTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWTESTTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewTestTaskData)
  })
_sym_db.RegisterMessage(NewTestTaskData)

CompositeTrainTaskData = _reflection.GeneratedProtocolMessageType('CompositeTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _COMPOSITETRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.CompositeTrainTaskData)
  })
_sym_db.RegisterMessage(CompositeTrainTaskData)

NewCompositeTrainTaskData = _reflection.GeneratedProtocolMessageType('NewCompositeTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWCOMPOSITETRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewCompositeTrainTaskData)
  })
_sym_db.RegisterMessage(NewCompositeTrainTaskData)

AggregateTrainTaskData = _reflection.GeneratedProtocolMessageType('AggregateTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATETRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.AggregateTrainTaskData)
  })
_sym_db.RegisterMessage(AggregateTrainTaskData)

NewAggregateTrainTaskData = _reflection.GeneratedProtocolMessageType('NewAggregateTrainTaskData', (_message.Message,), {
  'DESCRIPTOR' : _NEWAGGREGATETRAINTASKDATA,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.NewAggregateTrainTaskData)
  })
_sym_db.RegisterMessage(NewAggregateTrainTaskData)

RegisterTasksParam = _reflection.GeneratedProtocolMessageType('RegisterTasksParam', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTASKSPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.RegisterTasksParam)
  })
_sym_db.RegisterMessage(RegisterTasksParam)

RegisterTasksResponse = _reflection.GeneratedProtocolMessageType('RegisterTasksResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTASKSRESPONSE,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.RegisterTasksResponse)
  })
_sym_db.RegisterMessage(RegisterTasksResponse)

TaskQueryFilter = _reflection.GeneratedProtocolMessageType('TaskQueryFilter', (_message.Message,), {
  'DESCRIPTOR' : _TASKQUERYFILTER,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.TaskQueryFilter)
  })
_sym_db.RegisterMessage(TaskQueryFilter)

QueryTasksParam = _reflection.GeneratedProtocolMessageType('QueryTasksParam', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTASKSPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryTasksParam)
  })
_sym_db.RegisterMessage(QueryTasksParam)

QueryTasksResponse = _reflection.GeneratedProtocolMessageType('QueryTasksResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTASKSRESPONSE,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.QueryTasksResponse)
  })
_sym_db.RegisterMessage(QueryTasksResponse)

GetTaskParam = _reflection.GeneratedProtocolMessageType('GetTaskParam', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetTaskParam)
  })
_sym_db.RegisterMessage(GetTaskParam)

ApplyTaskActionParam = _reflection.GeneratedProtocolMessageType('ApplyTaskActionParam', (_message.Message,), {
  'DESCRIPTOR' : _APPLYTASKACTIONPARAM,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ApplyTaskActionParam)
  })
_sym_db.RegisterMessage(ApplyTaskActionParam)

ApplyTaskActionResponse = _reflection.GeneratedProtocolMessageType('ApplyTaskActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYTASKACTIONRESPONSE,
  '__module__' : 'computetask_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.ApplyTaskActionResponse)
  })
_sym_db.RegisterMessage(ApplyTaskActionResponse)

_COMPUTETASKSERVICE = DESCRIPTOR.services_by_name['ComputeTaskService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'github.com/owkin/orchestrator/lib/asset'
  _COMPUTETASK_METADATAENTRY._options = None
  _COMPUTETASK_METADATAENTRY._serialized_options = b'8\001'
  _NEWCOMPUTETASK_METADATAENTRY._options = None
  _NEWCOMPUTETASK_METADATAENTRY._serialized_options = b'8\001'
  _COMPUTETASKCATEGORY._serialized_start=2780
  _COMPUTETASKCATEGORY._serialized_end=2890
  _COMPUTETASKSTATUS._serialized_start=2893
  _COMPUTETASKSTATUS._serialized_end=3044
  _COMPUTETASKACTION._serialized_start=3046
  _COMPUTETASKACTION._serialized_end=3163
  _COMPUTETASK._serialized_start=95
  _COMPUTETASK._serialized_end=780
  _COMPUTETASK_METADATAENTRY._serialized_start=725
  _COMPUTETASK_METADATAENTRY._serialized_end=772
  _NEWCOMPUTETASK._serialized_start=783
  _NEWCOMPUTETASK._serialized_end=1274
  _NEWCOMPUTETASK_METADATAENTRY._serialized_start=725
  _NEWCOMPUTETASK_METADATAENTRY._serialized_end=772
  _TRAINTASKDATA._serialized_start=1276
  _TRAINTASKDATA._serialized_end=1397
  _NEWTRAINTASKDATA._serialized_start=1399
  _NEWTRAINTASKDATA._serialized_end=1469
  _TESTTASKDATA._serialized_start=1471
  _TESTTASKDATA._serialized_end=1558
  _NEWTESTTASKDATA._serialized_start=1560
  _NEWTESTTASKDATA._serialized_end=1650
  _COMPOSITETRAINTASKDATA._serialized_start=1653
  _COMPOSITETRAINTASKDATA._serialized_end=1836
  _NEWCOMPOSITETRAINTASKDATA._serialized_start=1839
  _NEWCOMPOSITETRAINTASKDATA._serialized_end=1975
  _AGGREGATETRAINTASKDATA._serialized_start=1977
  _AGGREGATETRAINTASKDATA._serialized_end=2055
  _NEWAGGREGATETRAINTASKDATA._serialized_start=2057
  _NEWAGGREGATETRAINTASKDATA._serialized_end=2100
  _REGISTERTASKSPARAM._serialized_start=2102
  _REGISTERTASKSPARAM._serialized_end=2167
  _REGISTERTASKSRESPONSE._serialized_start=2169
  _REGISTERTASKSRESPONSE._serialized_end=2234
  _TASKQUERYFILTER._serialized_start=2237
  _TASKQUERYFILTER._serialized_end=2416
  _QUERYTASKSPARAM._serialized_start=2418
  _QUERYTASKSPARAM._serialized_end=2521
  _QUERYTASKSRESPONSE._serialized_start=2523
  _QUERYTASKSRESPONSE._serialized_end=2610
  _GETTASKPARAM._serialized_start=2612
  _GETTASKPARAM._serialized_end=2639
  _APPLYTASKACTIONPARAM._serialized_start=2641
  _APPLYTASKACTIONPARAM._serialized_end=2751
  _APPLYTASKACTIONRESPONSE._serialized_start=2753
  _APPLYTASKACTIONRESPONSE._serialized_end=2778
  _COMPUTETASKSERVICE._serialized_start=3166
  _COMPUTETASKSERVICE._serialized_end=3513
# @@protoc_insertion_point(module_scope)
