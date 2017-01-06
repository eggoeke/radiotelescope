import calendar
import sys
import posixpath
import os

def renderCal(month, year, equip):
	calendar.setfirstweekday(calendar.SUNDAY)
	mat = calendar.monthcalendar(year, month)
	render = open("renderCal.html", 'w')
	render.write(str(mat.__len__()))
	render.close()

	return
