# Code provided by HBO-ICT
from configparser import ConfigParser
from flask import current_app, g
import mysql.connector

# Connector is specifically well suited to work with Oege. See https://dev.mysql.com/doc/connector-python/en/
# Replace it with https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/ when using the MariaDB Docker image
# Alternative: use SQLAlchemy ORM. See documentation online for explanation.

def read_db_config(filename, section='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        return dict(parser.items(section))
    raise Exception(f'section \'{section}\' does not exist in file \'{filename}\'')

def get_db():
    if 'db' not in g:
        config = current_app.config['MYSQL_CONFIG']
        g.db = mysql.connector.connect(**config)
    return g.db

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def prepare_values(values) -> tuple:
    return values if values is None or isinstance(values, tuple) else (values,)

def execute_query(query, values=None):
    try:
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(query, prepare_values(values))
        cursor.close()
        connection.commit()
    except Exception as exception:
        print(exception)

def select_all(query, values=None):
    try:
        connection = get_db()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, prepare_values(values))
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as exception:
        print(exception)

def select_one(query, values=None):
    try:
        connection = get_db()
        cursor = connection.cursor(dictionary=True, buffered=True)
        cursor.execute(query, prepare_values(values))
        result = cursor.fetchone()
        cursor.close()
        return result
    except Exception as exception:
        print(exception)
