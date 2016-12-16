# coding=utf-8

import socket
import traceback
import logging
from datetime import datetime
from multiprocessing.dummy import Pool
from functools import partial
from lib.services import service
from lib.checker import check_port
from lib.preprocess import *


def pr_result(result):
    print('#' * 10)
    for r in result:
        if r is not None:
            print("{0:<5} {1:<12} {2}".format(r[0], service(r[0]), r[1]))

if __name__ == '__main__':
    options, args = parse_opt()
    target_ip = anlyze_host(options.target_host)
    target_ports = anlyze_ports(options.target_port)
    print("\nstart scanning at %s\n" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    start_time = datetime.now()
    check_func = partial(check_port, target_ip)
    with Pool(options.thread) as pool:
        pool = Pool(options.thread)
        result = pool.map(check_func, target_ports)
        pr_result(result)
        time_delta = datetime.now() - start_time
        print("\nSpeed %s to scan" % str(time_delta))
