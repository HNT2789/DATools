import random
import re
import string
import requests

import urllib3
method = ['GET','POST']
DOMBASE_REGEX = r"(?s)<!--.*?-->|\bescape\([^)]+\)|\([^)]+==[^(]+\)|\"[^\"]+\"|'[^']+'"
DOMBASE_PATTERN = (
    (r"<script[^>]*>[^<]*?(var|\n)\s*(\w+)\s*=[^;]*(document\.(location|URL|documentURI)|location\.(href|search)|window\.location)[^;]*;[^<]*(document\.write(ln)?\(|\.innerHTML\s*=|eval\(|setTimeout\(|setInterval\(|location\.(replace|assign)\(|setAttribute\()[^;]*\2.*?</script>"),
    (r"<script[^>]*>[^<]*?(document\.write\(|\.innerHTML\s*=|eval\(|setTimeout\(|setInterval\(|location\.(replace|assign)\(|setAttribute\()[^;]*(document\.(location|URL|documentURI)|location\.(href|search)|window\.location).*?</script> ")
)
XSS_PATTERN = (#regex, xss pay load, info xSS error, content remova rgex 
    (r"\A[^<>]*%(chars)s[^<>]*\Z", ('<', '>'), "\".xss.\", pure text response, %(filtering)s filtering", None),  
    (r"<!--[^>]*%(chars)s|%(chars)s[^<]*-->", ('<', '>'), "\"<!--.'.xss.'.-->\", inside the comment, %(filtering)s filtering", None),  
    (r"(?s)<script[^>]*>[^<]*?'[^<']*%(chars)s|%(chars)s[^<']*'[^<]*</script>", ('\'', ';'), "\"<script>.'.xss.'.</script>\", enclosed by <script> tags, inside single-quotes, %(filtering)s filtering", None),  
    (r'(?s)<script[^>]*>[^<]*?"[^<"]*%(chars)s|%(chars)s[^<"]*"[^<]*</script>', ('"''"', ';'), "'<script>.\".xss.\".</script>', enclosed by <script> tags, inside double-quotes, %(filtering)s filtering", None),
    (r"(?s)<script[^>]*>[^<]*?%(chars)s|%(chars)s[^<]*</script>", (';',), "\"<script>.xss.</script>\", enclosed by <script> tags, %(filtering)s filtering", None), 
    (r">[^<]*%(chars)s[^<]*(<|\Z)", ('<', '>'), "\">.xss.<\", outside of tags, %(filtering)s filtering", r"(?s)<script.+?</script>|<!--.*?-->"),
    (r"<[^>]*'[^>']*%(chars)s[^>']*'[^>]*>", ('\'',), "\"<.'.xss.'.>\", inside the tag, inside single-quotes, %(filtering)s filtering", r"(?s)<script.+?</script>|<!--.*?-->"),
    (r'<[^>]*"[^>"]*%(chars)s[^>"]*"[^>]*>', ('"',), "'<.\".xss.\".>', inside the tag, inside double-quotes, %(filtering)s filtering", r"(?s)<script.+?</script>|<!--.*?-->"),
    (r"<[^>]*%(chars)s[^>]*>", (), "\"<.xss.>\", inside the tag, outside of quotes, %(filtering)s filtering", r"(?s)<script.+?</script>|<!--.*?-->"),
    (),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),()
) 

def retrieveContent(url, cookie, data=None):#request to the URL and get CONTENT  
    # cookie = COOKIE
    if '?' in url:  
        retval = requests.get(url, cookies = cookie, allow_redirects = False)  
    else:
        retval = requests.post(url, cookies = cookie, data=data, allow_redirects = False)
    req =  retval.content   
    return req or ""  

def sourceContain(content, chars):
    content = re.sub(r"\\[%s]" % re.escape("".join(chars)), "", content) if chars else content 
    return all(char in content for char in chars)


def scanXSS(url,cookie = None,data=None):
    usable = False
    url, data = re.sub(r"=(&|\Z)", "=1\g<1>", url) if url else url, re.sub(r"=(&|\Z)", "=1\g<1>", data) if data else data  
    contentDombase = re.sub(DOMBASE_REGEX, "", retrieveContent(url, cookie, data))
    dombaseXSS = max(re.search(_, contentDombase) for _ in DOMBASE_PATTERN)
    if dombaseXSS:
        result = {'url' : url, 'parameter' : method, 'resp' : 'page itself appears to be XSS vulnerable (DOM)' } 
    try:
        for method in (GET, POST):
            pageURL = url if method is GET else (data or "")
            for match in re.finditer(r"((\A|[?&])(?P<parameter>[\w\[\]]+)=)(?P<value>[^&#]*)", pageURL):
                 found, usable = False, True
                 firstRandomstring, lastRandomstring = ("".join(random.sample(string.ascii_lowercase, LENTH_OF_RAN_CHAR)) for i in xrange(2))
                 for specialChars in (MORE_REGULAR_CHARACTER, REGULAR_CHARACTER):
                     if not found:
                        tempContent = pageURL.replace(match.group(0), "%s%s" % (match.group(0), urllib3.quote("%s%s%s%s" % ("'""'" if specialChars == MORE_REGULAR_CHARACTER else "", firstRandomstring, "".join(random.sample(specialChars, len(specialChars))), lastRandomstring))))
                        content = (retrieveContent(tempContent,cookie, data) if method is GET else retrieveContent(url,cookie, tempContent)).replace("%s%s" % ("'" if specialChars == MORE_REGULAR_CHARACTER else "", firstRandomstring), firstRandomstring)
                        for payload in re.finditer("%s([^ ]+?)%s" % (firstRandomstring, lastRandomstring), content, re.I):
                            for regex, vulPattern, errorInfo, deleteableContent in XSS_PATTERN:
                                comtentRemoveregex = re.search(regex % {"chars": re.escape(payload.group(0))}, re.sub(deleteableContent or "", "", content), re.I) 
                                if comtentRemoveregex and not found and payload.group(1).strip():
                                    if sourceContain(payload.group(1), vulPattern):
                                        found = True
                                        ketqua = {'url' : url, 'parameter' : phase, 'resp' : errorInfo % dict((("filtering", "no" if all(char in payload.group(1) for char in MORE_REGULAR_CHARACTER) else "some"),)) }
                                        break  
        if not usable:
            pass
    except:
        print("exception found")
    return result

# url = "https://www.betacinemas.vn/nhuong-quyen.htm"
# data = None
# cookie = None
# content = retrieveContent(url, cookie, data)
# contentDombase = re.sub(DOMBASE_REGEX, "", content.decode('utf-8'))
# abc = re.search("_", contentDombase)
# print(abc)
# dombaseXSS = max(re.search(_, contentDombase) for _ in DOMBASE_PATTERN)
# if dombaseXSS:   
#     result = {'url' : url, 'parameter' : method, 'resp' : 'page itself appears to be XSS vulnerable (DOM)' } 
found, usable = False, True
print(usable)