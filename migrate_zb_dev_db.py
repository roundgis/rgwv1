import sqlite3
import rg_lib
import models


def main(src_db, target_db):
    with rg_lib.DbConnWrap(sqlite3.connect(src_db, check_same_thread=False)) as conn1:
        conn1.conn_obj.execute("BEGIN")
        with rg_lib.DbConnWrap(sqlite3.connect(target_db, check_same_thread=False)) as conn2:
            conn2.conn_obj.execute("BEGIN")
            models.ZbDevice.Init(conn2.conn_obj)
            for row in conn1.conn_obj.execute("select id,nid,moduleid,name,cts,device_no,remark from rxg_zb_device"):
                print(row)
                conn2.conn_obj.execute("insert or ignore into rgw_zb_device(id,nid,moduleid,name,cts,device_no,remark) values(?,?,?,?,?,?,?)",
                                       (row[0],row[1],row[2],row[3],row[4],row[5], row[6] if row[6] else ''))


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])


