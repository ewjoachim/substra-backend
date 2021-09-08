# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import performance_pb2 as performance__pb2


class PerformanceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterPerformance = channel.unary_unary(
                '/orchestrator.PerformanceService/RegisterPerformance',
                request_serializer=performance__pb2.NewPerformance.SerializeToString,
                response_deserializer=performance__pb2.Performance.FromString,
                )
        self.GetComputeTaskPerformance = channel.unary_unary(
                '/orchestrator.PerformanceService/GetComputeTaskPerformance',
                request_serializer=performance__pb2.GetComputeTaskPerformanceParam.SerializeToString,
                response_deserializer=performance__pb2.Performance.FromString,
                )


class PerformanceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterPerformance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetComputeTaskPerformance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PerformanceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterPerformance': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPerformance,
                    request_deserializer=performance__pb2.NewPerformance.FromString,
                    response_serializer=performance__pb2.Performance.SerializeToString,
            ),
            'GetComputeTaskPerformance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetComputeTaskPerformance,
                    request_deserializer=performance__pb2.GetComputeTaskPerformanceParam.FromString,
                    response_serializer=performance__pb2.Performance.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'orchestrator.PerformanceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PerformanceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterPerformance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/orchestrator.PerformanceService/RegisterPerformance',
            performance__pb2.NewPerformance.SerializeToString,
            performance__pb2.Performance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetComputeTaskPerformance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/orchestrator.PerformanceService/GetComputeTaskPerformance',
            performance__pb2.GetComputeTaskPerformanceParam.SerializeToString,
            performance__pb2.Performance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
