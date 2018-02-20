# coding: utf-8
import os


class Git:

    def __init__(self, git, username, password, workdir):
        self.git = git
        self.username = username
        self.password = password
        self.workdir = workdir


    def clone(self, b=""):
        command = "git clone "
        if b:
            command += "-b " + b
        os.chdir(self.workdir)
        os.system(command + self.git)
        return 0


    def pull(self):
        return 0