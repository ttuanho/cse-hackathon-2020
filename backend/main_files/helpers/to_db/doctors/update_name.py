from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE doctors
SET name = %s
WHERE doctor_id = %s
"""



def update_name(name, doctor_id):
	cur.execute(query, [name, doctor_id])
	CONNECTION.commit()
