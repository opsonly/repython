 #!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2019-10-22 08:45 
# @Author : opsonly 
# @Site :  
# @File : nglog.py 
# @Software: PyCharm

import sys
import re

def read_log(path):
    with open(path) as f:
        for line in f:
            yield line



def parse(path):
    o = re.compile(r'(?P<ip>\d{1,3}\.)')
    for line in read_log(path):
        m = o.search(line.rstrip('\n'))
        if m:
            yield m.groupdict()



def count(key,data):
    if key not in data.keys():
        data[key] = 0
    data[key] += 1
    return data


def analyze(path):
    ret = {}

    def init_data():
        return {
            'ip':{},
            'url':{},
            'ua':{},
            'status':{}
        }
    for item in parse(path):
        time = item['time'].strftime('%Y%m%d%H%M')
        if time not in ret.keys():
            ret[time] = init_data()

        data = ret[time]

        for key,value in data.items():

            if key != 'throughput':

                data[key] = count(item[key],value)


        data['throughput'] += int(item['length'])


    return ret


def render_line(name,data):
    pass

def render_pie(name,data):
    pass

def main():
    data = analyze(sys.argv[1])

    throughput = []
    rs = list(data.items())
    rs.sort(key=lambda x:x[0])
    throughput = [x[1]['throughput'] for x in rs]
