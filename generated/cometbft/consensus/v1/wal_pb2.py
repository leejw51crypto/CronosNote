# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/consensus/v1/wal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cometbft.consensus.v1 import types_pb2 as cometbft_dot_consensus_dot_v1_dot_types__pb2
from cometbft.types.v1 import events_pb2 as cometbft_dot_types_dot_v1_dot_events__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63ometbft/consensus/v1/wal.proto\x12\x15\x63ometbft.consensus.v1\x1a!cometbft/consensus/v1/types.proto\x1a\x1e\x63ometbft/types/v1/events.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x95\x01\n\x07MsgInfo\x12\x31\n\x03msg\x18\x01 \x01(\x0b\x32\x1e.cometbft.consensus.v1.MessageB\x04\xc8\xde\x1f\x00\x12\x1b\n\x07peer_id\x18\x02 \x01(\tB\n\xe2\xde\x1f\x06PeerID\x12:\n\x0creceive_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x01\"q\n\x0bTimeoutInfo\x12\x35\n\x08\x64uration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\r\n\x05round\x18\x03 \x01(\x05\x12\x0c\n\x04step\x18\x04 \x01(\r\"\x1b\n\tEndHeight\x12\x0e\n\x06height\x18\x01 \x01(\x03\"\x85\x02\n\nWALMessage\x12H\n\x16\x65vent_data_round_state\x18\x01 \x01(\x0b\x32&.cometbft.types.v1.EventDataRoundStateH\x00\x12\x32\n\x08msg_info\x18\x02 \x01(\x0b\x32\x1e.cometbft.consensus.v1.MsgInfoH\x00\x12:\n\x0ctimeout_info\x18\x03 \x01(\x0b\x32\".cometbft.consensus.v1.TimeoutInfoH\x00\x12\x36\n\nend_height\x18\x04 \x01(\x0b\x32 .cometbft.consensus.v1.EndHeightH\x00\x42\x05\n\x03sum\"u\n\x0fTimedWALMessage\x12\x32\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12.\n\x03msg\x18\x02 \x01(\x0b\x32!.cometbft.consensus.v1.WALMessageB8Z6github.com/cometbft/cometbft/api/cometbft/consensus/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.consensus.v1.wal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/cometbft/cometbft/api/cometbft/consensus/v1'
  _MSGINFO.fields_by_name['msg']._options = None
  _MSGINFO.fields_by_name['msg']._serialized_options = b'\310\336\037\000'
  _MSGINFO.fields_by_name['peer_id']._options = None
  _MSGINFO.fields_by_name['peer_id']._serialized_options = b'\342\336\037\006PeerID'
  _MSGINFO.fields_by_name['receive_time']._options = None
  _MSGINFO.fields_by_name['receive_time']._serialized_options = b'\220\337\037\001\310\336\037\001'
  _TIMEOUTINFO.fields_by_name['duration']._options = None
  _TIMEOUTINFO.fields_by_name['duration']._serialized_options = b'\310\336\037\000\230\337\037\001'
  _TIMEDWALMESSAGE.fields_by_name['time']._options = None
  _TIMEDWALMESSAGE.fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _MSGINFO._serialized_start=213
  _MSGINFO._serialized_end=362
  _TIMEOUTINFO._serialized_start=364
  _TIMEOUTINFO._serialized_end=477
  _ENDHEIGHT._serialized_start=479
  _ENDHEIGHT._serialized_end=506
  _WALMESSAGE._serialized_start=509
  _WALMESSAGE._serialized_end=770
  _TIMEDWALMESSAGE._serialized_start=772
  _TIMEDWALMESSAGE._serialized_end=889
# @@protoc_insertion_point(module_scope)
