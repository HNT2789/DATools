import json
import os
import re
from concurrent.futures import ThreadPoolExecutor

import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
)
PY_PATH = PY_PATH.replace("\\","/")

methods = [
    "CHECKIN", "CHECKOUT", "CONNECT", "GET", "HEAD","INDEX",
    "LINK", "LOCK", "MKCOL", "MOVE", "NOEXISTE", "ORDERPATCH", "OPTIONS",
    "POST", "PROPFIND", "PROPPATCH", "REPORT", "SEARCH", "SHOWMETHOD",
    "SPACEJUMP", "TEXTSEARCH", "TRACE", "TRACK", "UNLINK","UNLOCK",
]
# Dangerious Methods: 'COPY', 'DELETE', 'PUT',  'PATCH', 'UNCHECKOUT',


def methods_from_http_options(console, target_url, options, proxies, cookies):
    options_methods = []
    # logger.verbose("Pulling available methods from server with an OPTIONS request")
    try:
        r = requests.options(
            url=target_url, proxies=proxies, cookies=cookies, verify=options.verify
        )
    except requests.exceptions.ProxyError:
        # logger.error("Invalid proxy specified ")
        raise SystemExit
    if r.status_code == 200:
        # logger.debug(r.headers)
        if "Allow" in r.headers:
            # logger.info("URL answers with a list of options: {}".format(r.headers["Allow"]))
            include_options_methods = console.input(
                "[bold orange3][?][/bold orange3] Do you want to add these methods to the test (be careful, some methods can be dangerous)? [Y/n] "
            )
            if not include_options_methods.lower() == "n":
                for method in r.headers["Allow"].replace(" ", "").split(","):
                    if method not in options_methods:
                        # logger.debug(f"Adding new method {method} to methods")
                        options_methods.append(method)
                    else:
                        pass
                        # logger.debug(f"Method {method} already in known methods, passing")
            else:
                pass
                # logger.debug("Methods found with OPTIONS won't be added to the tested methods")
        else:
            pass
            # logger.verbose("URL doesn't answer with a list of options")
    else:
        pass
        # logger.verbose("URL rejects OPTIONS")
    return options_methods


def test_method(method, target_url, proxies, cookies, result):
    try:
        r = requests.request(
            method=method,
            url=target_url,
            proxies=proxies,
            cookies=cookies,
            stream=False,  # If True, this is to prevent the download of huge files, focus on the request, not on the data
        )
    except requests.exceptions.ProxyError:
        # logger.error("Invalid proxy specified ")
        raise SystemExit
    # logger.debug(f"Obtained result: {method}, {str(r.status_code)}, {str(len(r.text))}, {r.reason}")
    result[method] = {
        "status_code": r.status_code,
        "length": len(r.text),
        "reason": r.reason[:100],
    }


def json_export(result, tg):
    directory = f"{PY_PATH}/Output/verbtampering"
    os.makedirs(directory, exist_ok=True)
    with open(f"{directory}/{tg}", "w") as f:
        f.write(json.dumps(result, indent=4) + "\n")


def start(target_url):
    # logger.info("Starting HTTP verb enumerating and tampering")
    global methods, tg
    result = {}
    proxies = None

    cookies = {}

    # Sort uniq
    methods = [m.upper() for m in methods]
    methods = sorted(set(methods))

    # Waits for all the threads to be completed
    with ThreadPoolExecutor(max_workers=min(8, len(methods))) as tp:
        for method in methods:
            tp.submit(test_method, method, target_url, proxies, cookies, result)

    # Sorting the result by method name
    result = {key: result[key] for key in sorted(result)}

    # Parsing and print result
    # print_result(console, result)
    # Export to JSON
    if len(result) == 0:
        return None
    else:
        if re.match("http\w?://\w+\.\w+", target_url):
            tg = target_url.split("/")[2]
            json_export(result, tg)
        return result
