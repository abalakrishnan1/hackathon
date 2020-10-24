from flask import Flask, url_for, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = '9b707acd44ab23af0309c0ef6962e477'

def prime(number):
    factors = []
    factorsum = 0
    for i in range((int(number/2))):
        if number%(i+1) == 0:
            factors.append(i+1)
    for l in range(len(factors)):
        factorsum += factors[l]
    if factorsum == 1:
        return "Yes"
    else:
        return 'No'


# routes by default
@app.route("/", methods=["GET", "POST"])
def home():
    global numberinput
    global isPrime
    if request.method == 'GET':
        return render_template('home.html', title='Home')
    else:
        numberinput = (request.form.get('numin'))
        isPrime = str(prime(int(numberinput)))
        return redirect(url_for('result', numberinput=numberinput, isPrime=isPrime))

@app.route("/results/<numberinput>", methods=["GET", "POST"])
def result(numberinput):
    return render_template('results.html', methods=(['GET', 'POST']), title='Results', numberinput=numberinput, isPrime=isPrime)


if __name__ == "__main__":
    app.run(debug=True)
