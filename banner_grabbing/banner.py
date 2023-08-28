#!/usr/bin/python2.7
import socket
import sys

if len(sys.argv)<=2:
    print "Incorret use"
    print sys.argv[0], "[TARGET] [PORT]"
    exit()

ip = sys.argv[1]
port = int(sys.argv[2])

def get_name(p):
    found = False
    try:
        name = socket.getservbyport(p)
        print "Unavailable service -->", p, "[", socket.getservbyport(p),"]"
    except socket.error:
        print "Unavailable service -->", p, "[no service name]"

def http(p):
    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.settimeout(2.3)
        mysocket.connect((ip,p))
        payload = mysocket.send("HEAD / HTTP/1.0\r\n\r\n")
        banner = mysocket.recv(1024)
        mysocket.close()
        return banner
    except socket.timeout:
        get_name(p)
        exit()

if (port == 80 or port == 443):
    banner = http(port)
    print banner
    exit()

try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.settimeout(2.3)
    conn = mysocket.connect((ip,port))
    banner = mysocket.recv(1024)
    mysocket.close()

    print "\n", banner

except socket.timeout:
    get_name(port)
    exit()
