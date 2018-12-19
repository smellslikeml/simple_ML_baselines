#!/usr/bin/env python
import subprocess
import os
import sys

contest_lst = sys.argv[1]
with open(contest_lst, 'r') as contest_file:
    contests = contest_file.readlines()
contests = [con.strip() for con in contests]

os.chdir('../../')
for con in contests:
    if not os.path.exists(con):
        os.mkdir(con)
        os.chdir(con)
        os.mkdir('data')
        os.mkdir('src')
        os.chdir('data')
        subprocess.call("kaggle competitions -c download {}".format(con), shell=True)
        os.chdir('../../')

    

