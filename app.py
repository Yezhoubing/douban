from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")#相当于return index()

@app.route('/movie')
def movie():
    datalist=[]
    conn=sqlite3.connect("douban.db")
    cur=conn.cursor()
    sql="select * from douban_250"
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("movie.html",movies=datalist)

@app.route('/score')
def score():
    film_score=[]#电影评分
    film_num=[]#每个评分的电影数
    conn = sqlite3.connect("douban.db")
    cur = conn.cursor()
    sql = "select score,count(score) from douban_250 group by score"
    data = cur.execute(sql)
    for item in data:
        film_score.append(item[0])#注意添加的时候整型是否可以，此处可以
        film_num.append(item[1])
    con=dict(zip(film_score,film_num))
    cur.close()
    conn.close()
    return render_template("score.html",con=con)

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    # 本地运行参数置空即可，如果要放在自己服务器上运行，可改相关参数，例如host='0.0.0.0',port=8000,debug=True
    app.run()
