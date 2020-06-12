
from json import dumps
import sys, os
from flask import Flask, request, Response, send_from_directory, redirect
import time, datetime
import main_files.helpers as helpers
from flask_cors import CORS
import flask


from main_files.helpers.to_db.doctors.create_doctors import create_doctors
from main_files.helpers.to_db.doctors.delete_doctors import delete_doctors
from main_files.helpers.from_db.validates.doctors.validate_doctor_id import validate_doctor_id_from_doctors
from main_files.helpers.to_db.doctors.update_name import update_name
from main_files.helpers.to_db.doctors.update_license_code import update_license_code
from main_files.helpers.to_db.doctors.update_license_expiry_date import update_license_expiry_date
from main_files.helpers.to_db.doctors.update_qualification import update_qualification
from main_files.helpers.to_db.doctors.update_qualification_level import update_qualification_level
from main_files.helpers.to_db.submissions.create_submissions import create_submissions
from main_files.helpers.to_db.submissions.delete_submissions import delete_submissions
from main_files.helpers.from_db.validates.submissions.validate_submission_id import validate_submission_id_from_submissions
from main_files.helpers.to_db.submissions.update_description import update_description
from main_files.helpers.to_db.submissions.update_age import update_age
from main_files.helpers.to_db.submissions.update_gender import update_gender
from main_files.helpers.to_db.submissions.update_client_email import update_client_email
from main_files.helpers.to_db.symptoms.create_symptoms import create_symptoms
from main_files.helpers.to_db.symptoms.delete_symptoms import delete_symptoms
from main_files.helpers.from_db.validates.symptoms.validate_symptom_id import validate_symptom_id_from_symptoms
from main_files.helpers.to_db.symptoms.update_description import update_description
from main_files.helpers.to_db.symptom_tag_relations.create_symptom_tag_relations import create_symptom_tag_relations
from main_files.helpers.to_db.symptom_tag_relations.delete_symptom_tag_relations import delete_symptom_tag_relations
from main_files.helpers.from_db.validates.symptom_tag_relations.validate_symptom_tag_relation_id import validate_symptom_tag_relation_id_from_symptom_tag_relations
from main_files.helpers.to_db.symptom_tag_relations.update_symptom_id import update_symptom_id
from main_files.helpers.to_db.symptom_tag_relations.update_tag_id import update_tag_id
from main_files.helpers.to_db.doctor_tag_relations.create_doctor_tag_relations import create_doctor_tag_relations
from main_files.helpers.to_db.doctor_tag_relations.delete_doctor_tag_relations import delete_doctor_tag_relations
from main_files.helpers.from_db.validates.doctor_tag_relations.validate_doctor_tag_relation_id import validate_doctor_tag_relation_id_from_doctor_tag_relations
from main_files.helpers.to_db.doctor_tag_relations.update_doctor_id import update_doctor_id
from main_files.helpers.to_db.doctor_tag_relations.update_tag_id import update_tag_id
from main_files.helpers.to_db.tags.create_tags import create_tags
from main_files.helpers.to_db.tags.delete_tags import delete_tags
from main_files.helpers.from_db.validates.tags.validate_tag_id import validate_tag_id_from_tags
from main_files.helpers.to_db.tags.update_tag_name import update_tag_name
from main_files.helpers.to_db.booking_events.create_booking_events import create_booking_events
from main_files.helpers.to_db.booking_events.delete_booking_events import delete_booking_events
from main_files.helpers.from_db.validates.booking_events.validate_booking_event_id import validate_booking_event_id_from_booking_events
from main_files.helpers.to_db.booking_events.update_start_time import update_start_time
from main_files.helpers.to_db.booking_events.update_end_time import update_end_time
from main_files.helpers.to_db.booking_events.update_reference import update_reference
from main_files.helpers.to_db.booking_events.update_doctor_id import update_doctor_id
from main_files.helpers.to_db.booking_events.update_submission_id import update_submission_id


app = Flask(__name__, static_url_path='/static/')
CORS(app)

if __name__ == '__main__':
    app.run(port=8080, debug=True)


"""
=========== DOCTORS ===========
"""


# Create a new entry /row in table "doctors" 
@app.route("/doctors/insert/", methods=["POST"])
def server_create_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr



