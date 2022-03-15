#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:19:21 2022

@author: alejandro
"""
from multiprocessing import Process
from multiprocessing import Condition, Lock
from multiprocessing import Array, Manager

# En el 7 los que hacen trampas son el 0 y el 2
class Table():
    def __init__(self, NPHIL, manager):
        self.NPHIL = NPHIL
        self.list_phil = manager.list([False for i in range(NPHIL)])
        self.mutex = Lock()
        self.free_fork = Condition(self.mutex)
        self.phil= None
        
    def set_current_phil(self, num):
        self.phil = num
    
    def wants_eat(self, num):
        self.mutex.acquire()
        self.free_fork.wait_for(self.no_comen_lados)
        self.list_phil[self.phil] = True
        #print(self.list_phil[:], flush = True)
        #self.list_phil[num] = True
        self.mutex.release()
        
    def no_comen_lados(self):
        return (not self.list_phil[(self.phil-1)%self.NPHIL]) and (not self.list_phil[(self.phil+1)%self.NPHIL])
    
    def wants_think(self, num):
        self.mutex.acquire()
        self.list_phil[self.phil] = False
        #self.list_phil[num] = False
        #print(self.list_phil[:], flush = True)
        self.free_fork.notify()
        self.mutex.release()
    
    
    
    
    
    
    
    
    
    