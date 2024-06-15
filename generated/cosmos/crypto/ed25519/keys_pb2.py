# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/crypto/ed25519/keys.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from amino import amino_pb2 as amino_dot_amino__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/crypto/ed25519/keys.proto\x12\x15\x63osmos.crypto.ed25519\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\"d\n\x06PubKey\x12)\n\x03key\x18\x01 \x01(\x0c\x42\x1c\xfa\xde\x1f\x18\x63rypto/ed25519.PublicKey:/\x8a\xe7\xb0*\x18tendermint/PubKeyEd25519\x92\xe7\xb0*\tkey_field\x98\xa0\x1f\x00\"c\n\x07PrivKey\x12*\n\x03key\x18\x01 \x01(\x0c\x42\x1d\xfa\xde\x1f\x19\x63rypto/ed25519.PrivateKey:,\x8a\xe7\xb0*\x19tendermint/PrivKeyEd25519\x92\xe7\xb0*\tkey_fieldB2Z0github.com/cosmos/cosmos-sdk/crypto/keys/ed25519b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crypto.ed25519.keys_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/cosmos/cosmos-sdk/crypto/keys/ed25519'
  _PUBKEY.fields_by_name['key']._options = None
  _PUBKEY.fields_by_name['key']._serialized_options = b'\372\336\037\030crypto/ed25519.PublicKey'
  _PUBKEY._options = None
  _PUBKEY._serialized_options = b'\212\347\260*\030tendermint/PubKeyEd25519\222\347\260*\tkey_field\230\240\037\000'
  _PRIVKEY.fields_by_name['key']._options = None
  _PRIVKEY.fields_by_name['key']._serialized_options = b'\372\336\037\031crypto/ed25519.PrivateKey'
  _PRIVKEY._options = None
  _PRIVKEY._serialized_options = b'\212\347\260*\031tendermint/PrivKeyEd25519\222\347\260*\tkey_field'
  _PUBKEY._serialized_start=100
  _PUBKEY._serialized_end=200
  _PRIVKEY._serialized_start=202
  _PRIVKEY._serialized_end=301
# @@protoc_insertion_point(module_scope)