# Delete a entry /row in table "doctors" 
@app.route("/doctors/delete/", methods=["DELETE"])
def server_create_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Get record of "name" in table "doctors" 
@app.route("/doctors/select/name/", methods=["GET"])
def server_select_name_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "name" in table "doctors" 
@app.route("/doctors/insert/name/", methods=["POST"])
def server_insert_name_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "name" in table "doctors" 
@app.route("/doctors/update/name/", methods=["PUT"])
def server_update_name_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Delete record of "name" in table "doctors" 
@app.route("/doctors/delete/name/", methods=["DELETE"])
def server_delete_name_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Get record of "license_code" in table "doctors" 
@app.route("/doctors/select/license_code/", methods=["GET"])
def server_select_license_code_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "license_code" in table "doctors" 
@app.route("/doctors/insert/license_code/", methods=["POST"])
def server_insert_license_code_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "license_code" in table "doctors" 
@app.route("/doctors/update/license_code/", methods=["PUT"])
def server_update_license_code_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Delete record of "license_code" in table "doctors" 
@app.route("/doctors/delete/license_code/", methods=["DELETE"])
def server_delete_license_code_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Get record of "license_expiry_date" in table "doctors" 
@app.route("/doctors/select/license_expiry_date/", methods=["GET"])
def server_select_license_expiry_date_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "license_expiry_date" in table "doctors" 
@app.route("/doctors/insert/license_expiry_date/", methods=["POST"])
def server_insert_license_expiry_date_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "license_expiry_date" in table "doctors" 
@app.route("/doctors/update/license_expiry_date/", methods=["PUT"])
def server_update_license_expiry_date_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Delete record of "license_expiry_date" in table "doctors" 
@app.route("/doctors/delete/license_expiry_date/", methods=["DELETE"])
def server_delete_license_expiry_date_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Get record of "qualification" in table "doctors" 
@app.route("/doctors/select/qualification/", methods=["GET"])
def server_select_qualification_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "qualification" in table "doctors" 
@app.route("/doctors/insert/qualification/", methods=["POST"])
def server_insert_qualification_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "qualification" in table "doctors" 
@app.route("/doctors/update/qualification/", methods=["PUT"])
def server_update_qualification_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Delete record of "qualification" in table "doctors" 
@app.route("/doctors/delete/qualification/", methods=["DELETE"])
def server_delete_qualification_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Get record of "qualification_level" in table "doctors" 
@app.route("/doctors/select/qualification_level/", methods=["GET"])
def server_select_qualification_level_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "qualification_level" in table "doctors" 
@app.route("/doctors/insert/qualification_level/", methods=["POST"])
def server_insert_qualification_level_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "qualification_level" in table "doctors" 
@app.route("/doctors/update/qualification_level/", methods=["PUT"])
def server_update_qualification_level_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



# Delete record of "qualification_level" in table "doctors" 
@app.route("/doctors/delete/qualification_level/", methods=["DELETE"])
def server_delete_qualification_level_doctors():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_id = request.form.get('doctor_id')
	if (validate_doctor_id_from_doctors(doctor_id) == False):
		return dumps({'_error':'doctor_id is invalid'})
	return dumps({})



"""
=========== SUBMISSIONS ===========
"""


# Create a new entry /row in table "submissions" 
@app.route("/submissions/insert/", methods=["POST"])
def server_create_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr



# Delete a entry /row in table "submissions" 
@app.route("/submissions/delete/", methods=["DELETE"])
def server_create_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Get record of "description" in table "submissions" 
@app.route("/submissions/select/description/", methods=["GET"])
def server_select_description_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "description" in table "submissions" 
@app.route("/submissions/insert/description/", methods=["POST"])
def server_insert_description_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "description" in table "submissions" 
@app.route("/submissions/update/description/", methods=["PUT"])
def server_update_description_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	submission_id = request.form.get('submission_id')
	if (validate_submission_id_from_submissions(submission_id) == False):
		return dumps({'_error':'submission_id is invalid'})
	return dumps({})



# Delete record of "description" in table "submissions" 
@app.route("/submissions/delete/description/", methods=["DELETE"])
def server_delete_description_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	submission_id = request.form.get('submission_id')
	if (validate_submission_id_from_submissions(submission_id) == False):
		return dumps({'_error':'submission_id is invalid'})
	return dumps({})



