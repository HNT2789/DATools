{
    "CHECKIN": {
        "status_code": 405,
        "length": 1588,
        "reason": "Method Not Allowed"
    },
    "CHECKOUT": {
        "status_code": 405,
        "length": 1589,
        "reason": "Method Not Allowed"
    },
    "CONNECT": {
        "status_code": 400,
        "length": 1551,
        "reason": "Bad Request"
    },
    "GET": {
        "status_code": 200,
        "length": 609845,
        "reason": "OK"
    },
    "HEAD": {
        "status_code": 200,
        "length": 0,
        "reason": "OK"
    },
    "INDEX": {
        "status_code": 405,
        "length": 1586,
        "reason": "Method Not Allowed"
    },
    "LINK": {
        "status_code": 405,
        "length": 1585,
        "reason": "Method Not Allowed"
    },
    "LOCK": {
        "status_code": 405,
        "length": 1585,
        "reason": "Method Not Allowed"
    },
    "MKCOL": {
        "status_code": 405,
        "length": 1586,
        "reason": "Method Not Allowed"
    },
    "MOVE": {
        "status_code": 405,
        "length": 1585,
        "reason": "Method Not Allowed"
    },
    "NOEXISTE": {
        "status_code": 405,
        "length": 1589,
        "reason": "Method Not Allowed"
    },
    "OPTIONS": {
        "status_code": 405,
        "length": 1588,
        "reason": "Method Not Allowed"
    },
    "ORDERPATCH": {
        "status_code": 405,
        "length": 1591,
        "reason": "Method Not Allowed"
    },
    "POST": {
        "status_code": 400,
        "length": 6279,
        "reason": "Bad Request"
    },
    "PROPFIND": {
        "status_code": 405,
        "length": 1589,
        "reason": "Method Not Allowed"
    },
    "PROPPATCH": {
        "status_code": 405,
        "length": 1590,
        "reason": "Method Not Allowed"
    },
    "REPORT": {
        "status_code": 405,
        "length": 1587,
        "reason": "Method Not Allowed"
    },
    "SEARCH": {
        "status_code": 405,
        "length": 1587,
        "reason": "Method Not Allowed"
    },
    "SHOWMETHOD": {
        "status_code": 405,
        "length": 1591,
        "reason": "Method Not Allowed"
    },
    "SPACEJUMP": {
        "status_code": 405,
        "length": 1590,
        "reason": "Method Not Allowed"
    },
    "TEXTSEARCH": {
        "status_code": 405,
        "length": 1591,
        "reason": "Method Not Allowed"
    },
    "TRACE": {
        "status_code": 405,
        "length": 1586,
        "reason": "Method Not Allowed"
    },
    "TRACK": {
        "status_code": 405,
        "length": 1586,
        "reason": "Method Not Allowed"
    },
    "UNLINK": {
        "status_code": 405,
        "length": 1587,
        "reason": "Method Not Allowed"
    },
    "UNLOCK": {
        "status_code": 405,
        "length": 1587,
        "reason": "Method Not Allowed"
    }
}
