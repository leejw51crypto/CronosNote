# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/vesting/v1beta1/vesting.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from amino import amino_pb2 as amino_dot_amino__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/vesting/v1beta1/vesting.proto\x12\x16\x63osmos.vesting.v1beta1\x1a\x11\x61mino/amino.proto\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/auth/v1beta1/auth.proto\"\x82\x04\n\x12\x42\x61seVestingAccount\x12<\n\x0c\x62\x61se_account\x18\x01 \x01(\x0b\x32 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12{\n\x10original_vesting\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12y\n\x0e\x64\x65legated_free\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12|\n\x11\x64\x65legated_vesting\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\x03:&\x8a\xe7\xb0*\x1d\x63osmos-sdk/BaseVestingAccount\x88\xa0\x1f\x00\"\xac\x01\n\x18\x43ontinuousVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x12\n\nstart_time\x18\x02 \x01(\x03:,\x8a\xe7\xb0*#cosmos-sdk/ContinuousVestingAccount\x88\xa0\x1f\x00\"\x92\x01\n\x15\x44\x65layedVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:)\x8a\xe7\xb0* cosmos-sdk/DelayedVestingAccount\x88\xa0\x1f\x00\"\x8b\x01\n\x06Period\x12\x0e\n\x06length\x18\x01 \x01(\x03\x12q\n\x06\x61mount\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\xec\x01\n\x16PeriodicVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x12\n\nstart_time\x18\x02 \x01(\x03\x12\x42\n\x0fvesting_periods\x18\x03 \x03(\x0b\x32\x1e.cosmos.vesting.v1beta1.PeriodB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:*\x8a\xe7\xb0*!cosmos-sdk/PeriodicVestingAccount\x88\xa0\x1f\x00\"\x94\x01\n\x16PermanentLockedAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:*\x8a\xe7\xb0*!cosmos-sdk/PermanentLockedAccount\x88\xa0\x1f\x00\x42\x33Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.vesting.v1beta1.vesting_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
  _BASEVESTINGACCOUNT.fields_by_name['base_account']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['base_account']._serialized_options = b'\320\336\037\001'
  _BASEVESTINGACCOUNT.fields_by_name['original_vesting']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['original_vesting']._serialized_options = b'\310\336\037\000\250\347\260*\001\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _BASEVESTINGACCOUNT.fields_by_name['delegated_free']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['delegated_free']._serialized_options = b'\310\336\037\000\250\347\260*\001\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _BASEVESTINGACCOUNT.fields_by_name['delegated_vesting']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['delegated_vesting']._serialized_options = b'\310\336\037\000\250\347\260*\001\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _BASEVESTINGACCOUNT._options = None
  _BASEVESTINGACCOUNT._serialized_options = b'\212\347\260*\035cosmos-sdk/BaseVestingAccount\210\240\037\000'
  _CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
  _CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _CONTINUOUSVESTINGACCOUNT._options = None
  _CONTINUOUSVESTINGACCOUNT._serialized_options = b'\212\347\260*#cosmos-sdk/ContinuousVestingAccount\210\240\037\000'
  _DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
  _DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _DELAYEDVESTINGACCOUNT._options = None
  _DELAYEDVESTINGACCOUNT._serialized_options = b'\212\347\260* cosmos-sdk/DelayedVestingAccount\210\240\037\000'
  _PERIOD.fields_by_name['amount']._options = None
  _PERIOD.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
  _PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
  _PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _PERIODICVESTINGACCOUNT._options = None
  _PERIODICVESTINGACCOUNT._serialized_options = b'\212\347\260*!cosmos-sdk/PeriodicVestingAccount\210\240\037\000'
  _PERMANENTLOCKEDACCOUNT.fields_by_name['base_vesting_account']._options = None
  _PERMANENTLOCKEDACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _PERMANENTLOCKEDACCOUNT._options = None
  _PERMANENTLOCKEDACCOUNT._serialized_options = b'\212\347\260*!cosmos-sdk/PermanentLockedAccount\210\240\037\000'
  _BASEVESTINGACCOUNT._serialized_start=170
  _BASEVESTINGACCOUNT._serialized_end=684
  _CONTINUOUSVESTINGACCOUNT._serialized_start=687
  _CONTINUOUSVESTINGACCOUNT._serialized_end=859
  _DELAYEDVESTINGACCOUNT._serialized_start=862
  _DELAYEDVESTINGACCOUNT._serialized_end=1008
  _PERIOD._serialized_start=1011
  _PERIOD._serialized_end=1150
  _PERIODICVESTINGACCOUNT._serialized_start=1153
  _PERIODICVESTINGACCOUNT._serialized_end=1389
  _PERMANENTLOCKEDACCOUNT._serialized_start=1392
  _PERMANENTLOCKEDACCOUNT._serialized_end=1540
# @@protoc_insertion_point(module_scope)
