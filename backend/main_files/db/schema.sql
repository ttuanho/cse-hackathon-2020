-- By
-- ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
-- ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
--    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
--    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
--    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
--    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 
                                                         
-- Email: ttuan.ho@outlook.com                                                         


drop table if exists doctors; 
create table doctors (
    doctor_id bigint,
    name varchar(100),
    license_code varchar(200),
    license_expiry_date varchar(20),
    qualification varchar(500),
    qualification_level varchar(100),

    primary key (doctor_id)
);

CREATE SEQUENCE doctor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

drop table if exists submissions; 
create table submissions (
    submission_id bigint,
    description varchar(1000),
    age int,
    gender varchar(20),
    client_email varchar(600),

    primary key (submission_id)
);

CREATE SEQUENCE submission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

drop table if exists symptoms; 
create table symptoms (
    symptom_id bigint,
    description varchar(1000),

    primary key (symptom_id)
);

CREATE SEQUENCE symptom_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

drop table if exists symptom_tag_relations; 
create table symptom_tag_relations (
    symptom_tag_relation_id bigint,
    symptom_id bigint,
    tag_id bigint,

    primary key (symptom_tag_relation_id),
    foreign key (symptom_id) references symptoms(symptom_id),
    foreign key (tag_id) references tags(tag_id)
);

CREATE SEQUENCE symptom_tag_relation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

drop table if exists doctor_tag_relations; 
create table doctor_tag_relations (
    doctor_tag_relation_id bigint,
    doctor_id bigint,
    tag_id bigint,

    primary key (doctor_tag_relation_id),
    foreign key (doctor_id) references doctors(doctor_id),
    foreign key (tag_id) references tags(tag_id)
);

CREATE SEQUENCE doctor_tag_relation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

drop table if exists tags; 
create table tags (
    tag_id bigint,
    tag_name varchar(200)

    primary key (tag_id)
);

CREATE SEQUENCE tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

drop table if exists booking_events; 
create table booking_events (
    booking_event_id bigint,
    start_time varchar(20),
    end_time varchar(20),
    description varchar(1000),
    reference varchar(2000), -- ie video url

    doctor_id bigint,
    submission_id bigint,

    primary key (booking_event_id),
    foreign key (doctor_id) references doctors(doctor_id),
    foreign key (submission_id) references submissions(submission_id)
);

CREATE SEQUENCE booking_event_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

