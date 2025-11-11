import platform
import psutil
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Nomes dos integrantes
n1 = "Anna Bosquilia Navarro"
n2 = "Victor Augusto Esmaniotto"

def obter_metricas():
    so = platform.platform().replace("u", "v").replace("U", "V")
    pid = os.getpid()
    cpu = psutil.cpu_percent()
    memoria_mb = psutil.virtual_memory().used // 1024 ** 2
    return {
        "so": so,
        "pid": pid,
        "vso_cpu": cpu,
        "memoria_mb": memoria_mb
    }

@app.route("/info")
def info():
    return jsonify({
        "integrantes": f"{n1} e {n2}"
    })

@app.route("/metricas")
def metricas():
    return jsonify(obter_metricas())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
