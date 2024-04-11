
# TCP SYN Flood Simulation and Socket Communication

This project includes two separate Python scripts demonstrating two different networking concepts:

## 1. TCP SYN Flood Attack Simulation
This script simulates a TCP SYN flood attack using the Scapy library. It's intended for educational purposes to understand how SYN flood attacks work. The script sends a specified number of TCP/IP packets with random source IPs and ports to a target destination.

### Usage
- The user is prompted to enter the destination IP address, destination port, and the number of packets to send.
- The script requires Python 3 and the Scapy library.
- Ensure to use this script responsibly and ethically, with explicit permission from the target host.

## 2. Socket Communication
This part of the project demonstrates basic socket programming in Python, including a simple server-client communication setup.

### Server
- The server script initializes a socket, binds to a specified port (above 1024), and listens for incoming connections.
- Upon a successful connection, it sends a welcome message to the client before closing the connection.

### Client
- The client script connects to the server using its hostname and port.
- It receives a welcome message from the server and then closes the connection.

### Getting Started
- Run the server script first to ensure it's listening for connections.
- Then, run the client script to initiate communication with the server.

## Prerequisites
- Python 3
- Scapy library for the TCP SYN flood simulation script
- A network environment where the server and client scripts can communicate

