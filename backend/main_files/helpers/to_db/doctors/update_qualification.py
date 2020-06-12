from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE doctors
SET qualification = %s
WHERE doctor_id = %s
"""



def update_qualification(qualification, doctor_id):
	cur.execute(query, [qualification, doctor_id])
	CONNECTION.commit()
