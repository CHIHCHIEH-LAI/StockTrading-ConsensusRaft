# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\x12\x04raft\"\x96\x01\n\x0c\x45ntryRequest\x12\x10\n\x08leaderId\x18\x01 \x01(\x05\x12\x0f\n\x07logTerm\x18\x02 \x01(\x05\x12\x10\n\x08logIndex\x18\x03 \x01(\x05\x12&\n\x0btransaction\x18\x04 \x01(\x0b\x32\x11.raft.Transaction\x12\x13\n\x0bprevLogTerm\x18\x05 \x01(\x05\x12\x14\n\x0cprevLogIndex\x18\x06 \x01(\x05\"\xc4\x01\n\x0bTransaction\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x0f\n\x07stockId\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x12:\n\x0ftransactionType\x18\x06 \x01(\x0e\x32!.raft.Transaction.TransactionType\"$\n\x0fTransactionType\x12\x07\n\x03\x42UY\x10\x00\x12\x08\n\x04SELL\x10\x01\"C\n\rEntryResponse\x12\x0f\n\x07logTerm\x18\x01 \x01(\x05\x12\x10\n\x08logIndex\x18\x02 \x01(\x05\x12\x0f\n\x07success\x18\x03 \x01(\x08\"[\n\x0bVoteRequest\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\x05\x12\x14\n\x0clastLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0blastLogTerm\x18\x04 \x01(\x05\"1\n\x0cVoteResponse\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0bvoteGranted\x18\x02 \x01(\x08\x32G\n\x11\x43lientRaftService\x12\x32\n\x08\x41\x64\x64\x45ntry\x12\x11.raft.Transaction\x1a\x13.raft.EntryResponse2\x83\x01\n\x13InternalRaftService\x12\x36\n\x0b\x41ppendEntry\x12\x12.raft.EntryRequest\x1a\x13.raft.EntryResponse\x12\x34\n\x0bRequestVote\x12\x11.raft.VoteRequest\x1a\x12.raft.VoteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ENTRYREQUEST']._serialized_start=21
  _globals['_ENTRYREQUEST']._serialized_end=171
  _globals['_TRANSACTION']._serialized_start=174
  _globals['_TRANSACTION']._serialized_end=370
  _globals['_TRANSACTION_TRANSACTIONTYPE']._serialized_start=334
  _globals['_TRANSACTION_TRANSACTIONTYPE']._serialized_end=370
  _globals['_ENTRYRESPONSE']._serialized_start=372
  _globals['_ENTRYRESPONSE']._serialized_end=439
  _globals['_VOTEREQUEST']._serialized_start=441
  _globals['_VOTEREQUEST']._serialized_end=532
  _globals['_VOTERESPONSE']._serialized_start=534
  _globals['_VOTERESPONSE']._serialized_end=583
  _globals['_CLIENTRAFTSERVICE']._serialized_start=585
  _globals['_CLIENTRAFTSERVICE']._serialized_end=656
  _globals['_INTERNALRAFTSERVICE']._serialized_start=659
  _globals['_INTERNALRAFTSERVICE']._serialized_end=790
# @@protoc_insertion_point(module_scope)
