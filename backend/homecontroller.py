from fastapi import FastAPI
from fastapi.responses import JSONResponse
from product.productDAO import productDAO

app=FastAPI()
nDAO=productDAO()

@app.get("/user.reg")
def userReg(ID,PW):
    result=nDAO.reg(ID,PW) 
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result, headers=h)

@app.get("/product.get")
def userGet():
    result=nDAO.get()
    h={"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result, headers=h)

@app.get("/dbtest")
def db_test():
    return nDAO.test_connection()

@app.get("/product.reg")
def product_regg(
    p_id:int,
    p_name: str,
    p_brand_id: int,
    p_category_id: int,
    p_price: int,
    p_image: str,
    p_location: str
):
    print("받은 값:",p_id, p_name, p_brand_id, p_category_id, p_price, p_image, p_location)
    result = nDAO.product_reg(p_id,p_name, p_brand_id, p_category_id, p_price, p_image, p_location)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)
