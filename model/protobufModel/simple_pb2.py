# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simple.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0csimple.proto\",\n\x06Simple\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61llsign\x18\x02 \x01(\tb\x06proto3'
)




_SIMPLE = _descriptor.Descriptor(
  name='Simple',
  full_name='Simple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='Simple.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='callsign', full_name='Simple.callsign', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=60,
)

DESCRIPTOR.message_types_by_name['Simple'] = _SIMPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Simple = _reflection.GeneratedProtocolMessageType('Simple', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLE,
  '__module__' : 'simple_pb2'
  # @@protoc_insertion_point(class_scope:Simple)
  })
_sym_db.RegisterMessage(Simple)


# @@protoc_insertion_point(module_scope)
