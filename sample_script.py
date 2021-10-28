"""
Moving tasks of a project from one stage to another
"""

import xmlrpc.client

# ======================================
# CHANGE THE CONSTANTS HERE ACCORDINGLY
# ======================================
url = "http://localhost:8069"
db = "training"
username, password = 'admin', 'admin'


def authentication():
    common = xmlrpc.client.ServerProxy(url + "/xmlrpc/2/common")
    return common.authenticate(db, username, password, {})


uid = authentication()

# USAGES
models = xmlrpc.client.ServerProxy(url + "/xmlrpc/2/object")


def _rpc(*args):
    # shorthand for running xmlrpc requests
    return models.execute_kw(db, uid, password,
                             *args)


# SCRIPT START
_rpc(
    "car.car", "create",
    [{
        "name": "Phantom",
        "brand": "Rolls Royce",
        "miles": 0
    }]
)
