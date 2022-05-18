# web crawler for gathering URLs
import json
import os
import subprocess
from bs4 import BeautifulSoup

import requests
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get(target_url):
    url ='https://sitereport.netcraft.com/?url='+target_url+"&ajax=dcg"
    url0 ='https://sitereport.netcraft.com/?url='+target_url
    url1 ='https://sitereport.netcraft.com/?url='+target_url+"&ajax=ssl"
    url2 ='https://sitereport.netcraft.com/?url='+target_url+"&ajax=uptime"
    request = requests.Session()

    result = request.get(url)
    result0 = request.get(url0)
    result1 = request.get(url1)
    result2 = request.get(url2)
    soup = BeautifulSoup(result0.content, "html.parser")


    # background = soup.find_all("section",attrs={"id":"background_table_section"})
    network = soup.find_all("section",attrs={"id":"network_table_section"})
    #final list of data extracted 
    # background_table = []
    network_talbe = []
    # for x in background:
    #     background_table.append(str(x))

    background_table = json.loads(result.text)
    result_final=background_table['background_table']

    for x in network:
        network_talbe.append(str(x))
    result_final+=network_talbe[0]

    ssl_table = json.loads(result1.text)
    result_final+=ssl_table['ssl_table']

    host_table = json.loads(result2.text)
    result_final+=host_table['history_table']
    if result_final != "":
        tg = target_url.split("/")[2]
        
        json_export(result_final,tg)
        return result_final
    else:
        return None

def json_export(result, tg):
    directory = f"{BASE_DIR}/../media/toolkit/netcraft/"
    os.makedirs(directory, exist_ok=True)
    with open(f"{directory}/{tg}", "w") as f:
        f.write(json.dumps(result, indent=4) + "\n")