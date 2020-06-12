from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """
insert into symptom_tag_relations (
    symptom_tag_relation_id,
    symptom_id,
    tag_id
) values (
    nextval('symptom_tag_relation_id_seq'),
    %s,
    %s
);

"""


def create_symptom_tag_relations(symptom_id=None, tag_id=None):
    cur.execute(query, [
        symptom_id, 
        tag_id
    ])
    CONNECTION.commit()

    # cur.close()

