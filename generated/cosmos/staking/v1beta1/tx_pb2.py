# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/staking/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/staking/v1beta1/tx.proto\x12\x16\x63osmos.staking.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\"\x9c\x04\n\x12MsgCreateValidator\x12\x43\n\x0b\x64\x65scription\x18\x01 \x01(\x0b\x32#.cosmos.staking.v1beta1.DescriptionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x46\n\ncommission\x18\x02 \x01(\x0b\x32\'.cosmos.staking.v1beta1.CommissionRatesB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12M\n\x13min_self_delegation\x18\x03 \x01(\tB0\xd2\xb4-\ncosmos.Int\xda\xde\x1f\x15\x63osmossdk.io/math.Int\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x35\n\x11\x64\x65legator_address\x18\x04 \x01(\tB\x1a\x18\x01\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x11validator_address\x18\x05 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12>\n\x06pubkey\x18\x06 \x01(\x0b\x32\x14.google.protobuf.AnyB\x18\xca\xb4-\x14\x63osmos.crypto.PubKey\x12\x33\n\x05value\x18\x07 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:@\x82\xe7\xb0*\x11validator_address\x8a\xe7\xb0*\x1d\x63osmos-sdk/MsgCreateValidator\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1c\n\x1aMsgCreateValidatorResponse\"\xe3\x02\n\x10MsgEditValidator\x12\x43\n\x0b\x64\x65scription\x18\x01 \x01(\x0b\x32#.cosmos.staking.v1beta1.DescriptionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12<\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12\x46\n\x0f\x63ommission_rate\x18\x03 \x01(\tB-\xd2\xb4-\ncosmos.Dec\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\x12\x44\n\x13min_self_delegation\x18\x04 \x01(\tB\'\xd2\xb4-\ncosmos.Int\xda\xde\x1f\x15\x63osmossdk.io/math.Int:>\x82\xe7\xb0*\x11validator_address\x8a\xe7\xb0*\x1b\x63osmos-sdk/MsgEditValidator\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1a\n\x18MsgEditValidatorResponse\"\xf1\x01\n\x0bMsgDelegate\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12\x34\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:9\x82\xe7\xb0*\x11\x64\x65legator_address\x8a\xe7\xb0*\x16\x63osmos-sdk/MsgDelegate\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x15\n\x13MsgDelegateResponse\"\xc5\x02\n\x12MsgBeginRedelegate\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12@\n\x15validator_src_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12@\n\x15validator_dst_address\x18\x03 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12\x34\n\x06\x61mount\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:@\x82\xe7\xb0*\x11\x64\x65legator_address\x8a\xe7\xb0*\x1d\x63osmos-sdk/MsgBeginRedelegate\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"`\n\x1aMsgBeginRedelegateResponse\x12\x42\n\x0f\x63ompletion_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x90\xdf\x1f\x01\"\xf5\x01\n\rMsgUndelegate\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12\x34\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:;\x82\xe7\xb0*\x11\x64\x65legator_address\x8a\xe7\xb0*\x18\x63osmos-sdk/MsgUndelegate\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x91\x01\n\x15MsgUndelegateResponse\x12\x42\n\x0f\x63ompletion_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x90\xdf\x1f\x01\x12\x34\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\xac\x02\n\x1cMsgCancelUnbondingDelegation\x12\x33\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressString\x12\x34\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x17\n\x0f\x63reation_height\x18\x04 \x01(\x03:J\x82\xe7\xb0*\x11\x64\x65legator_address\x8a\xe7\xb0*\'cosmos-sdk/MsgCancelUnbondingDelegation\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"&\n$MsgCancelUnbondingDelegationResponse\"\xb2\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x39\n\x06params\x18\x02 \x01(\x0b\x32\x1e.cosmos.staking.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:7\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*$cosmos-sdk/x/staking/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse2\x9d\x06\n\x03Msg\x12q\n\x0f\x43reateValidator\x12*.cosmos.staking.v1beta1.MsgCreateValidator\x1a\x32.cosmos.staking.v1beta1.MsgCreateValidatorResponse\x12k\n\rEditValidator\x12(.cosmos.staking.v1beta1.MsgEditValidator\x1a\x30.cosmos.staking.v1beta1.MsgEditValidatorResponse\x12\\\n\x08\x44\x65legate\x12#.cosmos.staking.v1beta1.MsgDelegate\x1a+.cosmos.staking.v1beta1.MsgDelegateResponse\x12q\n\x0f\x42\x65ginRedelegate\x12*.cosmos.staking.v1beta1.MsgBeginRedelegate\x1a\x32.cosmos.staking.v1beta1.MsgBeginRedelegateResponse\x12\x62\n\nUndelegate\x12%.cosmos.staking.v1beta1.MsgUndelegate\x1a-.cosmos.staking.v1beta1.MsgUndelegateResponse\x12\x8f\x01\n\x19\x43\x61ncelUnbondingDelegation\x12\x34.cosmos.staking.v1beta1.MsgCancelUnbondingDelegation\x1a<.cosmos.staking.v1beta1.MsgCancelUnbondingDelegationResponse\x12h\n\x0cUpdateParams\x12\'.cosmos.staking.v1beta1.MsgUpdateParams\x1a/.cosmos.staking.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
  _MSGCREATEVALIDATOR.fields_by_name['description']._options = None
  _MSGCREATEVALIDATOR.fields_by_name['description']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGCREATEVALIDATOR.fields_by_name['commission']._options = None
  _MSGCREATEVALIDATOR.fields_by_name['commission']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGCREATEVALIDATOR.fields_by_name['min_self_delegation']._options = None
  _MSGCREATEVALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\322\264-\ncosmos.Int\332\336\037\025cosmossdk.io/math.Int\310\336\037\000\250\347\260*\001'
  _MSGCREATEVALIDATOR.fields_by_name['delegator_address']._options = None
  _MSGCREATEVALIDATOR.fields_by_name['delegator_address']._serialized_options = b'\030\001\322\264-\024cosmos.AddressString'
  _MSGCREATEVALIDATOR.fields_by_name['validator_address']._options = None
  _MSGCREATEVALIDATOR.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _MSGCREATEVALIDATOR.fields_by_name['pubkey']._options = None
  _MSGCREATEVALIDATOR.fields_by_name['pubkey']._serialized_options = b'\312\264-\024cosmos.crypto.PubKey'
  _MSGCREATEVALIDATOR.fields_by_name['value']._options = None
  _MSGCREATEVALIDATOR.fields_by_name['value']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGCREATEVALIDATOR._options = None
  _MSGCREATEVALIDATOR._serialized_options = b'\202\347\260*\021validator_address\212\347\260*\035cosmos-sdk/MsgCreateValidator\350\240\037\000\210\240\037\000'
  _MSGEDITVALIDATOR.fields_by_name['description']._options = None
  _MSGEDITVALIDATOR.fields_by_name['description']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGEDITVALIDATOR.fields_by_name['validator_address']._options = None
  _MSGEDITVALIDATOR.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _MSGEDITVALIDATOR.fields_by_name['commission_rate']._options = None
  _MSGEDITVALIDATOR.fields_by_name['commission_rate']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037\033cosmossdk.io/math.LegacyDec'
  _MSGEDITVALIDATOR.fields_by_name['min_self_delegation']._options = None
  _MSGEDITVALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\322\264-\ncosmos.Int\332\336\037\025cosmossdk.io/math.Int'
  _MSGEDITVALIDATOR._options = None
  _MSGEDITVALIDATOR._serialized_options = b'\202\347\260*\021validator_address\212\347\260*\033cosmos-sdk/MsgEditValidator\350\240\037\000\210\240\037\000'
  _MSGDELEGATE.fields_by_name['delegator_address']._options = None
  _MSGDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGDELEGATE.fields_by_name['validator_address']._options = None
  _MSGDELEGATE.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _MSGDELEGATE.fields_by_name['amount']._options = None
  _MSGDELEGATE.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGDELEGATE._options = None
  _MSGDELEGATE._serialized_options = b'\202\347\260*\021delegator_address\212\347\260*\026cosmos-sdk/MsgDelegate\350\240\037\000\210\240\037\000'
  _MSGBEGINREDELEGATE.fields_by_name['delegator_address']._options = None
  _MSGBEGINREDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGBEGINREDELEGATE.fields_by_name['validator_src_address']._options = None
  _MSGBEGINREDELEGATE.fields_by_name['validator_src_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _MSGBEGINREDELEGATE.fields_by_name['validator_dst_address']._options = None
  _MSGBEGINREDELEGATE.fields_by_name['validator_dst_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _MSGBEGINREDELEGATE.fields_by_name['amount']._options = None
  _MSGBEGINREDELEGATE.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGBEGINREDELEGATE._options = None
  _MSGBEGINREDELEGATE._serialized_options = b'\202\347\260*\021delegator_address\212\347\260*\035cosmos-sdk/MsgBeginRedelegate\350\240\037\000\210\240\037\000'
  _MSGBEGINREDELEGATERESPONSE.fields_by_name['completion_time']._options = None
  _MSGBEGINREDELEGATERESPONSE.fields_by_name['completion_time']._serialized_options = b'\310\336\037\000\250\347\260*\001\220\337\037\001'
  _MSGUNDELEGATE.fields_by_name['delegator_address']._options = None
  _MSGUNDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUNDELEGATE.fields_by_name['validator_address']._options = None
  _MSGUNDELEGATE.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _MSGUNDELEGATE.fields_by_name['amount']._options = None
  _MSGUNDELEGATE.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGUNDELEGATE._options = None
  _MSGUNDELEGATE._serialized_options = b'\202\347\260*\021delegator_address\212\347\260*\030cosmos-sdk/MsgUndelegate\350\240\037\000\210\240\037\000'
  _MSGUNDELEGATERESPONSE.fields_by_name['completion_time']._options = None
  _MSGUNDELEGATERESPONSE.fields_by_name['completion_time']._serialized_options = b'\310\336\037\000\250\347\260*\001\220\337\037\001'
  _MSGUNDELEGATERESPONSE.fields_by_name['amount']._options = None
  _MSGUNDELEGATERESPONSE.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGCANCELUNBONDINGDELEGATION.fields_by_name['delegator_address']._options = None
  _MSGCANCELUNBONDINGDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCANCELUNBONDINGDELEGATION.fields_by_name['validator_address']._options = None
  _MSGCANCELUNBONDINGDELEGATION.fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _MSGCANCELUNBONDINGDELEGATION.fields_by_name['amount']._options = None
  _MSGCANCELUNBONDINGDELEGATION.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGCANCELUNBONDINGDELEGATION._options = None
  _MSGCANCELUNBONDINGDELEGATION._serialized_options = b'\202\347\260*\021delegator_address\212\347\260*\'cosmos-sdk/MsgCancelUnbondingDelegation\350\240\037\000\210\240\037\000'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority\212\347\260*$cosmos-sdk/x/staking/MsgUpdateParams'
  _MSG._options = None
  _MSG._serialized_options = b'\200\347\260*\001'
  _MSGCREATEVALIDATOR._serialized_start=283
  _MSGCREATEVALIDATOR._serialized_end=823
  _MSGCREATEVALIDATORRESPONSE._serialized_start=825
  _MSGCREATEVALIDATORRESPONSE._serialized_end=853
  _MSGEDITVALIDATOR._serialized_start=856
  _MSGEDITVALIDATOR._serialized_end=1211
  _MSGEDITVALIDATORRESPONSE._serialized_start=1213
  _MSGEDITVALIDATORRESPONSE._serialized_end=1239
  _MSGDELEGATE._serialized_start=1242
  _MSGDELEGATE._serialized_end=1483
  _MSGDELEGATERESPONSE._serialized_start=1485
  _MSGDELEGATERESPONSE._serialized_end=1506
  _MSGBEGINREDELEGATE._serialized_start=1509
  _MSGBEGINREDELEGATE._serialized_end=1834
  _MSGBEGINREDELEGATERESPONSE._serialized_start=1836
  _MSGBEGINREDELEGATERESPONSE._serialized_end=1932
  _MSGUNDELEGATE._serialized_start=1935
  _MSGUNDELEGATE._serialized_end=2180
  _MSGUNDELEGATERESPONSE._serialized_start=2183
  _MSGUNDELEGATERESPONSE._serialized_end=2328
  _MSGCANCELUNBONDINGDELEGATION._serialized_start=2331
  _MSGCANCELUNBONDINGDELEGATION._serialized_end=2631
  _MSGCANCELUNBONDINGDELEGATIONRESPONSE._serialized_start=2633
  _MSGCANCELUNBONDINGDELEGATIONRESPONSE._serialized_end=2671
  _MSGUPDATEPARAMS._serialized_start=2674
  _MSGUPDATEPARAMS._serialized_end=2852
  _MSGUPDATEPARAMSRESPONSE._serialized_start=2854
  _MSGUPDATEPARAMSRESPONSE._serialized_end=2879
  _MSG._serialized_start=2882
  _MSG._serialized_end=3679
# @@protoc_insertion_point(module_scope)
