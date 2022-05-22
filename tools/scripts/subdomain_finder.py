import os
import subprocess
import time
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = BASE_DIR.replace("\\","/")

PY_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
)
PY_PATH = PY_PATH.replace("\\","/")

def knockpy(target_url):
    knockpyurl = BASE_DIR + "/scripts/knockpy/knockpy.py"
    command = [
        "python",
        knockpyurl,
        f"{target_url}",
        "-t",
        "1",
        "--no-http-code",
        "404",
        "500",
    ]

    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output = []
    for line in process.stdout:
        # if (re.match(r"[\d\.]+.*[\w\.]+.*", line.decode("utf-8")) or 'times' in line.decode("utf-8")):
        # sys.stdout.write(str(line))
        output.append(line.decode("utf-8"))
        yield f"{line.decode('utf-8')}"
        time.sleep(0.5)
    tg = target_url
    json_export(output, tg)



def json_export(result, tg):
    directory = f"{PY_PATH}/Output/subdomain"
    os.makedirs(directory, exist_ok=True)
    with open(f"{directory}/{tg}", "w") as f:
        f.write(json.dumps(result, indent=4) + "\n")

