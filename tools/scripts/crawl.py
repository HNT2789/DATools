import time
import subprocess
import os
import json

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
    tg = urltarget.split("/")[2]
    json_export(output, tg)

def crawllinkcookie(urltarget, cookie):
    spiderurl = BASE_DIR + "\\scripts\\spider\\spiderweb.py"
    command = [
        "python",
        spiderurl,
        "-w",
        urltarget,
        "--cookie",
        cookie,

    ]
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output = []
    for line in process.stdout:
        output.append(line.decode("utf-8"))
        yield f"{line.decode('utf-8')}"
        time.sleep(0.5)
    tg = urltarget.split("/")[2]
    json_export(output, tg)

def json_export(result, tg):
    directory = f"{BASE_DIR}/../media/toolkit/crawl/"
    os.makedirs(directory, exist_ok=True)
    with open(f"{directory}/{tg}", "w") as f:
        f.write(json.dumps(result, indent=4) + "\n")