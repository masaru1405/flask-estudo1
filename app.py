from flask import Flask, render_template, request, session, redirect, url_for

app = Flask("projeto")
app.secret_key = "olamundo1984"

### ROTA INDEX ###
@app.route("/")
def ola_mundo():
  return render_template("index.html", nome="Kaio", frutas=[]), 200

### EXEMPLOS DE ROTAS ###
@app.route("/informacao")
@app.route("/informacao/<nome>")
@app.route("/informacao/<nome>/<idade>")
def informacao(nome="", idade=""):
  return "Informação<br>Nome: {}<br>Idade: {}".format(nome, idade), 200

### FORMULÁRIOS GET/POST ###
@app.route("/formulario_get")
def formulario_get():
  return render_template("formulario_get.html"), 200

@app.route("/formulario_post")
def formulario_post():
  return render_template("formulario_post.html"), 200

@app.route("/receber_valores" ,methods=['GET', 'POST'])
def receber():
  if request.method == "GET":
    return "Método GET!<br>Nome: {}<br>Idade: {}".format(request.args.get("nome"),request.args.get("idade")), 200
  elif request.method == "POST":
    return "Método POST!<br>Nome: {}<br>Idade: {}".format(request.form["nome"],request.form["idade"]), 200
  else:  
    return "Método não definido", 200

@app.route("/formulario_user")
def formuser():
  return render_template("formulario_usuario.html"), 200

@app.route("/info_usuario", methods=['GET', 'POST'])
def info_user():
  return render_template("render_info_user.html", fname=request.form["fname"], lname=request.form["lname"], color=request.form["colors"], gender=request.form["gender_choice"]), 200


### SESSAO ###
@app.route("/sessao")
def acesso_sessao():
  return """
    <h1>Início da Sessão:</h1>
    <form action="{}" method="post">
      Usuário: <input type="text" name="user" /><br/>
      <input type="submit" value="Acesso restrito" />
    </form>
  """.format(url_for('validacao_sessao')), 200

@app.route("/validacao", methods=['POST'])
def validacao_sessao():
  if request.method == "POST":
    session['usuario'] = request.form["user"]
    return redirect(url_for('acesso_restrito'))

@app.route("/restrito")
def acesso_restrito():
  if(session['usuario']):
    return "Estou na área de acesso restrito!<br/>Usuário: {}".format(session['usuario']), 200
  return redirect(url_for('acesso_sessao'))

@app.route("/sair")
def sair_sessao():
  session.pop('usuario', None)
  return redirect(url_for('acesso_sessao'))

app.run()