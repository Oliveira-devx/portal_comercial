from flask import Flask, render_template, request

from mysql.connector import error

from conexao import consultar

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/produtos")
def produtos():
    busca = request.args.get("busca", "").strip()

    sql = """SELECT 
            p.id_produto AS id,
            p.nome_produto AS produto,
            c.categoria, 
            p.preco_unit AS preço
            FROM produtos AS p 
            INNER JOIN categorias AS c 
            ON c.ID_Categoria = p.ID_Categoria
            WHERE p.Nome_Produto LIKE """

    dados = consultar(sql, (f"%{busca}%",))
    return render_template("tabela.html", titulo="Produtos", dados=dados, busca=busca)


@app.errorhandler(error)
def erro_banco(error):
    """ "qualquer erro fora de um formulario cai aqui."""
    app.logger.error("falha mysql %s", error)
    mensagem = (
        "falha ao acessar o banaco de dados, confira o .env e se o mysql está ligado."
    )
    return render_template("erro.html", mensagem=mensagem), 500
