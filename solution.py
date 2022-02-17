# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(('127.0.0.1', port))
    serverSocket.listen(1)
    while True:
        # Establish the connection
        # print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            print('Ready to serve...')
            try:
                message = connectionSocket.recv(port).decode()
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()

                # Send one HTTP header line into socket.
                # Fill in start
                connectionSocket.send("HTTP/1.1 200 OK \r\n\r\n".encode())
                # Fill in end

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
        # Send response message for file not found (404)
        # Fill in start
                connectionSocket.send("file not found".encode())
        # Fill in end

        # Close client socket
        # Fill in start
                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
        # Fill in end

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)