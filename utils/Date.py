from datetime import datetime

def getToday(format: str):
    rowDate = datetime.today()
    
    # formatting
    format = format.replace("%Y", rowDate.strftime("%Y"))
    format = format.replace("%m", rowDate.strftime("%m").replace("0", ""))
    format = format.replace("%d", rowDate.strftime("%d"))
    dayOfWeekTable = ["월", "화", "수", "목", "금", "토", "일"]
    format = format.replace("%w", dayOfWeekTable[rowDate.weekday()])
    
    return format