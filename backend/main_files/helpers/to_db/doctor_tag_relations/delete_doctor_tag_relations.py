from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM doctor_tag_relations
WHERE  doctor_tag_relation_id = %s
"""


def delete_doctor_tag_relations(doctor_tag_relation_id):
    cur.execute(query, [doctor_tag_relation_id])
    CONNECTION.commit()
    # cur.close()