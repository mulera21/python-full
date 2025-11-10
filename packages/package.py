#package

import os

path = r"C:\Users\admin\OneDrive\Desktop\stick man"

#check if path exists
if os.path.exists(path):
    print("The specified path exists.")
else:
    print("The specified path does not exist.")

