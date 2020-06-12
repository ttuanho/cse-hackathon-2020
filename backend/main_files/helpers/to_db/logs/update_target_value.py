from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET target_value = %s
WHERE log_id = %s
"""



def update_target_value(target_value, log_id):
	cur.execute(query, [target_value, log_id])
	CONNECTION.commit()
