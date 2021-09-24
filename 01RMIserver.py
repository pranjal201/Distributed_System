import Pyro4
import random
import os
import datetime
import subprocess

now = datetime.datetime.now()
print('date: '+now.strftime('%d-%m-%y')+'Time: '+now.strftime('%H:%M:%S'))


@Pyro4.expose
class Server(object):
    def get_usid(self, name):
        return "Hello {0}.\nYour Current User Session is {1}:".format(name, random.randint(0,1000))

    def add(self, a, b):
        return "{0}+{1} = {2}".format(a, b, a+b)

    def sub(self, a, b):
        return "{0}-{1} = {2}".format(a, b, a-b)

    def multiply(self, a, b):
        return "{0}*{1} = {2}".format(a, b, a*b)

    def divide(self, a, b):
        return "{0}//{1} = {2}".format(a, b, a//b)

    def table(self, a):
        tab = [a*i for i in range(1, 11)]
        return tab


daemon = Pyro4.Daemon()

ns = Pyro4.locateNS()
url = daemon.register(Server)
ns.register("RMI.calculator", url)
print("The server is now active, please request your calculations or start file\
transfer")
daemon.requestLoop()