# Get record of "age" in table "submissions" 
@app.route("/submissions/select/age/", methods=["GET"])
def server_select_age_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "age" in table "submissions" 
@app.route("/submissions/insert/age/", methods=["POST"])
def server_insert_age_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "age" in table "submissions" 
@app.route("/submissions/update/age/", methods=["PUT"])
def server_update_age_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	submission_id = request.form.get('submission_id')
	if (validate_submission_id_from_submissions(submission_id) == False):
		return dumps({'_error':'submission_id is invalid'})
	return dumps({})



# Delete record of "age" in table "submissions" 
@app.route("/submissions/delete/age/", methods=["DELETE"])
def server_delete_age_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	submission_id = request.form.get('submission_id')
	if (validate_submission_id_from_submissions(submission_id) == False):
		return dumps({'_error':'submission_id is invalid'})
	return dumps({})



# Get record of "gender" in table "submissions" 
@app.route("/submissions/select/gender/", methods=["GET"])
def server_select_gender_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "gender" in table "submissions" 
@app.route("/submissions/insert/gender/", methods=["POST"])
def server_insert_gender_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "gender" in table "submissions" 
@app.route("/submissions/update/gender/", methods=["PUT"])
def server_update_gender_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	submission_id = request.form.get('submission_id')
	if (validate_submission_id_from_submissions(submission_id) == False):
		return dumps({'_error':'submission_id is invalid'})
	return dumps({})



# Delete record of "gender" in table "submissions" 
@app.route("/submissions/delete/gender/", methods=["DELETE"])
def server_delete_gender_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	submission_id = request.form.get('submission_id')
	if (validate_submission_id_from_submissions(submission_id) == False):
		return dumps({'_error':'submission_id is invalid'})
	return dumps({})



# Get record of "client_email" in table "submissions" 
@app.route("/submissions/select/client_email/", methods=["GET"])
def server_select_client_email_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "client_email" in table "submissions" 
@app.route("/submissions/insert/client_email/", methods=["POST"])
def server_insert_client_email_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "client_email" in table "submissions" 
@app.route("/submissions/update/client_email/", methods=["PUT"])
def server_update_client_email_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	submission_id = request.form.get('submission_id')
	if (validate_submission_id_from_submissions(submission_id) == False):
		return dumps({'_error':'submission_id is invalid'})
	return dumps({})



# Delete record of "client_email" in table "submissions" 
@app.route("/submissions/delete/client_email/", methods=["DELETE"])
def server_delete_client_email_submissions():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	submission_id = request.form.get('submission_id')
	if (validate_submission_id_from_submissions(submission_id) == False):
		return dumps({'_error':'submission_id is invalid'})
	return dumps({})



"""
=========== SYMPTOMS ===========
"""


# Create a new entry /row in table "symptoms" 
@app.route("/symptoms/insert/", methods=["POST"])
def server_create_symptoms():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr



# Delete a entry /row in table "symptoms" 
@app.route("/symptoms/delete/", methods=["DELETE"])
def server_create_symptoms():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Get record of "description" in table "symptoms" 
@app.route("/symptoms/select/description/", methods=["GET"])
def server_select_description_symptoms():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "description" in table "symptoms" 
@app.route("/symptoms/insert/description/", methods=["POST"])
def server_insert_description_symptoms():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "description" in table "symptoms" 
@app.route("/symptoms/update/description/", methods=["PUT"])
def server_update_description_symptoms():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	symptom_id = request.form.get('symptom_id')
	if (validate_symptom_id_from_symptoms(symptom_id) == False):
		return dumps({'_error':'symptom_id is invalid'})
	return dumps({})



# Delete record of "description" in table "symptoms" 
@app.route("/symptoms/delete/description/", methods=["DELETE"])
def server_delete_description_symptoms():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	symptom_id = request.form.get('symptom_id')
	if (validate_symptom_id_from_symptoms(symptom_id) == False):
		return dumps({'_error':'symptom_id is invalid'})
	return dumps({})



"""
=========== SYMPTOM_TAG_RELATIONS ===========
"""


# Create a new entry /row in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/insert/", methods=["POST"])
def server_create_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr



# Delete a entry /row in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/delete/", methods=["DELETE"])
def server_create_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Get record of "symptom_id" in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/select/symptom_id/", methods=["GET"])
def server_select_symptom_id_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "symptom_id" in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/insert/symptom_id/", methods=["POST"])
def server_insert_symptom_id_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "symptom_id" in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/update/symptom_id/", methods=["PUT"])
def server_update_symptom_id_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	symptom_tag_relation_id = request.form.get('symptom_tag_relation_id')
	if (validate_symptom_tag_relation_id_from_symptom_tag_relations(symptom_tag_relation_id) == False):
		return dumps({'_error':'symptom_tag_relation_id is invalid'})
	return dumps({})



