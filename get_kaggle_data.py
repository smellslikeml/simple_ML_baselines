#!/usr/bin/env python
import subprocess
import os
import sys

kg_usr = os.environ['kg_usr']
kg_pwd = os.environ['kg_pwd']

contest_lst = sys.argv[1]
with open(contest_lst, 'r') as contest_file:
    contests = contest_file.readlines()
contests = [con.strip() for con in contests]

os.chdir('../')
for con in contests:
    if not os.path.exists(con):
        os.mkdir(con)
        os.chdir(con)
        os.mkdir('data')
        os.mkdir('src')
        os.chdir('data')
        subprocess.call("kg download -u {} -p {} -c {}".format(kg_usr, kg_pwd, con), shell=True)
        os.chdir('../../')

    

