"""
craft_api.py -- The pycraft API

"""


import zmq


class CraftAPI:
    """a class for pycraft API"""
    def __init__(self):
        """
        The constructor for class CraftAPI

        The constructor creates ZeroMQ context and connects the socket to
        port 1234, the default port of pycraft.
        """
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect('tcp://localhost:1234')


    def add_brick_block(self, position):
        """
        add_brick_block -- add a brick block to a given position

        Arguments:
        position -- the position of the block
        """
        self.socket.send(' '.join(repr(n) for n in position).encode('utf-8'))
