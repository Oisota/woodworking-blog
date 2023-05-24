-- migrate:up
create table user (
	id integer primary key autoincrement,
	email text,
	password_hash text
);

create table post (
	id integer primary key autoincrement,
	title text not null,
	title_slug text not null,
	publish_date integer not null,
	body text not null
);

-- migrate:down
drop table user;
drop table post;