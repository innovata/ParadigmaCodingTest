"""
This is PostgreSQL module.

You must set up the OS-Environment like below :

1. export PSQL_USER=[user_name]
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import sys
import inspect
from pychall import dbg
from contextlib import contextmanager


if 'PSQL_USER' not in list(os.environ):
    print(f"{'#'*50} {__name__}\nException Guide :{__doc__}")
    sys.exit(1)

def dbconnector(dbname):
    """Check if db exists & Connect to DB."""
    whoiam = f"{__name__} | {inspect.stack()[0][3]}"
    PSQL_USER = os.environ['PSQL_USER']
    try:
        conn = psycopg2.connect(user=PSQL_USER, dbname=dbname)
    except Exception as e:
        print(f"{'#'*50} {whoiam}\nException : {e}\nAutomatically switch to default DATABASE({PSQL_USER}).")
        conn = psycopg2.connect(user=PSQL_USER, dbname=PSQL_USER)
    return conn

@contextmanager
def dbgen(dbname, sql):
    whoiam = f"{__name__} | {inspect.stack()[0][3]}"
    print(f"\n{'='*50} {whoiam}")
    conn = dbconnector(dbname)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    try:
        cur = conn.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            print(f"{'#'*50} {whoiam}\nException : {e}")
        print('Start yield')
        yield
        print('End yield')
    finally:
        if conn:
            conn.close()

class DataBase:

    def __init__(self):
        self.user = os.environ['PSQL_USER']

    def createdb(self, dbname):
        sql = f"CREATE DATABASE {dbname};"
        with dbgen(dbname=self.user, sql=sql):
            print(f"Completed creating DB({dbname})")

    def dropdb(self, dbname):
        sql = f"DROP DATABASE {dbname};"
        with dbgen(dbname=self.user, sql=sql):
            print(f"Completed dropping DB({dbname})")

def create_dbs(dbnames=['places','people']):
    db = DataBase()
    for dbname in dbnames:
        db.createdb(dbname=dbname)

def drop_dbs(dbnames=['places','people']):
    db = DataBase()
    for dbname in dbnames:
        db.dropdb(dbname=dbname)
