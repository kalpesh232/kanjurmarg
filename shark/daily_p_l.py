# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, jsonify
import pandas as pd

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    if request.method == 'POST':
        open = request.form.get('open')
        print('*' * 153, type(open))
        if 'file' not in request.files:
            print('No File Provided')
            return jsonify({'error' : 'No File Provided'}), 400
        else:
            file = request.files['file']
            print('file : ', file.filename)
        if file.filename == '':
            return jsonify({'error' : 'No File Selected'}), 400
        else:
            df = pd.read_csv(file)
            df = df.drop(['Date','Price','Vol.'],axis=1)
            df['Open'] = df['Open'].str.replace(',', '').astype(float)
            df['Low'] = df['Low'].str.replace(',', '').astype(float)
            df['High'] = df['High'].str.replace(',', '').astype(float)
            df['Open-Low'] = df['Open'] - df['Low']
            df['High-Open'] = df['High'] - df['Open']
            avg_low = df['Open-Low'].mean()
            avg_high = df['High-Open'].mean()
            print('*' * 153, type(avg_low))
            print('Single day ideally Low RS. : ', avg_low )
            print('Single day ideally High RS. : ', avg_high )
            buy = float(open) - avg_low
            sell = float(open) + avg_high
            print('Ideally buy this at price RS. : ',  buy)
            print('Ideally sell this at price RS. : ',  sell)
    return render_template('x.html')

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', debug=True)