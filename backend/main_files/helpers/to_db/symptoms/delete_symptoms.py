from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM symptoms
WHERE  symptom_id = %s
"""


def delete_symptoms(symptom_id):
    cur.execute(query, [symptom_id])
    CONNECTION.commit()
    # cur.close()