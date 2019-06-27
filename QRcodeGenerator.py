# Created by Selva
# Made with ❤️ by Selva
import pyqrcode 
from pyqrcode import *

"""Python script to create qr code images for my friend.
    Libraries needed: pyqrcode & pypng """

for i in range(1,140):
    s = "https://selvasoft.in?i=" + str(i)
    url = pyqrcode.create(s) 
    url.png(str(i)+".png", scale = 8) 
