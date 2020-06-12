from main_files.db.connect_db import CONNECTION
cur = CONNECTION.cursor()

query = """

UPDATE logs
SET
    ip_addr = %s,
    action = %s,
    target_value = %s,
    html_dom_elem = %s,
    html_attr = %s,
    curr_url = %s,
    dest_url = %s,
    referrer = %s,
    referrer_type = %s,
    referrer_id = %s,
    access_time = %s,
    set_cookie = %s,
    browser_used = %s,
    browser_used_version = %s,
    os = %s,
    os_version = %s,
    langs_used = %s
WHERE log_id = %s

"""


def update_logs(ip_addr=None, action=None, target_value=None, html_dom_elem=None, html_attr=None, curr_url=None, dest_url=None, referrer=None, referrer_type=None, referrer_id=None, access_time=None, set_cookie=None, browser_used=None, browser_used_version=None, os=None, os_version=None, langs_used=None):
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

