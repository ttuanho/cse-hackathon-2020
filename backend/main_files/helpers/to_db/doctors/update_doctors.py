from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

UPDATE doctors
SET
    name = %s,
    license_code = %s,
    license_expiry_date = %s,
    qualification = %s,
    qualification_level = %s
WHERE doctor_id = %s

"""


def update_doctors(name=None, license_code=None, license_expiry_date=None, qualification=None, qualification_level=None):
    cur.execute(query, [
        name, 
        license_code, 
        license_expiry_date, 
        qualification, 
        qualification_level
    ])
    CONNECTION.commit()

    # cur.close()

