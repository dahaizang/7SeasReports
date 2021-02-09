import report

def main():
    aReport = report.report()
    aReport.execute(reportName = "0VerView", table = "0VerView", excelFile = "./0VerView.xlsx")
    aReport.execute(reportName = "2019v1Member", table = "2019v1Member", excelFile = "./2019v1Member.xlsx")
    aReport.execute(reportName = "2019v1MemberClass", table="2019v1MemberClass", excelFile = "./2019v1MemberClass.xlsx")
    aReport.execute(reportName = "2019v1MemberClassCount", table="2019v1MemberClassCount", excelFile = "./2019v1MemberClassCount.xlsx")
    aReport.execute(reportName="2019v1RegisteredWaitingPayment", table="2019v1RegisteredWaitingPayment",
                    excelFile="./2019v1RegisteredWaitingPayment.xlsx")
    aReport.execute(reportName = "2019v1UserClassSelection", table="2019v1UserClassSelection", excelFile = "./2019v1UserClassSelection.xlsx")
    aReport.execute(reportName = "2019v1UserClassCount", table = "2019v1UserClassCount", excelFile = "./2019v1UserClassCount.xlsx")
    aReport.execute(reportName="2019v1AllClassSelection", table="2019v1AllClassSelection",
                    excelFile="./2019v1AllClassSelection.xlsx")

    aReport.execute(reportName="v1Donations", table="v1Donations",
                excelFile="./v1Donations.xlsx")

if __name__ == "__main__":
    main()
