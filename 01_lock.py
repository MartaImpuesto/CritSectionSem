#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:08:28 2022

@author: Marta Impuesto
"""

from multiprocessing import Process, Lock
from multiprocessing import current_process
from multiprocessing import Value, Array

N = 8
def task(lock, common, tid):
    lock.acquire()
    try:
        for i in range(100):
            print(f"{tid}−{i}: Critical section", flush = True)
            v = common.value + 1
            print(f"{tid}−{i}: Inside critical section", flush = True)
            common.value = v
            print(f"{tid}−{i}: End of critical section", flush = True)
    finally:
        lock.release()
        
def main():
    lock = Lock()
    lp = []
    common = Value('i', 0)
    
    for tid in range(N):
        lp.append(Process(target=task, args=(lock, common, tid)))
    print (f"Valor inicial del contador {common.value}", flush = True)
    for p in lp:
        p.start()
        
    for p in lp:
        p.join()
    
    print (f"Valor final del contador {common.value}", flush = True)
    print ("fin")
    
if __name__ == "__main__":
    main()