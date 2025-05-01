from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


# uphd
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/stok'
db = SQLAlchemy()
app = Flask(__name__)
def init_app(app):
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/stok'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/stok'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Initialize the db with the app

class PercentageTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing primary key
    low_per = db.Column(db.Float, nullable=False)
    high_per = db.Column(db.Float, nullable=False)


init_app(app)

# Create an application context
with app.app_context():

    try:
        db.session.execute(text('SELECT 1'))
        print("Database connection established successfully.")
        db.create_all()
        print("Table 'PercentageTable' created successfully.")
    except Exception as e :
        print(f"Database connection failed: {e}")

# if __name__ == '__main__':
#     app.run(debug=True)

    