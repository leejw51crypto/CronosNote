# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/evm/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ethermint.evm.v1 import params_pb2 as ethermint_dot_evm_dot_v1_dot_params__pb2
from ethermint.evm.v1 import state_pb2 as ethermint_dot_evm_dot_v1_dot_state__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x65thermint/evm/v1/genesis.proto\x12\x10\x65thermint.evm.v1\x1a\x1d\x65thermint/evm/v1/params.proto\x1a\x1c\x65thermint/evm/v1/state.proto\x1a\x14gogoproto/gogo.proto\"x\n\x0cGenesisState\x12\x38\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32 .ethermint.evm.v1.GenesisAccountB\x04\xc8\xde\x1f\x00\x12.\n\x06params\x18\x02 \x01(\x0b\x32\x18.ethermint.evm.v1.ParamsB\x04\xc8\xde\x1f\x00\"j\n\x0eGenesisAccount\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x39\n\x07storage\x18\x03 \x03(\x0b\x32\x17.ethermint.evm.v1.StateB\x0f\xc8\xde\x1f\x00\xaa\xdf\x1f\x07StorageB(Z&github.com/evmos/ethermint/x/evm/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.evm.v1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/evmos/ethermint/x/evm/types'
  _GENESISSTATE.fields_by_name['accounts']._options = None
  _GENESISSTATE.fields_by_name['accounts']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISACCOUNT.fields_by_name['storage']._options = None
  _GENESISACCOUNT.fields_by_name['storage']._serialized_options = b'\310\336\037\000\252\337\037\007Storage'
  _GENESISSTATE._serialized_start=135
  _GENESISSTATE._serialized_end=255
  _GENESISACCOUNT._serialized_start=257
  _GENESISACCOUNT._serialized_end=363
# @@protoc_insertion_point(module_scope)