# Delete record of "symptom_id" in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/delete/symptom_id/", methods=["DELETE"])
def server_delete_symptom_id_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	symptom_tag_relation_id = request.form.get('symptom_tag_relation_id')
	if (validate_symptom_tag_relation_id_from_symptom_tag_relations(symptom_tag_relation_id) == False):
		return dumps({'_error':'symptom_tag_relation_id is invalid'})
	return dumps({})



# Get record of "tag_id" in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/select/tag_id/", methods=["GET"])
def server_select_tag_id_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "tag_id" in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/insert/tag_id/", methods=["POST"])
def server_insert_tag_id_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "tag_id" in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/update/tag_id/", methods=["PUT"])
def server_update_tag_id_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	symptom_tag_relation_id = request.form.get('symptom_tag_relation_id')
	if (validate_symptom_tag_relation_id_from_symptom_tag_relations(symptom_tag_relation_id) == False):
		return dumps({'_error':'symptom_tag_relation_id is invalid'})
	return dumps({})



# Delete record of "tag_id" in table "symptom_tag_relations" 
@app.route("/symptom_tag_relations/delete/tag_id/", methods=["DELETE"])
def server_delete_tag_id_symptom_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	symptom_tag_relation_id = request.form.get('symptom_tag_relation_id')
	if (validate_symptom_tag_relation_id_from_symptom_tag_relations(symptom_tag_relation_id) == False):
		return dumps({'_error':'symptom_tag_relation_id is invalid'})
	return dumps({})



"""
=========== DOCTOR_TAG_RELATIONS ===========
"""


# Create a new entry /row in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/insert/", methods=["POST"])
def server_create_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr



# Delete a entry /row in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/delete/", methods=["DELETE"])
def server_create_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Get record of "doctor_id" in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/select/doctor_id/", methods=["GET"])
def server_select_doctor_id_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "doctor_id" in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/insert/doctor_id/", methods=["POST"])
def server_insert_doctor_id_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "doctor_id" in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/update/doctor_id/", methods=["PUT"])
def server_update_doctor_id_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_tag_relation_id = request.form.get('doctor_tag_relation_id')
	if (validate_doctor_tag_relation_id_from_doctor_tag_relations(doctor_tag_relation_id) == False):
		return dumps({'_error':'doctor_tag_relation_id is invalid'})
	return dumps({})



# Delete record of "doctor_id" in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/delete/doctor_id/", methods=["DELETE"])
def server_delete_doctor_id_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_tag_relation_id = request.form.get('doctor_tag_relation_id')
	if (validate_doctor_tag_relation_id_from_doctor_tag_relations(doctor_tag_relation_id) == False):
		return dumps({'_error':'doctor_tag_relation_id is invalid'})
	return dumps({})



# Get record of "tag_id" in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/select/tag_id/", methods=["GET"])
def server_select_tag_id_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "tag_id" in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/insert/tag_id/", methods=["POST"])
def server_insert_tag_id_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "tag_id" in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/update/tag_id/", methods=["PUT"])
def server_update_tag_id_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_tag_relation_id = request.form.get('doctor_tag_relation_id')
	if (validate_doctor_tag_relation_id_from_doctor_tag_relations(doctor_tag_relation_id) == False):
		return dumps({'_error':'doctor_tag_relation_id is invalid'})
	return dumps({})



# Delete record of "tag_id" in table "doctor_tag_relations" 
@app.route("/doctor_tag_relations/delete/tag_id/", methods=["DELETE"])
def server_delete_tag_id_doctor_tag_relations():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	doctor_tag_relation_id = request.form.get('doctor_tag_relation_id')
	if (validate_doctor_tag_relation_id_from_doctor_tag_relations(doctor_tag_relation_id) == False):
		return dumps({'_error':'doctor_tag_relation_id is invalid'})
	return dumps({})



"""
=========== TAGS ===========
"""


# Create a new entry /row in table "tags" 
@app.route("/tags/insert/", methods=["POST"])
def server_create_tags():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr



