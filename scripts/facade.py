class TCPConnection:
    def connect(self):
        print("TCPConnection: connect")

class UDPConnection:
    def connect(self):
        print("UDPConnection: connect")

class HTTPConnection:
    def connect(self):
        print("HTTPConnection: connect")

class NetworkFacade:
    def __init__(self):
        self.tcp_connection = TCPConnection()
        self.udp_connection = UDPConnection()
        self.http_connection = HTTPConnection()

    def connect(self, protocol):
        if protocol == "TCP":
            self.tcp_connection.connect()
        elif protocol == "UDP":
            self.udp_connection.connect()
        elif protocol == "HTTP":
            self.http_connection.connect()

network = NetworkFacade()
network.connect("TCP")
network.connect("UDP")
network.connect("HTTP")
