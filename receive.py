import win32clipboard
import time

while True:

    try:
        file = open(r"\\Computer_Username\Users\Public\PROJECT CONNECT\clip.txt", "r+")

        val = file.readlines()

        ans = ""

        for i in val:
            ans += i

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(ans)
        win32clipboard.CloseClipboard()
    except:
        print("ERROR ENCOUNTERED!!!")
        time.sleep(2)
        pass
