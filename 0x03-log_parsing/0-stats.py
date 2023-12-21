#!/usr/bin/python3
""" This module defines a script that adds all arguments to a Python list,
    and then save them to a file
"""
import sys


def print_status(status_l, size):
    print("File size: {:d}".format(size))
    for i in status_l:
        if status_l[i] != 0:
            print("{}: {:d}".format(i, status_l[i]))


if __name__ == "__main__":
    s_list = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
              '405': 0, '500': 0}
    line_cnt = 0
    tot_sz = 0
    try:
        for line in sys.stdin:
            if line_cnt % 10 == 0 and line_cnt != 0:
                print_status(s_list, tot_sz)
            try:
                list_line = [x for x in line.split(" ") if x.strip()]
                if list_line[-2] in s_list:
                    s_list[list_line[-2]] += 1
                tot_sz += int(list_line[-1].strip("\n"))
            except Exception:
                pass
            line_cnt += 1
    except KeyboardInterrupt:
        print_status(s_list, tot_sz)
        raise
    print_status(s_list, tot_sz)
