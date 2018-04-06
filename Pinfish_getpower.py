import jfwTelnet as jfw
import pxaTelnet as pxa
import os.path
import numpy as np
import pandas as pd
import csv
import re
from time import sleep



power_list = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"
             ,"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"
             ,"0","0","0","0","0","0","0","0"]

last_jfw_port = 0

def power_insert_value(p):
    p = p.split('\r')[0]
    return p

def create_csv(pl):
    fname = raw_input("For save file before exit... please input Pinfish S/N:")
    dir_path = 'D:\Development\Project\CTH\CABU\Pinfish\Pinfish Auto Reader\Python Code\Test_result'
    fname_test_result = dir_path + '\\' + fname + '.csv'
    print "\nFile path >>> " + dir_path + "\n"
    if os.path.isfile(fname_test_result):
        print "File name >>> " + fname + " ....Already exist!!!!"
        backup_path = 'D:\Development\Project\CTH\CABU\Pinfish\Pinfish Auto Reader\Python Code\Test_result\Backup'
        backup_file = backup_path + '\\' + fname + '_2' + '.csv'
        np.savetxt(backup_file, pl, delimiter=",", fmt='%s')
        print "save backup file " + fname + " to " + backup_file + "    done...    :)\n"
    else:
        # print fname_test_result
        print "create new file >>> " + fname
        fname_full = fname_test_result
        np.savetxt(fname_full, pl, delimiter=",", fmt='%s')
        print "save file " + fname + " to " + fname_full + "\n"

    print "Saving file...\n"



def create_new_list(plist):
    from operator import itemgetter
    new_power_list = itemgetter(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)(plist)
    return  new_power_list

def print_power_list(list):
    list_counter = 1
    for i in list:
        if i != '0':
            print "Power at port J" + str(list_counter) + " =" + i + "\n"
        list_counter += 1

if __name__ == "__main__":

    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    print "Starting to test...\n"
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    jfw.jfw_connect()
    pxa.pxa_connect()

    while True:
        pxa_power = 0
        port_num = ""
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + "\n"
        print "Last JFW port is:" + str(last_jfw_port) + "\n"
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

        port_num = raw_input(""""Please input port number or type "exit" to close:""")
        if port_num == "":
            print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            print "You press enter only!!!"
            print "Switch will change port to 1"
            print "Please insert new port number"
            print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            port_num = 1


        elif port_num == 'exit':
            print "\n....................exit program!!!\n"
            break
        else:
            convert_portnum = int(port_num)
            if convert_portnum :
                # print(port_num)
                # print "Switch to port number: %s." % port_num
                jfw.jfw_switch_port(port_num)
                pxa_power = pxa.pxa_getPower()
                print "PXA read power = " + pxa_power
                power_list[int(port_num)] = str(power_insert_value(pxa_power))
                print "power_list value is :" + power_list[int(port_num)]

                # power_list.insert(int(port_num),str(power_insert_value(pxa_power)))

            elif port_num == "":
                print "You press Enter"
                print "Please insert new port number"

            else:
                print "Please insert new port number"
                print  port_num

        last_jfw_port = port_num




    print "Last JFW port is:" + str(last_jfw_port) + "\n"
    # print power_list[1:]
    # print "J22 resule is : " + power_list[21]
    new_power_list = create_new_list(power_list)
    # print  new_power_list
    print_power_list(new_power_list)

    # list_counter = 1
    # for i in new_list:
    #     if i != '0':
    #         print "Power at port J" + str(list_counter) + " =" + i + "\n"
    #     list_counter += 1

    create_csv(new_power_list)

    jfw.jfw_close()
    pxa.pxa_close()

