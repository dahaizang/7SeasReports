# -*- coding: utf-8 -*-

import xlrd
import report

class ExcelToMySQL :
    def execute(self, table, excelFile):
        r = report.report()
        r.connectToDB()
        r.getDBTableMetaData(table)
#        r.loadExcelToMySQL("non_website_orders", "importExcel.xlsx")
        # Open the workbook and define the worksheet
        book = xlrd.open_workbook("importExcel.xlsx")

        #sheet = book.sheet_by_name("Client_Data")
        sheet = book.sheet_by_index(0)

        # Establish a MySQL Connection
        cnx = r.cnx

        # Get the cursor, which is used to traverse the database, line by line
        cursor = cnx.cursor()

        # Create the INSERT INTO sql query
        query = """
        INSERT
        INTO
        e7se41220768516.non_website_orders
        (sequence,
         wechat_nickname,
         name,
         username,
         email,
         payment_amount,
         payment_method,
         date_paid,
         country,
         city,
         remark)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Create a for loop to iterate through each row in the xls file, starting from row 2
        for r in range(1, sheet.nrows):
            sequence = sheet.cell(r, 0).value
            wechat_nickname = sheet.cell(r, 1).value
            name = sheet.cell(r, 2).value
            username = sheet.cell(r, 3).value
            email = sheet.cell(r, 4).value
            payment_amount = sheet.cell(r, 5).value
            payment_method = sheet.cell(r, 6).value
            date_paid = sheet.cell(r, 7).value
            country = sheet.cell(r, 8).value
            city = sheet.cell(r, 9).value
            remark = sheet.cell(r, 10).value

            values = (sequence,
            wechat_nickname,
            name,
            username,
            email,
            payment_amount,
            payment_method,
            date_paid,
            country,
            city,
            remark)

            # Execute sql query
            cursor.execute(query, values)
            cnx.commit()

        # Close the cursor
        cursor.close()

        # Commit the transaction
        cnx.commit()

        # Print results
        print("Data imported successfully")
        columns = str(sheet.ncols)
        rows = str(sheet.nrows)

def main():
    loader = ExcelToMySQL()
    loader.execute("non_website_orders", "importExcel.xlsx")

if __name__ == "__main__":
    main()
