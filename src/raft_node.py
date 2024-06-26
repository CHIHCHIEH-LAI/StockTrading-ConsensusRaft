import asyncio
from loguru import logger

from src.consensus.heartbeat_manager import HeartbeatManager
from src.consensus.log_manager import LogManager, LogEntry
from src.consensus.state_machine import StateMachine
from src.consensus.election_module import ElectionModule
from src.channel.grpc_client import gRPCClient
from src.schema.transaction import Transaction

class RaftNode:
    def __init__(self, nodeId: int, memberTable: dict):
        self.nodeId = nodeId
        self.memberTable = memberTable
        self.gRPC_client = gRPCClient()
        self.state_machine = StateMachine()
        self.log_manager = LogManager(nodeId, memberTable, self.gRPC_client)
        self.election_module = ElectionModule(self.log_manager, self.gRPC_client, self.state_machine, memberTable)
        self.heartbeat_manager = HeartbeatManager(self.gRPC_client, memberTable)
     
    async def run(self):
        while not self.state_machine.is_stopped():
            if self.state_machine.is_follower():
                self.wait_for_heartbeat()
            elif self.state_machine.is_candidate():
                await self.run_election()
            elif self.state_machine.is_leader():
                await self.multicast_heartbeats()
            else:
                break
            self.print_snapshot()
            await asyncio.sleep(1)

    def stop(self):
        self.state_machine.to_stopped()

    def wait_for_heartbeat(self):
        if self.heartbeat_manager.has_timed_out():
            self.state_machine.to_candidate()

    async def run_election(self):
        voteRequest = {
            'term': self.state_machine.get_current_term(),
            'candidateId': self.nodeId,
            'lastLogIndex': self.log_manager.get_last_index(),
            'lastLogTerm': self.log_manager.get_last_term()
        }
        success = await self.election_module.run_election(self.nodeId, voteRequest)
        if success:
            self.election_module.update_leaderId(self.nodeId)
            self.state_machine.to_leader()
        else:
            self.state_machine.to_follower()

    def respond_vote_request(self, term: int, lastLogIndex: int, lastLogTerm: int):
        return self.election_module.respond_vote_request(
            term=term,
            lastLogIndex=lastLogIndex, 
            lastLogTerm=lastLogTerm
        )

    async def multicast_heartbeats(self):
        heartbeat = {
            'leaderId': self.nodeId,
            'term': self.state_machine.get_current_term()
        }
        await self.heartbeat_manager.multicast_heartbeats(self.nodeId, heartbeat)

    def respond_heartbeat(self, term: int, leaderId: int):
        if term >= self.state_machine.get_current_term():
            self.state_machine.set_current_term(term)
            self.state_machine.to_follower()
            self.heartbeat_manager.update_heartbeat()
            self.election_module.update_leaderId(leaderId)
            return True
        return False
    
    async def add_transaction(self, transaction: Transaction):
        if self.nodeId != self.election_module.leaderId:
            host, port = self.memberTable[self.election_module.leaderId]
            success = await self.gRPC_client.make_add_transaction_rpc(host, port, transaction.to_dict())
            return success
        else:
            success = await self.log_manager.add_transaction(self.state_machine.get_current_term(), transaction.to_dict())
            return success
    
    def append_log_entry(self, log_entry: LogEntry):
        success = self.log_manager.append_log_entry(log_entry)
        return success, 0, 0
    
    def print_snapshot(self):
        snapshot = {
            'nodeId': self.nodeId,
            'state': self.state_machine.state,
            'currentTerm': self.state_machine.currentTerm,
            'heartbeatTimeout': self.heartbeat_manager.heartbeatTimeout,
            'lastHeartbeat': f'{self.heartbeat_manager.lastHeartbeat.minute}:{self.heartbeat_manager.lastHeartbeat.second}',
            # 'voteCount': self.election_module.vote_count,
            'leaderId': self.election_module.leaderId,
            'lastTerm': self.log_manager.get_last_term(),
            'lastIndex': self.log_manager.get_last_index(),
            'lastEntry': self.log_manager.entries[-1].transaction.to_dict() if len(self.log_manager.entries) > 0 else None
        }
        logger.debug(f'Snapshot: {snapshot}')
