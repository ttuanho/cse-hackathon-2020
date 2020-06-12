from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """
insert into doctors (
    doctor_id,
    name,
    license_code,
    license_expiry_date,
    qualification,
    qualification_level
) values (
    nextval('doctor_id_seq'),
    %s,
    %s,
    %s,
    %s,
    %s
);

"""


def create_doctors(name=None, license_code=None, license_expiry_date=None, qualification=None, qualification_level=None):
    cur.execute(query, [
        name, 
        license_code, 
        license_expiry_date, 
        qualification, 
        qualification_level
    ])
    CONNECTION.commit()

    # cur.close()

