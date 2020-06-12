from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

DELETE FROM doctors
WHERE  doctor_id = %s
"""


def delete_doctors(doctor_id):
    cur.execute(query, [doctor_id])
    CONNECTION.commit()
    # cur.close()