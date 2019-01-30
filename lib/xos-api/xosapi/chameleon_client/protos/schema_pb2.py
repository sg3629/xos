#!/usr/bin/env python

# Copyright 2017 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto

from __future__ import absolute_import
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema.proto',
  package='schema',
  syntax='proto3',
  serialized_pb=_b('\n\x0cschema.proto\x12\x06schema\x1a\x1bgoogle/protobuf/empty.proto\"A\n\tProtoFile\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\r\n\x05proto\x18\x02 \x01(\t\x12\x12\n\ndescriptor\x18\x03 \x01(\x0c\"B\n\x07Schemas\x12!\n\x06protos\x18\x01 \x03(\x0b\x32\x11.schema.ProtoFile\x12\x14\n\x0cswagger_from\x18\x02 \x01(\t2G\n\rSchemaService\x12\x36\n\tGetSchema\x12\x16.google.protobuf.Empty\x1a\x0f.schema.Schemas\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_PROTOFILE = _descriptor.Descriptor(
  name='ProtoFile',
  full_name='schema.ProtoFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='schema.ProtoFile.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto', full_name='schema.ProtoFile.proto', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descriptor', full_name='schema.ProtoFile.descriptor', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=118,
)


_SCHEMAS = _descriptor.Descriptor(
  name='Schemas',
  full_name='schema.Schemas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protos', full_name='schema.Schemas.protos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swagger_from', full_name='schema.Schemas.swagger_from', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=186,
)

_SCHEMAS.fields_by_name['protos'].message_type = _PROTOFILE
DESCRIPTOR.message_types_by_name['ProtoFile'] = _PROTOFILE
DESCRIPTOR.message_types_by_name['Schemas'] = _SCHEMAS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtoFile = _reflection.GeneratedProtocolMessageType('ProtoFile', (_message.Message,), dict(
  DESCRIPTOR = _PROTOFILE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.ProtoFile)
  ))
_sym_db.RegisterMessage(ProtoFile)

Schemas = _reflection.GeneratedProtocolMessageType('Schemas', (_message.Message,), dict(
  DESCRIPTOR = _SCHEMAS,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.Schemas)
  ))
_sym_db.RegisterMessage(Schemas)



_SCHEMASERVICE = _descriptor.ServiceDescriptor(
  name='SchemaService',
  full_name='schema.SchemaService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=188,
  serialized_end=259,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSchema',
    full_name='schema.SchemaService.GetSchema',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_SCHEMAS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEMASERVICE)

DESCRIPTOR.services_by_name['SchemaService'] = _SCHEMASERVICE

# @@protoc_insertion_point(module_scope)
