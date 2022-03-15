#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:26:32 2022

@author: alejandro
"""

from multiprocessing import Process
from multiprocessing import Condition, Lock
from multiprocessing import Array, Manager
import time
import random

from monitor import Table

NPHIL = 5
K = 100

def delay(n):
    time.sleep(random.random()/n)

def philosopher_task(num:int, table: Table):
    table.set_current_phil(num)
    while True:
        print (f"Philosopher {num} thinking", flush = True)
        print (f"Philosopher {num} wants to eat", flush = True)
        table.wants_eat(num)
        print (f"Philosopher {num} eating", flush = True)
        table.wants_think(num)
        print (f"Philosopher {num} stops eating", flush = True)

def main():
    manager = Manager()
    table = Table(NPHIL, manager)
    philosophers = [Process(target=philosopher_task, args=(i,table)) for i in range(NPHIL)]
    for i in range(NPHIL):
        philosophers[i].start()
    for i in range(NPHIL):
        philosophers[i].join()

if __name__ == "__main__":
    main()