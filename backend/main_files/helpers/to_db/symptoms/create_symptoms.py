from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """
insert into symptoms (
    symptom_id,
    description
) values (
    nextval('symptom_id_seq'),
    %s
);

"""


def create_symptoms(description=None):
    cur.execute(query, [
        description
    ])
    CONNECTION.commit()

    # cur.close()

