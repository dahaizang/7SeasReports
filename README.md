# 7SeasReports
Python code to generate reports from 7SeasCalligraphy MySQL database by converting
tables/views into Excel sheets

To run this program (report.py if you have a Python environmnet, or report.exe if you do not), place a config.json file in the same directory as 
the program and run the program using Python 3

Content of the config.json file should contain the credentials of your MySQL database.

{  
  "user" : "DB user id",  
  "password" : "DB password",  
  "host" : "DB Host name",  
  "port" : "Port number",  
  "database": "database to use"  
}

This program only works with 7SeasCalligraphy database views. But you can modify the code to 
have it work with your own database tables/view