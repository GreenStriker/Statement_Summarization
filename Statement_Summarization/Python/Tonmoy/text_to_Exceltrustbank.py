import xlwt
import os
from decimal import Decimal
Date = ""
valueDate=""
particular=""
withdrawal = 0.0
deposit = 0.0
Balance = 0.0

branch=""
time=""
dbbl2 = []


i=2

bb = 0.0
class dbbl:
    def __init__(self, Date, valueDate, particular, withdrawal, deposit, Balance, branch,time):
        self.Date = Date
        self.valueDate = valueDate
        self.particular = particular
        self.withdrawal = withdrawal
        self.deposit = deposit
        self.Balance = Balance
        self.branch = branch
        self.time = time

with open("Text file/dutch.txt", "r", encoding="utf-8") as f:


    for line in f:
        line = line.split(" ")
        len = line.__len__()
        # print(line[len-3])

        try:
            if (isinstance((Decimal(line[len-4])),Decimal)):
                 # print("h3")


                 if((Decimal(line[len-3]))> bb):
                     # print("h4")
                     deposit=Decimal(line[len-4])
                     count=len-5
                     # print(deposit)

                 else:
                    # print("h5")
                    withdrawal=Decimal(line[len-4])
                    count = len - 5


        except:
            # print("h6")
            deposit = 0
            withdrawal = 0
            count=len-4


        while (i <= count):
            particular = particular + line[i] + ' '
            i+=1

        #print(deposit)
        dbbl2.append(dbbl(line[0], line[1], particular, withdrawal, deposit, Decimal(line[len - 3]), line[len - 2], line[len - 1]))


        bb=Decimal(line[len - 3])
        deposit=0
        withdrawal=0
        particular = ""
        i=2


f.close()


print(dbbl2[0].Date)
print(dbbl2[1].Date)
print(dbbl2[2].Date)


# wb = xlwt.Workbook()
# ws = wb.add_sheet('DBBL Test Sheet')
#
# column_name = ["Date", "BRN", "Description", "Reference", "Debits", "Credits", "Balance"]
#
# heading = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',
#     num_format_str='#,##0.00')
#
# # Printing Column Name
# for x in range(7):
#     ws.write(0, x, column_name[x], heading)
#
# # Printing row data
# for y in range(dbbl2.__len__()):
#     ws.write(y + 1, 0, dbbl2[y].Date)
#     ws.write(y + 1, 1, dbbl2[y].BRN)
#     ws.write(y + 1, 2, dbbl2[y].Description)
#     ws.write(y + 1, 3, dbbl2[y].Reference)
#     ws.write(y + 1, 4, dbbl2[y].Debits)
#     ws.write(y + 1, 5, dbbl2[y].Credits)
#     ws.write(y + 1, 6, dbbl2[y].Balance)
#
# wb.save('example.xls')
#
# print("Text to Excel conversation is done!")
#


