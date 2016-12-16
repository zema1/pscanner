# coding = utf-8


import re
import socket
import optparse
import sys

common_ports = """1, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 25, 37, 39, 42, 43, 49, 50, 53, 63, 67, 68, 69, 70, 71, 72, 73, 73, 79, 80,
                88, 95, 101, 102, 105, 107, 109, 110, 111, 113, 115, 117, 119, 123, 137, 138, 139, 143, 161, 162, 163, 164, 174, 177, 178, 179,
                191, 194, 199, 201, 202, 204, 206, 209, 210, 213, 220, 245, 347, 363, 369, 370, 372, 389, 427, 434, 435, 443, 444, 445, 464, 468,
                487, 488, 496, 500, 535, 538, 546, 547, 554, 563, 565, 587, 610, 611, 612, 631, 636, 674, 694, 749, 750, 751, 752, 754, 760, 765,
                767, 873, 992, 993, 994, 995, 1080, 1109, 1236, 1300, 1433, 1434, 1494, 1512, 1524, 1525, 1645, 1646, 1649, 1701, 1718, 1719, 1720,
                1758, 1759, 1789, 1812, 1813, 1911, 1985, 1986, 1997, 2049, 2053, 2102, 2103, 2104, 2105, 2401, 2430, 2430, 2431, 2600, 2601, 2602,
                2603, 2604, 2605, 2606, 2809, 3130, 3306, 3346, 4011, 4321, 4444, 5002, 5308, 5999, 6000, 7000, 7001, 7002, 7003, 7004, 7005, 7006,
                7007, 7008, 7009, 9876, 10080, 11371, 11720, 13720, 13721, 13722, 13724, 13782, 13783, 22273, 26000, 26208, 33434"""

# test_ports = """80, 1433, 443, 8000, 8080"""


def anlyze_host(target_host):
    """check and convert domain to xx.xx.xx.xx"""
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    match = pattern.match(target_host)
    if match:
        return(match.group())
    else:
        try:
            target_ip = socket.gethostbyname(target_host)
            print("Get ip of %s: %s\n" % (target_host, target_ip))
            return(target_ip)
        except socket.gaierror:
            print(err, 'Hostname could not be resolved.\n')
        except Exception as err:
            print("Unknown error. Please check your network.")
            exit(0)


def anlyze_ports(target_ports):
    try:
        pattern = re.compile(r'(\d+)-(\d+)')
        match = pattern.match(target_ports)
        if match:
            start_port = int(match.group(1))
            end_port = int(match.group(2))
            return([x for x in range(start_port, end_port + 1)])
        else:
            return([int(x) for x in target_ports.split(',')])
    except Exception as err:
        print("\nports format error")
        print(parser.usage)
        exit(0)


def parse_opt():
    usage = 'Usage: python {} -t <host> -p <port>'.format(sys.argv[0])
    parser = optparse.OptionParser(usage, version='%prog v0.1')
    parser.add_option('-t', '--target', dest='target_host', type='string',
                      help='specify target host(s)')
    parser.add_option('-p', '--port', dest='target_port', type='string',
                      help='<port ranges>: Only scan specified ports',
                      default=common_ports)
    parser.add_option('--thread', dest='thread', type='int',
                      help='specify thread count', default=20)
    (options, args) = parser.parse_args()
    if options.target_host is None:
        parser.print_help()
        exit(0)
    else:
        return options, args
