# request.form.get('key')
# request.form['kay']

# --------------- session handling with cokkie

from flask import Flask, request, render_template, make_response, session, url_for, redirect
import requests

app = Flask(__name__)
app.secret_key = 'asasd$@#$@$5443'

@app.route("/", methods=["GET",'POST'])
def hello_world():
    if request.method == 'POST' :

        email = request.form['email']
        # -------- session handling with session
        session['userEmail']= email
        password = request.form['password']
        # email = request.form.get('email')
        # password = request.form.get('password')
        print(email, ' ', password)
        print(request.form)
        # return "Value Printed"
        # ----------- session handling with cookie start 
        # res = make_response(render_template('profile.html'))
        # print('1.1 : ', res)
        # res.set_cookie("userEmail", request.form['email'])
        # print('1.2 : ', res)
        # return res
        # ----------- session handling with cookie end
        return render_template('profile.html')
    if 'userEmail' in session:
        return "You are already Logged in"
    return  render_template('login.html')

@app.route("/getUserID", methods=["GET", "POST"])
def getUserID():
#    name = request.cookies.get('userEmail')
   name = session.get('userEmail')
   if name == None :
    #    name = 'Guest'
       return redirect(url_for('hello_world'))
   return  f'Welcome ! {name}'

@app.route("/logout", methods = ["GET","POST"])
def logout():
    # ---------- for cookie
    # res = make_response(render_template('profile.html'))
    # res.delete_cookie('userEmail')
    # return res

    # -------- for session 
    session.pop('userEmail')
    return redirect(url_for('hello_world'))
# -----
@app.route("/index", methods=["GET",'POST'])
def index():
    person = {
        "name" : "kalpesh",
        "language" : "python",
        "framework" : ["flask", "django", "bottel"]
    }
    res = requests.post('http://192.168.1.72:5000/make_json', json = person)
    print('res : ', res.text)
    return res.text

@app.route("/make_json", methods=["GET",'POST'])
def make_json():
    print('request : ', request)
    if request.is_json:
        # return "Yes! Request is JSON"
        # return request.json
        print(request.json['name'])
        print(request.json['language'])
        print(request.json.get('framework'))
        return request.json.get('name')
    return "No! Request is Not JSON"


if __name__ == '__main__':
    app.run(host='0.0.0.0')