from PIL import Image as PillowImage, ImageDraw as PillowImageDraw, ImageFont as PillowImageFont

class TextVO:
    def __init__(self, value, fontPath, size, color = "black"):
        self.__value = value
        self.__fontPath = fontPath
        self.__size = size
        self.__color = color
        
    def getValue(self):
        return self.__value
        
    def getFontPath(self):
        return self.__fontPath
    
    def getSize(self):
        return self.__size
    
    def getColor(self):
        return self.__color

class PosVO:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y   

class Image:
    def __init__(self, path):
        self.image = PillowImage.open(path)
        
    def addText(self, textVO: TextVO, posVO: PosVO):
        selectedFont = self.__getFont(textVO.getFontPath(), textVO.getSize())
        imageDraw = self.__getImageDraw(self.image)
        self.__draw(imageDraw, textVO, posVO, selectedFont)
        return self
    
    def addTextAlignX(self, textVO: TextVO, posY: int):
        selectedFont = self.__getFont(textVO.getFontPath(), textVO.getSize())
        imageDraw = self.__getImageDraw(self.image)
        centerPosX = (self.image.width - selectedFont.getlength(textVO.getValue())) / 2
        self.__draw(imageDraw, textVO, PosVO(centerPosX, posY), selectedFont)
        return self
        
    def save(self, path, fileName):
        self.image = self.image.convert("RGB")
        self.image.save(f"{path}/{fileName}.jpg", "JPEG")
        
    def __getFont(self, fontPath: str, size: int):
        return PillowImageFont.truetype(fontPath, size)
    
    def __getImageDraw(self, image):
        return PillowImageDraw.Draw(image)
    
    def __draw(self, imageDraw, textVO: TextVO, posVO: PosVO, font):
        imageDraw.text((posVO.getX(), posVO.getY()), textVO.getValue(), fill=textVO.getColor(), font=font, align='center')
