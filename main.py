import win32clipboard
import time

while True:

    try:
        time.sleep(2)
        win32clipboard.OpenClipboard()
        Question = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        print(Question)
        file = open(r"\\Computer_Username\Users\Public\PROJECT CONNECT\clip.txt", "w+")
        file.write(Question)
        file.close()
    except:
        print("ERROR!!")
        pass