from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    height /= 100
    bmi = weight/(height*height)
    if bmi < 16:
        res = "Severely underweight"
    elif 16 <= bmi < 18.5:
        res = "Underweight"
    elif 18.5 <= bmi < 25:
        res = "Normal"
    elif 25 <= bmi < 30:
        res = "overweight"
    else:
        res = "obese"
    return render_template('exercise2.html', res=res)

if __name__ == '__main__':
  app.run(debug=True)
