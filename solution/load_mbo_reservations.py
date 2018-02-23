def xstrip(s):
	return None if not s.strip() else s.strip()

def nstrip(s):
	return None if not s.strip() else int(s.strip())	

def dfix(s):
	xstrip(s)
	if len(s) ==7:
		return s+'-01 00:00:00'
	elif len(s) ==8:
		return s+'-01 00:00:00'
	elif s[:10]=='2018-02-30':
		return '2018-02-28'	
	else:
		return xstrip(s)
			

import csv, MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="homestead",
                     passwd="secret",
                     db="peerfit")

dbcur = db.cursor()

file_dir = '../data/'

input_files = ['mbo-reservations_01-2018.csv', 'mbo-reservations_02-2018.csv']

date_keys = ['2018-01-01','2018-02-01']


query = "INSERT INTO peerfit.mbo_reservations(MEMBER_ID, STUDIO_KEY, DATE_KEY, STUDIO_ADDRESS_STREET, STUDIO_ADDRESS_STATE, STUDIO_ADDRESS_ZIP, " \
											  "CLASS_TAG, VIEWED_AT, RESERVED_AT, CANCELED_AT, CLASS_TIME_AT, CHECKED_IN_AT) " \
											  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

#Parse mbo reservations files
loop_count=0
load_count=0
error_count=0
for file in input_files:
	with open(file_dir+input_files[loop_count], 'r') as loadfile:
		reader = csv.DictReader(loadfile, delimiter=',')
		for row in reader:
			#print(row)
			try:
				dbcur.execute(query,  [ nstrip(row['member_id']), row['studio_key'].strip(), date_keys[loop_count], row['studio_address_street'].strip(), 
									row['studio_address_state'].strip(), row['studio_address_zip'].strip(), row['class_tag'].strip(), 
									dfix(row['viewed_at']), dfix(row['reserved_at']), dfix(row['canceled_at']), dfix(row['class_time_at']), 
									dfix(row['checked_in_at'])])
				db.commit()
				load_count=load_count + 1
			except:
				db.rollback()
				print("Unable to insert row: " + str(row))
				error_count = error_count + 1
		loop_count = loop_count + 1					
loadfile.close()	
dbcur.close()
print("Successfully loaded " + str(load_count) + " records!")
if error_count > 0:
	print("Unable to load " + str(error_count) + " records")