# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NameServer.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10NameServer.proto\x1a\x1bgoogle/protobuf/empty.proto\" \n\x0ctestResponse\x12\x10\n\x08sentence\x18\x01 \x01(\t\"+\n\x18GetChatParametersRequest\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\t\":\n\x19GetChatParametersResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"K\n\x15RegisterClientRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\")\n\x16RegisterClientResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xd7\x01\n\x11NameServerService\x12L\n\x11GetChatParameters\x12\x19.GetChatParametersRequest\x1a\x1a.GetChatParametersResponse\"\x00\x12\x43\n\x0eRegisterClient\x12\x16.RegisterClientRequest\x1a\x17.RegisterClientResponse\"\x00\x12/\n\x04test\x12\x16.google.protobuf.Empty\x1a\r.testResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'NameServer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TESTRESPONSE']._serialized_start=49
  _globals['_TESTRESPONSE']._serialized_end=81
  _globals['_GETCHATPARAMETERSREQUEST']._serialized_start=83
  _globals['_GETCHATPARAMETERSREQUEST']._serialized_end=126
  _globals['_GETCHATPARAMETERSRESPONSE']._serialized_start=128
  _globals['_GETCHATPARAMETERSRESPONSE']._serialized_end=186
  _globals['_REGISTERCLIENTREQUEST']._serialized_start=188
  _globals['_REGISTERCLIENTREQUEST']._serialized_end=263
  _globals['_REGISTERCLIENTRESPONSE']._serialized_start=265
  _globals['_REGISTERCLIENTRESPONSE']._serialized_end=306
  _globals['_NAMESERVERSERVICE']._serialized_start=309
  _globals['_NAMESERVERSERVICE']._serialized_end=524
# @@protoc_insertion_point(module_scope)
