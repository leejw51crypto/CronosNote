# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/evm/v1/params_v4.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ethermint.evm.v1 import chain_config_v0_pb2 as ethermint_dot_evm_dot_v1_dot_chain__config__v0__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ethermint/evm/v1/params_v4.proto\x12\x10\x65thermint.evm.v1\x1a\x14gogoproto/gogo.proto\x1a&ethermint/evm/v1/chain_config_v0.proto\"\xb1\x02\n\x08V4Params\x12\'\n\tevm_denom\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"evm_denom\"\x12/\n\renable_create\x18\x02 \x01(\x08\x42\x18\xf2\xde\x1f\x14yaml:\"enable_create\"\x12+\n\x0b\x65nable_call\x18\x03 \x01(\x08\x42\x16\xf2\xde\x1f\x12yaml:\"enable_call\"\x12\x42\n\nextra_eips\x18\x04 \x01(\x0b\x32\x1b.ethermint.evm.v1.ExtraEIPsB\x11\xe2\xde\x1f\tExtraEIPs\xc8\xde\x1f\x00\x12;\n\x0c\x63hain_config\x18\x05 \x01(\x0b\x32\x1f.ethermint.evm.v1.V0ChainConfigB\x04\xc8\xde\x1f\x00\x12\x1d\n\x15\x61llow_unprotected_txs\x18\x06 \x01(\x08\"2\n\tExtraEIPs\x12%\n\x04\x65ips\x18\x01 \x03(\x03\x42\x17\xe2\xde\x1f\x04\x45IPs\xf2\xde\x1f\x0byaml:\"eips\"B(Z&github.com/evmos/ethermint/x/evm/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.evm.v1.params_v4_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/evmos/ethermint/x/evm/types'
  _V4PARAMS.fields_by_name['evm_denom']._options = None
  _V4PARAMS.fields_by_name['evm_denom']._serialized_options = b'\362\336\037\020yaml:\"evm_denom\"'
  _V4PARAMS.fields_by_name['enable_create']._options = None
  _V4PARAMS.fields_by_name['enable_create']._serialized_options = b'\362\336\037\024yaml:\"enable_create\"'
  _V4PARAMS.fields_by_name['enable_call']._options = None
  _V4PARAMS.fields_by_name['enable_call']._serialized_options = b'\362\336\037\022yaml:\"enable_call\"'
  _V4PARAMS.fields_by_name['extra_eips']._options = None
  _V4PARAMS.fields_by_name['extra_eips']._serialized_options = b'\342\336\037\tExtraEIPs\310\336\037\000'
  _V4PARAMS.fields_by_name['chain_config']._options = None
  _V4PARAMS.fields_by_name['chain_config']._serialized_options = b'\310\336\037\000'
  _EXTRAEIPS.fields_by_name['eips']._options = None
  _EXTRAEIPS.fields_by_name['eips']._serialized_options = b'\342\336\037\004EIPs\362\336\037\013yaml:\"eips\"'
  _V4PARAMS._serialized_start=117
  _V4PARAMS._serialized_end=422
  _EXTRAEIPS._serialized_start=424
  _EXTRAEIPS._serialized_end=474
# @@protoc_insertion_point(module_scope)
