# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/bank/v1beta1/genesis.proto\x12\x13\x63osmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xf9\x02\n\x0cGenesisState\x12\x36\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x39\n\x08\x62\x61lances\x18\x02 \x03(\x0b\x32\x1c.cosmos.bank.v1beta1.BalanceB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12q\n\x06supply\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12@\n\x0e\x64\x65nom_metadata\x18\x04 \x03(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x41\n\x0csend_enabled\x18\x05 \x03(\x0b\x32 .cosmos.bank.v1beta1.SendEnabledB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\xb0\x01\n\x07\x42\x61lance\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12p\n\x05\x63oins\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['balances']._options = None
  _GENESISSTATE.fields_by_name['balances']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['supply']._options = None
  _GENESISSTATE.fields_by_name['supply']._serialized_options = b'\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['denom_metadata']._options = None
  _GENESISSTATE.fields_by_name['denom_metadata']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['send_enabled']._options = None
  _GENESISSTATE.fields_by_name['send_enabled']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _BALANCE.fields_by_name['address']._options = None
  _BALANCE.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _BALANCE.fields_by_name['coins']._options = None
  _BALANCE.fields_by_name['coins']._serialized_options = b'\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\310\336\037\000\250\347\260*\001'
  _BALANCE._options = None
  _BALANCE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GENESISSTATE._serialized_start=191
  _GENESISSTATE._serialized_end=568
  _BALANCE._serialized_start=571
  _BALANCE._serialized_end=747
# @@protoc_insertion_point(module_scope)
