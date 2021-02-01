module: library

depends:
- tp/libs/sqlite3

inc_dirs:
- tp/libs/sqlite3
- tp/libs/python/src/Include

c_flags:
- -DMODULE_NAME="sqlite3"
- -w

srcs:
- module.c
- util.c
- cursor.c
- cache.c
- statement.c
- prepare_protocol.c
- row.c
- microprotocols.c
- connection.c
