import report

def main():
    aReport = report.report()

    aReport.execute(reportName = "2019v1Member", table = "2019v1Member", excelFile = "./2019v1Member.xlsx")
    aReport.execute(reportName="2019v1RegisteredWaitingPayment", table="2019v1RegisteredWaitingPayment", excelFile="./2019v1RegisteredWaitingPayment.xlsx")
    aReport.execute(reportName = "2019v1UserClassSelection", table="2019v1UserClassSelection", excelFile = "./2019v1UserClassSelection.xlsx")
    aReport.execute(reportName = "2019v1MemberClass", table="2019v1MemberClass", excelFile = "./2019v1MemberClass.xlsx")
    aReport.execute(reportName = "2019v1MemberClassCount", table="2019v1MemberClassCount", excelFile = "./2019v1MemberClassCount.xlsx")

    #aReport.execute(reportName = "Non-Member /w Class", table="vwOnlineClassNonMember", excelFile = "./OnlineClassNonMember.xlsx")
    #aReport.execute(reportName = "Orders", table="vwOrder", excelFile = "./Orders.xlsx")
    #aReport.execute(reportName = "Order Items", table="vwOrderItem", excelFile = "./OrderItems.xlsx")
    #aReport.execute(reportName = "Products", table="vwProduct", excelFile = "./Products.xlsx")
    #aReport.execute(reportName = "User Info", table="vwUserInfo", excelFile = "./UserInfo.xlsx")
    #aReport.execute(reportName = "Donations", table="vwDonations", excelFile = "./Donations.xlsx")



if __name__ == "__main__":
    main()
