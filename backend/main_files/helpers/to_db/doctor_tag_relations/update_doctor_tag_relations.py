from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

UPDATE doctor_tag_relations
SET
    doctor_id = %s,
    tag_id = %s
WHERE doctor_tag_relation_id = %s

"""


def update_doctor_tag_relations(doctor_id=None, tag_id=None):
    cur.execute(query, [
        doctor_id, 
        tag_id
    ])
    CONNECTION.commit()

    # cur.close()

