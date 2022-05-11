from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():    
    return render_template('idx.html')  # Render the index page at the start

@app.route('/s1', methods=['GET', 'POST']) # If button is pressed
def start1():
    cust = pd.read_csv('cust.csv')   # Reading the customer purchase history csv
    stock = pd.read_csv('stock.csv') # Reading the stock csv
    
    if request.method == 'POST':
        if request.form.get('action1') == 'Stock Details': 
            return render_template('sd.html', tables=[stock.to_html()], titles=[''])
        elif  request.form.get('action2') == 'Purchase History':
            return render_template('ph.html', tables=[cust.to_html()], titles=[''])
        
    elif request.method == 'GET':
        return render_template('idx.html', form=form)

    return render_template('idx.html')
    

if __name__ == '__main__':
   app.run(debug = True)
