import calendar
import sys

def renderCal(month, year, equip):
	calendar.setfirstweekday(calendar.SUNDAY)
	mat = calendar.monthcalendar(year, month)
	render = open("renderCal.html", 'w')
	str1 = ('<table border="1" cellpadding="0" cellspacing="0" class="month">'
	'<tr><th colspan="7" class="month">' + calendar.month_name[month] +' '+ str(year) + '</th></tr>'
	'<tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th>'
	'<th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>'
	)

	render.write(str1)
	render.close()

	return
