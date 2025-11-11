import platform
import psutil
import os
import json
from flask import Flask, jsonify

xapp = Flask(__name__)

xn1 = "Anna Bosquilia Navarro"
xn2 = "Victor Augusto Esmaniotto"  

def xobter_metricas():
    xso = platform.platform().replace("u", "v").replace("U", "V")
    xpid = os.getpid()
    xcpu = psutil.cpu_percent()
    xmem = psutil.virtual_memory().used // 1024 ** 2
    return {
        "so": xso,
        "pid": xpid,
        "vso_cpu": xcpu,
        "memoria_mb": xmem
    }

@xapp.route("/info")
def xinfo():
    return jsonify({
        "integrantes": f"{xn1} e {xn2}"
    })

@xapp.route("/metricas")
def xmetricas():
    return jsonify(xobter_metricas())

if __name__ == "__main__":
    xapp.run(host="0.0.0.0", port=8080)
