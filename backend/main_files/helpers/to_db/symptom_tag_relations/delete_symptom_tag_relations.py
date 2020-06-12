from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM symptom_tag_relations
WHERE  symptom_tag_relation_id = %s
"""


def delete_symptom_tag_relations(symptom_tag_relation_id):
    cur.execute(query, [symptom_tag_relation_id])
    CONNECTION.commit()
    # cur.close()