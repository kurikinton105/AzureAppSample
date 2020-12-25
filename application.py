from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == 'GET':
        text = "ここに結果が出力されます"
        return render_template("page.html",text=text)
    elif request.method == 'POST':
        name = request.form["name"]
        text = "こんにちは" + name + "さん"
        return render_template("page.html",text=text)

## 実行
if __name__ == "__main__":
    app.run(debug=True)