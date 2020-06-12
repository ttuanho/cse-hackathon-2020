from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE logs
SET ip_addr = %s
WHERE log_id = %s
"""



def update_ip_addr(ip_addr, log_id):
	cur.execute(query, [ip_addr, log_id])
	CONNECTION.commit()
