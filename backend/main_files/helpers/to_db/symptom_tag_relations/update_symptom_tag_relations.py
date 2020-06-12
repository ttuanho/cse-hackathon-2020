from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

UPDATE symptom_tag_relations
SET
    symptom_id = %s,
    tag_id = %s
WHERE symptom_tag_relation_id = %s

"""


def update_symptom_tag_relations(symptom_id=None, tag_id=None):
    cur.execute(query, [
        symptom_id, 
        tag_id
    ])
    CONNECTION.commit()

    # cur.close()

