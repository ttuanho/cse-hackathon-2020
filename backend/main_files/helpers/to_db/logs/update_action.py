from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET action = %s
WHERE log_id = %s
"""



def update_action(action, log_id):
	cur.execute(query, [action, log_id])
	CONNECTION.commit()
