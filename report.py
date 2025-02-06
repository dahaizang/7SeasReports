"""class to extract conetent from a MySQl view/table into an Excel file"""
import datetime
import sys

import mysql.connector
import os
import json
import xlsxwriter
import credentials

class report:

    database = None
    user = None
    password = None
    host = None
    port = None
    columnList = []
    columnNames = ""
    reportFile = None
    cnx = None

    configJsonFile = 'config.json'

    def __init__(self):
        self.getCredentials()

    def getCredentials(self):
        aCredential = credentials.credentials()
        self.user = aCredential.user
        self.password = aCredential.password
        self.host = aCredential.host
        self.port = aCredential.port
        self.database = aCredential.database

    def connectToDB(self):
        if self.cnx == None:
            self.cnx = mysql.connector.connect(user = self.user,
                                      password = self.password,
                                      host = self.host,
                                      port = self.port,
                                      database = self.database)

    def getDBTableMetaData(self, table):
        self.connectToDB()
        cursor = self.cnx.cursor()
        query = "select column_name from information_schema.columns where table_name = '" + table + "' order by ordinal_position"
        # print(query)
        cursor.execute(query)
        self.columnList = []
        self.columnNames = None
        for columnName in cursor:
            self.columnList.append(columnName[0])
            if self.columnNames == None:
                self.columnNames = '"' + columnName[0] + '"'
            else:
                self.columnNames += ',"' + columnName[0] + '"'

    # export table data to an Excel file, old version
    def execute(self, table, excelFile):
        self.getDBTableMetaData(table)

        self.connectToDB()
        cursor = self.cnx.cursor()
        #sqlString = "SELECT " + self.columnNames + " FROM " + self.database + "." + table
        sqlString = "SELECT * FROM " + self.database + ".`" + table + "`"
        #print(sqlString)

        cursor.execute(sqlString)

        workbook = xlsxwriter.Workbook(excelFile)
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0
        for columnHeading in self.columnList:
            worksheet.write(row, col, columnHeading)
            col += 1

        for aRow in cursor:
            col = 0
            row += 1
            for aCell in aRow:
                worksheet.write(row, col, aCell)
                col += 1

        print('\n' + table + ' is saved in file:\n' + os.path.abspath(excelFile) + ' with ' + str(row) +' rows')
        workbook.close()

        cursor.close()
        self.cnx.close()
        self.cnx = None

    # export table data to an Excel file. This version auto sizes the columns based on content
    def export_to_excel(self, table_name, output_file):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                           host=self.host, port=self.port,
                                           database=self.database)
        cursor = self.cnx.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]

        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet()

        for col_num, column_name in enumerate(column_names):
            worksheet.write(0, col_num, column_name)

        for row_num, row in enumerate(rows, start=1):
            for col_num, cell in enumerate(row):
                worksheet.write(row_num, col_num, cell)

        for col_num, column_name in enumerate(column_names):
            max_len = max([len(str(cell)) for cell in [column_name] + [row[col_num] for row in rows]]) + 2
            worksheet.set_column(col_num, col_num, max_len)

        print('\n' + table_name + ' is saved in file:\n' + os.path.abspath(output_file) + ' with ' + str(len(rows)) +' rows')

        workbook.close()
        cursor.close()
        self.cnx.close()

    # export data from tabels and pu them into sheets in the Excel workbook and save to file
    def executeMulti(self, excelFile, tables):
        # Create a workbook.
        workbook = xlsxwriter.Workbook(excelFile)
        for table in tables:
            self.getDBTableMetaData(table)

            self.connectToDB()
            cursor = self.cnx.cursor()
            #sqlString = "SELECT " + self.columnNames + " FROM " + self.database + "." + table
            sqlString = "SELECT * FROM " + self.database + ".`" + table + "`"
            #print(sqlString)

            cursor.execute(sqlString)
            sheetName = ""
            if table.startswith('2020CM春季-'):
                sheetName = table[9:]
            else:
                sheetName = table

            worksheet = workbook.add_worksheet(sheetName)

            row = 0
            col = 0
            for columnHeading in self.columnList:
                worksheet.write(row, col, columnHeading)
                col += 1

            for aRow in cursor:
                col = 0
                row += 1
                for aCell in aRow:
                    worksheet.write(row, col, aCell)
                    col += 1

            print('\n' + table + ' with ' + str(row) + ' rows is added to sheet ' + sheetName + ' in file ' + os.path.abspath(excelFile) )
        workbook.close()

        cursor.close()
        self.cnx.close()
        self.cnx = None
