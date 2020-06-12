from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE doctors
SET license_code = %s
WHERE doctor_id = %s
"""



def update_license_code(license_code, doctor_id):
	cur.execute(query, [license_code, doctor_id])
	CONNECTION.commit()
