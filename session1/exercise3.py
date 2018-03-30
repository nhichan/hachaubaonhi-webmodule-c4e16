from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')
def index(username):

    users = [
        {
            'username':'nhi',
            'gender':0,
            'hobby':'dancing'
        },
        {
            'username':'john',
            'gender':1,
            'hobby':'singing'
        },
        {
            'username':'quynh',
            'gender':0,
            'hobby':'reading'
        },
    ]
    for u in users:
        if (u['username'] == username):
            return render_template('exercise3.html',user=u)
        return 'User not found'

if __name__ == '__main__':
  app.run(debug=True)
