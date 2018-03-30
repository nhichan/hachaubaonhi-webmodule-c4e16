from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    height /= 100
    bmi = weight/(height*height)
    if bmi < 16:
        return "Severely underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obese"



if __name__ == '__main__':
  app.run(debug=True)
