from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

UPDATE booking_events
SET
    start_time = %s,
    end_time = %s,
    reference = %s,
    doctor_id = %s,
    submission_id = %s
WHERE booking_event_id = %s

"""


def update_booking_events(start_time=None, end_time=None, reference=None, doctor_id=None, submission_id=None):
    cur.execute(query, [
        start_time, 
        end_time, 
        reference, 
        doctor_id, 
        submission_id
    ])
    CONNECTION.commit()

    # cur.close()

