import socketserver
import os

history = "history.txt"

class MyTCPHandler(socketserver.StreamRequestHandler):
    # Store connected clients
    clients = []

    def handle(self):
        # Add the new client
        self.clients.append(self)

        # Read the client's name first
        self.name = self.rfile.readline().strip().decode("utf-8")
        print(f"[NEW CONNECTION] ({self.name}) connected")

        # Send history to new users
        self.send_history()

        try:
            while True:
                # Read message from the client
                self.data = self.rfile.readline().strip()
                if not self.data:
                    break  # Disconnect if no data

                # Format message with sender's name
                message = self.data.decode('utf-8')

                # Clears the chat if the user writes clear
                if message.lower() == "clear":
                    with open(history, "w") as file:
                        print("History cleared")
                else:
                    format_message = f"{self.name}: {message}"
                    print(format_message)

                    # Save message
                    self.save_message(format_message)

                    # Broadcast message to all clients
                    self.broadcast_message(format_message)

        finally:
            # Remove client on disconnect
            self.clients.remove(self)
            print(f"[DISCONNECTED] ({self.name}) disconnected")

    def send_history(self):
        # Send previous messages to new client from file
        if os.path.exists(history):
            with open(history, "r") as file:
                for message in file:
                    self.wfile.write(bytes(message, "utf-8"))
                    self.wfile.flush()

    def save_message(self, message):
        # Save message to file
        with open(history, "a") as file:
            file.write(message + "\n")

    def broadcast_message(self, message):
        # Send a message to all connected clients except the sender
        formatted_message = message + "\n"
        for client in self.clients:
            if client != self:
                client.wfile.write(bytes(formatted_message, "utf-8"))
                client.wfile.flush()

# Handling multiple clients
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    # Listen on all interfaces
    HOST, PORT = "0.0.0.0", 9999
    # Run the server
    with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Server started on {HOST}:{PORT}")
        server.serve_forever()