import os
import re
from django.shortcuts import render
# from numpy import not_equal
from .scripts.ultil import xmltodict
from .forms import BurptoSqlmap, CvedesForm, Exploitsqlmap, URLForm, SubDomainForm, CrawlForm
from .scripts import cvescanner, netcraft, verbtampering, subdomain_finder, burpconvert, crawl
from django.http.response import StreamingHttpResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = BASE_DIR.replace("\\","/")
PY_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
)
PY_PATH = PY_PATH.replace("\\","/")
# Create your views here.
def home(request):
    return render(request, "toolkit/home.html")

def igtools(request):
    if request.method == "GET":
        return render(request, "toolkit/igtools.html")

def extools(request):
    if request.method == "GET":
        return render(request, "toolkit/extools.html")

def cvedes(request):
    if request.method == "GET":
        return render(request, "toolkit/cvedes.html", {"form": CvedesForm()})

    else:
        try:
            global cve_id, user_name
            form = CvedesForm(request.POST)
            if form.is_valid():
                cve_id = form.cleaned_data.get("cve_id")
                cve_id = cve_id.upper()
                cve_id = cve_id.replace(" ","-")
                pattern = re.compile("^(CVE-(1999|2\d{3})-(0\d{2}[1-9]|[1-9]\d{3,}))$")
                check = pattern.match(cve_id)
                if check is None:
                    return render(
                        request,
                        "toolkit/cvedes.html",
                        {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
                    )
                else:
                    result = cvescanner.cve_search(cve_id)
                    context = {"result": result}
                    return render(request, "toolkit/cvedes.html", context)

        except ValueError:
            return render(
                request,
                "toolkit/cvedes.html",
                {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
            )

def burpConvert(request):
    if request.method == "GET":
        return render(request, "toolkit/burp.html", {"form": CvedesForm()})
    else:
        try:
            global my_dict, context
            form = BurptoSqlmap(request.POST)
            if form.is_valid():
                burptosqlmap = form.data.get("burptosqlmap")
                burptosqlmap = BASE_DIR+"/"+burptosqlmap
                print(burptosqlmap)
                if burptosqlmap:
                    with open(burptosqlmap,"r") as xml_obj:
                        #coverting the xml data to Python dictionary
                        my_dict = xmltodict.parse(xml_obj.read())
                        #closing the file
                        xml_obj.close()
                    items = []
                    item = {'url':[], 'method':[], 'status':[], 'request':[], 'host':[], 'responselength':[]}
                    for i in range (0, len(my_dict['items']['item'])):
                        item['url'] = my_dict['items']['item'][i]['url']
                        item['method'] = my_dict['items']['item'][i]['method']
                        item['status'] = my_dict['items']['item'][i]['status']
                        item['host'] = my_dict['items']['item'][i]['host']['@ip']
                        item['responselength'] = my_dict['items']['item'][i]['responselength']
                        item['request'] = my_dict['items']['item'][i]['request']['#text']
                        items.append(item)
                        item = {'url':[], 'method':[], 'status':[], 'request':[], 'host':[], 'responselength':[]}
                    context = {"result": items}
                    return render(request, "toolkit/burp.html", context)
                else:
                    print("Directory not exists.")
            context = {"result": None}
            return render(request, "toolkit/burp.html", context)
        except ValueError:
            return render(
                request,
                "toolkit/burp.html",
                {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
            )

def exploitsqlmap(request,id):
    id = id-1
    if request.method == "POST":
        form = Exploitsqlmap(request.POST)
        sqlmappath =  BASE_DIR + "/tools/scripts/sqlmap"
        risk_value = form.data.get("risk")
        level_value = form.data.get("level")
        database_value = form.data.get("database")
        tamper_value = form.data.getlist("tamper")
        tamper = ", ".join(tamper_value)
        result  = my_dict['items']['item'][id]['request']['#text']
        if database_value is None:
            burpconvert.nodbmsexploit(sqlmappath, result, risk_value, level_value,tamper)

        else:
            burpconvert.fullexploit(sqlmappath, result, database_value, risk_value, level_value, tamper)
        return render(request, "toolkit/burp.html", context)

def netCraft(request):
    if request.method == "GET":
        return render(request, "toolkit/netcraft.html", {"form": URLForm()})

    else:
        try:
            global target_url
            form = URLForm(request.POST)
            if form.is_valid():
                target_url = form.cleaned_data.get("target_url")
                pattern = re.compile('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
                check = pattern.match(target_url)
                result = netcraft.getNetcraft(target_url)
                if check is None:
                    return render(
                        request,
                        "toolkit/netcraft.html",
                        {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
                    )

                else:
                    print(result)
                    context = {"result": result, "target_url": target_url}
                    return render(request, "toolkit/netcraft.html", context)

        except ValueError:
            return render(
                request,
                "toolkit/netcraft.html",
                {"error": "Đã có lỗi xảy ra, xin hãy thử lại."},
            )

def verbtamper(request):
    if request.method == "GET":
        return render(request, "toolkit/verbtampering.html", {"form": URLForm()})

    else:
        try:
            global target_url
            form = URLForm(request.POST)
            if form.is_valid():
                target_url = form.cleaned_data.get("target_url")
                pattern = re.compile('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
                check = pattern.match(target_url)
                result = verbtampering.start(target_url)
                if result is None or check is None:
                    return render(
                        request,
                        "toolkit/verbtampering.html",
                        {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
                    )
                else:
                    context = {"result": result.items(), "target_url": target_url}
                    return render(request, "toolkit/verbtampering.html", context)

        except ValueError:
            return render(
                request,
                "toolkit/verbtampering.html",
                {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
            )

def subdomain(request):
    if request.method == "GET":
        return render(
            request, "toolkit/subdomain.html", {"form": SubDomainForm()}
        )
    else:
        try:
            global target_url
            form = SubDomainForm(request.POST)
            if form.is_valid():
                target_url = form.cleaned_data.get("target_url")
                pattern = re.compile('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
                check = pattern.match(target_url)
                if check is None:
                    return render(
                        request,
                        "toolkit/subdomain.html",
                        {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
                    )
                else:
                    target_url = target_url.replace("https://", "").replace("http://", "").replace("www.", "")
                    response = StreamingHttpResponse(
                        subdomain_finder.knockpy(target_url)
                    )  
                    response["Content-Type"] = "text/event-stream"
                    return response

        except ValueError:
            return render(
                request,
                "toolkit/subdomain.html",
                {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
            )

def crawler(request):
    if request.method == "GET":
        return render(
            request, "toolkit/crawl.html", {"form": CrawlForm()}
        )
    else:
        try:
            global target_url
            form = CrawlForm(request.POST)
            if form.is_valid():
                target_url = form.cleaned_data.get("target_url")
                pattern = re.compile("https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")
                check = pattern.match(target_url)
                cookie = form.cleaned_data.get("cookie")
                if check is None:
                    return render(
                        request,
                        "toolkit/crawl.html",
                        {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
                    )
                else:
                    if cookie == "":
                        response = StreamingHttpResponse(
                            crawl.crawllink(target_url)
                        )  
                        response["Content-Type"] = "text/event-stream"
                        return response
                    else:
                        response = StreamingHttpResponse(
                            crawl.crawllinkcookie(target_url, cookie)
                        )  
                        response["Content-Type"] = "text/event-stream"
                        return response

        except ValueError:
            return render(
                request,
                "toolkit/crawl.html",
                {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
            )

def detectxss(request):
    if request.method == "GET":
        return render(
            request, "toolkit/xss.html", {"form": CrawlForm()}
        )
    else:
        try:
            global target_url
            form = CrawlForm(request.POST)
            if form.is_valid():
                target_url = form.cleaned_data.get("target_url")
                pattern = re.compile("https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")
                check = pattern.match(target_url)
                cookie = form.cleaned_data.get("cookie")
                if check is None:
                    return render(
                        request,
                        "toolkit/xss.html",
                        {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
                    )
                else:
                    if cookie == "":
                        response = StreamingHttpResponse(
                            crawl.crawllink(target_url)
                        )  
                        response["Content-Type"] = "text/event-stream"
                        return response
                    else:
                        response = StreamingHttpResponse(
                            crawl.crawllinkcookie(target_url, cookie)
                        )  
                        response["Content-Type"] = "text/event-stream"
                        return response

        except ValueError:
            return render(
                request,
                "toolkit/xss.html",
                {"error": "Dữ liệu nhập vào không hợp lệ, xin hãy nhập lại."},
            )




