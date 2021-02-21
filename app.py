from flask import Flask, render_template, jsonify, request
import datetime
import pymongo
client = pymongo.MongoClient("")
app = Flask(__name__)

t = datetime.datetime.today()
today = t.strftime('%Y-%m-%d')


@app.route('/')
def home():
    return render_template('index.html', image_file=f'{today}_graph.png')


@app.route("/table_view")
def mypage():
    return render_template(f'{today}_table.html')


# @app.route("/reviews", methods=["GET"])
# def shopper_get():
#     return jsonify({"result":"success"},{"msg":"API CALL SUCCESS"})


# @app.route("/reviews", methods=["POST"])
# def review_post():
#     # //insert
#     title = request.form['title']
#     author = request.form['author']
#     review
#     db.reviews.insert_one({})
#     return jsonify({"result":"success"},{"msg":"POST API CALL SUCCESS"})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)       # port 번호는 3천이상으로 쓸것.
