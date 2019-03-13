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
    columnList = []
    columnNames = ""
    reportFile = None
    cnx = None

    configJsonFile = 'config.json'

    def __init__(self):
        with open(self.configJsonFile) as json_file:
            self.data = json.load(json_file)
            self.user = self.data['user']
            self.password = self.data['password']
            self.host = self.data['host']
            self.port = self.data['port']
            self.database = self.data['database']

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
                self.columnNames = columnName[0]
            else:
                self.columnNames += "," + columnName[0]


    def execute(self, reportName, table, excelFile):
        self.getDBTableMetaData(table)

        self.connectToDB()
        cursor = self.cnx.cursor()
        sqlString = "SELECT " + self.columnNames + " FROM " + self.database + "." + table
        # print(sqlString)

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

def main():
    aReport = report()

    aReport.execute(reportName = "Customers", table = "vwCustomer", excelFile = "./Customers.xlsx")
    aReport.execute(reportName = "Order Status", table="vwOrderStatus", excelFile = "./OrderStatus.xlsx")
    aReport.execute(reportName = "Membership", table="vwMembership", excelFile = "./Membership.xlsx")
    aReport.execute(reportName = "Members /w Class", table="vwMembershipAndClass", excelFile = "./MembershipAndClass.xlsx")
    aReport.execute(reportName = "Non-Member /w Class", table="vwOnlineClassNonMember", excelFile = "./OnlineClassNonMember.xlsx")
    aReport.execute(reportName = "Orders", table="vwOrder", excelFile = "./Orders.xlsx")
    aReport.execute(reportName = "Order Items", table="vwOrderItem", excelFile = "./OrderItems.xlsx")
    #aReport.execute(reportName = "Order Products", table="vwOrderProduct", excelFile = "./OrderProducts.xlsx")
    aReport.execute(reportName = "Products", table="vwProduct", excelFile = "./Products.xlsx")
    # aReport.execute(reportName = "Paid Members", table="vwRegisterAndPaidFor7SeasMembership", excelFile = "./RegisterAndPaidFor7SeasMembership.xlsx")
    aReport.execute(reportName = "User Info", table="vwUserInfo", excelFile = "./UserInfo.xlsx")
    aReport.execute(reportName = "Donations", table="vwDonations", excelFile = "./Donations.xlsx")


if __name__ == "__main__":
    main()
