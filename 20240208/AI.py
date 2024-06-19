import os  
from datetime import datetime   
import glob 
import time
import shutil

now = datetime.now()
datetime_1 = now.strftime("%Y%M%d%H%M%S")
print("datetime=", datetime_1[0])
print(datetime_1)
filelist = glob.glob("C:\\Study\\backup\\*.png")
print(filelist)
filename = 0
count = 0
while True:
    now = datetime.now()
    daye = now.strftime("%Y")
    damo = now.strftime("%m")
    dady = now.strftime("%d")
    daho = now.strftime("%H")
    dami = now.strftime("%M")
    print(dami)
    os.makedirs("C:\\Study\\backup\\" + daye + "\\" + damo + "\\" + dady + "\\" + daho + "\\" + dami, exist_ok=True)
    mk = "C:\\Study\\backup\\" + daye + "\\" + damo + "\\" + dady + "\\" + daho + "\\" + dami + "\\"
    for i in filelist:        
        os.rename(i, mk + dami + '.png')
        time.sleep(70)
        j = i 
        i = os.path.basename(i)
        if i == dami + '1':    
            shutil.move(j, mk + str(filename) + ".png")
            break
        filename += 1
        count += 1
        









