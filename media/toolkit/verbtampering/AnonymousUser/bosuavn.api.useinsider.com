{
    "CHECKIN": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "CHECKOUT": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "CONNECT": {
        "status_code": 400,
        "length": 4780,
        "reason": "Bad Request"
    },
    "GET": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "HEAD": {
        "status_code": 200,
        "length": 0,
        "reason": "OK"
    },
    "INDEX": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "LINK": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "LOCK": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "MKCOL": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "MOVE": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "NOEXISTE": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "OPTIONS": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "ORDERPATCH": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "POST": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "PROPFIND": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "PROPPATCH": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "REPORT": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "SEARCH": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "SHOWMETHOD": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "SPACEJUMP": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "TEXTSEARCH": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "TRACE": {
        "status_code": 405,
        "length": 155,
        "reason": "Not Allowed"
    },
    "TRACK": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "UNLINK": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    },
    "UNLOCK": {
        "status_code": 200,
        "length": 26,
        "reason": "OK"
    }
}
