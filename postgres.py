import psycopg2
from flask import Flask, render_template,request,url_for,redirect

app=Flask(__name__)

def db_con():
   conn=psycopg2.connect(database="flask_db", host="localhost", user="postgres",password="Atg@105pa",port="5432")
   return conn

@app.route('/')
def index():
    conn=db_con()
    cur=conn.cursor()
    cur.execute('''select * from courses order by id''')
    data=cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',data=data)

@app.route('/create', methods=['POST'])
def create():
    conn = db_con()
    cur = conn.cursor()
    name = request.form['name']
    fees = request.form['fees']
    duration = request.form['duration']
    cur.execute('''INSERT INTO courses (name, fees, duration) VALUES (%s, %s, %s)''', (name, fees, duration))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    conn = db_con()
    cur = conn.cursor()
    id = request.form['id']
    name = request.form['name']
    fees = request.form['fees']
    duration = request.form['duration']
    cur.execute('''UPDATE courses SET name=%s, fees=%s, duration=%s WHERE id=%s''', (name, fees, duration, id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    conn = db_con()
    cur = conn.cursor()
    id = request.form['id']
    cur.execute('''DELETE FROM courses WHERE id=%s''', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))






if __name__ == '__main__':
    app.run(debug=True)