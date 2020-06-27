import cv2
import pyzbar.pyzbar as pyzbar

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print("Webcam on.....")

# Add the Identification number to this list of IDs
IDs = ["2018393", "2018394", "2018395"]
# Attendance corresponding to the IDs
attendance = [False]*len(IDs)
end = False

while True:
    _, frame = capture.read()
    decoded_image = pyzbar.decode(frame)
    for data in decoded_image:
        # frame, data to print, (pixels from left, pixels from top), font,font size , color, thickness
        cv2.putText(frame, str(data.data)[2:-1], (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

        if str(data.data)[2:-1] in IDs:
            attendance[IDs.index(str(data.data)[2:-1])] = True
        elif str(data.data)[2:-1] == "CLOSE":
            end = True

    cv2.imshow("Show QR Code", frame)

    if cv2.waitKey(1) and end:
        print(attendance)
        break

capture.release()
cv2.destroyAllWindows()
