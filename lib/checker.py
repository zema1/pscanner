# coding=utf-8

import socket


def check_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        try:
            result = sock.connect_ex((ip, port))
        except KeyboardInterrupt:
            print("\nYou pressed Ctrl+C, Stopping Program.\n")
            exit(0)
        except socket.error as e:
            print("Couldn't connect to server\n")
            exit(0)
        except Exception as e:
            print("Unknown error occured", e)
            exit(0)

    if result == 0:
        return port, 'open'
    elif result == 10061:
        return port, 'closed'
    elif result == 10035:
        return port, 'filtered'
