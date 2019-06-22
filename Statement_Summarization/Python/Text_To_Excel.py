import xlwt
import os

directory_path = os.path.dirname(__file__)

Date = ""
BRN = "0"
Reference = "0"
Description = ""
Credits = 0
Debits = 0
Balance = 0
dbbl2 = []

class dbbl:
    def __init__(self, Date, BRN, Reference, Description, Credits, Debits, Balance):
        self.Date = Date
        self.BRN = BRN
        self.Reference = Reference
        self.Description = Description
        self.Credits = Credits
        self.Debits = Debits
        self.Balance = Balance

def Make_Excel(path):
    with open(path, "r", encoding="utf-8") as f:

        for line in f:
            line = line.split(" ")
            len = line.__len__()
            # print(line)

            try:
                if (isinstance((int(line[1])), int)):
                    BRN = line[1]
                    count = 2
            except:
                BRN = "0"
                count = 1

            while (count <= len - 4):
                try:
                    if (isinstance((int(line[count])), int)):
                        global Reference
                        Reference = Reference + line[count]
                        count = count + 1
                except:
                    global Description
                    Description = Description + line[count] + ' '
                    count = count + 1

            dbbl2.append(dbbl(line[0], BRN, Reference, Description, line[len - 3], line[len - 2], line[len - 1]))
            # dbbl2.append(dbbl(line[0], BRN, Reference, Description, int(line[len - 3]), int(line[len - 2]), int(line[len - 1])))
            Description = ""
            Reference = ""
            # if (re.match(r"([\d]{1,2}-(JAN|FEB|MAR|APR|MAY)-[\d]{2})", line)):
    f.close()

    wb = xlwt.Workbook()
    ws = wb.add_sheet('DBBL Test Sheet')

    column_name = ["Date", "BRN", "Description", "Reference", "Debits", "Credits", "Balance"]

    heading = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',
                          num_format_str='#,##0.00')

    # Printing Column Name
    for x in range(7):
        ws.write(0, x, column_name[x], heading)

    # Printing row data
    for y in range(dbbl2.__len__()):
        ws.write(y + 1, 0, dbbl2[y].Date)
        ws.write(y + 1, 1, dbbl2[y].BRN)
        ws.write(y + 1, 2, dbbl2[y].Description)
        ws.write(y + 1, 3, dbbl2[y].Reference)
        ws.write(y + 1, 5, dbbl2[y].Debits)
        ws.write(y + 1, 4, dbbl2[y].Credits)
        ws.write(y + 1, 6, dbbl2[y].Balance)

    wb.save(directory_path + '/example.xls')

    print("Text to Excel conversation is done!")

    # Opening the Excel File
    os.startfile(directory_path + '/example.xls')

# Make_Excel("C:/Statement/DBBL/Text file/dutch.txt")


