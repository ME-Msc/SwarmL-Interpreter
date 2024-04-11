# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import swarm_pb2 as swarm__pb2


class SwarmStub(object):
	"""The greeting service definition.
	"""

	def __init__(self, channel):
		"""Constructor.

		Args:
			channel: A grpc.Channel.
		"""
		self.trees_go_RPC_call = channel.unary_unary(
			'/swarm.Swarm/trees_go_RPC_call',
			request_serializer=swarm__pb2.TreesGoRequest.SerializeToString,
			response_deserializer=swarm__pb2.CommonReply.FromString,
		)
		self.createUavs = channel.unary_unary(
			'/swarm.Swarm/createUavs',
			request_serializer=swarm__pb2.CreateUavsRequest.SerializeToString,
			response_deserializer=swarm__pb2.CommonReply.FromString,
		)
		self.resetWorld = channel.unary_unary(
			'/swarm.Swarm/resetWorld',
			request_serializer=swarm__pb2.ResetWorldRequest.SerializeToString,
			response_deserializer=swarm__pb2.CommonReply.FromString,
		)


class SwarmServicer(object):
	"""The greeting service definition.
	"""

	def trees_go_RPC_call(self, request, context):
		"""Sends a greeting
		"""
		context.set_code(grpc.StatusCode.UNIMPLEMENTED)
		context.set_details('Method not implemented!')
		raise NotImplementedError('Method not implemented!')

	def createUavs(self, request, context):
		"""Missing associated documentation comment in .proto file."""
		context.set_code(grpc.StatusCode.UNIMPLEMENTED)
		context.set_details('Method not implemented!')
		raise NotImplementedError('Method not implemented!')

	def resetWorld(self, request, context):
		"""Missing associated documentation comment in .proto file."""
		context.set_code(grpc.StatusCode.UNIMPLEMENTED)
		context.set_details('Method not implemented!')
		raise NotImplementedError('Method not implemented!')


def add_SwarmServicer_to_server(servicer, server):
	rpc_method_handlers = {
		'trees_go_RPC_call': grpc.unary_unary_rpc_method_handler(
			servicer.trees_go_RPC_call,
			request_deserializer=swarm__pb2.TreesGoRequest.FromString,
			response_serializer=swarm__pb2.CommonReply.SerializeToString,
		),
		'createUavs': grpc.unary_unary_rpc_method_handler(
			servicer.createUavs,
			request_deserializer=swarm__pb2.CreateUavsRequest.FromString,
			response_serializer=swarm__pb2.CommonReply.SerializeToString,
		),
		'resetWorld': grpc.unary_unary_rpc_method_handler(
			servicer.resetWorld,
			request_deserializer=swarm__pb2.ResetWorldRequest.FromString,
			response_serializer=swarm__pb2.CommonReply.SerializeToString,
		),
	}
	generic_handler = grpc.method_handlers_generic_handler(
		'swarm.Swarm', rpc_method_handlers)
	server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Swarm(object):
	"""The greeting service definition.
	"""

	@staticmethod
	def trees_go_RPC_call(request,
	                      target,
	                      options=(),
	                      channel_credentials=None,
	                      call_credentials=None,
	                      insecure=False,
	                      compression=None,
	                      wait_for_ready=None,
	                      timeout=None,
	                      metadata=None):
		return grpc.experimental.unary_unary(request, target, '/swarm.Swarm/trees_go_RPC_call',
		                                     swarm__pb2.TreesGoRequest.SerializeToString,
		                                     swarm__pb2.CommonReply.FromString,
		                                     options, channel_credentials,
		                                     insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

	@staticmethod
	def createUavs(request,
	               target,
	               options=(),
	               channel_credentials=None,
	               call_credentials=None,
	               insecure=False,
	               compression=None,
	               wait_for_ready=None,
	               timeout=None,
	               metadata=None):
		return grpc.experimental.unary_unary(request, target, '/swarm.Swarm/createUavs',
		                                     swarm__pb2.CreateUavsRequest.SerializeToString,
		                                     swarm__pb2.CommonReply.FromString,
		                                     options, channel_credentials,
		                                     insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

	@staticmethod
	def resetWorld(request,
	               target,
	               options=(),
	               channel_credentials=None,
	               call_credentials=None,
	               insecure=False,
	               compression=None,
	               wait_for_ready=None,
	               timeout=None,
	               metadata=None):
		return grpc.experimental.unary_unary(request, target, '/swarm.Swarm/resetWorld',
		                                     swarm__pb2.ResetWorldRequest.SerializeToString,
		                                     swarm__pb2.CommonReply.FromString,
		                                     options, channel_credentials,
		                                     insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
