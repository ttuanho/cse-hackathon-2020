from main_files.db.connect_db import CONNECTION

cur = CONNECTION.cursor()



query = """

SELECT log_id
FROM logs
WHERE ip_addr = %s
"""


def validate_ip_addr(ip_addr):
	cur.execute(query, [ip_addr])
	res = None
	res = cur.fetchone()[0]
	# cur.close()
	return res!=None and res==ip_addr
