# encoding: utf-8

DIALECT = 'mysql'
DRIVER  = 'mysqlconnector'
USERNAME= 'root'
PASSWORD= 'cf789456'
HOST    = '127.0.0.1'
PORT    = '3306'
DATABASE= 'db_for_first'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False