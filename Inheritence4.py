# Inheritence4
# Example: Data Streaming
# Making abstract Class

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    # hameye exception ha bayad az class exception ers bari konand
    pass


class stream(ABC):
    def __init__(self):
        self.opened = False  # yani file dar hale hazer baste hast

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("stream is already Close")
        self.opened = false

    # we should force child classes to defein method
    # by using @abstractmethod which is defined in Up (import from abc...)
    @abstractmethod
    def read(self):
        pass


class filestreame(stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(stream):
    def read(self):
        print("Reading Data from a Network")


class MemoryStream(stream):
    def read(self):
        print("Reading Data from Memory")


example1 = MemoryStream()
example1.read()
