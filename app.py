# Main file ,run this file to start the app
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')  
import io
import base64
from datetime import datetime

app = Flask(__name__)

# customers table is basically list of all customers and  customer_data table is the table stores the data for each customer
# Change function to change any database schema
def create_database():
    conn = sqlite3.connect('Records.db')
    c = conn.cursor()
    # Table for storing customer details
    c.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT,
            LastName TEXT,
            DOB TEXT
        )
    ''')
    # Table for storing customer-specific data
    c.execute('''
        CREATE TABLE IF NOT EXISTS customer_data (
            CustomerID INTEGER,
            Month TEXT,
            Income REAL,
            Expenses REAL,
            FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
        )
    ''')
    conn.commit()
    conn.close()

# function to create plot and return as string
# Change function to produce a different graph
def create_plot(data, firstname, lastname):
    img = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.plot(data['Month'], data['Income'], marker='o', label='Income', color='blue')
    plt.plot(data['Month'], data['Expenses'], marker='o', label='Expenses', color='red')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title(f'Income vs Expenses for {firstname} {lastname}')
    plt.legend()
    plt.grid(True)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url



# Intitial and main page route and function to render the page
# Change function to add more customer data or information to the page
@app.route('/')
def index():

    conn = sqlite3.connect('Records.db')
    c = conn.cursor()
    # This specific task only requires us to  deal with one customer in the database but we do this so its easy to extend to multiple customers
    c.execute('SELECT * FROM customers ORDER BY ROWID DESC LIMIT 1')
    # Get the most recent customer
    customer = c.fetchone()  

    #We render plot only if customer is present in database
    if customer:
        customer_id ,firstname, lastname, dob = customer
        c.execute('SELECT Month, Income, Expenses FROM customer_data WHERE CustomerID = ?', (customer_id,))
        data = pd.DataFrame(c.fetchall(), columns=['Month', 'Income', 'Expenses'])
        plot_url = create_plot(data, firstname, lastname)
        conn.close()
        return render_template('index.html', plot_url=plot_url, firstname=firstname, lastname=lastname, dob=dob) 
    
    conn.close()
    return render_template('index.html', plot_url=None, firstname=None, lastname=None, dob=None)


# Route for adding data to the database
# change route function to add aditional customer info or data
@app.route('/add', methods=['POST'])
def add_task():
    # Get Customer information from form input
    firstname = request.form['FirstName']
    lastname = request.form['LastName']
    dob = datetime.strptime(
                     request.form['birthday'],
                     '%Y-%m-%d').date()
    # Get Customer data from file uploaded
    customerdata = request.files['CustomerData']
    df = pd.read_excel(customerdata)
    
    # Add customer information and excel data to customers and customer_data tables
    conn = sqlite3.connect('Records.db')
    c = conn.cursor()
    c.execute('INSERT INTO customers (FirstName, LastName, DOB) VALUES (?, ?, ?)', (firstname, lastname, dob))
    customer_id = c.lastrowid 
    df['CustomerID'] = customer_id   # we add customer id to dataframe since we copying dataframe to cusotmer_data table
    df.to_sql('customer_data', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

    # All data added so we redirect to home page
    return redirect(url_for('index'))


# Running the app , we intialize  database or connect to existing one at the start of the app
if __name__ == '__main__':
    create_database()
    app.run(debug=True)