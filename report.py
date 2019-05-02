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


    def execute(self, reportName, table, excelFile):
        self.getDBTableMetaData(table)

        self.connectToDB()
        cursor = self.cnx.cursor()
        #sqlString = "SELECT " + self.columnNames + " FROM " + self.database + "." + table
        sqlString = "SELECT * FROM " + self.database + "." + table
        print(sqlString)

        cursor.execute(sqlString)

        # Create a workbook and add a worksheet.
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

        print('\n' + reportName + ' Report is saved in file:\n' + os.path.abspath(excelFile))
        workbook.close()

        cursor.close()
        self.cnx.close()
        self.cnx = None
