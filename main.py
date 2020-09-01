import re
import sys
import design

import numpy as np
import pandas as pd
from pathlib import Path
from PyQt5 import QtWidgets

#Uncomment next two lines for full numpy output
#import sys
#np.set_printoptions(threshold=sys.maxsize)


content_list_clear = []

class TransmuteApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Button_pick_file.clicked.connect(self.browse_file)
        self.Button_check.clicked.connect(self.check_file)

    def browse_file(self):
        global pick_file
        pick_file = QtWidgets.QFileDialog.getOpenFileName(self, "Choose file")
        if pick_file:
#            self.line_file_pick.setText(Path(pick_file[0]).name)
            self.line_file_pick.setText(pick_file[0])        # Uncomment if you need full path to the file
#            tail = os.path.split(pick_file[0])         # Uncomment if you need get  part of path
#            self.lineFile.setText(tail[1])             # 
#            sfile__ = self.line_file_pick.text()

    def check_file(self):
        sfile__=open(self.line_file_pick.text(), "r")


#Open file for reding block. Read it and clear artifacts 
#my_file = open("профиль_тп_2.txt", "r")

        content = sfile__.read()
        content_list_dirt = re.split(';|,|P48=',content)
        sfile__.close()
        
        check_sum=0.0
        
        for item in content_list_dirt:
            try:
                int_value = float(item)
                check_sum+=int_value                #counter
            except ValueError:
                pass
            else:
                content_list_clear.append(float(item))
        self.l_check_before_result.setText(str(round(check_sum,3))) # print checksum
        

#Reshape block. Convert list to numpy array
#try:
#    arr = np.array(content_list_clear).reshape(31,48)
#except ValueError:
#    arr = np.array(content_list_clear).reshape(30,48)

#arr=np.transpose(arr[:,0::2]+arr[:,1::2])

#df = pd.DataFrame (arr)
#filepath = 'my_excel_file.xlsx'

#df.to_excel(filepath, index=False)

##text_file = open("sample.txt", "w")
##text_file.write(str(arr))
##text_file.close()

#print(round(np.sum(arr),3))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TransmuteApp() 
    window.show()
    app.exec_() 

if __name__ == '__main__': 
    main()