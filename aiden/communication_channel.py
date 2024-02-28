import socket

class CommunicationChannel:
    def __init__(self):
        """
        Initialize a new CommunicationChannel instance. This creates a new socket object for communication.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def establish_connection(self, host, port):
        """
        Establish a connection to the specified host and port. If successful, print a message indicating the connection was established.
        If an error occurs during the connection attempt, print the error message.

        :param host: The host to connect to.
        :param port: The port to connect to.
        """
        try:
            self.socket.connect((host, port))
            print("Connection established with the server.")
        except socket.error as e:
            print(f"Something went wrong: {e}")

    def close_connection(self):
        """
        Close the current communication connection. This closes the socket and prints a message indicating the connection was closed.
        """
        self.socket.close()
        print("Connection closed with the server.")

    def send_message(self, message):
        """
        Send the specified message to the connected server. The message is encoded as UTF-8 before sending. If successful, print a message indicating the message was sent.
        If an error occurs during the send attempt, print the error message.

        :param message: The message to send to the server.
        """
        try:
            self.socket.sendall(message.encode('utf-8'))
            print("Message sent to the server.")
        except socket.error as e:
            print(f"Something went wrong: {e}")

    def receive_message(self):
        """
        Receive a message from the connected server. The message is decoded as UTF-8 after receiving. If successful, print the received message.
        If an error occurs during the receive attempt, print the error message.

        :return: The received message from the server.
        """
        try:
            data = self.socket.recv(1024)
            print(
