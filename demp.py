# ESTABLISHING A CONNECTION

import psycopg2

connection=psycopg2.connect('dbname=example')

psycopg2.cursor = connection.cursor()

psycopg2.cursor.execute(
    '''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
    '''
)

psycopg2.cursor.execute(
    'INSERT INTO table2(id, completed) VALUES (1, True);'
)

connection.commit()

connection.close()
psycopg2.cursor.close()