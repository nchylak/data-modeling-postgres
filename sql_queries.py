# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS times;"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time timestamp references times(start_time) NOT NULL,
        user_id int references users(user_id) NOT NULL,
        level varchar,
        song_id varchar references songs(song_id),
        artist_id varchar references artists(artist_id),
        session_id varchar,
        location varchar,
        user_agent varchar
        );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id int PRIMARY KEY,
        first_name varchar,
        last_name varchar,
        gender varchar,
        level varchar
        );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id varchar PRIMARY KEY,
        title varchar,
        artist_id varchar,
        year int,
        duration float
        );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id varchar PRIMARY KEY,
        name varchar,
        location varchar,
        latitude float,
        longitude float
        );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS times (
        start_time timestamp PRIMARY KEY,
        hour int,
        day int,
        week int,
        month int,
        year int,
        weekday int
        );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id)
    DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE
        SET 
            first_name  = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            gender  = EXCLUDED.gender,
            level = EXCLUDED.level
    ;
""")

song_table_insert = ("""
    INSERT INTO songs
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO NOTHING;
""")

time_table_insert = ("""
    INSERT INTO times
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT
        songs.song_id,
        songs.artist_id
    FROM songs
    LEFT JOIN artists ON artists.artist_id = songs.artist_id
    WHERE
        songs.title = %s
        AND artists.name = %s
        AND ABS(songs.duration - %s) < 5;       
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]