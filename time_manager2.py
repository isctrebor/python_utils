import time
import datetime
from datetime import datetime as dt
from calendar import monthrange
class time_manager():
	def __init__(self):
		self.time_var = dt.now()
		self.util_time = dt
		self.format_date = "%Y-%m-%d"
		self.format_time = "%H:%M:%S"
		self.zero_complete = 3
		self.date = None
		self.date2 = None
		self.time = None
		self.timestamp = None
		self.julian = None

	def get_date_str(self):
		self.the_date = self.time_var.strftime(self.format_date)
		return self.the_date

	def get_date2_str(self):
		yy = datetime.datetime.today().strftime('%Y')
		mm = datetime.datetime.today().strftime('%m')
		dd = datetime.datetime.today().strftime('%d')
		yy2 = int(yy[2:4])
		self.date2 = str(yy2)+str(mm)+str(dd)
		return self.date2

	def get_time_str(self):
		self.time = str(self.time_var.strftime(self.format_time))
		return self.time

	def get_timestamp(self):
		self.timestamp = str(self.time_var.strftime(self.format_date +" "+self.format_time))
		return self.timestamp

	def get_julian(self):
		self.the_date = self.time_var.strftime(self.format_date)
		dt = datetime.datetime.strptime(self.the_date,self.format_date)
		tt = dt.timetuple()
		response = tt.tm_yday
		to_str = str(response)
		self.julian = to_str.zfill(self.zero_complete)
		return self.julian

	def return_week_interval(self,year,month,init,end):
		date_start = str(year)+"-"+str(month)+"-"+str(init)+" 00:00:00"
		date_end = str(year)+"-"+str(month)+"-"+str(end)+" 00:00:00"

		datetime_object1 = self.util_time.strptime(date_start, '%Y-%m-%d %H:%M:%S')
		datetime_object2 = self.util_time.strptime(date_end, '%Y-%m-%d %H:%M:%S')
		date_week_start = datetime_object1.isocalendar()[1]
		date_week_end = datetime_object2.isocalendar()[1]

		return {"start":date_week_start,"end":date_week_end}

	def get_number_days_month(self,year,month):
		total_days = monthrange(year, month)

		return total_days[1]



"""
object_time = time_manager() #instance object
date_str = object_time.get_date_str() # date YYYY-MM-DD Format
date_str2 = object_time.get_date2_str() # date YYMMDD Format
date_str3 = object_time.get_time_str() # time HH:MM:SS Format
date_str4 = object_time.get_timestamp() # timestamp YYYY-MM-DD HH:MM:SS Format 
date_str5 = object_time.get_julian() # Julian day 3 Filled zero
date_str6 = object_time.return_week_interval(2025,2,1,28)#Week Interval Number Year/month/start_day/end_day
date_str7 = object_time.get_number_days_month(2025,4)
print(date_str)
print(date_str2)
print(date_str3)
print(date_str4)
print(date_str5)
print(date_str6)
print(date_str7)
"""
