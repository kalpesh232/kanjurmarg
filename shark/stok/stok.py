

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, jsonify
import pandas as pd
import random
from stok_config import db, init_app
from sqlalchemy import text
from datetime import datetime

app = Flask(__name__)
init_app(app)

target_time = datetime.strptime("15:30", "%H:%M").time()
current_time = datetime.now().time()

@app.route('/',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    # 
    if current_time < target_time:
        companies = [
        "nhpc", "dn", "yhatcs", "gls", "smi", "ci", "ltf", "oi", "cis", "lhf", "li", "jp",
        "plng", "al", "l", "b", "hamc", "tp", "bhai", "em", "ib", "gcp", "pnb", "pi", "dlf",
        "ba", "as", "bf", "apasez", "utc", "tc", "ntpc", "ab", "tm", "spi", "ae", "bfinance",
        "hclt", "itc", "icicib", "hdfcb"
    ]

        # Print the list for verification
        random_company = random.choice(companies)
        print(random_company)
        print(companies.index(random_company)+1)
        # 
        if request.method == 'POST':
            open = request.form.get('open')
            # per = request.form.get('per')
            with app.app_context():
                low_query = db.session.execute(text('select low_per FROM percentage_table ORDER BY id ASC '))
                low_per = low_query.fetchall()[0][0]

                high_query = db.session.execute(text('select high_per FROM percentage_table ORDER BY id ASC '))
                high_per = high_query.fetchall()[0][0]
                
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
                df.columns = df.columns.str.lower()
                # df = df.drop(['Date','Price','Vol.'],axis=1)
                columns_to_drop = ['Date', 'Price', 'Vol.']
                df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
                # df['open'] = df['open'].str.replace(',', '').astype(float)
                # df['open'] = df['open'].apply(lambda x: str(x).replace(',', '') if isinstance(x, str) else x).astype(float)
                print(df)
                df['open'] = df['open'].apply(lambda x: float(str(x).replace(',', '')) if ',' in str(x) else float(x))

                # df['Low'] = df['Low'].str.replace(',', '').astype(float)
                df['Low'] = df['Low'].apply(lambda x: str(x).replace(',', '') if isinstance(x, str) else x).astype(float)
                # df['High'] = df['High'].str.replace(',', '').astype(float)
                df['High'] = df['High'].apply(lambda x: str(x).replace(',', '') if isinstance(x, str) else x).astype(float)
                df['open-Low'] = df['open'] - df['Low']
                df['High-open'] = df['High'] - df['open']
                avg_low = df['open-Low'].mean()
                avg_high = df['High-open'].mean()
                print('Single day ideally Low RS. : ', round(avg_low) )
                print('Single day ideally High RS. : ', round(avg_high) )
                buy = float(open) - avg_low
                max_buy = ( buy * (100 + float(low_per)))/100
                sell = float(open) + avg_high
                max_sell = ( sell * (100 + float(high_per)))/100
                print('____________________', buy)
                print('Ideally buy this at price RS. : ',  round(buy) , '-', round(max_buy))
                print('Ideally sell this at price RS. : ',  round(sell), '-', round(max_sell))
        return render_template('calculate_volatilty.html')
    else:
        if request.method == 'POST':
            placed = request.form.get('placed')
            low = request.form.get('low')
            high = request.form.get('high')
            print('='*50, low)
            if low :
                # more = int(low) - float(placed)
                more = float(low) - float(placed)
                more_per = (more/int(placed)) * 100
                with app.app_context():
                    query = db.session.execute(text('select low_per FROM percentage_table ORDER BY id ASC '))
                    per = query.fetchall()[0][0]
                    final_inc_or_dec = per +  float(more_per) 
                    final_low_per = round(final_inc_or_dec,2)
                    print('______________final_low_per : ', final_low_per)
                    query = db.session.execute(text(f'UPDATE percentage_table SET low_per = {final_low_per} WHERE id = {1} '))
                    db.session.commit()
            print('*'*50, high)
            if high :
                more = float(high) - float(placed)
                more_per = (more/int(placed)) * 100
                with app.app_context():
                    query = db.session.execute(text('select high_per FROM percentage_table ORDER BY id ASC '))
                    per = query.fetchall()[0][0]
                    print('_____________per : ', per)
                    final_inc_or_dec = per +  float(more_per) 
                    final_high_per = round(final_inc_or_dec,2)
                    print('_______________final_high_per : ', final_high_per)
                    query = db.session.execute(text(f'UPDATE percentage_table SET high_per = {final_high_per} WHERE id = {1} '))
                    db.session.commit()

                # Print confirmation
            print('Table updated successfully!')
        return render_template('cal_inc_per.html')
    


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', debug=True)

#  0.66
