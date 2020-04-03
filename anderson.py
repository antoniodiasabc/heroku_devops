import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def numeros_primos ():
    limite = 100
    qtd = 2
    n = 3

    primos = "1,2,"

    while qtd < limite:
        ehprimo = 1
        for i in range (2, n):
            if n % i == 0:
                ehprimo = 0
                break
        if (ehprimo):
            primos = primos + str(n) + ","
            qtd = qtd + 1
            print (qtd)
        n+=1
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
	