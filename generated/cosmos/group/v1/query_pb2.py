# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/group/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.group.v1 import types_pb2 as cosmos_dot_group_dot_v1_dot_types__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63osmos/group/v1/query.proto\x12\x0f\x63osmos.group.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1b\x63osmos/group/v1/types.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\")\n\x15QueryGroupInfoRequest\x12\x10\n\x08group_id\x18\x01 \x01(\x04\"B\n\x16QueryGroupInfoResponse\x12(\n\x04info\x18\x01 \x01(\x0b\x32\x1a.cosmos.group.v1.GroupInfo\"H\n\x1bQueryGroupPolicyInfoRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"N\n\x1cQueryGroupPolicyInfoResponse\x12.\n\x04info\x18\x01 \x01(\x0b\x32 .cosmos.group.v1.GroupPolicyInfo\"h\n\x18QueryGroupMembersRequest\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x87\x01\n\x19QueryGroupMembersResponse\x12-\n\x07members\x18\x01 \x03(\x0b\x32\x1c.cosmos.group.v1.GroupMember\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x80\x01\n\x19QueryGroupsByAdminRequest\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x85\x01\n\x1aQueryGroupsByAdminResponse\x12*\n\x06groups\x18\x01 \x03(\x0b\x32\x1a.cosmos.group.v1.GroupInfo\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"p\n QueryGroupPoliciesByGroupRequest\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x9a\x01\n!QueryGroupPoliciesByGroupResponse\x12\x38\n\x0egroup_policies\x18\x01 \x03(\x0b\x32 .cosmos.group.v1.GroupPolicyInfo\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x87\x01\n QueryGroupPoliciesByAdminRequest\x12\'\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x9a\x01\n!QueryGroupPoliciesByAdminResponse\x12\x38\n\x0egroup_policies\x18\x01 \x03(\x0b\x32 .cosmos.group.v1.GroupPolicyInfo\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"+\n\x14QueryProposalRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"D\n\x15QueryProposalResponse\x12+\n\x08proposal\x18\x01 \x01(\x0b\x32\x19.cosmos.group.v1.Proposal\"\x8b\x01\n\"QueryProposalsByGroupPolicyRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x90\x01\n#QueryProposalsByGroupPolicyResponse\x12,\n\tproposals\x18\x01 \x03(\x0b\x32\x19.cosmos.group.v1.Proposal\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"_\n\x1fQueryVoteByProposalVoterRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"G\n QueryVoteByProposalVoterResponse\x12#\n\x04vote\x18\x01 \x01(\x0b\x32\x15.cosmos.group.v1.Vote\"n\n\x1bQueryVotesByProposalRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x81\x01\n\x1cQueryVotesByProposalResponse\x12$\n\x05votes\x18\x01 \x03(\x0b\x32\x15.cosmos.group.v1.Vote\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x7f\n\x18QueryVotesByVoterRequest\x12\'\n\x05voter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"~\n\x19QueryVotesByVoterResponse\x12$\n\x05votes\x18\x01 \x03(\x0b\x32\x15.cosmos.group.v1.Vote\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x83\x01\n\x1aQueryGroupsByMemberRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x86\x01\n\x1bQueryGroupsByMemberResponse\x12*\n\x06groups\x18\x01 \x03(\x0b\x32\x1a.cosmos.group.v1.GroupInfo\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\".\n\x17QueryTallyResultRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\"R\n\x18QueryTallyResultResponse\x12\x36\n\x05tally\x18\x01 \x01(\x0b\x32\x1c.cosmos.group.v1.TallyResultB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"P\n\x12QueryGroupsRequest\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"~\n\x13QueryGroupsResponse\x12*\n\x06groups\x18\x01 \x03(\x0b\x32\x1a.cosmos.group.v1.GroupInfo\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xfb\x11\n\x05Query\x12\x8c\x01\n\tGroupInfo\x12&.cosmos.group.v1.QueryGroupInfoRequest\x1a\'.cosmos.group.v1.QueryGroupInfoResponse\".\x82\xd3\xe4\x93\x02(\x12&/cosmos/group/v1/group_info/{group_id}\x12\xa4\x01\n\x0fGroupPolicyInfo\x12,.cosmos.group.v1.QueryGroupPolicyInfoRequest\x1a-.cosmos.group.v1.QueryGroupPolicyInfoResponse\"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/group/v1/group_policy_info/{address}\x12\x98\x01\n\x0cGroupMembers\x12).cosmos.group.v1.QueryGroupMembersRequest\x1a*.cosmos.group.v1.QueryGroupMembersResponse\"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/group/v1/group_members/{group_id}\x12\x9a\x01\n\rGroupsByAdmin\x12*.cosmos.group.v1.QueryGroupsByAdminRequest\x1a+.cosmos.group.v1.QueryGroupsByAdminResponse\"0\x82\xd3\xe4\x93\x02*\x12(/cosmos/group/v1/groups_by_admin/{admin}\x12\xba\x01\n\x14GroupPoliciesByGroup\x12\x31.cosmos.group.v1.QueryGroupPoliciesByGroupRequest\x1a\x32.cosmos.group.v1.QueryGroupPoliciesByGroupResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/cosmos/group/v1/group_policies_by_group/{group_id}\x12\xb7\x01\n\x14GroupPoliciesByAdmin\x12\x31.cosmos.group.v1.QueryGroupPoliciesByAdminRequest\x1a\x32.cosmos.group.v1.QueryGroupPoliciesByAdminResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/cosmos/group/v1/group_policies_by_admin/{admin}\x12\x8a\x01\n\x08Proposal\x12%.cosmos.group.v1.QueryProposalRequest\x1a&.cosmos.group.v1.QueryProposalResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/group/v1/proposal/{proposal_id}\x12\xc1\x01\n\x16ProposalsByGroupPolicy\x12\x33.cosmos.group.v1.QueryProposalsByGroupPolicyRequest\x1a\x34.cosmos.group.v1.QueryProposalsByGroupPolicyResponse\"<\x82\xd3\xe4\x93\x02\x36\x12\x34/cosmos/group/v1/proposals_by_group_policy/{address}\x12\xc1\x01\n\x13VoteByProposalVoter\x12\x30.cosmos.group.v1.QueryVoteByProposalVoterRequest\x1a\x31.cosmos.group.v1.QueryVoteByProposalVoterResponse\"E\x82\xd3\xe4\x93\x02?\x12=/cosmos/group/v1/vote_by_proposal_voter/{proposal_id}/{voter}\x12\xa8\x01\n\x0fVotesByProposal\x12,.cosmos.group.v1.QueryVotesByProposalRequest\x1a-.cosmos.group.v1.QueryVotesByProposalResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/cosmos/group/v1/votes_by_proposal/{proposal_id}\x12\x96\x01\n\x0cVotesByVoter\x12).cosmos.group.v1.QueryVotesByVoterRequest\x1a*.cosmos.group.v1.QueryVotesByVoterResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/group/v1/votes_by_voter/{voter}\x12\xa0\x01\n\x0eGroupsByMember\x12+.cosmos.group.v1.QueryGroupsByMemberRequest\x1a,.cosmos.group.v1.QueryGroupsByMemberResponse\"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/group/v1/groups_by_member/{address}\x12\x9a\x01\n\x0bTallyResult\x12(.cosmos.group.v1.QueryTallyResultRequest\x1a).cosmos.group.v1.QueryTallyResultResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./cosmos/group/v1/proposals/{proposal_id}/tally\x12t\n\x06Groups\x12#.cosmos.group.v1.QueryGroupsRequest\x1a$.cosmos.group.v1.QueryGroupsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/cosmos/group/v1/groupsB&Z$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.group.v1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/group'
  _QUERYGROUPPOLICYINFOREQUEST.fields_by_name['address']._options = None
  _QUERYGROUPPOLICYINFOREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYGROUPSBYADMINREQUEST.fields_by_name['admin']._options = None
  _QUERYGROUPSBYADMINREQUEST.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYGROUPPOLICIESBYADMINREQUEST.fields_by_name['admin']._options = None
  _QUERYGROUPPOLICIESBYADMINREQUEST.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYPROPOSALSBYGROUPPOLICYREQUEST.fields_by_name['address']._options = None
  _QUERYPROPOSALSBYGROUPPOLICYREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYVOTEBYPROPOSALVOTERREQUEST.fields_by_name['voter']._options = None
  _QUERYVOTEBYPROPOSALVOTERREQUEST.fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYVOTESBYVOTERREQUEST.fields_by_name['voter']._options = None
  _QUERYVOTESBYVOTERREQUEST.fields_by_name['voter']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYGROUPSBYMEMBERREQUEST.fields_by_name['address']._options = None
  _QUERYGROUPSBYMEMBERREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYTALLYRESULTRESPONSE.fields_by_name['tally']._options = None
  _QUERYTALLYRESULTRESPONSE.fields_by_name['tally']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERY.methods_by_name['GroupInfo']._options = None
  _QUERY.methods_by_name['GroupInfo']._serialized_options = b'\202\323\344\223\002(\022&/cosmos/group/v1/group_info/{group_id}'
  _QUERY.methods_by_name['GroupPolicyInfo']._options = None
  _QUERY.methods_by_name['GroupPolicyInfo']._serialized_options = b'\202\323\344\223\002.\022,/cosmos/group/v1/group_policy_info/{address}'
  _QUERY.methods_by_name['GroupMembers']._options = None
  _QUERY.methods_by_name['GroupMembers']._serialized_options = b'\202\323\344\223\002+\022)/cosmos/group/v1/group_members/{group_id}'
  _QUERY.methods_by_name['GroupsByAdmin']._options = None
  _QUERY.methods_by_name['GroupsByAdmin']._serialized_options = b'\202\323\344\223\002*\022(/cosmos/group/v1/groups_by_admin/{admin}'
  _QUERY.methods_by_name['GroupPoliciesByGroup']._options = None
  _QUERY.methods_by_name['GroupPoliciesByGroup']._serialized_options = b'\202\323\344\223\0025\0223/cosmos/group/v1/group_policies_by_group/{group_id}'
  _QUERY.methods_by_name['GroupPoliciesByAdmin']._options = None
  _QUERY.methods_by_name['GroupPoliciesByAdmin']._serialized_options = b'\202\323\344\223\0022\0220/cosmos/group/v1/group_policies_by_admin/{admin}'
  _QUERY.methods_by_name['Proposal']._options = None
  _QUERY.methods_by_name['Proposal']._serialized_options = b'\202\323\344\223\002)\022\'/cosmos/group/v1/proposal/{proposal_id}'
  _QUERY.methods_by_name['ProposalsByGroupPolicy']._options = None
  _QUERY.methods_by_name['ProposalsByGroupPolicy']._serialized_options = b'\202\323\344\223\0026\0224/cosmos/group/v1/proposals_by_group_policy/{address}'
  _QUERY.methods_by_name['VoteByProposalVoter']._options = None
  _QUERY.methods_by_name['VoteByProposalVoter']._serialized_options = b'\202\323\344\223\002?\022=/cosmos/group/v1/vote_by_proposal_voter/{proposal_id}/{voter}'
  _QUERY.methods_by_name['VotesByProposal']._options = None
  _QUERY.methods_by_name['VotesByProposal']._serialized_options = b'\202\323\344\223\0022\0220/cosmos/group/v1/votes_by_proposal/{proposal_id}'
  _QUERY.methods_by_name['VotesByVoter']._options = None
  _QUERY.methods_by_name['VotesByVoter']._serialized_options = b'\202\323\344\223\002)\022\'/cosmos/group/v1/votes_by_voter/{voter}'
  _QUERY.methods_by_name['GroupsByMember']._options = None
  _QUERY.methods_by_name['GroupsByMember']._serialized_options = b'\202\323\344\223\002-\022+/cosmos/group/v1/groups_by_member/{address}'
  _QUERY.methods_by_name['TallyResult']._options = None
  _QUERY.methods_by_name['TallyResult']._serialized_options = b'\202\323\344\223\0020\022./cosmos/group/v1/proposals/{proposal_id}/tally'
  _QUERY.methods_by_name['Groups']._options = None
  _QUERY.methods_by_name['Groups']._serialized_options = b'\202\323\344\223\002\031\022\027/cosmos/group/v1/groups'
  _QUERYGROUPINFOREQUEST._serialized_start=219
  _QUERYGROUPINFOREQUEST._serialized_end=260
  _QUERYGROUPINFORESPONSE._serialized_start=262
  _QUERYGROUPINFORESPONSE._serialized_end=328
  _QUERYGROUPPOLICYINFOREQUEST._serialized_start=330
  _QUERYGROUPPOLICYINFOREQUEST._serialized_end=402
  _QUERYGROUPPOLICYINFORESPONSE._serialized_start=404
  _QUERYGROUPPOLICYINFORESPONSE._serialized_end=482
  _QUERYGROUPMEMBERSREQUEST._serialized_start=484
  _QUERYGROUPMEMBERSREQUEST._serialized_end=588
  _QUERYGROUPMEMBERSRESPONSE._serialized_start=591
  _QUERYGROUPMEMBERSRESPONSE._serialized_end=726
  _QUERYGROUPSBYADMINREQUEST._serialized_start=729
  _QUERYGROUPSBYADMINREQUEST._serialized_end=857
  _QUERYGROUPSBYADMINRESPONSE._serialized_start=860
  _QUERYGROUPSBYADMINRESPONSE._serialized_end=993
  _QUERYGROUPPOLICIESBYGROUPREQUEST._serialized_start=995
  _QUERYGROUPPOLICIESBYGROUPREQUEST._serialized_end=1107
  _QUERYGROUPPOLICIESBYGROUPRESPONSE._serialized_start=1110
  _QUERYGROUPPOLICIESBYGROUPRESPONSE._serialized_end=1264
  _QUERYGROUPPOLICIESBYADMINREQUEST._serialized_start=1267
  _QUERYGROUPPOLICIESBYADMINREQUEST._serialized_end=1402
  _QUERYGROUPPOLICIESBYADMINRESPONSE._serialized_start=1405
  _QUERYGROUPPOLICIESBYADMINRESPONSE._serialized_end=1559
  _QUERYPROPOSALREQUEST._serialized_start=1561
  _QUERYPROPOSALREQUEST._serialized_end=1604
  _QUERYPROPOSALRESPONSE._serialized_start=1606
  _QUERYPROPOSALRESPONSE._serialized_end=1674
  _QUERYPROPOSALSBYGROUPPOLICYREQUEST._serialized_start=1677
  _QUERYPROPOSALSBYGROUPPOLICYREQUEST._serialized_end=1816
  _QUERYPROPOSALSBYGROUPPOLICYRESPONSE._serialized_start=1819
  _QUERYPROPOSALSBYGROUPPOLICYRESPONSE._serialized_end=1963
  _QUERYVOTEBYPROPOSALVOTERREQUEST._serialized_start=1965
  _QUERYVOTEBYPROPOSALVOTERREQUEST._serialized_end=2060
  _QUERYVOTEBYPROPOSALVOTERRESPONSE._serialized_start=2062
  _QUERYVOTEBYPROPOSALVOTERRESPONSE._serialized_end=2133
  _QUERYVOTESBYPROPOSALREQUEST._serialized_start=2135
  _QUERYVOTESBYPROPOSALREQUEST._serialized_end=2245
  _QUERYVOTESBYPROPOSALRESPONSE._serialized_start=2248
  _QUERYVOTESBYPROPOSALRESPONSE._serialized_end=2377
  _QUERYVOTESBYVOTERREQUEST._serialized_start=2379
  _QUERYVOTESBYVOTERREQUEST._serialized_end=2506
  _QUERYVOTESBYVOTERRESPONSE._serialized_start=2508
  _QUERYVOTESBYVOTERRESPONSE._serialized_end=2634
  _QUERYGROUPSBYMEMBERREQUEST._serialized_start=2637
  _QUERYGROUPSBYMEMBERREQUEST._serialized_end=2768
  _QUERYGROUPSBYMEMBERRESPONSE._serialized_start=2771
  _QUERYGROUPSBYMEMBERRESPONSE._serialized_end=2905
  _QUERYTALLYRESULTREQUEST._serialized_start=2907
  _QUERYTALLYRESULTREQUEST._serialized_end=2953
  _QUERYTALLYRESULTRESPONSE._serialized_start=2955
  _QUERYTALLYRESULTRESPONSE._serialized_end=3037
  _QUERYGROUPSREQUEST._serialized_start=3039
  _QUERYGROUPSREQUEST._serialized_end=3119
  _QUERYGROUPSRESPONSE._serialized_start=3121
  _QUERYGROUPSRESPONSE._serialized_end=3247
  _QUERY._serialized_start=3250
  _QUERY._serialized_end=5549
# @@protoc_insertion_point(module_scope)
