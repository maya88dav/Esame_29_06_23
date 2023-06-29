#fastapi
from fastapi import FastAPI,Depends,HTTPException,status
import uvicorn
from pydantic import BaseModel
import joblib

app = FastAPI()

## Basemodel

class StartupData(BaseModel):
    rdSpend: float =73721
    administration: float = 121344
    marketingSpend: float = 211025


@app.on_event("startup")
def startup_event():
    global model    
    model = joblib.load("startup.pkl")
    print("Model Loaded")
    return model

@app.get("/")
def home():
    return {" ---->          http://localhost:8000/docs     <----------"}


@app.get("/predict")
async def predictget(data:StartupData=Depends()):
    try:
        X = [[data.rdSpend, data.administration, data.marketingSpend]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")
    


@app.post("/predict")
async def predictpost(data:StartupData):
    try:
        X = [[data.rdSpend, data.administration, data.marketingSpend]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")








if __name__ =="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)