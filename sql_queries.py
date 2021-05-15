# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY, 
    start_time time,
    user_id int , 
    level varchar NOT NULL, 
    song_id varchar , 
    artist_id varchar, 
    session_id int NOT NULL, 
    location varchar, 
    user_agent text    
);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
    user_id varchar CONSTRAINT users_pk PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar NOT NULL
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id varchar CONSTRAINT songs_pk PRIMARY KEY,
    title varchar,
    artist_id varchar,
    year int,
    duration FLOAT
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar CONSTRAINT artists_pk PRIMARY KEY,
    name varchar,
    location varchar,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time time,
    hour int,
    day varchar,
    week int,
    month int,
    year int,
    weekday int
    
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)

""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES(%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT song_id, b.artist_id
FROM songs a, artists b 
WHERE a.artist_id = b.artist_id
AND a.title = %s
AND b.name = %s
AND a.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]