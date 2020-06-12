from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """
insert into logs (
    log_id,
    ip_addr,
    action,
    target_value,
    html_dom_elem,
    html_attr,
    curr_url,
    dest_url,
    referrer,
    referrer_type,
    referrer_id,
    access_time,
    set_cookie,
    browser_used,
    browser_used_version,
    os,
    os_version,
    langs_used
) values (
    nextval('log_id_seq'),
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
);

"""


def create_logs(ip_addr=None, action=None, target_value=None, html_dom_elem=None, html_attr=None, curr_url=None, dest_url=None, referrer=None, referrer_type=None, referrer_id=None, access_time=None, set_cookie=None, browser_used=None, browser_used_version=None, os=None, os_version=None, langs_used=None):
    cur.execute(query, [
        ip_addr, 
        action, 
        target_value, 
        html_dom_elem, 
        html_attr, 
        curr_url, 
        dest_url, 
        referrer, 
        referrer_type, 
        referrer_id, 
        access_time, 
        set_cookie, 
        browser_used, 
        browser_used_version, 
        os, 
        os_version, 
        langs_used
    ])
    CONNECTION.commit()

    # cur.close()

