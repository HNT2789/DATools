import json
import os
from bs4 import BeautifulSoup
import builtwith as b   
import requests
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
)
PY_PATH = PY_PATH.replace("\\","/")

def getNetcraft(target_url):
    url ='https://sitereport.netcraft.com/?url='+target_url+"&ajax=dcg"
    url0 ='https://sitereport.netcraft.com/?url='+target_url
    url1 ='https://sitereport.netcraft.com/?url='+target_url+"&ajax=ssl"
    url2 ='https://sitereport.netcraft.com/?url='+target_url+"&ajax=uptime"
# ==============================================================
    request = requests.Session()
    result = request.get(url)
    result0 = request.get(url0)
    result1 = request.get(url1)
    result2 = request.get(url2)
    result_final = '<section class="site_report_table" id="background_table_section"> <div class="section_title"><h2>Built With</h2> <span class="section_links"> <a class="fas fa-link" href="#"></a> <a class="fas fa-arrow-up" href="#"></a> </span></div><div class="section_content"><div class="row">'+builtWith(target_url)+'</div></div></section><section class="site_report_table" id="background_table_section"> <div class="section_title"><h2>Insecure Header</h2> <span class="section_links"> <a class="fas fa-link" href="#"></a> <a class="fas fa-arrow-up" href="#"></a> </span></div><div class="section_content"><div class="row">'+insecureHeaders(target_url)+'</div></div></section>'
# ==============================================================
    try:
        soup = BeautifulSoup(result0.content, "html.parser")
        network = soup.find_all("section",attrs={"id":"network_table_section"})
        network_talbe = []
        for x in network:
            network_talbe.append(str(x))
        for index in range(0,len(network_talbe)):
            result_final+=network_talbe[index]
    except:
        result_final += ''
    #-----------------------------------------------------------
    try:     
        background_table = json.loads(result.text)
        result_final+=background_table['background_table']
    except:
        result_final += ''
    #-----------------------------------------------------------
    try:
        ssl_table = json.loads(result1.text)
        result_final+=ssl_table['ssl_table']
    except:
        result_final += ''
    #-----------------------------------------------------------
    try:
        host_table = json.loads(result2.text)
        result_final+=host_table['history_table']
    except:
        result_final += ''
# ==============================================================
    if result_final != "":
        tg = target_url.split("/")[2]
        json_export(result_final,tg)
        return result_final
    else:
        return None

def insecureHeaders(url):
    request = requests.Session()
    r = request.get(url)
    result = ''
    try:   
        xss_protect = r.headers['X-XSS-Protection']
        if 1 in xss_protect:        
            result+=(' <br>X-XSS-Protection đã được thiết lập')          
        else:          
            result+=(' <br>X-XSS-Protection chưa được thiết lập') 
    except:     
            result+=(' <br>X-XSS-Protection có thể đã bị tắt')   
# ==============================================================
    try:
        x_content = r.headers['X-Content-Type-Options']       
        if x_content == 'nosniff':          
            result+=(' <br>X-Content-Type-Options đã được thiết lập')   
        else:
            result+=(' <br>X-Content-Type-Options chưa được thiết lập')    
    except:         
        result +=(' <br>X-Content-Type-Options chưa được thiết lập') 
# ==============================================================
    try:       
        x_frame = r.headers['x-frame-options']         
        result +=(' <br>X-Frame-Options : %s' %x_frame)   
    except: 
        result +=(' <br>X-Frame-Options bị thiếu')  
# ==============================================================
    try: 
        csp = r.headers['Content-Security-Policy']         
        result +=(' <br>Content-Security-Policy : %s' % csp )    
    except:
        result +=(' <br>Content-Security-Policy bị thiếu')   
# ==============================================================
    try: 
        hsts = r.headers['Strict-Transport-Security']     
        result +=(' <br>Strict-Transport-Security: %s'%hsts)   
    except: 
        result +=(' <br>HTTP Strict-Transport-Security chưa được thiết lập')  
# ==============================================================
    try:         
        x_pcdp = r.headers['X-Permitted-Cross-Domain-Policies']            
        result +=(' <br>X-Permitted-Cross-Domain-Policies: %s ' %x_pcdp) 
    except: 
        result +=(' <br>X-Permitted-Cross-Domain-Policies chưa được thiết lập')   
# ===========================================================
    return result

def builtWith(target_url):
    try:
        data = b.parse(target_url)
        result = ''
        for key in data:
            result += str(key[0]).upper() + key[1:len(key)] + ' : ' + data[key][0]+'<br>'
        return result
    except:
        return 'Không thu thập được'
        
def json_export(result, tg):
    directory = f"{PY_PATH}/Output/netcraft/"
    os.makedirs(directory, exist_ok=True)
    with open(f"{directory}/{tg}", "w") as f:
        f.write(json.dumps(result, indent=4) + " \n")

# print(getNetcraft("http://actvn.edu.vn"))