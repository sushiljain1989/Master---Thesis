import sys
import subprocess
import shlex
import os
import time
from controller import controller
class FreneticController(controller):

	def runController(self , config):
		self.ip = config['ip']
		self.port = config['port']
		print "running controller at -> "+self.ip + ":" + self.port
		self.process = subprocess.Popen(["frenetic" , "http-controller" ], shell=False, stdout=subprocess.PIPE)
		while True:
                        if controller.checkPort(int(config['port'])) == 0:
                                break
                        else:
                                time.sleep(0.1)
		while True:
                        if controller.checkPort(8984) == 0:
                                break
                        else:
                                time.sleep(0.1)

		time.sleep(1)
		#print self.process.pid
		
		

	def stopController(self):
		print "stopping controller"
        	print self.port
        	cmd = 'lsof -t -i:{0}'.format(self.port)
        	pid = subprocess.check_output(cmd, shell=True)
        	pid = int(pid)
        	print pid
        	killcmd = 'sudo kill -9 {0}'.format(pid)
        	killcmd2 = 'sudo kill -9 {0}'.format(self.process.pid)
        	os.system(killcmd)
        	os.system(killcmd2)
