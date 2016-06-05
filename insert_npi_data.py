#!/usr/bin/python

import csv
from optparse import OptionParser
import MySQLdb
usage = "%prog [options] NPIFILE"
parser = OptionParser(usage=usage)
parser.add_option("-s", "--host", action="store", type="string", dest="host", default="localhost")
parser.add_option("-p", "--password", action="store", type="string", dest="password", default="")
parser.add_option("-u", "--username", action="store", type="string", dest="username", default="")
parser.add_option("-d", "--database", action="store", type="string", dest="database", default="NPI")

(options, args) = parser.parse_args()

if len(args) >= 1:
	db = MySQLdb.connect(host=options.host, user=options.username, passwd=options.password, db=options.database)
	c = db.cursor()

	totalRows = 0

	with open(args[0], 'rb') as csvfile:
		infile = csv.reader(csvfile)

		entities = []

		firstRow = True

		for row in infile:
			if firstRow:
				firstRow = False
				continue

			npi = long(row[0].strip())

			entityType = 0

			if (row[1].strip() != ""):
				entityType = int(row[1].strip())

			providerOrganization = row[4].strip()
			providerLastName = row[5].strip()
			providerFirstName = row[6].strip()
			providerMiddleName = row[7].strip()
			providerNamePrefix = row[8].strip()
			providerNameSuffix = row[9].strip()
			providerCredentials = row[10].strip()
			providerAddress1 = row[20].strip()
			providerAddress2 = row[21].strip()
			providerCity = row[22].strip()
			providerState = row[23].strip()

			providerPostalCode = row[24].strip()
			providerTelephone = row[34].strip()
			providerFax = row[35].strip()

			entity = (npi, entityType, providerOrganization, providerLastName, providerFirstName,
				providerMiddleName, providerNamePrefix, providerNameSuffix, providerCredentials,
				providerAddress1, providerAddress2, providerCity, providerState, providerPostalCode,
				providerTelephone, providerFax)

			entities.append(entity)

			if len(entities) >= 1000:
				c.executemany("""REPLACE INTO NPIData VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
					entities)
				db.commit()
				totalRows += len(entities)
				print "Inserted " + str(totalRows) + " rows."
				entities = []

	if len(entities) > 0:
		c.executemany("""REPLACE INTO NPIData VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
			entities)
		db.commit()
		totalRows += len(entities)
		print "Inserted " + str(totalRows) + " rows."
