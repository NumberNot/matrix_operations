import re
import numpy as np
import pandas as pd
from pathlib import Path
from PyQt5 import QtWidgets

#Uncomment next two lines for full numpy output
#import sys
#np.set_printoptions(threshold=sys.maxsize)

check_sum=0.0
content_list_clear = []

#Open file for reding block. Read it and clear artifacts 
my_file = open("профиль_тп_2.txt", "r")
content = my_file.read()
content_list_dirt = re.split(';|,|P48=',content)
my_file.close()

for item in content_list_dirt:
    try:
        int_value = float(item)
        check_sum+=int_value                #counter
    except ValueError:
        pass
    else:
        content_list_clear.append(float(item))
 
print(round(check_sum,3)) # print checksum

#Reshape block. Convert list to numpy array
try:
    arr = np.array(content_list_clear).reshape(31,48)
except ValueError:
    arr = np.array(content_list_clear).reshape(30,48)

arr=np.transpose(arr[:,0::2]+arr[:,1::2])

df = pd.DataFrame (arr)
filepath = 'my_excel_file.xlsx'

df.to_excel(filepath, index=False)

#text_file = open("sample.txt", "w")
#text_file.write(str(arr))
#text_file.close()

print(round(np.sum(arr),3))