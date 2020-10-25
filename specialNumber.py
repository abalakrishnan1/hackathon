from flask import Flask, url_for, redirect, render_template, session, request
import requests as r


app = Flask(__name__)
app.secret_key = '9b707acd44ab23af0309c0ef6962e477'

def prime(number):
    factors = []
    factorsum = 0
    for i in range((int(int(number)/2))):
        if int(number)%(i+1) == 0:
            factors.append(i+1)
    for l in range(len(factors)):
        factorsum += factors[l]
    if factorsum == 1:
        return "Yes"
    else:
        return 'No'

def findinpi(number):
  url = "https://www.angio.net/newpi/piquery"
  response = r.post(url, data = {"q":number})
  pidict = response.json()['r'][0]
  return(('This number appears ' + (str(pidict['c']))+' times in the first 200M digits') + ' and it occurs first ' + str(pidict['p']) + ' places after the decimal')

def twinprime(number):
    if prime(int(number)):
        if prime(int(number)+2) or prime(int(number)-2):
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'

def degreesforngon(number):
  #returns total degrees of ngon
  degrees=(180*(int(number)-2))/int(number)
  return degrees

def perfectnumber(number):
  factors = []
  factorsum = 0
  for i in range((int(int(number)/2))):
    if int(number)%(i+1) == 0:
      factors.append(i+1)
  for l in range(len(factors)):
    factorsum += factors[l]
  if factorsum == int(number):
    return 'Yes'
  else:
    return 'No'


def PerfectSquare(x):
    s = int(pow(x, 1 / 2))
    return pow(s, 2) == x


def fib(num):
    num = int(num)
    if PerfectSquare(5 * pow(num, 2) + 4) or PerfectSquare(5 * pow(num, 2) - 4):
        return 'Yes'
    else:
        return 'No'

def roots(num):
 num = int(num)
 y = 2
 c = 0
 while y <= 1000:
   s = int(pow(num,1/y))
   if pow(s,y) == num:
     c += 1
   y += 1
 return c

def factorial(n):
   n = int(n)
   i = f = 1
   while f < n:
       i += 1
       f *= i
   if f == n:
       return 'Yes'
   else:
       return 'No'



# routes by default
@app.route("/", methods=["GET", "POST"])
def home():
    global numberinput
    global isPrime
    global digitsOfPi
    global twinprime
    global ngon
    global perfect
    global fibi
    global root
    global fact
    if request.method == 'GET':
        return render_template('home.html', title='Home')
    else:
        numberinput = (request.form.get('numin'))
        isPrime = prime(numberinput)
        digitsOfPi = findinpi(numberinput)
        twinprime = twinprime(int(numberinput))
        ngon = degreesforngon(numberinput)
        perfect = perfectnumber(numberinput)
        fibi = fib(numberinput)
        root = roots(numberinput)
        fact = factorial(numberinput)

        return redirect(url_for('result', numberinput=numberinput, isPrime=isPrime, digitsOfPi=digitsOfPi,
                                twinprime=twinprime, ngon=ngon, perfect=perfect, fibi=fibi, root=root, fact=fact))


@app.route("/results/<numberinput>", methods=["GET", "POST"])
def result(numberinput):
    return render_template('results.html', methods=(['GET', 'POST']), title='Results', numberinput=numberinput,
                           isPrime=isPrime, digitsOfPi=digitsOfPi, twinprime=twinprime, ngon=ngon, perfect=perfect,
                           fibi=fibi, root=root, fact=fact)


if __name__ == "__main__":
    app.run(debug=True)
