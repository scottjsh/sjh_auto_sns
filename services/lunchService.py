from neis.NeisLunchAPI import NeisLunchAPI
from neis.Exception import *
from image.Image import *
from sns.Instagram import Instagram
from utils.Date import *
from dotenv import load_dotenv
import os

load_dotenv()

def addDateToImage(image: Image):
    textVO = TextVO(getToday("%m월 %d일 %w요일"), 
                "static/font/esamanruBold.ttf", 
                100)
    image.addTextAlignX(textVO, 150)
    
def addMenuToImage(image: Image, lunch):
    currentPosY = 600
    LEADING = 120
    for menu in lunch:
        if (len(menu) > 10):
            menu = menu.split("&")
        else:
            menu = menu.split()
    
        for idx, dividedMenu in enumerate(menu):
            textVO = TextVO(f"{'-  ' if idx == 0 else '    &'}{dividedMenu}", 
                            "static/font/esamanruMedium.ttf", 84)
            posVO = PosVO(125, currentPosY)
            image.addText(textVO, posVO)
            currentPosY += LEADING

def execute():
    try:
        # get today lunch
        todayLunch = NeisLunchAPI.getTodayLunch().format()

        # create today lunch image using templat lunch image
        todayLunchImage = Image("static/template_image/lunch_bg.png")
        addDateToImage(todayLunchImage)
        addMenuToImage(todayLunchImage, todayLunch)
        todayLunchImage.save("upload_image/lunch", "today_lunch")
        
        # upload today lunch image to story
        instagramClient = Instagram(os.getenv("SNS_INSTAGRAM_USER"), 
                                    os.getenv("SNS_INSTAGRAM_PW"))
        instagramClient.uploadPhotoToStory("upload_image/lunch/today_lunch.jpg")
        
    except FormatException as e:
        print(f"NeisLunchAPI > FormatException : {e}\n")