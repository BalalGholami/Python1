# Inheritence3
# Example: Data Streaming

class InvalidOperationError(Exception):
    # hameye exception ha bayad az class exception ers bari konand
    pass


class stream:
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


class filestreame(streaj):
    def read(self):
        print("Reading data from a file")


class NetworkStream(stream):
    def read(self):
        print("Reading Data from a Network")
