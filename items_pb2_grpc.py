# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import items_pb2 as items__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in items_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ItemServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetItemById = channel.unary_unary(
                '/ItemService/GetItemById',
                request_serializer=items__pb2.ItemRequest.SerializeToString,
                response_deserializer=items__pb2.ItemResponse.FromString,
                _registered_method=True)
        self.ListAllItems = channel.unary_stream(
                '/ItemService/ListAllItems',
                request_serializer=items__pb2.Empty.SerializeToString,
                response_deserializer=items__pb2.ItemResponse.FromString,
                _registered_method=True)
        self.AddItems = channel.stream_unary(
                '/ItemService/AddItems',
                request_serializer=items__pb2.ItemRequest.SerializeToString,
                response_deserializer=items__pb2.ItemsAddedResult.FromString,
                _registered_method=True)
        self.ChatAboutItems = channel.stream_stream(
                '/ItemService/ChatAboutItems',
                request_serializer=items__pb2.ChatMessage.SerializeToString,
                response_deserializer=items__pb2.ChatMessage.FromString,
                _registered_method=True)
        self.AddItem = channel.unary_unary(
                '/ItemService/AddItem',
                request_serializer=items__pb2.ItemRequest.SerializeToString,
                response_deserializer=items__pb2.ItemResponse.FromString,
                _registered_method=True)


class ItemServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetItemById(self, request, context):
        """Unary RPC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAllItems(self, request, context):
        """Server-streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddItems(self, request_iterator, context):
        """Client-streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChatAboutItems(self, request_iterator, context):
        """Bidirectional
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddItem(self, request, context):
        """Add this new unary RPC for single item addition
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ItemServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetItemById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetItemById,
                    request_deserializer=items__pb2.ItemRequest.FromString,
                    response_serializer=items__pb2.ItemResponse.SerializeToString,
            ),
            'ListAllItems': grpc.unary_stream_rpc_method_handler(
                    servicer.ListAllItems,
                    request_deserializer=items__pb2.Empty.FromString,
                    response_serializer=items__pb2.ItemResponse.SerializeToString,
            ),
            'AddItems': grpc.stream_unary_rpc_method_handler(
                    servicer.AddItems,
                    request_deserializer=items__pb2.ItemRequest.FromString,
                    response_serializer=items__pb2.ItemsAddedResult.SerializeToString,
            ),
            'ChatAboutItems': grpc.stream_stream_rpc_method_handler(
                    servicer.ChatAboutItems,
                    request_deserializer=items__pb2.ChatMessage.FromString,
                    response_serializer=items__pb2.ChatMessage.SerializeToString,
            ),
            'AddItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddItem,
                    request_deserializer=items__pb2.ItemRequest.FromString,
                    response_serializer=items__pb2.ItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ItemService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ItemService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ItemService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetItemById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ItemService/GetItemById',
            items__pb2.ItemRequest.SerializeToString,
            items__pb2.ItemResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListAllItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/ItemService/ListAllItems',
            items__pb2.Empty.SerializeToString,
            items__pb2.ItemResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddItems(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/ItemService/AddItems',
            items__pb2.ItemRequest.SerializeToString,
            items__pb2.ItemsAddedResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ChatAboutItems(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/ItemService/ChatAboutItems',
            items__pb2.ChatMessage.SerializeToString,
            items__pb2.ChatMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ItemService/AddItem',
            items__pb2.ItemRequest.SerializeToString,
            items__pb2.ItemResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
