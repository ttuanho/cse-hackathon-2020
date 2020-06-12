from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """
insert into booking_events (
    booking_event_id,
    start_time,
    end_time,
    reference,
    doctor_id,
    submission_id
) values (
    nextval('booking_event_id_seq'),
    %s,
    %s,
    %s,
    %s,
    %s
);

"""


def create_booking_events(start_time=None, end_time=None, reference=None, doctor_id=None, submission_id=None):
    cur.execute(query, [
        start_time, 
        end_time, 
        reference, 
        doctor_id, 
        submission_id
    ])
    CONNECTION.commit()

    # cur.close()

