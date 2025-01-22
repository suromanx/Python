from datetime import datetime
day = datetime.fromisoformat('1999-08-01 11:12:12')
today = datetime.today()

result = abs(today-day)
print(result)