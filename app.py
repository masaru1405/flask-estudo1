from flask import Flask, render_template, request

app = Flask("projeto")

@app.route("/")
def ola_mundo():
  return render_template("index.html", nome="Kaio", frutas=[]), 200

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

@app.route("/informacao")
@app.route("/informacao/<nome>")
@app.route("/informacao/<nome>/<idade>")
def informacao(nome="", idade=""):
  return "Informação<br>Nome: {}<br>Idade: {}".format(nome, idade), 200

app.run()