import cv2
import dropbox
import time
import random

startTime = time.time()

def take_snapshot():
    number = random.randint(0, 100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # reading frame while camera is on 
        ret, frame = videoCaptureObject.read()

        img_name = "img" + str(number) + ".jpg"
        cv2.imwrite(img_name, frame)

        startTime = time.time()
        result = False

    return img_name
    print("Snapshot is taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'sl.A7h1Rx2i4iJ8OCz_y-eg8D2GGJMWkS-EDqRrd-AAUQ6E28W2V9Ni4qBRltC0N09zmPY08zVILgi15LVPv0wJ3aRtZnT9bdA2ctHaL-N6IjttKnS2P9lqvtqBe8mhfNOfFCzD_ImBSZY'
    file = img_name
    file_from = file
    file_to = "/coding/"+ file_from

    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded successfully")

def main():
    while(True):
        if((time.time() - startTime) >= 5):
            name = take_snapshot()
            upload_file(name)

main()