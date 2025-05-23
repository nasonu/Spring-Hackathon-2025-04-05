from flask import Flask, redirect, render_template, session, flash, abort, url_for
from datetime import timedelta
import hashlib
import uuid
import re
import os

# FlaskやDjangoでは、デフォルトでtemplatesを認識するので、パス指定はtemplates以降を記載で問題ない
# 定数定義
EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
SESSION_DAYS = 30

app = Flask(__name__)
app.secret_key= os.getenv('SECRET_KEY', uuid.uuid4().hex) # .envファイルからシークレットキーを取得

# 起動時にセッションがあれば、channel.htmlへ遷移し、なければlogin.htmlへ遷移する
# 初回起動時のリダイレクト処理
@app.route('/', methods=['GET'])
def index():
    uid = session.get('uid')
    if uid is None:
        return redirect(url_for('login_page'))  # ←セッションがない場合login_page関数からログイン画面に戻る


# ログイン画面表示
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('auth/login.html')


# ログイン処理
@app.route('/login', methods=['POST'])
def login_process():
    pass


# ログアウト処理
@app.route('/login', methods=['POST'])
def logout():
    session.clear()
    return render_template(url_for('login_page'))


# サインアップ画面表示
@app.route('/signup',methods=['GET'])
def signup_page():
    return render_template('auth/sign_up.html')


# サインアップ処理
@app.route('/signup',methods=['POST'])
def signup_process():
    pass


# チャットルーム一覧表示
@app.route('/room/<cid>/message', methods=['GET'])
def room_page():
    return render_template('auth/room.html')    # ★htmlファイル名の確認


# チャットルーム作成処理
@app.route('/room/create', methods=['POST'])
def room_create():
    pass


# チャットルーム編集処理
@app.route('/room/update/<cid>', methods=['POST'])
def room_update():
    pass


# チャットルーム削除処理
@app.route('/room/delete/<cid>', methods=['POST'])
def room_delete():
    pass


# チャットメッセージ画面表示
@app.route('/room/<cid>/message', methods=['GET'])
def message_page():
    return render_template('auth/message.html')     # ★htmlファイル名の確認


# メッセージ送信処理
@app.route('/room/<cid>/message', methods=['POST'])
def message_create():
    pass


# メッセージ編集処理
@app.route('/room/<cid>/message/<message_id>', methods=['POST'])
def message_update():
    pass


# メッセージ削除処理
@app.route('/room/<cid>/message/<message_id>', methods=['POST'])
def message_delete():
    pass


# メッセージ翻訳処理
@app.route('/room/<cid>/message/<message_id>', methods=['POST'])
def message_translation():
    pass


# mainメソッド
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)




