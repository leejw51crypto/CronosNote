# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/privval/v1/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cometbft.types.v1 import types_pb2 as cometbft_dot_types_dot_v1_dot_types__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63ometbft/privval/v1/types.proto\x12\x13\x63ometbft.privval.v1\x1a\x1d\x63ometbft/types/v1/types.proto\x1a\x14gogoproto/gogo.proto\"6\n\x11RemoteSignerError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"!\n\rPubKeyRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\"z\n\x0ePubKeyResponse\x12\x35\n\x05\x65rror\x18\x02 \x01(\x0b\x32&.cometbft.privval.v1.RemoteSignerError\x12\x15\n\rpub_key_bytes\x18\x03 \x01(\x0c\x12\x14\n\x0cpub_key_type\x18\x04 \x01(\tJ\x04\x08\x01\x10\x02\"j\n\x0fSignVoteRequest\x12%\n\x04vote\x18\x01 \x01(\x0b\x32\x17.cometbft.types.v1.Vote\x12\x10\n\x08\x63hain_id\x18\x02 \x01(\t\x12\x1e\n\x16skip_extension_signing\x18\x03 \x01(\x08\"x\n\x12SignedVoteResponse\x12+\n\x04vote\x18\x01 \x01(\x0b\x32\x17.cometbft.types.v1.VoteB\x04\xc8\xde\x1f\x00\x12\x35\n\x05\x65rror\x18\x02 \x01(\x0b\x32&.cometbft.privval.v1.RemoteSignerError\"V\n\x13SignProposalRequest\x12-\n\x08proposal\x18\x01 \x01(\x0b\x32\x1b.cometbft.types.v1.Proposal\x12\x10\n\x08\x63hain_id\x18\x02 \x01(\t\"\x84\x01\n\x16SignedProposalResponse\x12\x33\n\x08proposal\x18\x01 \x01(\x0b\x32\x1b.cometbft.types.v1.ProposalB\x04\xc8\xde\x1f\x00\x12\x35\n\x05\x65rror\x18\x02 \x01(\x0b\x32&.cometbft.privval.v1.RemoteSignerError\"!\n\x10SignBytesRequest\x12\r\n\x05value\x18\x01 \x01(\x0c\"]\n\x11SignBytesResponse\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x35\n\x05\x65rror\x18\x02 \x01(\x0b\x32&.cometbft.privval.v1.RemoteSignerError\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse\"\xba\x05\n\x07Message\x12=\n\x0fpub_key_request\x18\x01 \x01(\x0b\x32\".cometbft.privval.v1.PubKeyRequestH\x00\x12?\n\x10pub_key_response\x18\x02 \x01(\x0b\x32#.cometbft.privval.v1.PubKeyResponseH\x00\x12\x41\n\x11sign_vote_request\x18\x03 \x01(\x0b\x32$.cometbft.privval.v1.SignVoteRequestH\x00\x12G\n\x14signed_vote_response\x18\x04 \x01(\x0b\x32\'.cometbft.privval.v1.SignedVoteResponseH\x00\x12I\n\x15sign_proposal_request\x18\x05 \x01(\x0b\x32(.cometbft.privval.v1.SignProposalRequestH\x00\x12O\n\x18signed_proposal_response\x18\x06 \x01(\x0b\x32+.cometbft.privval.v1.SignedProposalResponseH\x00\x12\x38\n\x0cping_request\x18\x07 \x01(\x0b\x32 .cometbft.privval.v1.PingRequestH\x00\x12:\n\rping_response\x18\x08 \x01(\x0b\x32!.cometbft.privval.v1.PingResponseH\x00\x12\x43\n\x12sign_bytes_request\x18\t \x01(\x0b\x32%.cometbft.privval.v1.SignBytesRequestH\x00\x12\x45\n\x13sign_bytes_response\x18\n \x01(\x0b\x32&.cometbft.privval.v1.SignBytesResponseH\x00\x42\x05\n\x03sumB6Z4github.com/cometbft/cometbft/api/cometbft/privval/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.privval.v1.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/cometbft/cometbft/api/cometbft/privval/v1'
  _SIGNEDVOTERESPONSE.fields_by_name['vote']._options = None
  _SIGNEDVOTERESPONSE.fields_by_name['vote']._serialized_options = b'\310\336\037\000'
  _SIGNEDPROPOSALRESPONSE.fields_by_name['proposal']._options = None
  _SIGNEDPROPOSALRESPONSE.fields_by_name['proposal']._serialized_options = b'\310\336\037\000'
  _REMOTESIGNERERROR._serialized_start=109
  _REMOTESIGNERERROR._serialized_end=163
  _PUBKEYREQUEST._serialized_start=165
  _PUBKEYREQUEST._serialized_end=198
  _PUBKEYRESPONSE._serialized_start=200
  _PUBKEYRESPONSE._serialized_end=322
  _SIGNVOTEREQUEST._serialized_start=324
  _SIGNVOTEREQUEST._serialized_end=430
  _SIGNEDVOTERESPONSE._serialized_start=432
  _SIGNEDVOTERESPONSE._serialized_end=552
  _SIGNPROPOSALREQUEST._serialized_start=554
  _SIGNPROPOSALREQUEST._serialized_end=640
  _SIGNEDPROPOSALRESPONSE._serialized_start=643
  _SIGNEDPROPOSALRESPONSE._serialized_end=775
  _SIGNBYTESREQUEST._serialized_start=777
  _SIGNBYTESREQUEST._serialized_end=810
  _SIGNBYTESRESPONSE._serialized_start=812
  _SIGNBYTESRESPONSE._serialized_end=905
  _PINGREQUEST._serialized_start=907
  _PINGREQUEST._serialized_end=920
  _PINGRESPONSE._serialized_start=922
  _PINGRESPONSE._serialized_end=936
  _MESSAGE._serialized_start=939
  _MESSAGE._serialized_end=1637
# @@protoc_insertion_point(module_scope)