from .ultil import xmltodict
import os
import sys
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = BASE_DIR.replace("\\","/")
PY_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
)
PY_PATH = PY_PATH.replace("\\","/")

directory = f"{PY_PATH}/Output/sqli/"

def writeFile(name_of_file,str):
    try:
        save_path = BASE_DIR + "/scripts/sqlmap"
        completeName = os.path.join(save_path, name_of_file)    
        obj = open(completeName, "w", encoding='UTF-8')
        obj.write(str)
        obj.close()
    except IOError:
        print("Ghi file lỗi!!!")
    else:
        print("Ghi file thành công")



def fullexploit(sqlmappath, result, database_value, risk_value, level_value,tamper):
    writeFile("sql.txt", result)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = timestr+".txt"
    cmd = "python " + sqlmappath + "/sqlmap.py -r " + sqlmappath + "/sql.txt" + " --dbms="+database_value+ " --risk="+risk_value+ " --level="+level_value+ " --tamper=\""+tamper+"\" --batch > " +filename
    print(cmd)
    os.system(cmd)
    if sys.platform.startswith("win32"):
        os.makedirs(directory, exist_ok=True)
        command = "move " +filename +" "+directory
        os.system(command)
    elif sys.platform.startswith("linux"):
        os.makedirs(directory, exist_ok=True)
        command = "mv " +filename +" "+directory
        os.system(command)
    else:
        print("[+] Error: Không xác định được flatform")

def nodbmsexploit(sqlmappath, result, risk_value, level_value,tamper):
    writeFile("sql.txt", result)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = timestr+".txt"
    cmd = "python " + sqlmappath + "/sqlmap.py -r " + sqlmappath + "/sql.txt" + " --risk="+risk_value+ " --level="+level_value+ " --tamper=\""+tamper+"\" --batch > " +filename
    print(cmd)
    os.system(cmd)
    
    if sys.platform.startswith("win32"):
        os.makedirs(directory, exist_ok=True)
        command = "move " +filename +" "+directory
        os.system(command)
    elif sys.platform.startswith("linux"):
        os.makedirs(directory, exist_ok=True)
        command = "mv " +filename +" "+directory
        os.system(command)
    else:
        print("[+] Error: Không xác định được flatform")

# def notamperexploit(sqlmappath, result):
#     writeFile("sql.txt", result)
#     command = [
#         "python",
#         "c:\\Users\\siaht\\Desktop\\TFCT\\DAtool\\DAtool\\tools\\scripts\\sqlmap\\sqlmap.py",
#         "-r",
#         "c:\\Users\\siaht\\Desktop\\TFCT\\DAtool\\DAtool\\tools\\scripts\\sqlmap\\sql.txt",
#         "--risk=2",
#         "--batch",
#     ]
#     print(command)
#     process = subprocess.Popen(
#         command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
#     )
#     output = []
#     for line in process.stdout:
#         output.append(line.decode("utf-8"))
#         yield f"{line.decode('utf-8')}"
#         time.sleep(0.5)
