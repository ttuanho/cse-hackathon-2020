from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

UPDATE symptoms
SET
    description = %s
WHERE symptom_id = %s

"""


def update_symptoms(description=None):
    cur.execute(query, [
        description
    ])
    CONNECTION.commit()

    # cur.close()

