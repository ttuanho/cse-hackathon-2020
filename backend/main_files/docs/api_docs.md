---
title: "API documents"
author: Tuan Ho
date: June 12, 2020
geometry: "left=0.3cm,right=0.3cm,top=1cm,bottom=1cm"
output: pdf_document
---


- Local root url: http://127.0.0.1:8080/
- Remote server url: N/A
- Every API requires `token` unless it's creating new record in the table

|Table / Service module|URL path                        |Body (POST) or Header params (GET)|Method  | Usage                   |
|----------------------|--------------------------------|----------------------------------|--------|-------------------------|
|**DOCTORS**       |/doctors/insert/             |                                  |POST    |Create / Inser new doctors   |
|**DOCTORS**       |/doctors/delete/             |                                  |DELETE  |Delete entry / row in doctors|
|**DOCTORS**|/doctors/select/name||GET|Get record of `name`|
|**DOCTORS**|/doctors/insert/name||POST|Create record of `name`|
|**DOCTORS**|/doctors/update/name||PUT|Change record of `name`|
|**DOCTORS**|/doctors/delete/name||DELETE|Delete record of `name`|
|**DOCTORS**|/doctors/select/license_code||GET|Get record of `license_code`|
|**DOCTORS**|/doctors/insert/license_code||POST|Create record of `license_code`|
|**DOCTORS**|/doctors/update/license_code||PUT|Change record of `license_code`|
|**DOCTORS**|/doctors/delete/license_code||DELETE|Delete record of `license_code`|
|**DOCTORS**|/doctors/select/license_expiry_date||GET|Get record of `license_expiry_date`|
|**DOCTORS**|/doctors/insert/license_expiry_date||POST|Create record of `license_expiry_date`|
|**DOCTORS**|/doctors/update/license_expiry_date||PUT|Change record of `license_expiry_date`|
|**DOCTORS**|/doctors/delete/license_expiry_date||DELETE|Delete record of `license_expiry_date`|
|**DOCTORS**|/doctors/select/qualification||GET|Get record of `qualification`|
|**DOCTORS**|/doctors/insert/qualification||POST|Create record of `qualification`|
|**DOCTORS**|/doctors/update/qualification||PUT|Change record of `qualification`|
|**DOCTORS**|/doctors/delete/qualification||DELETE|Delete record of `qualification`|
|**DOCTORS**|/doctors/select/qualification_level||GET|Get record of `qualification_level`|
|**DOCTORS**|/doctors/insert/qualification_level||POST|Create record of `qualification_level`|
|**DOCTORS**|/doctors/update/qualification_level||PUT|Change record of `qualification_level`|
|**DOCTORS**|/doctors/delete/qualification_level||DELETE|Delete record of `qualification_level`|
|**SUBMISSIONS**       |/submissions/insert/             |                                  |POST    |Create / Inser new submissions   |
|**SUBMISSIONS**       |/submissions/delete/             |                                  |DELETE  |Delete entry / row in submissions|
|**SUBMISSIONS**|/submissions/select/description||GET|Get record of `description`|
|**SUBMISSIONS**|/submissions/insert/description||POST|Create record of `description`|
|**SUBMISSIONS**|/submissions/update/description||PUT|Change record of `description`|
|**SUBMISSIONS**|/submissions/delete/description||DELETE|Delete record of `description`|
|**SUBMISSIONS**|/submissions/select/age||GET|Get record of `age`|
|**SUBMISSIONS**|/submissions/insert/age||POST|Create record of `age`|
|**SUBMISSIONS**|/submissions/update/age||PUT|Change record of `age`|
|**SUBMISSIONS**|/submissions/delete/age||DELETE|Delete record of `age`|
|**SUBMISSIONS**|/submissions/select/gender||GET|Get record of `gender`|
|**SUBMISSIONS**|/submissions/insert/gender||POST|Create record of `gender`|
|**SUBMISSIONS**|/submissions/update/gender||PUT|Change record of `gender`|
|**SUBMISSIONS**|/submissions/delete/gender||DELETE|Delete record of `gender`|
|**SUBMISSIONS**|/submissions/select/client_email||GET|Get record of `client_email`|
|**SUBMISSIONS**|/submissions/insert/client_email||POST|Create record of `client_email`|
|**SUBMISSIONS**|/submissions/update/client_email||PUT|Change record of `client_email`|
|**SUBMISSIONS**|/submissions/delete/client_email||DELETE|Delete record of `client_email`|
|**SYMPTOMS**       |/symptoms/insert/             |                                  |POST    |Create / Inser new symptoms   |
|**SYMPTOMS**       |/symptoms/delete/             |                                  |DELETE  |Delete entry / row in symptoms|
|**SYMPTOMS**|/symptoms/select/description||GET|Get record of `description`|
|**SYMPTOMS**|/symptoms/insert/description||POST|Create record of `description`|
|**SYMPTOMS**|/symptoms/update/description||PUT|Change record of `description`|
|**SYMPTOMS**|/symptoms/delete/description||DELETE|Delete record of `description`|
|**SYMPTOM_TAG_RELATIONS**       |/symptom_tag_relations/insert/             |                                  |POST    |Create / Inser new symptom_tag_relations   |
|**SYMPTOM_TAG_RELATIONS**       |/symptom_tag_relations/delete/             |                                  |DELETE  |Delete entry / row in symptom_tag_relations|
|**DOCTOR_TAG_RELATIONS**       |/doctor_tag_relations/insert/             |                                  |POST    |Create / Inser new doctor_tag_relations   |
|**DOCTOR_TAG_RELATIONS**       |/doctor_tag_relations/delete/             |                                  |DELETE  |Delete entry / row in doctor_tag_relations|
|**TAGS**       |/tags/insert/             |                                  |POST    |Create / Inser new tags   |
|**TAGS**       |/tags/delete/             |                                  |DELETE  |Delete entry / row in tags|
|**TAGS**|/tags/select/tag_name||GET|Get record of `tag_name`|
|**TAGS**|/tags/insert/tag_name||POST|Create record of `tag_name`|
|**TAGS**|/tags/update/tag_name||PUT|Change record of `tag_name`|
|**TAGS**|/tags/delete/tag_name||DELETE|Delete record of `tag_name`|
|**BOOKING_EVENTS**       |/booking_events/insert/             |                                  |POST    |Create / Inser new booking_events   |
|**BOOKING_EVENTS**       |/booking_events/delete/             |                                  |DELETE  |Delete entry / row in booking_events|
|**BOOKING_EVENTS**|/booking_events/select/start_time||GET|Get record of `start_time`|
|**BOOKING_EVENTS**|/booking_events/insert/start_time||POST|Create record of `start_time`|
|**BOOKING_EVENTS**|/booking_events/update/start_time||PUT|Change record of `start_time`|
|**BOOKING_EVENTS**|/booking_events/delete/start_time||DELETE|Delete record of `start_time`|
|**BOOKING_EVENTS**|/booking_events/select/end_time||GET|Get record of `end_time`|
|**BOOKING_EVENTS**|/booking_events/insert/end_time||POST|Create record of `end_time`|
|**BOOKING_EVENTS**|/booking_events/update/end_time||PUT|Change record of `end_time`|
|**BOOKING_EVENTS**|/booking_events/delete/end_time||DELETE|Delete record of `end_time`|
|**BOOKING_EVENTS**|/booking_events/select/reference||GET|Get record of `reference`|
|**BOOKING_EVENTS**|/booking_events/insert/reference||POST|Create record of `reference`|
|**BOOKING_EVENTS**|/booking_events/update/reference||PUT|Change record of `reference`|
|**BOOKING_EVENTS**|/booking_events/delete/reference||DELETE|Delete record of `reference`|

Updated on 12:54:56 June 12, 2020
