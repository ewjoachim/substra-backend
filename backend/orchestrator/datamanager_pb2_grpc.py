# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import datamanager_pb2 as datamanager__pb2


class DataManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterDataManager = channel.unary_unary(
                '/orchestrator.DataManagerService/RegisterDataManager',
                request_serializer=datamanager__pb2.NewDataManager.SerializeToString,
                response_deserializer=datamanager__pb2.DataManager.FromString,
                )
        self.GetDataManager = channel.unary_unary(
                '/orchestrator.DataManagerService/GetDataManager',
                request_serializer=datamanager__pb2.GetDataManagerParam.SerializeToString,
                response_deserializer=datamanager__pb2.DataManager.FromString,
                )
        self.QueryDataManagers = channel.unary_unary(
                '/orchestrator.DataManagerService/QueryDataManagers',
                request_serializer=datamanager__pb2.QueryDataManagersParam.SerializeToString,
                response_deserializer=datamanager__pb2.QueryDataManagersResponse.FromString,
                )


class DataManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterDataManager(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDataManager(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryDataManagers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterDataManager': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterDataManager,
                    request_deserializer=datamanager__pb2.NewDataManager.FromString,
                    response_serializer=datamanager__pb2.DataManager.SerializeToString,
            ),
            'GetDataManager': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDataManager,
                    request_deserializer=datamanager__pb2.GetDataManagerParam.FromString,
                    response_serializer=datamanager__pb2.DataManager.SerializeToString,
            ),
            'QueryDataManagers': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryDataManagers,
                    request_deserializer=datamanager__pb2.QueryDataManagersParam.FromString,
                    response_serializer=datamanager__pb2.QueryDataManagersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'orchestrator.DataManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterDataManager(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/orchestrator.DataManagerService/RegisterDataManager',
            datamanager__pb2.NewDataManager.SerializeToString,
            datamanager__pb2.DataManager.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDataManager(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/orchestrator.DataManagerService/GetDataManager',
            datamanager__pb2.GetDataManagerParam.SerializeToString,
            datamanager__pb2.DataManager.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryDataManagers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/orchestrator.DataManagerService/QueryDataManagers',
            datamanager__pb2.QueryDataManagersParam.SerializeToString,
            datamanager__pb2.QueryDataManagersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
