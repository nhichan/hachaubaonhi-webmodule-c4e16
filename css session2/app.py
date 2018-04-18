from flask import Flask, render_template, redirect, url_for, request, session
from models.service import Service
from models.user import User
from models.order import Order
from mongoengine import *
import mlab

app = Flask(__name__)
app.secret_key = "a-secret-key"
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects(gender=gender, yob__lte=1998)# Only find users whose age is 18 or less
    #john = all_services[0]
    return render_template('search.html',all_services=all_services)

@app.route('/admin')
def admin():
    services = Service.objects() #lay tu database len
    return render_template('admin.html',services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)#xoa 1 id
    if service_to_delete is None:
        return "not found"
    else:
        service_to_delete.delete()
        return redirect(url_for('admin'))#ko nen goi ten route ma nen goi function

@app.route('/detail/<service_id>')
def detail(service_id):
    if "user_id" not in session:
        return redirect(url_for('login'))
    service_to_detail = Service.objects.with_id(service_id)
    if service_to_detail is None:
        return "not found"
    else:
        return render_template('detail.html', service=service_to_detail)

@app.route('/new_service', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("new_service.html")
    elif request.method == 'POST':
        new_service = Service(name=request.form['name'],
                            gender=int(request.form['gender']),
                            yob=int(request.form['yob']),
                             address=request.form['address'])
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update_service/<service_id>', methods=['GET', 'POST'])
def update(service_id):
    service_to_modify = Service.objects.with_id(service_id)
    if service_to_modify is None:
        return "not found"
    if request.method == 'GET':
        return render_template("update_service.html", service=service_to_modify)
    elif request.method == 'POST':
        service_to_modify.name = request.form['name']
        service_to_modify.yob = int(request.form['yob'])
        service_to_modify.address = request.form['address']
        service_to_modify.save()
        return redirect(url_for('admin'))


@app.route('/sign-in',methods=['GET','POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method =='POST':
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']
        try:
            new_user = User(fullname=fullname, email=email, username=username, password=password)
            new_user.save()
        except Exception:
            return render_template('error.html')
        return redirect(url_for('index'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method =='POST':
        form = request.form
        username = form['username']
        password = form['password']

        user = User.objects.get(username = username, password = password)

        if user is not None:
            session['user_id'] = str(user.id)
            return redirect(url_for('index'))
        else:
            return "fail"

@app.route('/send_request/<requested>')
def send_request(requested):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    order = Order(userid=session['user_id'], serviceid=requested, is_accepted=False)
    order.save()
    return 'request sent!'

if __name__ == '__main__':
  app.run(debug=True)
