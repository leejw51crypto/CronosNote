# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/abci/v1beta2/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cometbft.abci.v1beta1 import types_pb2 as cometbft_dot_abci_dot_v1beta1_dot_types__pb2
from cometbft.types.v1beta1 import types_pb2 as cometbft_dot_types_dot_v1beta1_dot_types__pb2
from cometbft.types.v1beta2 import params_pb2 as cometbft_dot_types_dot_v1beta2_dot_params__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cometbft/abci/v1beta2/types.proto\x12\x15\x63ometbft.abci.v1beta2\x1a\x14gogoproto/gogo.proto\x1a!cometbft/abci/v1beta1/types.proto\x1a\"cometbft/types/v1beta1/types.proto\x1a#cometbft/types/v1beta2/params.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa1\x08\n\x07Request\x12\x32\n\x04\x65\x63ho\x18\x01 \x01(\x0b\x32\".cometbft.abci.v1beta1.RequestEchoH\x00\x12\x34\n\x05\x66lush\x18\x02 \x01(\x0b\x32#.cometbft.abci.v1beta1.RequestFlushH\x00\x12\x32\n\x04info\x18\x03 \x01(\x0b\x32\".cometbft.abci.v1beta2.RequestInfoH\x00\x12=\n\ninit_chain\x18\x05 \x01(\x0b\x32\'.cometbft.abci.v1beta2.RequestInitChainH\x00\x12\x34\n\x05query\x18\x06 \x01(\x0b\x32#.cometbft.abci.v1beta1.RequestQueryH\x00\x12?\n\x0b\x62\x65gin_block\x18\x07 \x01(\x0b\x32(.cometbft.abci.v1beta2.RequestBeginBlockH\x00\x12\x39\n\x08\x63heck_tx\x18\x08 \x01(\x0b\x32%.cometbft.abci.v1beta1.RequestCheckTxH\x00\x12=\n\ndeliver_tx\x18\t \x01(\x0b\x32\'.cometbft.abci.v1beta1.RequestDeliverTxH\x00\x12;\n\tend_block\x18\n \x01(\x0b\x32&.cometbft.abci.v1beta1.RequestEndBlockH\x00\x12\x36\n\x06\x63ommit\x18\x0b \x01(\x0b\x32$.cometbft.abci.v1beta1.RequestCommitH\x00\x12\x45\n\x0elist_snapshots\x18\x0c \x01(\x0b\x32+.cometbft.abci.v1beta1.RequestListSnapshotsH\x00\x12\x45\n\x0eoffer_snapshot\x18\r \x01(\x0b\x32+.cometbft.abci.v1beta1.RequestOfferSnapshotH\x00\x12N\n\x13load_snapshot_chunk\x18\x0e \x01(\x0b\x32/.cometbft.abci.v1beta1.RequestLoadSnapshotChunkH\x00\x12P\n\x14\x61pply_snapshot_chunk\x18\x0f \x01(\x0b\x32\x30.cometbft.abci.v1beta1.RequestApplySnapshotChunkH\x00\x12I\n\x10prepare_proposal\x18\x10 \x01(\x0b\x32-.cometbft.abci.v1beta2.RequestPrepareProposalH\x00\x12I\n\x10process_proposal\x18\x11 \x01(\x0b\x32-.cometbft.abci.v1beta2.RequestProcessProposalH\x00\x42\x07\n\x05valueJ\x04\x08\x04\x10\x05\"`\n\x0bRequestInfo\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x15\n\rblock_version\x18\x02 \x01(\x04\x12\x13\n\x0bp2p_version\x18\x03 \x01(\x04\x12\x14\n\x0c\x61\x62\x63i_version\x18\x04 \x01(\t\"\x8e\x02\n\x10RequestInitChain\x12\x32\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x10\n\x08\x63hain_id\x18\x02 \x01(\t\x12\x41\n\x10\x63onsensus_params\x18\x03 \x01(\x0b\x32\'.cometbft.types.v1beta2.ConsensusParams\x12@\n\nvalidators\x18\x04 \x03(\x0b\x32&.cometbft.abci.v1beta1.ValidatorUpdateB\x04\xc8\xde\x1f\x00\x12\x17\n\x0f\x61pp_state_bytes\x18\x05 \x01(\x0c\x12\x16\n\x0einitial_height\x18\x06 \x01(\x03\"\xe2\x01\n\x11RequestBeginBlock\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x34\n\x06header\x18\x02 \x01(\x0b\x32\x1e.cometbft.types.v1beta1.HeaderB\x04\xc8\xde\x1f\x00\x12\x41\n\x10last_commit_info\x18\x03 \x01(\x0b\x32!.cometbft.abci.v1beta2.CommitInfoB\x04\xc8\xde\x1f\x00\x12\x46\n\x14\x62yzantine_validators\x18\x04 \x03(\x0b\x32\".cometbft.abci.v1beta2.MisbehaviorB\x04\xc8\xde\x1f\x00\"\xc2\x02\n\x16RequestPrepareProposal\x12\x14\n\x0cmax_tx_bytes\x18\x01 \x01(\x03\x12\x0b\n\x03txs\x18\x02 \x03(\x0c\x12J\n\x11local_last_commit\x18\x03 \x01(\x0b\x32).cometbft.abci.v1beta2.ExtendedCommitInfoB\x04\xc8\xde\x1f\x00\x12=\n\x0bmisbehavior\x18\x04 \x03(\x0b\x32\".cometbft.abci.v1beta2.MisbehaviorB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06height\x18\x05 \x01(\x03\x12\x32\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x1c\n\x14next_validators_hash\x18\x07 \x01(\x0c\x12\x18\n\x10proposer_address\x18\x08 \x01(\x0c\"\xb5\x02\n\x16RequestProcessProposal\x12\x0b\n\x03txs\x18\x01 \x03(\x0c\x12\x45\n\x14proposed_last_commit\x18\x02 \x01(\x0b\x32!.cometbft.abci.v1beta2.CommitInfoB\x04\xc8\xde\x1f\x00\x12=\n\x0bmisbehavior\x18\x03 \x03(\x0b\x32\".cometbft.abci.v1beta2.MisbehaviorB\x04\xc8\xde\x1f\x00\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12\x0e\n\x06height\x18\x05 \x01(\x03\x12\x32\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x1c\n\x14next_validators_hash\x18\x07 \x01(\x0c\x12\x18\n\x10proposer_address\x18\x08 \x01(\x0c\"\xf1\x08\n\x08Response\x12=\n\texception\x18\x01 \x01(\x0b\x32(.cometbft.abci.v1beta1.ResponseExceptionH\x00\x12\x33\n\x04\x65\x63ho\x18\x02 \x01(\x0b\x32#.cometbft.abci.v1beta1.ResponseEchoH\x00\x12\x35\n\x05\x66lush\x18\x03 \x01(\x0b\x32$.cometbft.abci.v1beta1.ResponseFlushH\x00\x12\x33\n\x04info\x18\x04 \x01(\x0b\x32#.cometbft.abci.v1beta1.ResponseInfoH\x00\x12>\n\ninit_chain\x18\x06 \x01(\x0b\x32(.cometbft.abci.v1beta2.ResponseInitChainH\x00\x12\x35\n\x05query\x18\x07 \x01(\x0b\x32$.cometbft.abci.v1beta1.ResponseQueryH\x00\x12@\n\x0b\x62\x65gin_block\x18\x08 \x01(\x0b\x32).cometbft.abci.v1beta2.ResponseBeginBlockH\x00\x12:\n\x08\x63heck_tx\x18\t \x01(\x0b\x32&.cometbft.abci.v1beta2.ResponseCheckTxH\x00\x12>\n\ndeliver_tx\x18\n \x01(\x0b\x32(.cometbft.abci.v1beta2.ResponseDeliverTxH\x00\x12<\n\tend_block\x18\x0b \x01(\x0b\x32\'.cometbft.abci.v1beta2.ResponseEndBlockH\x00\x12\x37\n\x06\x63ommit\x18\x0c \x01(\x0b\x32%.cometbft.abci.v1beta1.ResponseCommitH\x00\x12\x46\n\x0elist_snapshots\x18\r \x01(\x0b\x32,.cometbft.abci.v1beta1.ResponseListSnapshotsH\x00\x12\x46\n\x0eoffer_snapshot\x18\x0e \x01(\x0b\x32,.cometbft.abci.v1beta1.ResponseOfferSnapshotH\x00\x12O\n\x13load_snapshot_chunk\x18\x0f \x01(\x0b\x32\x30.cometbft.abci.v1beta1.ResponseLoadSnapshotChunkH\x00\x12Q\n\x14\x61pply_snapshot_chunk\x18\x10 \x01(\x0b\x32\x31.cometbft.abci.v1beta1.ResponseApplySnapshotChunkH\x00\x12J\n\x10prepare_proposal\x18\x11 \x01(\x0b\x32..cometbft.abci.v1beta2.ResponsePrepareProposalH\x00\x12J\n\x10process_proposal\x18\x12 \x01(\x0b\x32..cometbft.abci.v1beta2.ResponseProcessProposalH\x00\x42\x07\n\x05valueJ\x04\x08\x05\x10\x06\"\xaa\x01\n\x11ResponseInitChain\x12\x41\n\x10\x63onsensus_params\x18\x01 \x01(\x0b\x32\'.cometbft.types.v1beta2.ConsensusParams\x12@\n\nvalidators\x18\x02 \x03(\x0b\x32&.cometbft.abci.v1beta1.ValidatorUpdateB\x04\xc8\xde\x1f\x00\x12\x10\n\x08\x61pp_hash\x18\x03 \x01(\x0c\"\\\n\x12ResponseBeginBlock\x12\x46\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1c.cometbft.abci.v1beta2.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitempty\"\x98\x02\n\x0fResponseCheckTx\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\x1e\n\ngas_wanted\x18\x05 \x01(\x03R\ngas_wanted\x12\x1a\n\x08gas_used\x18\x06 \x01(\x03R\x08gas_used\x12\x46\n\x06\x65vents\x18\x07 \x03(\x0b\x32\x1c.cometbft.abci.v1beta2.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitempty\x12\x11\n\tcodespace\x18\x08 \x01(\t\x12\x0e\n\x06sender\x18\t \x01(\t\x12\x10\n\x08priority\x18\n \x01(\x03\x12\x15\n\rmempool_error\x18\x0b \x01(\t\"\xe1\x01\n\x11ResponseDeliverTx\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\x1e\n\ngas_wanted\x18\x05 \x01(\x03R\ngas_wanted\x12\x1a\n\x08gas_used\x18\x06 \x01(\x03R\x08gas_used\x12\x46\n\x06\x65vents\x18\x07 \x03(\x0b\x32\x1c.cometbft.abci.v1beta2.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitempty\x12\x11\n\tcodespace\x18\x08 \x01(\t\"\xed\x01\n\x10ResponseEndBlock\x12G\n\x11validator_updates\x18\x01 \x03(\x0b\x32&.cometbft.abci.v1beta1.ValidatorUpdateB\x04\xc8\xde\x1f\x00\x12H\n\x17\x63onsensus_param_updates\x18\x02 \x01(\x0b\x32\'.cometbft.types.v1beta2.ConsensusParams\x12\x46\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x1c.cometbft.abci.v1beta2.EventB\x18\xc8\xde\x1f\x00\xea\xde\x1f\x10\x65vents,omitempty\"&\n\x17ResponsePrepareProposal\x12\x0b\n\x03txs\x18\x01 \x03(\x0c\"\x9f\x01\n\x17ResponseProcessProposal\x12M\n\x06status\x18\x01 \x01(\x0e\x32=.cometbft.abci.v1beta2.ResponseProcessProposal.ProposalStatus\"5\n\x0eProposalStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x41\x43\x43\x45PT\x10\x01\x12\n\n\x06REJECT\x10\x02\"Q\n\nCommitInfo\x12\r\n\x05round\x18\x01 \x01(\x05\x12\x34\n\x05votes\x18\x02 \x03(\x0b\x32\x1f.cometbft.abci.v1beta1.VoteInfoB\x04\xc8\xde\x1f\x00\"a\n\x12\x45xtendedCommitInfo\x12\r\n\x05round\x18\x01 \x01(\x05\x12<\n\x05votes\x18\x02 \x03(\x0b\x32\'.cometbft.abci.v1beta2.ExtendedVoteInfoB\x04\xc8\xde\x1f\x00\"n\n\x05\x45vent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12W\n\nattributes\x18\x02 \x03(\x0b\x32%.cometbft.abci.v1beta2.EventAttributeB\x1c\xc8\xde\x1f\x00\xea\xde\x1f\x14\x61ttributes,omitempty\";\n\x0e\x45ventAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x08\"\x80\x01\n\x10\x45xtendedVoteInfo\x12\x39\n\tvalidator\x18\x01 \x01(\x0b\x32 .cometbft.abci.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12\x19\n\x11signed_last_block\x18\x02 \x01(\x08\x12\x16\n\x0evote_extension\x18\x03 \x01(\x0c\"\xde\x01\n\x0bMisbehavior\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.cometbft.abci.v1beta2.MisbehaviorType\x12\x39\n\tvalidator\x18\x02 \x01(\x0b\x32 .cometbft.abci.v1beta1.ValidatorB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x32\n\x04time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x1a\n\x12total_voting_power\x18\x05 \x01(\x03*K\n\x0fMisbehaviorType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0e\x44UPLICATE_VOTE\x10\x01\x12\x17\n\x13LIGHT_CLIENT_ATTACK\x10\x02\x32\xbb\x0c\n\x0f\x41\x42\x43IApplication\x12O\n\x04\x45\x63ho\x12\".cometbft.abci.v1beta1.RequestEcho\x1a#.cometbft.abci.v1beta1.ResponseEcho\x12R\n\x05\x46lush\x12#.cometbft.abci.v1beta1.RequestFlush\x1a$.cometbft.abci.v1beta1.ResponseFlush\x12O\n\x04Info\x12\".cometbft.abci.v1beta2.RequestInfo\x1a#.cometbft.abci.v1beta1.ResponseInfo\x12^\n\tDeliverTx\x12\'.cometbft.abci.v1beta1.RequestDeliverTx\x1a(.cometbft.abci.v1beta2.ResponseDeliverTx\x12X\n\x07\x43heckTx\x12%.cometbft.abci.v1beta1.RequestCheckTx\x1a&.cometbft.abci.v1beta2.ResponseCheckTx\x12R\n\x05Query\x12#.cometbft.abci.v1beta1.RequestQuery\x1a$.cometbft.abci.v1beta1.ResponseQuery\x12U\n\x06\x43ommit\x12$.cometbft.abci.v1beta1.RequestCommit\x1a%.cometbft.abci.v1beta1.ResponseCommit\x12^\n\tInitChain\x12\'.cometbft.abci.v1beta2.RequestInitChain\x1a(.cometbft.abci.v1beta2.ResponseInitChain\x12\x61\n\nBeginBlock\x12(.cometbft.abci.v1beta2.RequestBeginBlock\x1a).cometbft.abci.v1beta2.ResponseBeginBlock\x12[\n\x08\x45ndBlock\x12&.cometbft.abci.v1beta1.RequestEndBlock\x1a\'.cometbft.abci.v1beta2.ResponseEndBlock\x12j\n\rListSnapshots\x12+.cometbft.abci.v1beta1.RequestListSnapshots\x1a,.cometbft.abci.v1beta1.ResponseListSnapshots\x12j\n\rOfferSnapshot\x12+.cometbft.abci.v1beta1.RequestOfferSnapshot\x1a,.cometbft.abci.v1beta1.ResponseOfferSnapshot\x12v\n\x11LoadSnapshotChunk\x12/.cometbft.abci.v1beta1.RequestLoadSnapshotChunk\x1a\x30.cometbft.abci.v1beta1.ResponseLoadSnapshotChunk\x12y\n\x12\x41pplySnapshotChunk\x12\x30.cometbft.abci.v1beta1.RequestApplySnapshotChunk\x1a\x31.cometbft.abci.v1beta1.ResponseApplySnapshotChunk\x12p\n\x0fPrepareProposal\x12-.cometbft.abci.v1beta2.RequestPrepareProposal\x1a..cometbft.abci.v1beta2.ResponsePrepareProposal\x12p\n\x0fProcessProposal\x12-.cometbft.abci.v1beta2.RequestProcessProposal\x1a..cometbft.abci.v1beta2.ResponseProcessProposalB8Z6github.com/cometbft/cometbft/api/cometbft/abci/v1beta2b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cometbft.abci.v1beta2.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/cometbft/cometbft/api/cometbft/abci/v1beta2'
  _REQUESTINITCHAIN.fields_by_name['time']._options = None
  _REQUESTINITCHAIN.fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _REQUESTINITCHAIN.fields_by_name['validators']._options = None
  _REQUESTINITCHAIN.fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _REQUESTBEGINBLOCK.fields_by_name['header']._options = None
  _REQUESTBEGINBLOCK.fields_by_name['header']._serialized_options = b'\310\336\037\000'
  _REQUESTBEGINBLOCK.fields_by_name['last_commit_info']._options = None
  _REQUESTBEGINBLOCK.fields_by_name['last_commit_info']._serialized_options = b'\310\336\037\000'
  _REQUESTBEGINBLOCK.fields_by_name['byzantine_validators']._options = None
  _REQUESTBEGINBLOCK.fields_by_name['byzantine_validators']._serialized_options = b'\310\336\037\000'
  _REQUESTPREPAREPROPOSAL.fields_by_name['local_last_commit']._options = None
  _REQUESTPREPAREPROPOSAL.fields_by_name['local_last_commit']._serialized_options = b'\310\336\037\000'
  _REQUESTPREPAREPROPOSAL.fields_by_name['misbehavior']._options = None
  _REQUESTPREPAREPROPOSAL.fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _REQUESTPREPAREPROPOSAL.fields_by_name['time']._options = None
  _REQUESTPREPAREPROPOSAL.fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _REQUESTPROCESSPROPOSAL.fields_by_name['proposed_last_commit']._options = None
  _REQUESTPROCESSPROPOSAL.fields_by_name['proposed_last_commit']._serialized_options = b'\310\336\037\000'
  _REQUESTPROCESSPROPOSAL.fields_by_name['misbehavior']._options = None
  _REQUESTPROCESSPROPOSAL.fields_by_name['misbehavior']._serialized_options = b'\310\336\037\000'
  _REQUESTPROCESSPROPOSAL.fields_by_name['time']._options = None
  _REQUESTPROCESSPROPOSAL.fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _RESPONSEINITCHAIN.fields_by_name['validators']._options = None
  _RESPONSEINITCHAIN.fields_by_name['validators']._serialized_options = b'\310\336\037\000'
  _RESPONSEBEGINBLOCK.fields_by_name['events']._options = None
  _RESPONSEBEGINBLOCK.fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _RESPONSECHECKTX.fields_by_name['events']._options = None
  _RESPONSECHECKTX.fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _RESPONSEDELIVERTX.fields_by_name['events']._options = None
  _RESPONSEDELIVERTX.fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _RESPONSEENDBLOCK.fields_by_name['validator_updates']._options = None
  _RESPONSEENDBLOCK.fields_by_name['validator_updates']._serialized_options = b'\310\336\037\000'
  _RESPONSEENDBLOCK.fields_by_name['events']._options = None
  _RESPONSEENDBLOCK.fields_by_name['events']._serialized_options = b'\310\336\037\000\352\336\037\020events,omitempty'
  _COMMITINFO.fields_by_name['votes']._options = None
  _COMMITINFO.fields_by_name['votes']._serialized_options = b'\310\336\037\000'
  _EXTENDEDCOMMITINFO.fields_by_name['votes']._options = None
  _EXTENDEDCOMMITINFO.fields_by_name['votes']._serialized_options = b'\310\336\037\000'
  _EVENT.fields_by_name['attributes']._options = None
  _EVENT.fields_by_name['attributes']._serialized_options = b'\310\336\037\000\352\336\037\024attributes,omitempty'
  _EXTENDEDVOTEINFO.fields_by_name['validator']._options = None
  _EXTENDEDVOTEINFO.fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _MISBEHAVIOR.fields_by_name['validator']._options = None
  _MISBEHAVIOR.fields_by_name['validator']._serialized_options = b'\310\336\037\000'
  _MISBEHAVIOR.fields_by_name['time']._options = None
  _MISBEHAVIOR.fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _MISBEHAVIORTYPE._serialized_start=5591
  _MISBEHAVIORTYPE._serialized_end=5666
  _REQUEST._serialized_start=224
  _REQUEST._serialized_end=1281
  _REQUESTINFO._serialized_start=1283
  _REQUESTINFO._serialized_end=1379
  _REQUESTINITCHAIN._serialized_start=1382
  _REQUESTINITCHAIN._serialized_end=1652
  _REQUESTBEGINBLOCK._serialized_start=1655
  _REQUESTBEGINBLOCK._serialized_end=1881
  _REQUESTPREPAREPROPOSAL._serialized_start=1884
  _REQUESTPREPAREPROPOSAL._serialized_end=2206
  _REQUESTPROCESSPROPOSAL._serialized_start=2209
  _REQUESTPROCESSPROPOSAL._serialized_end=2518
  _RESPONSE._serialized_start=2521
  _RESPONSE._serialized_end=3658
  _RESPONSEINITCHAIN._serialized_start=3661
  _RESPONSEINITCHAIN._serialized_end=3831
  _RESPONSEBEGINBLOCK._serialized_start=3833
  _RESPONSEBEGINBLOCK._serialized_end=3925
  _RESPONSECHECKTX._serialized_start=3928
  _RESPONSECHECKTX._serialized_end=4208
  _RESPONSEDELIVERTX._serialized_start=4211
  _RESPONSEDELIVERTX._serialized_end=4436
  _RESPONSEENDBLOCK._serialized_start=4439
  _RESPONSEENDBLOCK._serialized_end=4676
  _RESPONSEPREPAREPROPOSAL._serialized_start=4678
  _RESPONSEPREPAREPROPOSAL._serialized_end=4716
  _RESPONSEPROCESSPROPOSAL._serialized_start=4719
  _RESPONSEPROCESSPROPOSAL._serialized_end=4878
  _RESPONSEPROCESSPROPOSAL_PROPOSALSTATUS._serialized_start=4825
  _RESPONSEPROCESSPROPOSAL_PROPOSALSTATUS._serialized_end=4878
  _COMMITINFO._serialized_start=4880
  _COMMITINFO._serialized_end=4961
  _EXTENDEDCOMMITINFO._serialized_start=4963
  _EXTENDEDCOMMITINFO._serialized_end=5060
  _EVENT._serialized_start=5062
  _EVENT._serialized_end=5172
  _EVENTATTRIBUTE._serialized_start=5174
  _EVENTATTRIBUTE._serialized_end=5233
  _EXTENDEDVOTEINFO._serialized_start=5236
  _EXTENDEDVOTEINFO._serialized_end=5364
  _MISBEHAVIOR._serialized_start=5367
  _MISBEHAVIOR._serialized_end=5589
  _ABCIAPPLICATION._serialized_start=5669
  _ABCIAPPLICATION._serialized_end=7264
# @@protoc_insertion_point(module_scope)
