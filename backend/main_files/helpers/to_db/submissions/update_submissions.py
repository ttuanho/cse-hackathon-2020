from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

UPDATE submissions
SET
    description = %s,
    age = %s,
    gender = %s,
    client_email = %s
WHERE submission_id = %s

"""


def update_submissions(description=None, age=None, gender=None, client_email=None):
    cur.execute(query, [
        description, 
        age, 
        gender, 
        client_email
    ])
    CONNECTION.commit()

    # cur.close()

