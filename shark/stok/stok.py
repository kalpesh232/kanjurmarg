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
def hello_world():
    if current_time < target_time:
        companies = ["NHPC", "Deepak Nitrite", "Yatharth Hospital", "Alivus Life Sciences", "Sharda Motor Industries", "Coal India", "LT Foods", "Oil India", "CMS Info Systems", "LIC Housing Finance", "Likhitha Infra", "JK Paper", "Petronet LNG", "Alkem Laboratories", "Lupin", "Bosch", "HDFC Asset Mgmt Co", "Torrent Pharma", "Bajaj Holdings", "Eicher Motors", "IndusInd Bank", "Godrej Consumer", "PNB", "Pidilite Industries", "DLF", "Bajaj Auto", "Avenue Supermarts", "Bajaj Finserv", "Adani Ports", "UltraTech Cement", "Titan", "NTPC", "Adani Enterprises", "Tata Motors", "Sun Pharmaceutical", "Axis Bank", "Bajaj Finance", "HCL Technologies", "ITC", "ICICI Bank", "HDFC Bank"]

        
        random_company = random.choice(companies)
        print(random_company)
        print(companies.index(random_company)+1)
        stok_dic = {'stok_name': random_company , 'stok_index' : companies.index(random_company)+1}

        if request.method == 'POST':
            open = request.form.get('open')
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
                df.columns = df.columns.str.strip().str.lower()
                df = df[['open', 'high', 'low']]
            
                df['open'] = df['open'].apply(lambda x: float(str(x).replace(',', '')) if ',' in str(x) else float(x))
                df['low'] = df['low'].apply(lambda x: str(x).replace(',', '') if isinstance(x, str) else x).astype(float)
                df['high'] = df['high'].apply(lambda x: str(x).replace(',', '') if isinstance(x, str) else x).astype(float)
            
                df['open-low'] = df['open'] - df['low']
                df['high-open'] = df['high'] - df['open']

                avg_low = df['open-low'].mean()
                avg_high = df['high-open'].mean()
                print('Single day ideally Low RS. : ', round(avg_low) )
                print('Single day ideally High RS. : ', round(avg_high) )

                buy = float(open) - avg_low
                max_buy = ( buy * (100 + float(low_per)))/100
                sell = float(open) + avg_high
                max_sell = ( sell * (100 + float(high_per)))/100
                print('____________________', buy)
                print('Ideally buy this at price RS. : ',  round(buy) , '-', round(max_buy))
                print('Ideally sell this at price RS. : ',  round(sell), '-', round(max_sell))
                buy_sell = {'min_buy' : round(buy), 'max_buy' : round(max_buy), 'min_sell' : round(sell), 'max_sell' : round(max_sell), 'single_day_low' : round(avg_low), 'single_day_high' : round(avg_high) }
                return render_template('calculate_volatilty.html',buy_sell=buy_sell)

        return render_template('calculate_volatilty.html',stok_dic=stok_dic)
    
    else:
        if request.method == 'POST':
            placed = request.form.get('placed')
            low = request.form.get('low')
            high = request.form.get('high')
            
            if low :
                # more = int(low) - float(placed)
                more = float(low) - float(placed)
                more_per = (more/int(placed)) * 100
                with app.app_context():
                    query = db.session.execute(text('select low_per FROM percentage_table ORDER BY id ASC '))
                    per = query.fetchall()[0][0]
                    final_inc_or_dec = per +  float(more_per) 
                    final_low_per = round(final_inc_or_dec,2)
                    
                    query = db.session.execute(text(f'UPDATE percentage_table SET low_per = {final_low_per} WHERE id = {1} '))
                    db.session.commit()
        
            if high :
                more = float(high) - float(placed)
                more_per = (more/int(placed)) * 100
                with app.app_context():
                    query = db.session.execute(text('select high_per FROM percentage_table ORDER BY id ASC '))
                    per = query.fetchall()[0][0]
                    
                    final_inc_or_dec = per +  float(more_per) 
                    final_high_per = round(final_inc_or_dec,2)
                    
                    query = db.session.execute(text(f'UPDATE percentage_table SET high_per = {final_high_per} WHERE id = {1} '))
                    db.session.commit()

                # Print confirmation
            print('Table updated successfully!')
    return render_template('cal_inc_per.html')

if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0', debug=True)