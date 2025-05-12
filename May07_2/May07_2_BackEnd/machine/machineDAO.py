from datetime import datetime
from kwon.kwonDBManager import KwonDBManager

class MachineDAO:
    def get(self):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.201:1521/xe")

            sql = "select * from may07_deepracer_machine "
            sql += "order by dm_check_date desc"

            cur.execute(sql)
            # for m in cur:
            #     print(m[0], m[1], m[2], m[3])
            machines = []
            for no, color, status, checkDate in cur:
                m = {
                    "no": no,
                    "color": color,
                    "status": status,
                    "checkDate": datetime.strftime(checkDate, "%Y/%m/%d %H:%M"),
                }
                machines.append(m)
            return machines
        except:
            return {"result": "조회 실패"}
        finally:
            KwonDBManager.closeConCur(con, cur)

    def reg(self, color, status):
        try:
            con, cur = KwonDBManager.makeConCur("kwon/1@195.168.9.201:1521/xe")

            sql = "insert into may07_deepracer_machine values( "
            sql += "may07_deepracer_machine_seq.nextval, "
            sql += "'%s', '%s', sysdate) " % (color, status)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"result": color + "색 머신 등록 완료"}
            return {"result": "등록 실패"}
        except:
            return {"result": "등록 실패"}
        finally:
            KwonDBManager.closeConCur(con, cur)
