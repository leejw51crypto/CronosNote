# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/circuit/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from cosmos.circuit.v1 import types_pb2 as cosmos_dot_circuit_dot_v1_dot_types__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63osmos/circuit/v1/query.proto\x12\x11\x63osmos.circuit.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1d\x63osmos/circuit/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x63osmos/query/v1/query.proto\"&\n\x13QueryAccountRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"E\n\x0f\x41\x63\x63ountResponse\x12\x32\n\npermission\x18\x01 \x01(\x0b\x32\x1e.cosmos.circuit.v1.Permissions\"R\n\x14QueryAccountsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x8f\x01\n\x10\x41\x63\x63ountsResponse\x12>\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32,.cosmos.circuit.v1.GenesisAccountPermissions\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x1a\n\x18QueryDisabledListRequest\"-\n\x14\x44isabledListResponse\x12\x15\n\rdisabled_list\x18\x01 \x03(\t2\xad\x03\n\x05Query\x12\x89\x01\n\x07\x41\x63\x63ount\x12&.cosmos.circuit.v1.QueryAccountRequest\x1a\".cosmos.circuit.v1.AccountResponse\"2\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\'\x12%/cosmos/circuit/v1/accounts/{address}\x12\x82\x01\n\x08\x41\x63\x63ounts\x12\'.cosmos.circuit.v1.QueryAccountsRequest\x1a#.cosmos.circuit.v1.AccountsResponse\"(\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/circuit/v1/accounts\x12\x92\x01\n\x0c\x44isabledList\x12+.cosmos.circuit.v1.QueryDisabledListRequest\x1a\'.cosmos.circuit.v1.DisabledListResponse\",\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02!\x12\x1f/cosmos/circuit/v1/disable_listB\x1eZ\x1c\x63osmossdk.io/x/circuit/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.circuit.v1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\034cosmossdk.io/x/circuit/types'
  _QUERY.methods_by_name['Account']._options = None
  _QUERY.methods_by_name['Account']._serialized_options = b'\210\347\260*\001\202\323\344\223\002\'\022%/cosmos/circuit/v1/accounts/{address}'
  _QUERY.methods_by_name['Accounts']._options = None
  _QUERY.methods_by_name['Accounts']._serialized_options = b'\210\347\260*\001\202\323\344\223\002\035\022\033/cosmos/circuit/v1/accounts'
  _QUERY.methods_by_name['DisabledList']._options = None
  _QUERY.methods_by_name['DisabledList']._serialized_options = b'\210\347\260*\001\202\323\344\223\002!\022\037/cosmos/circuit/v1/disable_list'
  _QUERYACCOUNTREQUEST._serialized_start=186
  _QUERYACCOUNTREQUEST._serialized_end=224
  _ACCOUNTRESPONSE._serialized_start=226
  _ACCOUNTRESPONSE._serialized_end=295
  _QUERYACCOUNTSREQUEST._serialized_start=297
  _QUERYACCOUNTSREQUEST._serialized_end=379
  _ACCOUNTSRESPONSE._serialized_start=382
  _ACCOUNTSRESPONSE._serialized_end=525
  _QUERYDISABLEDLISTREQUEST._serialized_start=527
  _QUERYDISABLEDLISTREQUEST._serialized_end=553
  _DISABLEDLISTRESPONSE._serialized_start=555
  _DISABLEDLISTRESPONSE._serialized_end=600
  _QUERY._serialized_start=603
  _QUERY._serialized_end=1032
# @@protoc_insertion_point(module_scope)