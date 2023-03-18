# csv-file
CSV Data handler

Here this project provides two Django Rest Framework API endpoints for handling CSV data. 

1.The first endpoint allows users to upload a CSV file, which is then parsed and inserted into a Django database.

2.The second endpoint allows users to retrieve the top 50 rows of data from the database, sorted based on a specified column and order.
To use this project, you will need to have Python 3.x installed on your machine. Clone this repository and navigate to the project directory in your terminal.

Next, install the required Python packages using pip:
pip install -r requirements.txt
To start the Django development server, run the following command:
python manage.py runserver
To upload a CSV file, make a POST request to the data/upload/ endpoint with the file included in the request body as a form-data field named file. The API will parse the CSV file and insert each row into a DataModel object in the database.

To retrieve sorted data, make a GET request to the data/sorted/ endpoint with the desired column name and sort order specified in the query parameters.

The API will retrieve the top 50 rows of data sorted by the specified column and order, and return it in JSON format.



