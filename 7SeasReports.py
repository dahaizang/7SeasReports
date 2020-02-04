import report
import os
from datetime import datetime


def main():
    Reports2020()

def Reports2020():
    #aReport.execute(table = "2020Membership")
    #aReport.execute(table = "2020MembershipFromChina")
    # datetime object containing current date and time
    now = datetime.now()

    print("now =", now)
    dt_string = now.strftime("%m%d%H%M")
    print("date and time =", dt_string)

    aReport = report.report()
    #if not os.path.isdir("reports"):
    #    os.mkdir("reports")

    excel_filename = "2020全体会员." + dt_string + ".xlsx"
    aReport.execute(table = "2020AllMembers", excelFile = excel_filename)
    #aReport.execute(table="2020CMemberClass")
    tables= ["2020CMemberClass",
             "2020CM春季-楷书班-九成宫",
             "2020CM春季-小楷班-灵飞经",
             "2020CM春季-行书班-赵孟頫",
             "2020CM春季-隶书班",
             "2020CM春季-隶书班-曹全碑",
             "2020CM春季-行草班-米芾",
             "2020CM春季-楷书班-赵孟頫",
             "2020CM春季-硬笔班",
             "2020CM春季-小楷班",
             "2020CM春季-篆刻班",
             "2020CM春季-篆书班-石鼓文",
             "2020CM春季-楷书班-多宝塔"
             ]

    excel_filename = "2020春季各班选课." + dt_string + ".xlsx"
    aReport.executeMulti(excelFile = excel_filename, tables=tables)

def Reports2019():
    aReport = report.report()
    aReport.execute(reportName = "2019v1Member", table = "2019v1Member", excelFile = "./2019v1Member.xlsx")
    aReport.execute(reportName="2019v1RegisteredWaitingPayment", table="2019v1RegisteredWaitingPayment", excelFile="./2019v1RegisteredWaitingPayment.xlsx")
    #aReport.execute(reportName = "2019v1UserClassSelection", table="2019v1UserClassSelection", excelFile = "./2019v1UserClassSelection.xlsx")
    #aReport.execute(reportName = "2019v1MemberClass", table="2019v1MemberClass", excelFile = "./2019v1MemberClass.xlsx")
    #aReport.execute(reportName = "2019v1MemberClassCount", table="2019v1MemberClassCount", excelFile = "./2019v1MemberClassCount.xlsx")
    aReport.execute(reportName="2019v1AllClassSelection", table="2019v1AllClassSelection",
                    excelFile="./2019v1AllClassSelection.xlsx")
    #aReport.execute(reportName = "2019v1UserClassCount", table = "2019v1UserClassCount", excelFile = "./2019v1UserClassCount.xlsx")

    #aReport.execute(reportName = "Non-Member /w Class", table="vwOnlineClassNonMember", excelFile = "./OnlineClassNonMember.xlsx")
    #aReport.execute(reportName = "Orders", table="vwOrder", excelFile = "./Orders.xlsx")
    #aReport.execute(reportName = "Order Items", table="vwOrderItem", excelFile = "./OrderItems.xlsx")
    #aReport.execute(reportName = "Products", table="vwProduct", excelFile = "./Products.xlsx")
    #aReport.execute(reportName = "User Info", table="vwUserInfo", excelFile = "./UserInfo.xlsx")
    #aReport.execute(reportName = "Donations", table="vwDonations", excelFile = "./Donations.xlsx")



if __name__ == "__main__":
    main()
