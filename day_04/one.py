import calendar
import panda as pd
cal = calendar.month(2022, 9)
print("Here is the calendar:")
print(cal)


df = pd.read_csv('data.csv')
print(df.to_string())