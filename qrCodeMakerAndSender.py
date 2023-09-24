import qrcode
import csv
import yagmail
import os

masterStudentInfoCSV = "masterStudentInfo.csv"

masterListOfNamesAndIds = []
# read the master list of names and ids
with open(masterStudentInfoCSV, "r") as studentInfoCSV:
    reader = csv.reader(studentInfoCSV)
    rows = 0
    for row in reader:
        # append each row of info to the masterListOfNamesAndIds
        if row and rows > 0:
            masterListOfNamesAndIds.append(row)

        rows += 1

    for student in masterListOfNamesAndIds:
        id = str(student[1])
        email = student[11]

        code = qrcode.make(id)
        qrCodeString = "QRCode.png"
        code.save(qrCodeString)
        yag = yagmail.SMTP('INSERT EMAIL HERE', "INSERT PASSWORD HERE")
        yag.send(email, 'Attendance QRCode', contents="This is your attendance code to scan in",
                 attachments=qrCodeString)
        os.remove(qrCodeString)


