from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM submissions
WHERE  submission_id = %s
"""


def delete_submissions(submission_id):
    cur.execute(query, [submission_id])
    CONNECTION.commit()
    # cur.close()