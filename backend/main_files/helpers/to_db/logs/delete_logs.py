from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM logs
WHERE  log_id = %s
"""


def delete_logs(log_id):
    cur.execute(query, [log_id])
    CONNECTION.commit()
    # cur.close()