from DBconnectLibrary.kimDBmanager import kimDBmanager
class productDAO:
    def get(self):
        con, cur = None, None  # 초기화
        try:
            con, cur = kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            sql = "SELECT * FROM product_M ORDER BY p_name DESC"

            cur.execute(sql)
            products = []
            for p_id, p_name, p_brand_id, p_category_id, p_price, p_image, p_location in cur:
                p = {
                    "p_id": p_id,
                    "p_brand_id": p_brand_id,
                    "p_category_id": p_category_id,
                    "p_price": p_price,
                    "p_image": p_image,
                    "p_location": p_location,
                    "p_name": p_name
                }
                products.append(p)
            return products
        except Exception as e:
            print("조회 실패:", e)
            return {"result": "조회 실패"}
        finally:
            if con and cur:
                kimDBmanager.closeConCur(con, cur)

   # 함수세팅에 self뻬먹지말기!!!!
    def product_reg(self,p_id, p_name, p_brand_id, p_category_id, p_price, p_image, p_location):
 
        con, cur = None, None
        try:
            con, cur = kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            print("INSERT 실행 전")
            cur.execute("""
                INSERT INTO product_M 
                (p_id, p_name, p_brand_id, p_category_id, p_price, p_image, p_location)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, (p_id, p_name, p_brand_id, p_category_id, p_price, p_image, p_location))
            print("INSERT 실행 후")
            con.commit()
            print("커밋 완료")

        except Exception as e:
            print("DB INSERT 실패:", e)
            return {"result": "조회 실패"}
        finally:
            if con and cur:
                kimDBmanager.closeConCur(con, cur)
                
# 함수세팅에 self뻬먹지말기!!!!
    def user_reg(self, id,pw):
        con, cur = None, None
        try:
            con, cur = kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            print("INSERT 실행 전")
            print(id)
            print(pw)
            cur.execute("""
                INSERT INTO musinsaUser 
                (m_id,m_pw)
                VALUES (:1, :2)
            """, (id,pw))
            print("INSERT 실행 후")
            con.commit()
            print("커밋 완료")

        except Exception as e:
            print("DB INSERT 실패:", e)
            return {"result": "조회 실패"}
        finally:
            if con and cur:
                kimDBmanager.closeConCur(con, cur)



    def test_connection(self):
        con, cur = None, None
        try:
            con, cur = kimDBmanager.makeConCur("KIMCR/1@195.168.9.126:1521/xe")
            print("✅ 오라클 DB 연결 성공!")
            return {"result": "연결 성공"}
        except Exception as e:
            print("❌ DB 연결 실패:", e)
            return {"result": f"연결 실패: {e}"}
        finally:
            if con and cur:
                kimDBmanager.closeConCur(con, cur)

