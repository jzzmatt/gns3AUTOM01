#!/usr/bin/env python

import telnetlib
import sys
import time
import threading


def get_ip():
    hostslists = []
    hostDB = {}
    hosts_ip = []
    host_files = raw_input("Enter your host files\n->: ")

    with open(host_files, 'r') as files:
           for item in files.readlines():
                hosts_ip.append(item.rstrip('\n'))


    print(hosts_ip)

#    if len(hostslists) != 0:
#        for item in hostslists:
#             hostDB[item[1]] = item[0]
#    #print(hostDB)


#    for name, ip in hostDB.items():
#        hosts_ip.append(ip)


    return hosts_ip


def open_telnet_conn(ip, command):
     credential = {
                  'username': 'junior.mateus',
                  'password' : 'Checkk2009'
                   }
     tn= telnetlib.Telnet(ip)
     tn.read_until('Username:')
     tn.write(credential['username'] + "\n")
     time.sleep(1)

     if credential['password']:
        tn.read_until('Password:')
        tn.write(credential['password'] + "\n")
        time.sleep(1)


     tn.write("terminal length 0\n")
     time.sleep(1)


     tn.write("config term\n")
     time.sleep(1)



     with open(command, 'r') as f_command:
          for line in f_command.readlines():
                    tn.write(line+"\n")
                    time.sleep(1)


     output= tn.read_very_eager()
     print("------DISPLAY OUTPUT COMMAND ------")
     print(output)
     tn.close()
     print("**___SETUP {} ____END**".format(ip))
     time.sleep(1)



def create_threads():
     file_commands = raw_input('Enter your file command\n->: ')
     threads = []
     for ip in get_ip():
          #print("Execute on ip {}".format(ip))
          th = threading.Thread(target = open_telnet_conn, args = (ip,file_commands))
          th.start()
          threads.append(th)


     for th in threads:
               th.join()

if __name__=="__main__":
         create_threads()