from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT doctor_id
FROM doctors
WHERE license_expiry_date = %s
"""


def validate_license_expiry_date_from_doctors(license_expiry_date):
	cur.execute(query, [license_expiry_date])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==license_expiry_date
