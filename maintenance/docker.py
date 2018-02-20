# coding: utf-8
import os


class Docker:

    def __init__(self, dirs, name, is_production):
        self.name = name
        self.dir = dirs
        self.is_production = is_production


    def build_project(self):
        os.chdir(self.dirs)
        os.system('build -t ' + self.name + ' .s')


    def run_images(self):
        return 0


    def del_images(self):
        return os.system('docker rmi ' + self.name)


    def list_images(self):
        return os.system("docker images")


    def list_container(self, a=False):
        if a:
            return os.popen("docker ps -a")
        return os.popen("docker ps")


    def kill_container(self, name):
        return os.popen("docker kill " + name)


    def rm_container(self, name):
        try:
            self.kill_container(name)
        finally:
            return os.popen("docker rm " + name)
