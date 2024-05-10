import asyncio
import logging
import grpc
import time

from src.raft_node import RaftNode
from src.channel.proto import raft_pb2_grpc
from src.channel.grpc_server import gRPCServer

# Configure the logging module
logging.basicConfig(level=logging.INFO)

async def serve(id: int, memberTable: dict):
    raft_node = RaftNode(id, memberTable)
    server = grpc.aio.server()
    raft_pb2_grpc.add_RaftServiceServicer_to_server(gRPCServer(raft_node), server)
    host, port = memberTable[id]
    server.add_insecure_port(f'{host}:{port}')

    await server.start()
    time.sleep(5)
    # await raft_node.run()
    await server.wait_for_termination()

async def start_service():
    memberTable = {
        1: ('localhost', 50051),
        2: ('localhost', 50052),
        3: ('localhost', 50053),
        4: ('localhost', 50054),
        5: ('localhost', 50055)
    }

    servers = [
        serve(1, memberTable),
        serve(2, memberTable),
        serve(3, memberTable),
        serve(4, memberTable),
        serve(5, memberTable)
    ]

    await asyncio.gather(*servers)

if __name__ == '__main__':

    asyncio.run(start_service())