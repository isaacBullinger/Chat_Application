import socket
import sys
import threading

HOST, PORT = "192.168.1.139", 9999  # Sets host server IP and communication port

# Gets user name for introduction
name = input("Please enter your name: ") 

# Gives a list of options to the new user
print(f"Welcome to the chat {name}!\nOptions:\nType \"exit\" to exit.\nType \"clear\" to clear the chat history.")

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode("utf-8")
            if not message:
                break

            # Display received messages
            print(message) 
        except:
            break

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    
    # Send the name first
    sock.sendall(bytes(name + "\n", "utf-8"))

    # Start a thread to receive messages
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    # Send messages in a loop
    while True:
        msg = input()
        if msg.lower() == "exit":
            break  # Exit chat
        sock.sendall(bytes(msg + "\n", "utf-8"))