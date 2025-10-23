from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Time:",formatted_time)

even_date = datetime(2025,12,25,9,0,0)
# formatted_time = even_date.strftime("%m-%d-%Y %H:%M:%S")\
curreent_time = datetime.now()
time_difference = even_date - curreent_time
# print("Formatted Time:",formatted_time)
print("Days Reaining:",time_difference)
