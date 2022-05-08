import xmltodict
import os
import subprocess
import time
def writeFile(name_of_file,str):
    try:
        save_path = "DAtool/DAtool/tools/scripts/sqlmap"
        completeName = os.path.join(save_path, name_of_file)    
        # completeName = name_of_file 
        obj = open(completeName, "w", encoding='UTF-8')
        obj.write(str)
        obj.close()
    except IOError:
        print("Ghi file lỗi!!!")
    else:
        print("Ghi file thành công")



def fullexploit(sqlmappath, result, database_value, risk_value, level_value,tamper):
    writeFile("sql.txt", result)
    cmd = "python " + sqlmappath + "\\sqlmap.py -r " + sqlmappath + "\\sql.txt" + " --dbms="+database_value+ " --risk="+risk_value+ " --level="+level_value+ " --tamper=\""+tamper+"\" --batch > " + "result.txt"
    print(cmd)
    os.system(cmd)

def nodbmsexploit(sqlmappath, result, risk_value, level_value,tamper):
    writeFile("sql.txt", result)
    cmd = "python " + sqlmappath + "\\sqlmap.py -r " + sqlmappath + "\\sql.txt" + " --risk="+risk_value+ " --level="+level_value+ " --tamper=\""+tamper+"\" --batch > " + "result.txt"
    print(cmd)
    os.system(cmd)

def notamperexploit(sqlmappath, result):
    writeFile("sql.txt", result)
    command = [
        "python",
        "c:\\Users\\siaht\\Desktop\\TFCT\\DAtool\\DAtool\\tools\\scripts\\sqlmap\\sqlmap.py",
        "-r",
        "c:\\Users\\siaht\\Desktop\\TFCT\\DAtool\\DAtool\\tools\\scripts\\sqlmap\\sql.txt",
        "--risk=2",
        "--batch",
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
