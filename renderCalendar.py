import calendar
import sys


def renderCal(m, y, equip):
	global month
	global year
	month = m
	year = y
	calendar.setfirstweekday(calendar.SUNDAY)
	temp = 0
	tempmonth = 1;
	if(month > 12):
		global month
		temp = int(month/12)
		month = month - 12*temp
	elif(month < 1):
		global month
		tempmonth = month - 12
		temp = int(tempmonth/12)
		month = month - 12*temp

	year = year + temp
	mat = calendar.monthcalendar(year, month)
	render = open("app/templates/renderCal.html", 'w')
	str1 = ('{% extends "calendar.html" %}{% block calendar %}<table border="1" cellpadding="0" cellspacing="0" class="month">'
	'<tr><th colspan="7" class="month">' + calendar.month_name[month] +' '+ str(year) + '</th></tr>'
	'<tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th>'
	'<th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>'
	)
	for ma in mat:
		str1 = str1 + '<tr>'
		for m in ma:
			if m != 0:
				str1 = str1 + '<td>'+str(m)+'</td>'
			else:
				str1 = str1+ '<td></td>'
		str1 = str1 + '</tr>'
	str1 = str1 + '</table>{% endblock %}'
	render.write(str1)
	render.close()

	return
