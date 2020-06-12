from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """
insert into submissions (
    submission_id,
    description,
    age,
    gender,
    client_email
) values (
    nextval('submission_id_seq'),
    %s,
    %s,
    %s,
    %s
);

"""


def create_submissions(description=None, age=None, gender=None, client_email=None):
    cur.execute(query, [
        description, 
        age, 
        gender, 
        client_email
    ])
    CONNECTION.commit()

    # cur.close()

