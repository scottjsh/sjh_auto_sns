from .NeisAPI import NeisAPI
from utils.Date import *
import re
from .Exception import *
import traceback

class NeisLunchAPI(NeisAPI):
    NEIS_SERVICE_NAME = "mealServiceDietInfo"
    
    def __init__(self, lunch):
        self.__lunch = lunch    

    @classmethod
    def getTodayLunch(cls):
        todayLunch = (super(NeisLunchAPI, NeisLunchAPI)
                        .get(cls.NEIS_SERVICE_NAME, 
                             {"MLSV_YMD": getToday("%Y%m%d")})
                     )
        return cls(todayLunch)
    
    def format(self):
        try:
            rowData = self.__lunch["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
            formattedData = (re.sub(pattern=r'\([^)]*\)', repl="", string=rowData)
                             .replace(" ", "")
                            .split("<br/>"))
            return formattedData
        except:
            raise FormatException(traceback.format_exc())
        
        
        
    