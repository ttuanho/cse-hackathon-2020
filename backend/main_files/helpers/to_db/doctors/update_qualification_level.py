from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE doctors
SET qualification_level = %s
WHERE doctor_id = %s
"""



def update_qualification_level(qualification_level, doctor_id):
	cur.execute(query, [qualification_level, doctor_id])
	CONNECTION.commit()
