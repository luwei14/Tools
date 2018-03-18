#! /usr/bin/env python
import sqlite3
import csv
import sys

if __name__ == "__main__":
	params = sys.argv
	if len(params) < 6:
		print('''
				Please give the parameters in the order:
				dbpath, table name, csv file, csv delimiter,pks
			''')
		exit(0)
	dbpath = params[1]
	tbl = params[2]
	csvfile = params[3]
	delimiter = params[4]
	pks = params[5]
	print("Now Import file {} with delimiter {} into table {} of sqlite database {}...").format(csvfile,delimiter,tbl,  dbpath)
	conn = sqlite3.connect(dbpath)
	conn.text_factory = str
	cur = conn.cursor()

	with open(csvfile,"r") as ifile:
  		reader = csv.DictReader(ifile, delimiter=delimiter)
		row = next(reader)
		sql = '''CREATE TABLE IF NOT EXISTS {} ('''.format(tbl)
		fields = []
		for k,v in row.items():
			if v.replace(".","",1).isdigit():
				fields.append("{} NUMERIC".format(k))
			else:
				fields.append("{} TEXT".format(k))
		sql += ",".join(fields)
		sql += ", PRIMARY KEY ({}));".format(pks)
		print sql
		cur.execute(sql)
		k = 0
		while row:
			cols = ", ".join(row.keys())
			placeholders = ", ".join("?" * len(row))
			sql = "INSERT  INTO {} ({}) VALUES ({})".format(tbl, cols, placeholders)
			try:
				cur.execute(sql, row.values())
			except sqlite3.IntegrityError, e:
				pass
			row = next(reader)
			k += 1
			sys.stdout.write("\r {} records complete...".format(k))
			sys.stdout.flush()
	conn.commit()
	cur.close()
	conn.close()
	print("Complete.")
