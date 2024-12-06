# EPF

Project Description

This project is a simple web-based workflow system for capturing customer information and rendering a temporal graph of their income and expenses over the last 12 months. The system is built using HTML , Python and Flask, with SQLite for data storage and Matplotlib for graph visualization.


Installation and Running

Clone the repository and install the required packages outlined in the requirements.txt file using pip.
To run the application : python app.py   and then open browswer and navigate to http://127.0.0.1:5000


Solution Approach

1. Database Initialization:  
   - At the start of the application, a SQLite database (Records.db) is initialized with two tables:  
     - customers Table: This table stores customer details such as First Name, Last Name, and Date of Birth.  
     - customer_data Table: This table stores customer financial data which ismonthly income and expenses, associated with a CustomerID foreign key.  

2. User Interaction:  
   - The main page of the application presents a simple HTML form that allows users to:  
     - Input customer details: First Name, Last Name, and Date of Birth.  
     - Upload an Excel file containing financial data (monthly income and expenses) for the last 12 months. 
   - All the information is required to be filled in.  

3. Data Processing and Storage:  
   - Upon form submission:  
     - The entered customer details are stored in the customers table and auto incremented. 
     - The uploaded Excel file is processed using Pandas to extract financial data, which is then associated with the corresponding customer in the customer_data table using a unique CustomerID which is the incremented id.

4. Visualization:  
   - After  storing the data we redirect to the main page where the application generates a line graph using Matplotlib to visualize the customer's income and expenses trends over the last 12 months.  
   - The graph is embedded directly into the main page using a Base64-encoded PNG image.  
5. HTML Page:
   - The page is designed to show a graph of the recent customer financial data and does not show any graph when database is empty.
   
6. Code  Organization:  
   - The application code is structured into distinct functions to ensure clarity and maintainability:  
     - create_database(): Initializes the SQLite database with the 2 tables.  
     - create_plot(): Generates a visualization for customer data.  
     - index(): Serves the main page and displays the form and graph.  
     - add_task(): Handles form submission, data processing, and storage.


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


   









