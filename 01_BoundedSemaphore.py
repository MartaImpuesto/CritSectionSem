#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:08:28 2022

@author: Marta Impuesto
"""

from multiprocessing import Process, BoundedSemaphore
from multiprocessing import current_process
from multiprocessing import Value, Array

N = 8
def task(sem, common, tid):
    sem.acquire()
    try:
        for i in range(100):
            print(f"{tid}−{i}: Critical section", flush = True)
            v = common.value + 1
            print(f"{tid}−{i}: Inside critical section", flush = True)
            common.value = v
            print(f"{tid}−{i}: End of critical section", flush = True)
    finally:
        sem.release()
        
def main():
    sem = BoundedSemaphore(1)
    lp = []
    common = Value('i', 0)
    
    for tid in range(N):
        lp.append(Process(target=task, args=(sem, common, tid)))
    print (f"Valor inicial del contador {common.value}", flush = True)
    for p in lp:
        p.start()
        
    for p in lp:
        p.join()
    
    print (f"Valor final del contador {common.value}", flush = True)
    print ("fin")
    
if __name__ == "__main__":
    main()