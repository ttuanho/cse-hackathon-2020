from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM redirects
WHERE  redirect_id = %s
"""


def delete_redirects(redirect_id):
    cur.execute(query, [redirect_id])
    CONNECTION.commit()
    # cur.close()