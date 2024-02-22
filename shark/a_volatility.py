from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

def calculate_daily_returns(df):
    close_column = df.columns[df.columns.str.contains('Close', case=False)].tolist()
    if not close_column:
         raise KeyError("No column containing the word 'Close' found in the CSV file.")
    df['Daily Returns'] = df[close_column[0]].pct_change()
    return df

def calculate_daily_volatility(df):
    df["Daily Volatility"] = df['Daily Returns'].std()
    return df["Daily Volatility"].iloc[-1]

def calculate_annualized_volatility(daily_volatility, data_lenght):
    return daily_volatility * np.sqrt(data_lenght)

def analyze_index_data(file_path):
    df = pd.read_csv(file_path)
    df = calculate_daily_returns(df)
    daily_volatility = calculate_daily_volatility(df)
    data_lenght = len(df)
    annualized_volatility = calculate_annualized_volatility(daily_volatility, data_lenght)
    return annualized_volatility
  
   
@app.route('/', methods=['GET','POST'])
def calculate_volatilty():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        try :
            file_path = file.filename 
            file.save(file_path)

            result = analyze_index_data(file_path)

            return jsonify({'annualized_volatility ' : result})
        except Exception as e:
            return jsonify({'error ' : f' Error in Processing the File : {str(e)} '}), 500
    return render_template('calculate_volatilty.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)