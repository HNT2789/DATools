import time
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def crawllink(urltarget):
    spiderurl = BASE_DIR + "\\scripts\\spider\\spiderweb.py"
    command = [
        "python",
        spiderurl,
        "-w",
        urltarget,

    ]
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output = []
    for line in process.stdout:
        output.append(line.decode("utf-8"))
        yield f"{line.decode('utf-8')}"
        time.sleep(0.5)

def crawllinkcookie(urltarget, cookie):
    spiderurl = BASE_DIR + "\\scripts\\spider\\spiderweb.py"
    command = [
        "python",
        spiderurl,
        "-w",
        urltarget,
        "-c",
        cookie,

    ]
    print(command)
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output = []
    for line in process.stdout:
        output.append(line.decode("utf-8"))
        yield f"{line.decode('utf-8')}"
        time.sleep(0.5)
