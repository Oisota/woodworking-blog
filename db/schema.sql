CREATE TABLE IF NOT EXISTS "schema_migrations" (version varchar(128) primary key);
CREATE TABLE user (
	id integer primary key autoincrement,
	email text,
	password_hash text
);
CREATE TABLE post (
	id integer primary key autoincrement,
	title text not null,
	title_slug text not null,
	publish_date integer not null,
	body text not null
);
-- Dbmate schema migrations
INSERT INTO "schema_migrations" (version) VALUES
  ('20230520175922');
