from flask import Flask, render_template
from models.service import Service
from models.customer import Customer
from mongoengine import *
import mlab

app = Flask(__name__)
mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects(gender=gender, yob__lte=1998)# Only find users whose age is 18 or less
    return render_template('search.html',all_services=all_services)

@app.route('/customer')
def index_customer():
    all_customers = Customer.objects()
    return render_template('index_customer.html',all_customers=all_customers)

@app.route('/uncontacted_10_male_customers')
def index_male_customer():
    all_customers = Customer.objects(gender=1, contacted=False)[:10]
    return render_template('index_customer.html',all_customers=all_customers)

if __name__ == '__main__':
  app.run(debug=True)
