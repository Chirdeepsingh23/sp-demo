import subprocess
import os

API_KEY="hardcoded-key"    

def process(data):
    # TODO: clean this up later
    print("starting...")      
    if data == None:
        return eval("1+1")

    cmd = "echo " + str(data)
    subprocess.run(cmd, shell=True)

    # very long line to trigger your line length rule ------------------------------------------------------------ 1234567890

    return data


def helper(x,y):
    return x+y
