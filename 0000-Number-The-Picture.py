from PIL import Image, ImageDraw, ImageFont

class ImageToBeNumbered:
  def __init__(self):
    self.fnt = None
    self.ima = None
  def openFile(self, path):
    self.ima = Image.open(path)
    return True
  
  def setFont(self, font_path, font_size):
    self.fnt = ImageFont.truetype(font_path, font_size)
    return True
  def drawTheNumber(self, ):
    draw = ImageDraw.Draw(self.ima)
    draw.text(position, str, fill = color, font = self.cnt)
    self.im.save(str+"Numbered"+".jpg")
    self.im.show()
    return True
    
#FOLLOWING TEST
test = ImageToBeNumbered()
test.open("test.jpg")
test.setFont("xxx.ttf", 80) 
#IN WINDOWS HERE THROWS AN ERROR, A FULL PATH IS TO BE PROVIDED HERE eg. test.setFont("C:/Windows/Fonts/Candara.ttf", 80)
test.drawTheNumber((150, -10), "4", (255, 0, 0), test.fnt)
