import sys
import telnetlib
from time import sleep

host = "10.1.1.3"
port = 3001

tn = telnetlib.Telnet(host, port)
def jfw_connect():
    jfw_prompt = tn.read_until("JFW>>")
    print "############ JFW Connected from client...!!! Below is the datail ############"
    print jfw_prompt


def jfw_getid():
    tn.write("IDN" + "\n")
    tn.write("\n")
    print tn.read_until("JFW>>")

def jfw_switch_port(port_num):
    print "Recieved port num:" + str(port_num)
    tn.write("\n")
    tn.write("\n")
    tn.read_until("JFW>>")
    port_num = str(port_num)
    print "command to send >>> ssr1 " + port_num
    tn.write("ssr" + "1" + " " + port_num + "\n")
    print tn.read_until("JFW>>")
    sleep(0.5)
    print "switch port to ssr1 " + port_num + "\n"

def jfw_close():
    tn.close()
    print "############### JFW Telnet connection closed!!! ###############"