# Calculate total trip expenditure
# to calculate hotel_cost-no of days of vacation
# plane ticket depends on the city
# calculate car rental-each day-discount
# expenditure

num_of_days_in_hotel = int(input('Number of days stayed in hotel'))
def hotel_cost():
  return num_of_days_in_hotel * 100
def car_rental():
  if num_of_days_in_hotel <15 and num_of_days_in_hotel >0:
    return num_of_days_in_hotel*40 -10
  elif num_of_days_in_hotel <30 and num_of_days_in_hotel >=15:
    return num_of_days_in_hotel*35 -20
  else :
    return num_of_days_in_hotel*30-40

def plane_ticket_cost(city):
  if city == 'Spain':
    return 600
  elif city == 'Iceland':
    return 1000
  else :
    print('Ticket not available to this destination')
    return 0

expenditure = float(input('Enter your expenditure: '))
city = input('Do you want to go to Spain or Iceland')
total_cost = expenditure + hotel_cost() + car_rental() + plane_ticket_cost(city)
print(total_cost)







from datetime import time,date,datetime

import calendar

current_day=date.today()
print(current_day)
print(current_day.month)
print(current_day.year)
print(current_day.day)
current_time=datetime.now()
print(current_time)






import random
from datetime import date
date1=date(2018,3,11)
date2=date(2023,9,16)
year_random=random.randint(date1.year,date2.year)
month_random=random.randint(date1.month,date2.month)
day_random=random.randint(date1.day,date2.day)
date3=date(year_random,month_random,day_random)