# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\"\x07\n\x05\x45mpty\"(\n\x05Reply\x12\x10\n\x08response\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\x32\xfe\x03\n\x07Gateway\x12\x1e\n\x0cligarLampada\x12\x06.Empty\x1a\x06.Reply\x12!\n\x0f\x64\x65sligarLampada\x12\x06.Empty\x1a\x06.Reply\x12$\n\x12obterStatusLampada\x12\x06.Empty\x1a\x06.Reply\x12\x19\n\x07ligarAr\x12\x06.Empty\x1a\x06.Reply\x12\x1c\n\ndesligarAr\x12\x06.Empty\x1a\x06.Reply\x12\x1f\n\robterStatusAr\x12\x06.Empty\x1a\x06.Reply\x12\x1a\n\x08ligarSom\x12\x06.Empty\x1a\x06.Reply\x12\x1d\n\x0b\x64\x65sligarSom\x12\x06.Empty\x1a\x06.Reply\x12 \n\x0eobterStatusSom\x12\x06.Empty\x1a\x06.Reply\x12%\n\x13\x61umentarTemperatura\x12\x06.Empty\x1a\x06.Reply\x12%\n\x13\x64iminuirTemperatura\x12\x06.Empty\x1a\x06.Reply\x12\"\n\x10obterTemperatura\x12\x06.Empty\x1a\x06.Reply\x12 \n\x0e\x61umentarVolume\x12\x06.Empty\x1a\x06.Reply\x12 \n\x0e\x64iminuirVolume\x12\x06.Empty\x1a\x06.Reply\x12\x1d\n\x0bobterVolume\x12\x06.Empty\x1a\x06.Replyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=18
  _globals['_EMPTY']._serialized_end=25
  _globals['_REPLY']._serialized_start=27
  _globals['_REPLY']._serialized_end=67
  _globals['_GATEWAY']._serialized_start=70
  _globals['_GATEWAY']._serialized_end=580
# @@protoc_insertion_point(module_scope)
