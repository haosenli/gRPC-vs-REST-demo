# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"(\n\nAddRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\x1d\n\x0b\x41\x64\x64Response\x12\x0e\n\x06result\x18\x01 \x01(\x05\x32\x44\n\nCalculator\x12\x36\n\x03\x41\x64\x64\x12\x16.calculator.AddRequest\x1a\x17.calculator.AddResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ADDREQUEST']._serialized_start=32
  _globals['_ADDREQUEST']._serialized_end=72
  _globals['_ADDRESPONSE']._serialized_start=74
  _globals['_ADDRESPONSE']._serialized_end=103
  _globals['_CALCULATOR']._serialized_start=105
  _globals['_CALCULATOR']._serialized_end=173
# @@protoc_insertion_point(module_scope)
