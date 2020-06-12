from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE doctors
SET license_expiry_date = %s
WHERE doctor_id = %s
"""



def update_license_expiry_date(license_expiry_date, doctor_id):
	cur.execute(query, [license_expiry_date, doctor_id])
	CONNECTION.commit()
