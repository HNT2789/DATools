{
    "CHECKIN": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "CHECKOUT": {
        "status_code": 400,
        "length": 0,
        "reason": "Bad Request"
    },
    "CONNECT": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "GET": {
        "status_code": 200,
        "length": 81671,
        "reason": "OK"
    },
    "HEAD": {
        "status_code": 200,
        "length": 0,
        "reason": "OK"
    },
    "INDEX": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "LINK": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "LOCK": {
        "status_code": 200,
        "length": 81665,
        "reason": "OK"
    },
    "MKCOL": {
        "status_code": 200,
        "length": 81673,
        "reason": "OK"
    },
    "MOVE": {
        "status_code": 200,
        "length": 81674,
        "reason": "OK"
    },
    "NOEXISTE": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "OPTIONS": {
        "status_code": 200,
        "length": 81665,
        "reason": "OK"
    },
    "ORDERPATCH": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "POST": {
        "status_code": 200,
        "length": 81663,
        "reason": "OK"
    },
    "PROPFIND": {
        "status_code": 200,
        "length": 81668,
        "reason": "OK"
    },
    "PROPPATCH": {
        "status_code": 200,
        "length": 81680,
        "reason": "OK"
    },
    "REPORT": {
        "status_code": 200,
        "length": 81661,
        "reason": "OK"
    },
    "SEARCH": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "SHOWMETHOD": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "SPACEJUMP": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "TEXTSEARCH": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "TRACK": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "UNLINK": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "UNLOCK": {
        "status_code": 200,
        "length": 81667,
        "reason": "OK"
    }
}
