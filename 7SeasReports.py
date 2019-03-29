import report

def main():
    aReport = report.report()

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
