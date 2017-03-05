import sys
import subprocess
import shlex
import os
import shutil
from application_runner import application_runner
import time
from controller import controller
class pyretic_application_runner(application_runner):

	def __init__(self, config, testBedHomePath):
        	self.config = config
        	self.testbedhome = testBedHomePath
        

	def runApp(self , applicationName , config, testbedhome):
		#self.port = self.config['port']
                #os.chdir(self.testbedhome+"apps/pyretic")
                shutil.copy(self.config['appsdir']+applicationName , self.config['home']+'/pyretic/modules')
		os.chdir(self.config['home'])
		process = subprocess.Popen(["pyretic.py" , "-m" , "p0" , "pyretic.modules."+applicationName.split(".")[0] ], shell=False, stdout=subprocess.PIPE)
                while True:
                        if controller.check_port(int(self.config['port'])) == 0:
                                break
                        else:
                                time.sleep(0.1)
		#time.sleep(3)
		#out, err = process.communicate(commands)
                #print out


        def stopApp(self):
                print "stopping application"
		try:
                        cmd = 'lsof -t -i:{0}'.format(self.config['port'])

                        pid = subprocess.check_output(cmd, shell=True)
                        pid = int(pid)
                        killcmd = 'kill -9 {0}'.format(pid)
                        os.system(killcmd)

                        cmd2 = 'lsof -t -i:{0}'.format(41414)
                        pid2 = subprocess.check_output(cmd2, shell=True)
                        pid2 = pid2.replace('\n',' ')
                        killcmd2 = 'kill -9 {0}'.format(pid2)
                        os.system(killcmd2)
                except subprocess.CalledProcessError, e:
                        print e.output
