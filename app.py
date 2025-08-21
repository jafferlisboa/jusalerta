from flask import Flask, render_template

# Se suas pastas forem "templates" e "static" com esses nomes,
# você nem precisaria passar os parâmetros abaixo — deixei explícito.
app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    # Renderiza templates/index.html
    return render_template("index.html")


@app.route("/termosecondicoes")
def termos():
    # Renderiza templates/termos.html
    return render_template("termos.html")

@app.route("/sucesso")
def sucesso():
    # Renderiza templates/termos.html
    return render_template("sucesso.html")

@app.route("/j")
def j():
    # Renderiza templates/termos.html
    return render_template("redirect.html")

if __name__ == "__main__":
    # Execução local para desenvolvimento
    # Depois do deploy, use um servidor WSGI (ex.: gunicorn) e NÃO esse modo debug.
    app.run(host="0.0.0.0", port=5000, debug=True)
