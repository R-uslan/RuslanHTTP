import socket


class TCPServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 8080):
        self.address = (host, port)
        self.running = False
        self.socket: socket.socket = None
        self.buffer_size = 4096  # Used for recv

    def start(self):
        """
        Creates a socket, listens on the specified address, and accepts connections.
        """
        self.running = True
        print(f"Starting server on {self.address}...")

        self.s = socket.create_server(self.address, reuse_port=True)

        while self.running:
            try:
                conn, addr = self.s.accept()
                print(f"Connection from {addr}")
                self.handle_connection(conn, addr)
                conn.close()
            except KeyboardInterrupt:
                print("Keyboard interrupt detected.")
                self.stop()

    def stop(self):
        """
        Gracefully shutdown server.
        """
        print("Stopping server...")
        self.running = False
        if self.socket:
            self.socket.close()

    def handle_connection(self, conn, addr):
        """
        Handle the TCP connection. To be overridden by inheritor.
        """
        print(f"Handled connection from {addr}")
        conn.recv(self.buffer_size)
        conn.sendall(b"Connection received")


if __name__ == "__main__":
    server = TCPServer()
    server.start()