# Delete a entry /row in table "tags" 
@app.route("/tags/delete/", methods=["DELETE"])
def server_create_tags():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Get record of "tag_name" in table "tags" 
@app.route("/tags/select/tag_name/", methods=["GET"])
def server_select_tag_name_tags():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "tag_name" in table "tags" 
@app.route("/tags/insert/tag_name/", methods=["POST"])
def server_insert_tag_name_tags():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "tag_name" in table "tags" 
@app.route("/tags/update/tag_name/", methods=["PUT"])
def server_update_tag_name_tags():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	tag_id = request.form.get('tag_id')
	if (validate_tag_id_from_tags(tag_id) == False):
		return dumps({'_error':'tag_id is invalid'})
	return dumps({})



# Delete record of "tag_name" in table "tags" 
@app.route("/tags/delete/tag_name/", methods=["DELETE"])
def server_delete_tag_name_tags():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	tag_id = request.form.get('tag_id')
	if (validate_tag_id_from_tags(tag_id) == False):
		return dumps({'_error':'tag_id is invalid'})
	return dumps({})



"""
=========== BOOKING_EVENTS ===========
"""


# Create a new entry /row in table "booking_events" 
@app.route("/booking_events/insert/", methods=["POST"])
def server_create_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr



# Delete a entry /row in table "booking_events" 
@app.route("/booking_events/delete/", methods=["DELETE"])
def server_create_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Get record of "start_time" in table "booking_events" 
@app.route("/booking_events/select/start_time/", methods=["GET"])
def server_select_start_time_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "start_time" in table "booking_events" 
@app.route("/booking_events/insert/start_time/", methods=["POST"])
def server_insert_start_time_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "start_time" in table "booking_events" 
@app.route("/booking_events/update/start_time/", methods=["PUT"])
def server_update_start_time_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Delete record of "start_time" in table "booking_events" 
@app.route("/booking_events/delete/start_time/", methods=["DELETE"])
def server_delete_start_time_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Get record of "end_time" in table "booking_events" 
@app.route("/booking_events/select/end_time/", methods=["GET"])
def server_select_end_time_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "end_time" in table "booking_events" 
@app.route("/booking_events/insert/end_time/", methods=["POST"])
def server_insert_end_time_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "end_time" in table "booking_events" 
@app.route("/booking_events/update/end_time/", methods=["PUT"])
def server_update_end_time_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Delete record of "end_time" in table "booking_events" 
@app.route("/booking_events/delete/end_time/", methods=["DELETE"])
def server_delete_end_time_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Get record of "reference" in table "booking_events" 
@app.route("/booking_events/select/reference/", methods=["GET"])
def server_select_reference_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "reference" in table "booking_events" 
@app.route("/booking_events/insert/reference/", methods=["POST"])
def server_insert_reference_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "reference" in table "booking_events" 
@app.route("/booking_events/update/reference/", methods=["PUT"])
def server_update_reference_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Delete record of "reference" in table "booking_events" 
@app.route("/booking_events/delete/reference/", methods=["DELETE"])
def server_delete_reference_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Get record of "doctor_id" in table "booking_events" 
@app.route("/booking_events/select/doctor_id/", methods=["GET"])
def server_select_doctor_id_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "doctor_id" in table "booking_events" 
@app.route("/booking_events/insert/doctor_id/", methods=["POST"])
def server_insert_doctor_id_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "doctor_id" in table "booking_events" 
@app.route("/booking_events/update/doctor_id/", methods=["PUT"])
def server_update_doctor_id_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Delete record of "doctor_id" in table "booking_events" 
@app.route("/booking_events/delete/doctor_id/", methods=["DELETE"])
def server_delete_doctor_id_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Get record of "submission_id" in table "booking_events" 
@app.route("/booking_events/select/submission_id/", methods=["GET"])
def server_select_submission_id_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.args.get('token')



# Create record of "submission_id" in table "booking_events" 
@app.route("/booking_events/insert/submission_id/", methods=["POST"])
def server_insert_submission_id_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')



# Change record of "submission_id" in table "booking_events" 
@app.route("/booking_events/update/submission_id/", methods=["PUT"])
def server_update_submission_id_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



# Delete record of "submission_id" in table "booking_events" 
@app.route("/booking_events/delete/submission_id/", methods=["DELETE"])
def server_delete_submission_id_booking_events():
	cookie = request.cookies.get("_s")
	ip_addr = flask.request.remote_addr
	token = request.form.get('token')
	booking_event_id = request.form.get('booking_event_id')
	if (validate_booking_event_id_from_booking_events(booking_event_id) == False):
		return dumps({'_error':'booking_event_id is invalid'})
	return dumps({})



