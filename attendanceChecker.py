import csv
import qrCodeReader


def checkAttendance(scanInDict, masterStudentInfoCSV):
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

    attendees = []
    absentees = []

    attendeeIDs = list(scanInDict.keys())
    for student in masterListOfNamesAndIds:
        id = student[1]
        studentCopy = student.copy()
        if id in attendeeIDs:
            studentScanIn = scanInDict[id]
            studentCopy.append(scanInDict[id])
            attendees.append(studentCopy)
        else:
            absentees.append(studentCopy)

    with open("attendees.csv", "w") as attendeesCSV:
        writer = csv.writer(attendeesCSV)
        writer.writerow(
            ["Section", "ID", "First Name", "Middle Name", "Last Name", "Grade Basis", "Level", "Major 1", "Major 2",
             "College", "Gender/ Pronoun", "Email Address", "Timestamp"])
        writer.writerows(attendees)

    with open("absentees.csv", "w") as attendeesCSV:
        writer = csv.writer(attendeesCSV)
        writer.writerow(
            ["Section", "ID", "First Name", "Middle Name", "Last Name", "Grade Basis", "Level", "Major 1", "Major 2",
             "College", "Gender/ Pronoun", "Email Address"])
        writer.writerows(absentees)


def main():
    masterStudentInfoCSVName = "masterStudentInfo.csv"
    scanInDict = qrCodeReader.qrCodeReader()
    checkAttendance(scanInDict, masterStudentInfoCSVName)


main()
