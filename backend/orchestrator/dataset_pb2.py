# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import datamanager_pb2 as datamanager__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdataset.proto\x12\x0corchestrator\x1a\x11\x64\x61tamanager.proto\"y\n\x07\x44\x61taset\x12/\n\x0c\x64\x61ta_manager\x18\x01 \x01(\x0b\x32\x19.orchestrator.DataManager\x12\x1e\n\x16train_data_sample_keys\x18\x02 \x03(\t\x12\x1d\n\x15test_data_sample_keys\x18\x03 \x03(\t\"\x1e\n\x0fGetDatasetParam\x12\x0b\n\x03key\x18\x01 \x01(\t2T\n\x0e\x44\x61tasetService\x12\x42\n\nGetDataset\x12\x1d.orchestrator.GetDatasetParam\x1a\x15.orchestrator.DatasetB)Z\'github.com/owkin/orchestrator/lib/assetb\x06proto3')



_DATASET = DESCRIPTOR.message_types_by_name['Dataset']
_GETDATASETPARAM = DESCRIPTOR.message_types_by_name['GetDatasetParam']
Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'dataset_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.Dataset)
  })
_sym_db.RegisterMessage(Dataset)

GetDatasetParam = _reflection.GeneratedProtocolMessageType('GetDatasetParam', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETPARAM,
  '__module__' : 'dataset_pb2'
  # @@protoc_insertion_point(class_scope:orchestrator.GetDatasetParam)
  })
_sym_db.RegisterMessage(GetDatasetParam)

_DATASETSERVICE = DESCRIPTOR.services_by_name['DatasetService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'github.com/owkin/orchestrator/lib/asset'
  _DATASET._serialized_start=50
  _DATASET._serialized_end=171
  _GETDATASETPARAM._serialized_start=173
  _GETDATASETPARAM._serialized_end=203
  _DATASETSERVICE._serialized_start=205
  _DATASETSERVICE._serialized_end=289
# @@protoc_insertion_point(module_scope)
