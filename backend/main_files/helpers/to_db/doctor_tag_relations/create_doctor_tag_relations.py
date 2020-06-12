from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """
insert into doctor_tag_relations (
    doctor_tag_relation_id,
    doctor_id,
    tag_id
) values (
    nextval('doctor_tag_relation_id_seq'),
    %s,
    %s
);

"""


def create_doctor_tag_relations(doctor_id=None, tag_id=None):
    cur.execute(query, [
        doctor_id, 
        tag_id
    ])
    CONNECTION.commit()

    # cur.close()

