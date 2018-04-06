import sys
import telnetlib
from time import sleep

host = "10.1.1.2"
port = 5023

tn = telnetlib.Telnet(host, port)

def pxa_connect():
    pxa_prompt  = tn.read_until("SCPI>")
    print "############ PXA Connected from client...!!! Below is the detail ############"
    print pxa_prompt

def pxa_getPower():
    sleep(1)
    print "Get power from PXA >>>"
    print "command to send >>> READ:CHPower:CHPower?"
    tn.write("READ:CHPower:CHPower?" + "\n")
    power = tn.read_until("SCPI>")
    print "Power result is " + power + "\n"
    return power

def pxa_getID():
    print "Get IDN"
    print "command to send >>> *IDN?"
    tn.write("*IDN?" + "\n")
    print tn.read_until("SCPI>")


def pxa_close():
    tn.close()
    print "############### PXA Telnet connection closed!!! ###############"
