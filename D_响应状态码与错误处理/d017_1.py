# -*- coding: UTF-8 -*-
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item}")
async def read_item(item: str):
    if item not in items:
        #自定义错误
        raise HTTPException(status_code=404, detail="Item not found")
    pass
    pass
    return {"item": items[item]}

# 添加自定义标题
@app.get("/items-header/{item}")
async def read_item_header(item: str):
    if item not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"}, 
            # X-Error 自定义。例如，对于某些类型的安全性。
            # OAuth 2.0和某些安全实用程序在内部需要/使用此功能。
        )
    return {"item": items[item]}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)