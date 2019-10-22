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
    data = {
        'ip':{},
        'url':{},
        'ua':{},
        'status':{}
    }
    for item in parse(path):
        for key,value in data.items():

            if key != 'throughput':

                data[key] = count(item[key],value)


        data['throughput'] += int(item['length'])


    return data


def render_line(name,data):
    pass


