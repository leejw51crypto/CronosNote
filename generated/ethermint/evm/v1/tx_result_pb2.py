# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ethermint/evm/v1/tx_result.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ethermint.evm.v1 import transaction_logs_pb2 as ethermint_dot_evm_dot_v1_dot_transaction__logs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ethermint/evm/v1/tx_result.proto\x12\x10\x65thermint.evm.v1\x1a\x14gogoproto/gogo.proto\x1a\'ethermint/evm/v1/transaction_logs.proto\"\xd3\x01\n\x08TxResult\x12\x35\n\x10\x63ontract_address\x18\x01 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:\"contract_address\"\x12\r\n\x05\x62loom\x18\x02 \x01(\x0c\x12J\n\x07tx_logs\x18\x03 \x01(\x0b\x32!.ethermint.evm.v1.TransactionLogsB\x16\xf2\xde\x1f\x0eyaml:\"tx_logs\"\xc8\xde\x1f\x00\x12\x0b\n\x03ret\x18\x04 \x01(\x0c\x12\x10\n\x08reverted\x18\x05 \x01(\x08\x12\x10\n\x08gas_used\x18\x06 \x01(\x04:\x04\x88\xa0\x1f\x00\x42(Z&github.com/evmos/ethermint/x/evm/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.evm.v1.tx_result_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/evmos/ethermint/x/evm/types'
  _TXRESULT.fields_by_name['contract_address']._options = None
  _TXRESULT.fields_by_name['contract_address']._serialized_options = b'\362\336\037\027yaml:\"contract_address\"'
  _TXRESULT.fields_by_name['tx_logs']._options = None
  _TXRESULT.fields_by_name['tx_logs']._serialized_options = b'\362\336\037\016yaml:\"tx_logs\"\310\336\037\000'
  _TXRESULT._options = None
  _TXRESULT._serialized_options = b'\210\240\037\000'
  _TXRESULT._serialized_start=118
  _TXRESULT._serialized_end=329
# @@protoc_insertion_point(module_scope)