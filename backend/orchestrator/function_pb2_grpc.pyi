"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import function_pb2
import grpc

class FunctionServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    RegisterFunction: grpc.UnaryUnaryMultiCallable[
        function_pb2.NewFunction,
        function_pb2.Function,
    ]
    GetFunction: grpc.UnaryUnaryMultiCallable[
        function_pb2.GetFunctionParam,
        function_pb2.Function,
    ]
    QueryFunctions: grpc.UnaryUnaryMultiCallable[
        function_pb2.QueryFunctionsParam,
        function_pb2.QueryFunctionsResponse,
    ]
    UpdateFunction: grpc.UnaryUnaryMultiCallable[
        function_pb2.UpdateFunctionParam,
        function_pb2.UpdateFunctionResponse,
    ]

class FunctionServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def RegisterFunction(
        self,
        request: function_pb2.NewFunction,
        context: grpc.ServicerContext,
    ) -> function_pb2.Function: ...
    @abc.abstractmethod
    def GetFunction(
        self,
        request: function_pb2.GetFunctionParam,
        context: grpc.ServicerContext,
    ) -> function_pb2.Function: ...
    @abc.abstractmethod
    def QueryFunctions(
        self,
        request: function_pb2.QueryFunctionsParam,
        context: grpc.ServicerContext,
    ) -> function_pb2.QueryFunctionsResponse: ...
    @abc.abstractmethod
    def UpdateFunction(
        self,
        request: function_pb2.UpdateFunctionParam,
        context: grpc.ServicerContext,
    ) -> function_pb2.UpdateFunctionResponse: ...

def add_FunctionServiceServicer_to_server(servicer: FunctionServiceServicer, server: grpc.Server) -> None: ...
