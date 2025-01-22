from datetime import datetime
from datetime import timedelta
day = datetime.fromisoformat('1999-08-01 11:12:12')

day_2 = datetime.fromisoformat('1992-08-01 11:12:12')

result = abs(day - day_2)

print(result)

days = result.days
print(days)