# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: swarm.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bswarm.proto\x12\x05swarm\" \n\x0eTreesGoRequest\x12\x0e\n\x06uav_id\x18\x01 \x01(\x03\"$\n\x11\x43reateUavsRequest\x12\x0f\n\x07uav_cnt\x18\x01 \x01(\x03\"\x13\n\x11ResetWorldRequest\"\x1e\n\x0b\x43ommonReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xc5\x01\n\x05Swarm\x12@\n\x11trees_go_RPC_call\x12\x15.swarm.TreesGoRequest\x1a\x12.swarm.CommonReply\"\x00\x12<\n\ncreateUavs\x12\x18.swarm.CreateUavsRequest\x1a\x12.swarm.CommonReply\"\x00\x12<\n\nresetWorld\x12\x18.swarm.ResetWorldRequest\x1a\x12.swarm.CommonReply\"\x00\x42,\n\x16io.grpc.examples.swarmB\nSwarmProtoP\x01\xa2\x02\x03SWMb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'swarm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026io.grpc.examples.swarmB\nSwarmProtoP\001\242\002\003SWM'
  _globals['_TREESGOREQUEST']._serialized_start=22
  _globals['_TREESGOREQUEST']._serialized_end=54
  _globals['_CREATEUAVSREQUEST']._serialized_start=56
  _globals['_CREATEUAVSREQUEST']._serialized_end=92
  _globals['_RESETWORLDREQUEST']._serialized_start=94
  _globals['_RESETWORLDREQUEST']._serialized_end=113
  _globals['_COMMONREPLY']._serialized_start=115
  _globals['_COMMONREPLY']._serialized_end=145
  _globals['_SWARM']._serialized_start=148
  _globals['_SWARM']._serialized_end=345
# @@protoc_insertion_point(module_scope)