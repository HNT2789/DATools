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
        "length": 92815,
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
        "length": 92815,
        "reason": "OK"
    },
    "MKCOL": {
        "status_code": 200,
        "length": 92820,
        "reason": "OK"
    },
    "MOVE": {
        "status_code": 200,
        "length": 92817,
        "reason": "OK"
    },
    "NOEXISTE": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "OPTIONS": {
        "status_code": 200,
        "length": 92818,
        "reason": "OK"
    },
    "ORDERPATCH": {
        "status_code": 400,
        "length": 2959,
        "reason": "Bad Request"
    },
    "POST": {
        "status_code": 200,
        "length": 92816,
        "reason": "OK"
    },
    "PROPFIND": {
        "status_code": 200,
        "length": 92818,
        "reason": "OK"
    },
    "PROPPATCH": {
        "status_code": 200,
        "length": 92814,
        "reason": "OK"
    },
    "REPORT": {
        "status_code": 200,
        "length": 92818,
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
    "TRACE": {
        "status_code": 400,
        "length": 0,
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
        "length": 92815,
        "reason": "OK"
    }
}
