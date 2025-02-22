# 7SeasReports
Python code to generate reports from 7SeasCalligraphy MySQL database by converting
tables/views into Excel sheets

To run this program (7SeasReports.py if you have a Python environmnet, or 7SeasReports.exe if you do not), place a credentials.py file in the same directory as 
the program and run the program using Python 3

Content of the credentials.py file should contain the credentials of your MySQL database.

class credentials:  
    user = 'DB user id'  
    password = 'DB password'  
    host = '7seascalligraphy.org'  
    port = 3306  
    database = 'database to use'


This program only works with 7SeasCalligraphy database views. But you can modify the code to 
have it work with your own database tables/view

TO create a Windows executable, run
pyinstaller -F 7SeasReports.py