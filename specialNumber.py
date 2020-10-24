from flask import Flask, url_for, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = '9b707acd44ab23af0309c0ef6962e477'



# routes by default
@app.route("/", methods=["GET", "POST"])
def home():
    global numberinput
    if request.method == 'GET':
        return render_template('home.html', title='Home')
    else:
        numberinput = (request.form.get('numin'))
        return redirect(url_for('result', numberinput=numberinput))

@app.route("/results/<numberinput>", methods=["GET", "POST"])
def result(numberinput):
    return render_template('results.html', methods=(['GET', 'POST']), title='Results', numberinput=numberinput)


if __name__ == "__main__":
    app.run(debug=True)
