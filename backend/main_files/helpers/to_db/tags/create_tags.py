from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """
insert into tags (
    tag_id,
    tag_name
) values (
    nextval('tag_id_seq'),
    %s
);

"""


def create_tags(tag_name=None):
    cur.execute(query, [
        tag_name
    ])
    CONNECTION.commit()

    # cur.close()

