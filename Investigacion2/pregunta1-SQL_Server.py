from os import getenv
import pymssql
server = getenv("127.0.0.1")
user = getenv("sa")
password = getenv("inicio")
db = pymssql.connect(server, user, password, "prog3")