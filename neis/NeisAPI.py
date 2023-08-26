from abc import abstractclassmethod, ABC
from dotenv import load_dotenv
import os;
import requests

load_dotenv()

class NeisAPI(ABC):
    @staticmethod
    def get(service, queryParams: dict):
        BASE_URL = ("https://open.neis.go.kr/hub" +
                    f"/{service}?" +
                    f"KEY={os.getenv('NEIS_API_KEY')}" +
                    "&Type=json" +
                    "&ATPT_OFCDC_SC_CODE=H10" +
                    "&SD_SCHUL_CODE=7480072")
    
        strParams = ""
        for param in queryParams:
            strParams += f"&{param}={queryParams[param]}"
        return requests.get(BASE_URL + strParams).json()
        
    @abstractclassmethod
    def format(self):
        pass
        