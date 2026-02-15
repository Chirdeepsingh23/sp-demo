import subprocess

def run_command(user_input):
    # TODO fix later
    print("running")    
    subprocess.run(user_input, shell=True)
    return eval(user_input)
