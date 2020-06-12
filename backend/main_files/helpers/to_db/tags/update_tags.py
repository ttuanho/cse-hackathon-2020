from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

UPDATE tags
SET
    tag_name = %s
WHERE tag_id = %s

"""


def update_tags(tag_name=None):
    cur.execute(query, [
        tag_name
    ])
    CONNECTION.commit()

    # cur.close()

