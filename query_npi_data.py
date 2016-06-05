#!/usr/bin/python

import csv
from optparse import OptionParser
import MySQLdb
usage = "%prog [options] NPI"
parser = OptionParser(usage=usage)
parser.add_option("-s", "--host", action="store", type="string", dest="host", default="localhost")
parser.add_option("-p", "--password", action="store", type="string", dest="password", default="")
parser.add_option("-u", "--username", action="store", type="string", dest="username", default="")
parser.add_option("-d", "--database", action="store", type="string", dest="database", default="NPI")

(options, args) = parser.parse_args()

db = MySQLdb.connect(host=options.host, user=options.username, passwd=options.password, db=options.database)
c = db.cursor()

for arg in args:
	c.execute("SELECT * FROM NPIData WHERE NPI = " + arg)
	rows = c.fetchall()

	for row in rows:
		print "NPI         : " + str(row[0])
		print "Type        : " + str(row[1])
		print "Name        : " + row[4] + " " + row[5] + " " + row[3]
		print "Address     : " + row[9]
		print "              " + row[10]
		print "              " + row[11] + ", " + row[12] + " " + row[13]
		print "Phone       : " + row[14]
		print "Fax         : " + row[15]
		print
