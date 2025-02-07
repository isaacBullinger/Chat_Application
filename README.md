# Overview

This is a simple chat application I wrote in Python!

Make sure you have Python installed on all machines. You also need to get the IP address of the server machine. This is done by going into the terminal or command prompt and typing these commands:

For a Linux machine use the command:
```
ip a
```

In Windows use the command:
```
ipconfig
```

Update the IP address in TCP_client.py to the IP address of the server.

Choose a machine for the server. Download the file TCP_server.py to the machine. Then download TCP_client.py to the clients. After that run the TCP_server.py file on the server machine.
Navigate to the directory that your python file is in the terminal, then run it using this command:
```
python TCP_server.py
```
or
```
python3 TCP_server.py
```

Navigate to the directory that the python file is in. Then run TCP_client.py on the clients.
```
python TCP_client.py
```
or
```
python3 TCP_client.py
```

The client file will ask for your name, input it. Then type a message, the message will be sent to all of the clients on the server. When a user connects, the server sends a message to all users.

There is also persistent storage in a history.txt file. Any new clients can read the chat history. Any client can clear the chat history by typing "clear". Clients can also disconnect from the chat by typing "exit".

I wanted to write this software to increase my skill in networks. So I decided to build a simple chat application in the terminal.

[Software Demo Video](https://youtu.be/UGaR3pt96kg)

# Network Communication

I used a client/server architecture for the messaging app, This allows multiple users to connect and chat at the same time.

I used TCP and port 9999.

The format of messages sent between client and server are text-based messages encoded in UTF-8.

# Development Environment

I used Visual Studio code with the NeoVim extension on my Linux operating system. I chose a Debian operating system for the server and used NeoVim to write the server code. To test the software I used VirtualBox with a Windows virtual machine as another client and a Debian virtual machine as the server. I used my host machine as a client.

I used Python as the programming languages.
Libraries:
os
socket
socketserver
sys
threading

# Useful Websites

* [Python Socketserver Documentation](https://docs.python.org/3/library/socketserver.html)
* [VirtualBox](https://www.oracle.com/virtualization/technologies/vm/downloads/virtualbox-downloads.html)

# Future Work

* Implement a way to close the server.
* Add a way for users to privately message each other.
* Only allow admins to clear the chat history.
