from flask import Flask, render_template

app = Flask(__name__)


# ---------- Operações (lógica em Python) ----------
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


OPERACOES = {
    "soma": somar,
    "subtracao": subtrair,
    "multiplicacao": multiplicar,
    "divisao": dividir,
}


def calcular(operacao, form):
    """Lê os valores do formulário e devolve (resultado, erro)."""
    try:
        a = float(form.get("a", "").replace(",", "."))
        b = float(form.get("b", "").replace(",", "."))
    except ValueError:
        return None, "Digite dois números válidos."
    try:
        resultado = OPERACOES[operacao](a, b)
    except ZeroDivisionError as e:
        return None, str(e)
    return f"{resultado:g}", None


# ---------- Rotas ----------
from flask import request


@app.route("/")
def inicio():
    return render_template("index.html", ativa="inicio")


def pagina(operacao, titulo, simbolo):
    resultado = erro = None
    a = b = ""
    if request.method == "POST":
        a, b = request.form.get("a", ""), request.form.get("b", "")
        resultado, erro = calcular(operacao, request.form)
    return render_template(
        "operacao.html", ativa=operacao, titulo=titulo, simbolo=simbolo,
        resultado=resultado, erro=erro, a=a, b=b,
    )


@app.route("/soma", methods=["GET", "POST"])
def soma():
    return pagina("soma", "Soma", "+")


@app.route("/subtracao", methods=["GET", "POST"])
def subtracao():
    return pagina("subtracao", "Subtração", "−")


@app.route("/multiplicacao", methods=["GET", "POST"])
def multiplicacao():
    return pagina("multiplicacao", "Multiplicação", "×")


@app.route("/divisao", methods=["GET", "POST"])
def divisao():
    return pagina("divisao", "Divisão", "÷")


if __name__ == "__main__":
    app.run(debug=True)
