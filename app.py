
from flask import Flask
from flask import render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='VTM Site')


@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About')



def calculate_top_area(radius):
    return 3.14*(radius**2)

def calculate_side_area(radius,height):
    return 2*(3.14*(height*radius))



@app.route('/estimate', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi = 3.14
        topArea = pi * radius**2
        sidesArea = 2*(pi*(radius*height))
        totalArea = topArea+sidesArea
        totalSqFt = totalArea / 144
        materialCost = 25 * totalSqFt
        laborCost = 15 * totalSqFt
        totalCostEstimate = "${:,.2f}".format(round(materialCost + laborCost, 2))
        return (render_template('estimate.html', estimate = totalCostEstimate))
    return render_template('estimate.html', pageTitle='Estimator')

if __name__ == '__main__':
    app.run(debug=True)