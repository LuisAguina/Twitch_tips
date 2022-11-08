
from flask import Flask, g, session, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'rh'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/minigame')
def minigame():
    return render_template("minigame.html")




@app.route('/videos')
def videos():
    return render_template("videos.html")
@app.route('/comentarios')
def comentarios():
    return render_template("comentarios.html")
@app.route('/register')
def register():
    return render_template("register.php")
@app.route('/login')
def login():
    return render_template("login.php")



@app.route('/contactos')
def contactos():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
    cursor = conn.cursor()
    cursor.execute('select id,correo,comentarios,telefono,asunto from comenta order by id')
    datos = cursor.fetchall()
    return render_template("contactos.html", comentarios= datos)

@app.route('/agrega_contactos',methods={"post"})

def agrega_contactos():
    if request.method == 'POST':
      
        aux_usuario = request.form['introducir_nombre']
        aux_correo = request.form['introducir_email']
        aux_comentarios = request.form['introducir_mensaje']
        aux_telefono= request.form['introducir_telefono']
        aux_asunto= request.form['introducir_asunto']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (usuario,correo,comentarios,telefono,asunto) values (%s,%s,%s,%s,%s)',(aux_usuario,aux_correo,aux_comentarios,aux_telefono,aux_asunto))
        conn.commit()
    return redirect(url_for('index'))


@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
    cursor = conn.cursor()
    cursor.execute('select id, usuario,correo,comentarios,telefono,asunto from comenta order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", usuario = datos)

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
    cursor = conn.cursor()
    cursor.execute('select id,usuario,correo,comentarios,telefono,asunto from comenta where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", comentar=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
     
        aux_usuario = request.form['introducir_nombre']
        aux_correo = request.form['introducir_email']
        aux_comentarios = request.form['introducir_mensaje']
        aux_telefono= request.form['introducir_telefono']
        aux_asunto= request.form['introducir_asunto']
        
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
        cursor = conn.cursor()
        cursor.execute('update comenta set usuario = %s,correo = %s,comentarios = %s,telefono = %s,asunto = %s ',(aux_usuario,aux_correo,aux_comentarios,aux_telefono,aux_asunto))
        conn.commit()
        return redirect(url_for('crud'))

@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
    cursor = conn.cursor()
    cursor.execute('delete from comenta where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))

@app.route('/insertar')
def insertar():
    return render_template("insertar.html")
#ediño gay








#ortiz gay












if __name__ == '__main__':
    app.run(debug=True)


