# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/distribution/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/distribution/v1beta1/genesis.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\x8a\x01\n\x15\x44\x65legatorWithdrawInfo\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x32\n\x10withdraw_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xe0\x01\n!ValidatorOutstandingRewardsRecord\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12s\n\x13outstanding_rewards\x18\x02 \x03(\x0b\x32\x1c.cosmos.base.v1beta1.DecCoinB8\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xcb\x01\n$ValidatorAccumulatedCommissionRecord\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12[\n\x0b\x61\x63\x63umulated\x18\x02 \x01(\x0b\x32;.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xcf\x01\n ValidatorHistoricalRewardsRecord\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12\x0e\n\x06period\x18\x02 \x01(\x04\x12S\n\x07rewards\x18\x03 \x01(\x0b\x32\x37.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb9\x01\n\x1dValidatorCurrentRewardsRecord\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12P\n\x07rewards\x18\x02 \x01(\x0b\x32\x34.cosmos.distribution.v1beta1.ValidatorCurrentRewardsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xf0\x01\n\x1b\x44\x65legatorStartingInfoRecord\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12T\n\rstarting_info\x18\x03 \x01(\x0b\x32\x32.cosmos.distribution.v1beta1.DelegatorStartingInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xdf\x01\n\x19ValidatorSlashEventRecord\x12<\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\x0e\n\x06period\x18\x03 \x01(\x04\x12Z\n\x15validator_slash_event\x18\x04 \x01(\x0b\x32\x30.cosmos.distribution.v1beta1.ValidatorSlashEventB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb6\x07\n\x0cGenesisState\x12>\n\x06params\x18\x01 \x01(\x0b\x32#.cosmos.distribution.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x41\n\x08\x66\x65\x65_pool\x18\x02 \x01(\x0b\x32$.cosmos.distribution.v1beta1.FeePoolB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12_\n\x18\x64\x65legator_withdraw_infos\x18\x03 \x03(\x0b\x32\x32.cosmos.distribution.v1beta1.DelegatorWithdrawInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x33\n\x11previous_proposer\x18\x04 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x66\n\x13outstanding_rewards\x18\x05 \x03(\x0b\x32>.cosmos.distribution.v1beta1.ValidatorOutstandingRewardsRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12w\n!validator_accumulated_commissions\x18\x06 \x03(\x0b\x32\x41.cosmos.distribution.v1beta1.ValidatorAccumulatedCommissionRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12n\n\x1cvalidator_historical_rewards\x18\x07 \x03(\x0b\x32=.cosmos.distribution.v1beta1.ValidatorHistoricalRewardsRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12h\n\x19validator_current_rewards\x18\x08 \x03(\x0b\x32:.cosmos.distribution.v1beta1.ValidatorCurrentRewardsRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x65\n\x18\x64\x65legator_starting_infos\x18\t \x03(\x0b\x32\x38.cosmos.distribution.v1beta1.DelegatorStartingInfoRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x61\n\x16validator_slash_events\x18\n \x03(\x0b\x32\x36.cosmos.distribution.v1beta1.ValidatorSlashEventRecordB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42\x37Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa8\xe2\x1e\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/distribution/types\250\342\036\001'
  _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._options = None
  _DELEGATORWITHDRAWINFO.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._options = None
  _DELEGATORWITHDRAWINFO.fields_by_name['withdraw_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DELEGATORWITHDRAWINFO._options = None
  _DELEGATORWITHDRAWINFO._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._options = None
  _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._options = None
  _VALIDATOROUTSTANDINGREWARDSRECORD.fields_by_name['outstanding_rewards']._serialized_options = b'\252\337\037+github.com/cosmos/cosmos-sdk/types.DecCoins\310\336\037\000\250\347\260*\001'
  _VALIDATOROUTSTANDINGREWARDSRECORD._options = None
  _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._options = None
  _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._options = None
  _VALIDATORACCUMULATEDCOMMISSIONRECORD.fields_by_name['accumulated']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _VALIDATORACCUMULATEDCOMMISSIONRECORD._options = None
  _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._options = None
  _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._options = None
  _VALIDATORHISTORICALREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _VALIDATORHISTORICALREWARDSRECORD._options = None
  _VALIDATORHISTORICALREWARDSRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._options = None
  _VALIDATORCURRENTREWARDSRECORD.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._options = None
  _VALIDATORCURRENTREWARDSRECORD.fields_by_name['rewards']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _VALIDATORCURRENTREWARDSRECORD._options = None
  _VALIDATORCURRENTREWARDSRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._options = None
  _DELEGATORSTARTINGINFORECORD.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._options = None
  _DELEGATORSTARTINGINFORECORD.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._options = None
  _DELEGATORSTARTINGINFORECORD.fields_by_name['starting_info']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _DELEGATORSTARTINGINFORECORD._options = None
  _DELEGATORSTARTINGINFORECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._options = None
  _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._options = None
  _VALIDATORSLASHEVENTRECORD.fields_by_name['validator_slash_event']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _VALIDATORSLASHEVENTRECORD._options = None
  _VALIDATORSLASHEVENTRECORD._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['fee_pool']._options = None
  _GENESISSTATE.fields_by_name['fee_pool']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._options = None
  _GENESISSTATE.fields_by_name['delegator_withdraw_infos']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['previous_proposer']._options = None
  _GENESISSTATE.fields_by_name['previous_proposer']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _GENESISSTATE.fields_by_name['outstanding_rewards']._options = None
  _GENESISSTATE.fields_by_name['outstanding_rewards']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._options = None
  _GENESISSTATE.fields_by_name['validator_accumulated_commissions']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['validator_historical_rewards']._options = None
  _GENESISSTATE.fields_by_name['validator_historical_rewards']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['validator_current_rewards']._options = None
  _GENESISSTATE.fields_by_name['validator_current_rewards']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['delegator_starting_infos']._options = None
  _GENESISSTATE.fields_by_name['delegator_starting_infos']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['validator_slash_events']._options = None
  _GENESISSTATE.fields_by_name['validator_slash_events']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE._options = None
  _GENESISSTATE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _DELEGATORWITHDRAWINFO._serialized_start=223
  _DELEGATORWITHDRAWINFO._serialized_end=361
  _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_start=364
  _VALIDATOROUTSTANDINGREWARDSRECORD._serialized_end=588
  _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_start=591
  _VALIDATORACCUMULATEDCOMMISSIONRECORD._serialized_end=794
  _VALIDATORHISTORICALREWARDSRECORD._serialized_start=797
  _VALIDATORHISTORICALREWARDSRECORD._serialized_end=1004
  _VALIDATORCURRENTREWARDSRECORD._serialized_start=1007
  _VALIDATORCURRENTREWARDSRECORD._serialized_end=1192
  _DELEGATORSTARTINGINFORECORD._serialized_start=1195
  _DELEGATORSTARTINGINFORECORD._serialized_end=1435
  _VALIDATORSLASHEVENTRECORD._serialized_start=1438
  _VALIDATORSLASHEVENTRECORD._serialized_end=1661
  _GENESISSTATE._serialized_start=1664
  _GENESISSTATE._serialized_end=2614
# @@protoc_insertion_point(module_scope)