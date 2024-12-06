# EPF

Project Description

This project is a simple web-based workflow system for capturing customer information and rendering a temporal graph of their income and expenses over the last 12 months. The system is built using HTML , Python and Flask, with SQLite for data storage and Matplotlib for graph visualization.


Installation and Running

Clone the repository and install the required packages outlined in the requirements.txt file using pip.
To run the application : python app.py
Open browswer and navigate to http://127.0.0.1:5000


How it works
1. At the start of the app a database is created with 2 tables ( customers and customer_data)
2. A form is presented on the main page with required input fields to input customer details(First Name, Last Name, Date of Birth) and upload their financial data( Excel file).
3. Customer information is stored in the customers table and financial data is stored in the customer_data table.
4. A line graph showing income and expenses trends and display it on the same page.

Assumptions 

Single User: There is no login or user management, as specified in the assignment pdf.
Simple Database: SQLite is used for simplicity, with two tables (customers and customer_data).
One Customer at a Time: The system always displays the most recent customer's graph and extending to multiple customers would involve adding a simple selection mechanism.
Customer infor: We only take in First name, last name and date of birth of the customer.
Excel File Format: The uploaded file is an excel file and  is assumed to contain Month, Income, and Expenses columns.

Extensibility

The system designed with 2 tables already allows the addition of multiple customers in the database but only shows graph of the most recent customer added as required by the task, however we can introduce a dropdown list  for selecting different customers.
The system can also allow users to compare multiple customers' financial data by simply altering the create plot function.
Any additional preprocessing of the excel data can simply be done in the add route function before adding data to the database without changing any of the other functions.


   









