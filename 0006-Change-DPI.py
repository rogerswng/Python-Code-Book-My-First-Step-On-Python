from PIL import Image
import os

class Change_DPI:
    def __init__(self):
        self.path = None

    def setPath(self, path):
        self.path = path
        return True

    def setDPI(self, x, y):
        self.x_DPI = x
        self.y_DPI = y
        return True
    
    def changeDPI(self):
        files = os.listdir(self.path)
        is_exist = False
        for img in files:
            if img.endswith((".jpg", ".png")):
                is_exist = True
                img_path = os.path.join(self.path, img)
                im = Image.open(img_path)
                x, y = im.size
                print("origin img size: {0}*{1}".format(x, y))
                if x > self.x_DPI:
                    x_resize = self.x_DPI
                    y_resize = int(y*(self.x_DPI/x))
                    f_resize = im.resize((x_resize, y_resize))
                    f_resize.save(img_path)
                    continue
                if y > self.x_DPI:
                    y_resize = self.y_DPI
                    x_resize = int(x*(self.y_DPI/y))
                    f_resize = im.resize((x_resize, y_resize), Image.ANTIALIAS)
                    f_resize.save(img_path)
                    continue
        if is_exist == False:
            print("No imgs found under current path")

#FOLLOWING TESTS
test = Change_DPI()
test.setPath("C:\Users\Rogers\Desktop\Python")
test.setDPI(1136, 640)
test.changeDPI()
