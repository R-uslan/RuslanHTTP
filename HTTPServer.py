import socket

from TCPServer import TCPServer


class HTTPServer(TCPServer):
    def handle_connection(self, conn: socket.socket, addr: tuple) -> None:
        """
        Handles the incoming HTTP request.
        """
        raw_request = self.get_raw_request(conn)

        conn.sendall(raw_request)

        print(f"Handled connection from {addr}")

    def get_raw_request(self, conn: socket.socket) -> bytearray:
        HTTP_HEADER_END = b"\r\n\r\n"
        raw_request = bytearray()

        while chunk := conn.recv(self.buffer_size):
            raw_request.extend(chunk)
            if HTTP_HEADER_END in raw_request:
                break
        return raw_request


if __name__ == "__main__":
    server = HTTPServer()
    server.start()
