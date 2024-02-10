import report
import os
from datetime import datetime


def main():
    Reports2024Spring()

def Reports2024Spring():
    now = datetime.now()

    print("now =", now)
    dt_string = now.strftime("%m%d%H%M")
    print("date and time =", dt_string)

    aReport = report.report()
    if not os.path.isdir("2024"):
        os.mkdir("2024")

    excel_filename = "2024/2024全体会员." + dt_string + ".xlsx"
    aReport.execute(table="v2024Member", excelFile=excel_filename)
    excel_filename = "2024/2024春季选课." + dt_string + ".xlsx"
    aReport.execute(table="v2024SpringClass", excelFile=excel_filename)


#    excel_filename = "2023/v2023MemberEx." + dt_string + ".xlsx"
#    aReport.execute(table = "v2023MemberEx", excelFile = excel_filename)

#    aReport.execute(table="vwUserInfo", excelFile = "./UserInfo.xlsx")
# return
def Reports2023Fall():

    now = datetime.now()

    print("now =", now)
    dt_string = now.strftime("%m%d%H%M")
    print("date and time =", dt_string)

    aReport = report.report()
    if not os.path.isdir("2023"):
        os.mkdir("2023")

    excel_filename = "2023/2023全体会员." + dt_string + ".xlsx"
    aReport.execute(table = "v2023Member", excelFile = excel_filename)
    excel_filename = "2023/2023秋季选课." + dt_string + ".xlsx"
    aReport.execute(table = "v2023FallClass", excelFile = excel_filename)
#    excel_filename = "2023/v2023MemberEx." + dt_string + ".xlsx"
#    aReport.execute(table = "v2023MemberEx", excelFile = excel_filename)

#    aReport.execute(table="vwUserInfo", excelFile = "./UserInfo.xlsx")
    #return

def Reports2023Spring():

    now = datetime.now()

    print("now =", now)
    dt_string = now.strftime("%m%d%H%M")
    print("date and time =", dt_string)

    aReport = report.report()
    if not os.path.isdir("2023"):
        os.mkdir("2023")

    excel_filename = "2023/2023全体会员." + dt_string + ".xlsx"
    aReport.execute(table = "v2023Member", excelFile = excel_filename)
    excel_filename = "2023/2023春季选课." + dt_string + ".xlsx"
    aReport.execute(table = "v2023SpringClass", excelFile = excel_filename)
#    excel_filename = "2023/v2023MemberEx." + dt_string + ".xlsx"
#    aReport.execute(table = "v2023MemberEx", excelFile = excel_filename)

#    aReport.execute(table="vwUserInfo", excelFile = "./UserInfo.xlsx")
    #return


def Reports2021Spring():
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

    excel_filename = "2021全体会员." + dt_string + ".xlsx"
    aReport.execute(table = "2021AllMembers", excelFile = excel_filename)
    aReport.execute(table="vwUserInfo", excelFile = "./UserInfo.xlsx")
    #return

    tables= ["2021CMemberClass",
        "2021CM春季-楷书班-九成宫",
        "2021CM春季-隶书班",
        "2021CM春季-楷书班-赵孟頫",
        "2021CM春季-行草班-二王尺牍",
        "2021CM春季-行草班-二王尺牍（旁听）",
        "2021CM春季-小楷班",
        "2021CM春季-诗词班",
        "2021CM春季-篆刻班",
        "2021CM春季-硬笔班",
        "2021CM春季-软硬班-跋保母",
        "2021CM春季-兰亭互助班",
        "2021CM春季-多宝塔互助班",
        "2021CM春季-书法与艺术研讨班"
        ]

    excel_filename = "2021春季各班选课." + dt_string + ".xlsx"
    aReport.executeMulti(excelFile = excel_filename, tables=tables)


def Reports2020Fall():
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
    aReport.execute(table="vwUserInfo", excelFile = "./UserInfo.xlsx")
    #aReport.execute(table="2020FMemberClass", excelFile = "./2020FMemberClass." + dt_string + ".xlsx")

    tables= ["2020FMemberClass",
        "2020FM秋季-楷书班",
        "2020FM秋季-隶书班",
        "2020FM秋季-楷书班-赵孟頫",
        "2020FM秋季-集王圣教序",
        "2020FM秋季-兰亭集序",
        "2020FM秋季-行草班-文徵明",
        "2020FM秋季-行草班-文徵明（旁听）",
        "2020FM秋季-小楷班",
        "2020FM秋季-篆书班",
        "2020FM秋季-篆刻班",
        "2020FM秋季-硬笔班",
        "2020FM秋季-软硬班-跋保母",
        "2020FM秋季-章草兴趣班"
        ]

    excel_filename = "2020秋季各班选课." + dt_string + ".xlsx"
    aReport.executeMulti(excelFile = excel_filename, tables=tables)

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
    aReport.execute(table="vwUserInfo", excelFile = "./UserInfo.xlsx")
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
