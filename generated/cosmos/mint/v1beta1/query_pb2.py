# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/mint/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.mint.v1beta1 import mint_pb2 as cosmos_dot_mint_dot_v1beta1_dot_mint__pb2
from amino import amino_pb2 as amino_dot_amino__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/mint/v1beta1/query.proto\x12\x13\x63osmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/mint/v1beta1/mint.proto\x1a\x11\x61mino/amino.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\x14\n\x12QueryParamsRequest\"M\n\x13QueryParamsResponse\x12\x36\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.mint.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x17\n\x15QueryInflationRequest\"c\n\x16QueryInflationResponse\x12I\n\tinflation\x18\x01 \x01(\x0c\x42\x36\xd2\xb4-\ncosmos.Dec\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x1e\n\x1cQueryAnnualProvisionsRequest\"r\n\x1dQueryAnnualProvisionsResponse\x12Q\n\x11\x61nnual_provisions\x18\x01 \x01(\x0c\x42\x36\xd2\xb4-\ncosmos.Dec\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x32\xc5\x03\n\x05Query\x12\x80\x01\n\x06Params\x12\'.cosmos.mint.v1beta1.QueryParamsRequest\x1a(.cosmos.mint.v1beta1.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/mint/v1beta1/params\x12\x8c\x01\n\tInflation\x12*.cosmos.mint.v1beta1.QueryInflationRequest\x1a+.cosmos.mint.v1beta1.QueryInflationResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/mint/v1beta1/inflation\x12\xa9\x01\n\x10\x41nnualProvisions\x12\x31.cosmos.mint.v1beta1.QueryAnnualProvisionsRequest\x1a\x32.cosmos.mint.v1beta1.QueryAnnualProvisionsResponse\".\x82\xd3\xe4\x93\x02(\x12&/cosmos/mint/v1beta1/annual_provisionsB+Z)github.com/cosmos/cosmos-sdk/x/mint/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.mint.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/mint/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYINFLATIONRESPONSE.fields_by_name['inflation']._options = None
  _QUERYINFLATIONRESPONSE.fields_by_name['inflation']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037\033cosmossdk.io/math.LegacyDec\310\336\037\000\250\347\260*\001'
  _QUERYANNUALPROVISIONSRESPONSE.fields_by_name['annual_provisions']._options = None
  _QUERYANNUALPROVISIONSRESPONSE.fields_by_name['annual_provisions']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037\033cosmossdk.io/math.LegacyDec\310\336\037\000\250\347\260*\001'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/mint/v1beta1/params'
  _QUERY.methods_by_name['Inflation']._options = None
  _QUERY.methods_by_name['Inflation']._serialized_options = b'\202\323\344\223\002 \022\036/cosmos/mint/v1beta1/inflation'
  _QUERY.methods_by_name['AnnualProvisions']._options = None
  _QUERY.methods_by_name['AnnualProvisions']._serialized_options = b'\202\323\344\223\002(\022&/cosmos/mint/v1beta1/annual_provisions'
  _QUERYPARAMSREQUEST._serialized_start=186
  _QUERYPARAMSREQUEST._serialized_end=206
  _QUERYPARAMSRESPONSE._serialized_start=208
  _QUERYPARAMSRESPONSE._serialized_end=285
  _QUERYINFLATIONREQUEST._serialized_start=287
  _QUERYINFLATIONREQUEST._serialized_end=310
  _QUERYINFLATIONRESPONSE._serialized_start=312
  _QUERYINFLATIONRESPONSE._serialized_end=411
  _QUERYANNUALPROVISIONSREQUEST._serialized_start=413
  _QUERYANNUALPROVISIONSREQUEST._serialized_end=443
  _QUERYANNUALPROVISIONSRESPONSE._serialized_start=445
  _QUERYANNUALPROVISIONSRESPONSE._serialized_end=559
  _QUERY._serialized_start=562
  _QUERY._serialized_end=1015
# @@protoc_insertion_point(module_scope)
