import shutil
import subprocess

__author__ = 'root'

class Container:

    def __init__(self,name,path):
        self.name = name

        self.path = path
        #path is from / at qemu     "/container/lxc1"

        self.free = True


    def startContainer(self):

        cmd = "virsh -c lxc:// start " + self.name
        subprocess.call(cmd,shell = True)
        return

    def stopContainer(self):

        cmd = "virsh -c lxc:// destroy " + self.name
        subprocess.call(cmd,shell = True)
        return


    def reloadContainer(self):

        #remove /<container path>/var/www/html/hackademic
        shutil.rmtree(self.path + "/var/www/html/hackademic")

        #remove session files
        #session files stored at self.path/var/lib/php/session/sess_<session_id>
        self.free = True
        return

    def isFree(self):
        return self.free

if __name__=='__main__':

    temp = Container('rootfs','/container/rootfs')
    temp.startContainer()
    temp.stopContainer()




