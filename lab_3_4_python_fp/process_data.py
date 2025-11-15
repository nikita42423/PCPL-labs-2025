import json
import sys
import os
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
import random

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'data_light.json')

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    salaries = [f"зарплата {random.randint(100000, 200000)} руб." for _ in arg]
    return list(map(lambda x: f"{x[0]}, {x[1]}", zip(arg, salaries)))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
