from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM tags
WHERE  tag_id = %s
"""


def delete_tags(tag_id):
    cur.execute(query, [tag_id])
    CONNECTION.commit()
    # cur.close()