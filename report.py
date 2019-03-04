"""base class to represent a report and methods to run a report from a MySQl view/table"""
import datetime
import sys

import mysql.connector
import os
import json
import xlsxwriter

class report:

    database = None
    user = None
    password = None
    host = None
    port = None
    table = None
    columnList = None
    reportFile = None

    configJsonFile = 'config.json'

    def __init__(self, table, columnList):
        self.table = table
        self.columnList = columnList
        with open(self.configJsonFile) as json_file:
            self.data = json.load(json_file)
            self.user = data['user']
            self.password = data['password']
            self.host = data['host']
            self.port = data['port']
            self.database = data['database']

    def connectToDB() -> object:
        cnx = mysql.connector.connect(user=user, password=password,
                                    host=host,
                                    port=port,
                                    database=database)
        return cnx


    def execute():
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
