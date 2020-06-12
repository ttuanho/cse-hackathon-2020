from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

UPDATE redirects
SET ip_addr = %s
WHERE redirect_id = %s
"""



def update_ip_addr(ip_addr, redirect_id):
	cur.execute(query, [ip_addr, redirect_id])
	CONNECTION.commit()
