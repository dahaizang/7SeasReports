import datetime
import sys

import mysql.connector
import os
import json
import xlsxwriter


# define the name of the directory to be created
database = None

configJsonFile = 'config.json'

def connectToDB() -> object:
    with open(configJsonFile) as json_file:
        data = json.load(json_file)
        user = data['user']
        password = data['password']
        host = data['host']
        port = data['port']
        global database
        database = data['database']
    cnx = mysql.connector.connect(user=user, password=password,
                                  host=host,
                                  port=port,
                                  database=database)
    return cnx

def makedir(path):
    if not (os.path.isdir(path)):
        try:
            os.makedirs(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
            sys.exit()
        else:
            print("Successfully created the directory %s" % path)


def main():
    table = "vwCustomer"
    columns: str = "CustomerID,user_login,user_email,DateRegistered,first_name,last_name,nick_name,wechat_id"
    columnList = ["CustomerID","user_login","user_email","DateRegistered","first_name","last_name","nick_name","wechat_id"]

    cnx = connectToDB()
    cursor = cnx.cursor()

    query = ("SELECT " + columns +
             " FROM " + database + "." + table)

    cursor.execute(query)

    # Create a workbook and add a worksheet.
    excelFile = './Customers.xlsx'
    workbook = xlsxwriter.Workbook(excelFile)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for columnHeading in columnList:
        worksheet.write(row, col, columnHeading)
        col += 1

    for (customer_id, user_login, user_email, DateRegistered, first_name, last_name, nick_name, wechat_id) in cursor:
        line = "\n" + customer_id + "," + user_login + "," + user_email + "," + DateRegistered\
               + "," + first_name + "," + last_name + "," + nick_name + "," + wechat_id
        rowData = [customer_id,user_login,user_email,DateRegistered,
               first_name,last_name,nick_name,wechat_id]
        col = 0
        row += 1
        for cell in rowData:
            worksheet.write(row, col, cell)
            col += 1

    print('\nReport is saved in file:\n' + os.path.abspath(excelFile))
    workbook.close()

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    main()
