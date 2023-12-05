from flask import Flask, render_template, request, flash, redirect
import random

kon = ["ไตเติ้ล", "แอร์", "นายเจิมศักดิ์", "ต้าร์","เหมียว","พี่พิม","พี่กล้า","น้องข้าว","บีม","พี่ทราย","พี่นก","ป้าจิ๋ม","โชกุน"]
lol = ["ไตเติ้ล", "แอร์", "นายเจิมศักดิ์", "ต้าร์","เหมียว","พี่พิม","พี่กล้า","น้องข้าว","บีม","พี่ทราย","พี่นก","ป้าจิ๋ม","โชกุน"]
are = []
konn = False

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # ใส่คีย์ของคุณที่นี่

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    global konn
    drawer_name = request.form.get('drawer_name')
    if drawer_name in lol:
        konn = True
    if konn:
        drawn_player = random.choice(kon)
        if drawer_name not in are:
            while True:
                if drawn_player == drawer_name:
                    drawn_player = random.choice(kon)
                else:
                    break
            are.append(drawer_name)
            kon.remove(drawn_player)
            konn = False  # แก้ไขนี้
        else:
            drawn_player = "คุณจับไปแล้ว"
    else:
        drawn_player = "คุณไม่ใช่ผู้เล่น"
    return render_template('draw.html', mon=drawn_player)


@app.route('/player')
def player():
    return render_template('player.html', pla=lol)
