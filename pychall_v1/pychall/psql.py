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

# @contextmanager
# class dbcontextmanager:
#     def __init__(self, gen):
#         print(f"{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
#         self.gen = gen
#         print(f"gen : {gen}")
#
#     def __call__(self, user, dbname):
#         print(f"{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
#         self.user, self.dbname = user, dbname
#         return self
#
#     def __enter__(self):
#         print(f"{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
#         conn = psycopg2.connect(user=self.user)
#
#     def __exit__(self, *_, **__):
#         print(f"{'='*50} {__class__.__name__} | {inspect.stack()[0][3]}")
#         try:
#             print("try next(geni)")
#             next(self.geni)
#         except StopIteration:
#             print('StopIteration')
#             pass

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

@contextmanager
def tblgen(conn):
    print(f"\n{'='*50} {__name__} | {inspect.stack()[0][3]}")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    try:
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

def initdbs(dbnames=['Place','Person']):
    for dbname in dbnames:
        db = DataBase()
        db.createdb(dbname=dbname)

class Model:

    def __init__(self, dbname, modelcls):
        self.user = os.environ['PSQL_USER']
        self.dbname = dbname.lower()
        self.modelname = modelcls.__name__.lower()

    def oneway_op(self, sql):
        whoiam = f"{__class__} | {inspect.stack()[0][3]}"
        conn = psycopg2.connect(user=self.user, dbname=self.dbname)
        with tblgen(conn=conn):
            cur = conn.cursor()
            try:
                cur.execute(sql)
            except Exception as e:
                print(f"{'#'*50} {whoiam}\nException : {e}")
            else:
                print(f"{'*'*50} {whoiam}\nCompleted operation( {sql} ).")

    def oneway_ops(self, sqls):
        whoiam = f"{__class__} | {inspect.stack()[0][3]}"
        conn = psycopg2.connect(user=self.user, dbname=self.dbname)
        with tblgen(conn=conn):
            cur = conn.cursor()
            try:
                for sql in sqls:
                    cur.execute(sql)
            except Exception as e:
                print(f"{'#'*50} {whoiam}\nException : {e}")
            else:
                print(f"{'*'*50} {whoiam}\nCompleted operations( cnt:{len(sqls)} ).")

    def droptbl(self):
        sql = f"DROP TABLE {self.modelname};"
        self.oneway_op(sql=sql)

    def insert_one(self, sql):
        self.oneway_op(sql=sql)

    def insert_many(self, dics):
        sqls = []
        for d in dics:
            cols = f"({', '.join(d.keys())})"
            vals = tuple(str(e) for e in d.values())
            sql = f"INSERT INTO {self.modelname} {cols} VALUES {str(vals)}"
            sqls.append(sql)
        self.oneway_ops(sqls=sqls)

    def select(self, sql, size=0):
        whoiam = f"{__class__} | {inspect.stack()[0][3]}"
        conn = psycopg2.connect(user=self.user, dbname=self.dbname)
        with tblgen(conn=conn):
            cur = conn.cursor()
            try:
                cur.execute(query=sql)
            except Exception as e:
                print(f"{'#'*50} {whoiam}\nException : {e}")
            else:
                if size is 1:
                    rows = [cur.fetchone()]
                elif size > 1:
                    rows = cur.fetchmany(size=size)
                else:
                    rows = cur.fetchall()
                print(f"{'*'*50} {whoiam}\nCompleted select( {sql} ).")
                return rows

    def update_one(self, sql):
        self.oneway_op(sql=sql)

    def update_many(self, sqls):
        self.oneway_ops(sqls=sqls)
