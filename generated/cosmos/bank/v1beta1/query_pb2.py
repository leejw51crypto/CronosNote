# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/bank/v1beta1/query.proto\x12\x13\x63osmos.bank.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1b\x63osmos/query/v1/query.proto\x1a\x11\x61mino/amino.proto\"Y\n\x13QueryBalanceRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"B\n\x14QueryBalanceResponse\x12*\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.Coin\"\xa1\x01\n\x17QueryAllBalancesRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\x12\x15\n\rresolve_denom\x18\x03 \x01(\x08:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xcc\x01\n\x18QueryAllBalancesResponse\x12s\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x90\x01\n\x1dQuerySpendableBalancesRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xd2\x01\n\x1eQuerySpendableBalancesResponse\x12s\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"i\n#QuerySpendableBalanceByDenomRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"R\n$QuerySpendableBalanceByDenomResponse\x12*\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.Coin\"_\n\x17QueryTotalSupplyRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xca\x01\n\x18QueryTotalSupplyResponse\x12q\n\x06supply\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x9a\xe7\xb0*\x0clegacy_coins\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"%\n\x14QuerySupplyOfRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"M\n\x15QuerySupplyOfResponse\x12\x34\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x14\n\x12QueryParamsRequest\"M\n\x13QueryParamsResponse\x12\x36\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"X\n\x1aQueryDenomsMetadataRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x97\x01\n\x1bQueryDenomsMetadataResponse\x12;\n\tmetadatas\x18\x01 \x03(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"*\n\x19QueryDenomMetadataRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"X\n\x1aQueryDenomMetadataResponse\x12:\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"7\n&QueryDenomMetadataByQueryStringRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"e\n\'QueryDenomMetadataByQueryStringResponse\x12:\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"d\n\x17QueryDenomOwnersRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"n\n\nDenomOwner\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x35\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x8e\x01\n\x18QueryDenomOwnersResponse\x12\x35\n\x0c\x64\x65nom_owners\x18\x01 \x03(\x0b\x32\x1f.cosmos.bank.v1beta1.DenomOwner\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"e\n\x17QuerySendEnabledRequest\x12\x0e\n\x06\x64\x65noms\x18\x01 \x03(\t\x12:\n\npagination\x18\x63 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x8f\x01\n\x18QuerySendEnabledResponse\x12\x36\n\x0csend_enabled\x18\x01 \x03(\x0b\x32 .cosmos.bank.v1beta1.SendEnabled\x12;\n\npagination\x18\x63 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x8f\x10\n\x05Query\x12\x9d\x01\n\x07\x42\x61lance\x12(.cosmos.bank.v1beta1.QueryBalanceRequest\x1a).cosmos.bank.v1beta1.QueryBalanceResponse\"=\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x32\x12\x30/cosmos/bank/v1beta1/balances/{address}/by_denom\x12\xa0\x01\n\x0b\x41llBalances\x12,.cosmos.bank.v1beta1.QueryAllBalancesRequest\x1a-.cosmos.bank.v1beta1.QueryAllBalancesResponse\"4\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02)\x12\'/cosmos/bank/v1beta1/balances/{address}\x12\xbc\x01\n\x11SpendableBalances\x12\x32.cosmos.bank.v1beta1.QuerySpendableBalancesRequest\x1a\x33.cosmos.bank.v1beta1.QuerySpendableBalancesResponse\">\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x33\x12\x31/cosmos/bank/v1beta1/spendable_balances/{address}\x12\xd7\x01\n\x17SpendableBalanceByDenom\x12\x38.cosmos.bank.v1beta1.QuerySpendableBalanceByDenomRequest\x1a\x39.cosmos.bank.v1beta1.QuerySpendableBalanceByDenomResponse\"G\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02<\x12:/cosmos/bank/v1beta1/spendable_balances/{address}/by_denom\x12\x94\x01\n\x0bTotalSupply\x12,.cosmos.bank.v1beta1.QueryTotalSupplyRequest\x1a-.cosmos.bank.v1beta1.QueryTotalSupplyResponse\"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/supply\x12\x94\x01\n\x08SupplyOf\x12).cosmos.bank.v1beta1.QuerySupplyOfRequest\x1a*.cosmos.bank.v1beta1.QuerySupplyOfResponse\"1\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/supply/by_denom\x12\x85\x01\n\x06Params\x12\'.cosmos.bank.v1beta1.QueryParamsRequest\x1a(.cosmos.bank.v1beta1.QueryParamsResponse\"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/params\x12\xab\x01\n\rDenomMetadata\x12..cosmos.bank.v1beta1.QueryDenomMetadataRequest\x1a/.cosmos.bank.v1beta1.QueryDenomMetadataResponse\"9\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02.\x12,/cosmos/bank/v1beta1/denoms_metadata/{denom}\x12\xda\x01\n\x1a\x44\x65nomMetadataByQueryString\x12;.cosmos.bank.v1beta1.QueryDenomMetadataByQueryStringRequest\x1a<.cosmos.bank.v1beta1.QueryDenomMetadataByQueryStringResponse\"A\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/bank/v1beta1/denoms_metadata_by_query_string\x12\xa6\x01\n\x0e\x44\x65nomsMetadata\x12/.cosmos.bank.v1beta1.QueryDenomsMetadataRequest\x1a\x30.cosmos.bank.v1beta1.QueryDenomsMetadataResponse\"1\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/denoms_metadata\x12\xa2\x01\n\x0b\x44\x65nomOwners\x12,.cosmos.bank.v1beta1.QueryDenomOwnersRequest\x1a-.cosmos.bank.v1beta1.QueryDenomOwnersResponse\"6\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02+\x12)/cosmos/bank/v1beta1/denom_owners/{denom}\x12\x9a\x01\n\x0bSendEnabled\x12,.cosmos.bank.v1beta1.QuerySendEnabledRequest\x1a-.cosmos.bank.v1beta1.QuerySendEnabledResponse\".\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02#\x12!/cosmos/bank/v1beta1/send_enabledB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
  _QUERYBALANCEREQUEST.fields_by_name['address']._options = None
  _QUERYBALANCEREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYBALANCEREQUEST._options = None
  _QUERYBALANCEREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYALLBALANCESREQUEST.fields_by_name['address']._options = None
  _QUERYALLBALANCESREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYALLBALANCESREQUEST._options = None
  _QUERYALLBALANCESREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._options = None
  _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._serialized_options = b'\310\336\037\000\250\347\260*\001\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYSPENDABLEBALANCESREQUEST.fields_by_name['address']._options = None
  _QUERYSPENDABLEBALANCESREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYSPENDABLEBALANCESREQUEST._options = None
  _QUERYSPENDABLEBALANCESREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYSPENDABLEBALANCESRESPONSE.fields_by_name['balances']._options = None
  _QUERYSPENDABLEBALANCESRESPONSE.fields_by_name['balances']._serialized_options = b'\310\336\037\000\250\347\260*\001\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYSPENDABLEBALANCEBYDENOMREQUEST.fields_by_name['address']._options = None
  _QUERYSPENDABLEBALANCEBYDENOMREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYSPENDABLEBALANCEBYDENOMREQUEST._options = None
  _QUERYSPENDABLEBALANCEBYDENOMREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYTOTALSUPPLYREQUEST._options = None
  _QUERYTOTALSUPPLYREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._options = None
  _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._serialized_options = b'\310\336\037\000\250\347\260*\001\232\347\260*\014legacy_coins\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._options = None
  _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._options = None
  _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._options = None
  _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYDENOMMETADATABYQUERYSTRINGRESPONSE.fields_by_name['metadata']._options = None
  _QUERYDENOMMETADATABYQUERYSTRINGRESPONSE.fields_by_name['metadata']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _DENOMOWNER.fields_by_name['address']._options = None
  _DENOMOWNER.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _DENOMOWNER.fields_by_name['balance']._options = None
  _DENOMOWNER.fields_by_name['balance']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERY.methods_by_name['Balance']._options = None
  _QUERY.methods_by_name['Balance']._serialized_options = b'\210\347\260*\001\202\323\344\223\0022\0220/cosmos/bank/v1beta1/balances/{address}/by_denom'
  _QUERY.methods_by_name['AllBalances']._options = None
  _QUERY.methods_by_name['AllBalances']._serialized_options = b'\210\347\260*\001\202\323\344\223\002)\022\'/cosmos/bank/v1beta1/balances/{address}'
  _QUERY.methods_by_name['SpendableBalances']._options = None
  _QUERY.methods_by_name['SpendableBalances']._serialized_options = b'\210\347\260*\001\202\323\344\223\0023\0221/cosmos/bank/v1beta1/spendable_balances/{address}'
  _QUERY.methods_by_name['SpendableBalanceByDenom']._options = None
  _QUERY.methods_by_name['SpendableBalanceByDenom']._serialized_options = b'\210\347\260*\001\202\323\344\223\002<\022:/cosmos/bank/v1beta1/spendable_balances/{address}/by_denom'
  _QUERY.methods_by_name['TotalSupply']._options = None
  _QUERY.methods_by_name['TotalSupply']._serialized_options = b'\210\347\260*\001\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/supply'
  _QUERY.methods_by_name['SupplyOf']._options = None
  _QUERY.methods_by_name['SupplyOf']._serialized_options = b'\210\347\260*\001\202\323\344\223\002&\022$/cosmos/bank/v1beta1/supply/by_denom'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\210\347\260*\001\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/params'
  _QUERY.methods_by_name['DenomMetadata']._options = None
  _QUERY.methods_by_name['DenomMetadata']._serialized_options = b'\210\347\260*\001\202\323\344\223\002.\022,/cosmos/bank/v1beta1/denoms_metadata/{denom}'
  _QUERY.methods_by_name['DenomMetadataByQueryString']._options = None
  _QUERY.methods_by_name['DenomMetadataByQueryString']._serialized_options = b'\210\347\260*\001\202\323\344\223\0026\0224/cosmos/bank/v1beta1/denoms_metadata_by_query_string'
  _QUERY.methods_by_name['DenomsMetadata']._options = None
  _QUERY.methods_by_name['DenomsMetadata']._serialized_options = b'\210\347\260*\001\202\323\344\223\002&\022$/cosmos/bank/v1beta1/denoms_metadata'
  _QUERY.methods_by_name['DenomOwners']._options = None
  _QUERY.methods_by_name['DenomOwners']._serialized_options = b'\210\347\260*\001\202\323\344\223\002+\022)/cosmos/bank/v1beta1/denom_owners/{denom}'
  _QUERY.methods_by_name['SendEnabled']._options = None
  _QUERY.methods_by_name['SendEnabled']._serialized_options = b'\210\347\260*\001\202\323\344\223\002#\022!/cosmos/bank/v1beta1/send_enabled'
  _QUERYBALANCEREQUEST._serialized_start=291
  _QUERYBALANCEREQUEST._serialized_end=380
  _QUERYBALANCERESPONSE._serialized_start=382
  _QUERYBALANCERESPONSE._serialized_end=448
  _QUERYALLBALANCESREQUEST._serialized_start=451
  _QUERYALLBALANCESREQUEST._serialized_end=612
  _QUERYALLBALANCESRESPONSE._serialized_start=615
  _QUERYALLBALANCESRESPONSE._serialized_end=819
  _QUERYSPENDABLEBALANCESREQUEST._serialized_start=822
  _QUERYSPENDABLEBALANCESREQUEST._serialized_end=966
  _QUERYSPENDABLEBALANCESRESPONSE._serialized_start=969
  _QUERYSPENDABLEBALANCESRESPONSE._serialized_end=1179
  _QUERYSPENDABLEBALANCEBYDENOMREQUEST._serialized_start=1181
  _QUERYSPENDABLEBALANCEBYDENOMREQUEST._serialized_end=1286
  _QUERYSPENDABLEBALANCEBYDENOMRESPONSE._serialized_start=1288
  _QUERYSPENDABLEBALANCEBYDENOMRESPONSE._serialized_end=1370
  _QUERYTOTALSUPPLYREQUEST._serialized_start=1372
  _QUERYTOTALSUPPLYREQUEST._serialized_end=1467
  _QUERYTOTALSUPPLYRESPONSE._serialized_start=1470
  _QUERYTOTALSUPPLYRESPONSE._serialized_end=1672
  _QUERYSUPPLYOFREQUEST._serialized_start=1674
  _QUERYSUPPLYOFREQUEST._serialized_end=1711
  _QUERYSUPPLYOFRESPONSE._serialized_start=1713
  _QUERYSUPPLYOFRESPONSE._serialized_end=1790
  _QUERYPARAMSREQUEST._serialized_start=1792
  _QUERYPARAMSREQUEST._serialized_end=1812
  _QUERYPARAMSRESPONSE._serialized_start=1814
  _QUERYPARAMSRESPONSE._serialized_end=1891
  _QUERYDENOMSMETADATAREQUEST._serialized_start=1893
  _QUERYDENOMSMETADATAREQUEST._serialized_end=1981
  _QUERYDENOMSMETADATARESPONSE._serialized_start=1984
  _QUERYDENOMSMETADATARESPONSE._serialized_end=2135
  _QUERYDENOMMETADATAREQUEST._serialized_start=2137
  _QUERYDENOMMETADATAREQUEST._serialized_end=2179
  _QUERYDENOMMETADATARESPONSE._serialized_start=2181
  _QUERYDENOMMETADATARESPONSE._serialized_end=2269
  _QUERYDENOMMETADATABYQUERYSTRINGREQUEST._serialized_start=2271
  _QUERYDENOMMETADATABYQUERYSTRINGREQUEST._serialized_end=2326
  _QUERYDENOMMETADATABYQUERYSTRINGRESPONSE._serialized_start=2328
  _QUERYDENOMMETADATABYQUERYSTRINGRESPONSE._serialized_end=2429
  _QUERYDENOMOWNERSREQUEST._serialized_start=2431
  _QUERYDENOMOWNERSREQUEST._serialized_end=2531
  _DENOMOWNER._serialized_start=2533
  _DENOMOWNER._serialized_end=2643
  _QUERYDENOMOWNERSRESPONSE._serialized_start=2646
  _QUERYDENOMOWNERSRESPONSE._serialized_end=2788
  _QUERYSENDENABLEDREQUEST._serialized_start=2790
  _QUERYSENDENABLEDREQUEST._serialized_end=2891
  _QUERYSENDENABLEDRESPONSE._serialized_start=2894
  _QUERYSENDENABLEDRESPONSE._serialized_end=3037
  _QUERY._serialized_start=3040
  _QUERY._serialized_end=5103
# @@protoc_insertion_point(module_scope)