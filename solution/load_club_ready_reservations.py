def xstrip(s):
	return None if not s else s.strip()

def nstrip(s):
	return None if not s else int(s.strip())	

def dfix(s):
	if not s:
		return None
	elif len(s) ==7:
		return s+'-01 00:00:00'
	#elif len(s) ==8:
	#	return date_keys[loop_count] + ' ' + s
	else:
		return xstrip(s)

def bfix(s):
	if s.lower()=='t':
		return 1
	elif s.lower()=='f':
		return 0
	else:
		return None			

import csv, MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="homestead",
                     passwd="secret",
                     db="peerfit")

dbcur = db.cursor()

file_dir = '../data/'

input_files = ['club-ready-reservations_01-2018.csv', 'club-ready-reservations_02-2018.csv']

date_keys = ['2018-01-01','2018-02-01']

query = "INSERT INTO peerfit.club_ready_reservations(DATE_KEY, MEMBER_ID, STUDIO_KEY, CLASS_TAG, INSTRUCTOR_FULL_NAME, LEVEL, CANCELED, RESERVED_FOR, SIGNED_IN_AT)" \
													 "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"



#Parse club ready reservations file
loop_count=0
load_count=0
error_count=0
for file in input_files:
	with open(file_dir+input_files[loop_count], 'r') as loadfile:
		reader = csv.DictReader(loadfile, delimiter=',')
		for row in reader:
			try:
				dbcur.execute(query, [date_keys[loop_count], nstrip(row['member_id']), xstrip(row['studio_key']), xstrip(row['class_tag']), xstrip(row['instructor_full_name']),
							  		 nstrip(row['level']), bfix(row['canceled']), dfix(row['reserved_for']), dfix(row['signed_in_at'])   ])
				db.commit()
				load_count=load_count + 1
			except Exception as e:
				db.rollback()
				print("Unable to insert row: " + str(row) + "\n" + e.message)
				error_count = error_count + 1
		loop_count = loop_count + 1			
loadfile.close()	
dbcur.close()
print("Successfully loaded " + str(load_count) + " records!")
if error_count > 0:
	print("Unable to load " + str(error_count) + " records")