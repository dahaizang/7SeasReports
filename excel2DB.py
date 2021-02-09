import xlrd
import mysql.connector

# Open the workbook and define the worksheet
book = xlrd.open_workbook(“importExcel.xls”)

sheet = book.sheet_by_name(“Client_Data”)
//sheet = book.sheet_by_index(0)

# Establish a MySQL Connection
database = MySQLdb.connect (host=“localhost”, user=“root”, passwd=“”, db=“mysqlPython)

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = “””INSERT INTO order (job_code, date, client, description, status, project_manager) VALUES (%s, %s, %s, %s, %s,%s)”””

# Create a for loop to iterate through each row in the xls file, starting from row 2
for r in range(1, sheet.nrows):
product = sheet.cell(r,0).value
customer = sheet.cell(r,1).value
rep = sheet.cell(r,2).value
date = sheet.cell(r,3).value
actual = sheet.cell(r,4).value
expected = sheet(r,5).value
open_opportunities = sheet(r,6).value

# Assign values from each row
values = (job_code, date, client, description, status, project_manager)

# Execute sql query
cursor.execute(query, values)
# Close the cursor
cursor.close()

#Commit the transaction
database.commit()
#Close the database connection
database.close()
#Print results
print “”
print “Data Imported successfully!!!”
print “”
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print “Summary of data imported: “ + columns + “ columns and “ + rows + ” rows”

2020春季-楷书班-九成宫
2020春季-小楷班-灵飞经
2020春季-行书班-赵孟頫
2020春季-隶书班
2020春季-隶书-曹全碑
2020春季-行草班-米芾
2020春季-楷书班-赵孟頫

2019秋季-楷书班-九成宫
2019秋季-楷书班-多宝塔
2019秋季-篆书班
2019秋季-隶书班
2019秋季-隶书班-曹全碑
2019秋季-行草班-米芾
2019秋季-行书班-赵孟頫