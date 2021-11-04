# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import node_pb2 as node__pb2


class NodeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterNode = channel.unary_unary(
                '/orchestrator.NodeService/RegisterNode',
                request_serializer=node__pb2.RegisterNodeParam.SerializeToString,
                response_deserializer=node__pb2.Node.FromString,
                )
        self.GetAllNodes = channel.unary_unary(
                '/orchestrator.NodeService/GetAllNodes',
                request_serializer=node__pb2.GetAllNodesParam.SerializeToString,
                response_deserializer=node__pb2.GetAllNodesResponse.FromString,
                )


class NodeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllNodes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterNode': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterNode,
                    request_deserializer=node__pb2.RegisterNodeParam.FromString,
                    response_serializer=node__pb2.Node.SerializeToString,
            ),
            'GetAllNodes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllNodes,
                    request_deserializer=node__pb2.GetAllNodesParam.FromString,
                    response_serializer=node__pb2.GetAllNodesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'orchestrator.NodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NodeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/orchestrator.NodeService/RegisterNode',
            node__pb2.RegisterNodeParam.SerializeToString,
            node__pb2.Node.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/orchestrator.NodeService/GetAllNodes',
            node__pb2.GetAllNodesParam.SerializeToString,
            node__pb2.GetAllNodesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)