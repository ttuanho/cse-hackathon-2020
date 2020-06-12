from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT doctor_id
FROM doctors
WHERE license_code = %s
"""


def validate_license_code_from_doctors(license_code):
	cur.execute(query, [license_code])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==license_code
