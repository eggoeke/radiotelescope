import calendar
import sys


def renderCal(m, y, equip):
	global month
	global nextmonth
	global nextyear
	global prevyear
	global prevmonth
	global year
	month = int(m)
	year = int(y)
	calendar.setfirstweekday(calendar.SUNDAY)
	temp = 0
	tempmonth = 1;
	if(month < 1):
		global month
		tempmonth = month - 12
		temp = int(tempmonth/12)
		month = month - 12*temp
	elif(month%12 == 0):
		global month
		temp = int((month-1)/12)
		month = month - 12*temp
	elif(month > 12):
		global month
		temp = int(month/12)
		month = month - 12*temp

	year = year + temp
	nextmonth = month + 1

	if(nextmonth<12 and nextmonth>0):
		temp = 0
	elif(nextmonth%12 == 0):
		global nextmonth
		temp = int((nextmonth-1)/12)
		nextmonth = nextmonth - 12*temp
	elif(nextmonth>12):
		global nextmonth
		temp = int(nextmonth/12)
		nextmonth = nextmonth - 12*temp
	elif(nextmonth < 1):
		global nextmonth
		tempmonth = nextmonth - 12
		temp = int(tempmonth/12)
		nextmonth = nextmonth - 12*temp

	nextyear = year+temp

	prevmonth = month - 1

	if(prevmonth<12 and prevmonth>0):
		temp = 0
	elif(prevmonth%12 == 0):
		global prevmonth
		temp = int((prevmonth-1)/12)
		prevmonth = prevmonth - 12*temp
	elif(prevmonth>12):
		global prevmonth
		temp = int(prevmonth/12)
		prevmonth = prevmonth - 12*temp
	elif(prevmonth < 1):
		global prevmonth
		tempmonth = prevmonth - 12
		temp = int(tempmonth/12)
		prevmonth = prevmonth - 12*temp

	prevyear = int(year+temp)



	year = year + temp
	mat = calendar.monthcalendar(year, month)
	render = open("app/templates/renderCal.html", 'w')
	str1 = ('{% extends "calendar.html" %}{% block calendar %}')
	if(equip == "ashtarut"):
		str1 = str1+'    <h2> Ashtarut |<a href="/schedule/'+str(month)+'/'+str(year)+'/astarte"> Astarte</a> | <a href="/schedule/'+str(month)+'/'+str(year)+'/spectrometer">Spectrometer</a></h2><p><br>'
	elif(equip == "astarte"):
		str1 = str1+'    <h2><a href="/schedule/'+str(month)+'/'+str(year)+'/ashtarut">Ashtarut</a> | Astarte | <a href="/schedule/'+str(month)+'/'+str(year)+'/spectrometer">Spectrometer</a></h2><p><br>'
	elif(equip == "spectrometer"):
		str1 = str1+'    <h2><a href="/schedule/'+str(month)+'/'+str(year)+'/ashtarut">Ashtarut</a> | <a href="/schedule/'+str(month)+'/'+str(year)+'/astarte">Astarte</a> | Spectrometer</h2><p><br>'

	str1 = str1 + ('      <h1><b><a href="/schedule/'+str(prevmonth)+'/'+str(prevyear)+'/'+equip+'"><</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/schedule/'+str(nextmonth)+'/'+str(nextyear)+'/'+equip+'">></a></h1 ></b><br>'
	'<table border="1" cellpadding="0" cellspacing="0" class="month">'
	'<tr><th colspan="7" class="month">' + calendar.month_name[month] +' '+ str(year) + '</th></tr>'
	'<tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th>'
	'<th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>'
	)
	for ma in mat:
		str1 = str1 + '<tr>'
		for m in ma:
			if m != 0:
				str1 = str1 + '<td><div align="left">'+str(m)+'<br> time<br>time<br></div></td>'
			else:
				str1 = str1+ '<td></td>'
		str1 = str1 + '</tr>'
	str1 = str1 + '</table>{% endblock %}'
	render.write(str1)
	render.close()

	return
