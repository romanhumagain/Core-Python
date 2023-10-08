import datetime

# # To get the current date and time 
# current_datetime = datetime.datetime.now()
# print(current_datetime) # e.g... 2023-10-08 09:37:09.182655

# # To create a specific date 
# d = datetime.date(2023, 10, 8)
# print(d)  # 2023-10-08

# #  To get the today date 
# date = datetime.date.today()
# print(date)

# # Creating a specific time 
# t = datetime.time(12, 45, 33)
# print(t)  # 12:45:33


# === Adding and subtracting the datetime 
now = datetime.datetime.now()
print(now)


# creating a time delta of 10 days
delta_time = datetime.timedelta(days=10)

# adding 10 days from today date 
date_in_future = now + delta_time
print("Date 10 days from today:", date_in_future)

# Subtracting 10 days from today
date_in_past = now - delta_time
print("Date 10 days ago:", date_in_past)






