import cv2
import pandas as pd
import numpy as np


def qrCodeReader():
    qrCodeDet = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 300)

    qrCodeIDList = []
    timestampList = []

    while True:
        camOn, frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)
        hasQRCode, qrCodeInfo, corners, qrCodeArray = qrCodeDet.detectAndDecodeMulti(frame)

        if hasQRCode and corners is not None and qrCodeInfo[0] != "":
            frame = cv2.polylines(frame, corners.astype(np.int32), True, (0, 255, 0), thickness=20)

            timeNow = pd.to_datetime("now", format="%m-%d-%Y %H:%M:%S")
            timeNowFormatted = timeNow.strftime("%m-%d-%Y %H:%M:%S")
            timeNowFormatted = pd.to_datetime(timeNowFormatted, format="%m-%d-%Y %H:%M:%S")

            idNum = qrCodeInfo[0]

            if idNum not in qrCodeIDList and idNum is not None:
                qrCodeIDList.append(idNum)
                timestampList.append(timeNowFormatted)

        cv2.imshow("webcam", frame)

        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyWindow("webcam")

    scanInDict = {ID: timestamp for ID, timestamp in zip(qrCodeIDList, timestampList)}

    return scanInDict
