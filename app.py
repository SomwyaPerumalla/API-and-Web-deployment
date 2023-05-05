import uvicorn
from fastapi import FastAPI
from Features import features
import numpy as np
import pickle
import pandas as pd
app = FastAPI()
model = pickle.load(open('Model_pox.pkl', 'rb'))
@app.get('/')
def index():
    return {'message': 'Hello, Welcome'}

@app.post("/predict")
def predict_pox(data:features):
    data=data.dict()
    Rectal_Pain=data['Rectal_Pain']
    Sore_Throat=data['Sore_Throat']
    Penile_Oedema=data['Penile_Oedema']
    Oral_Lesions=data['Oral_Lesions']
    Solitary_Lesion=data['Solitary_Lesion']
    Swollen_Tonsils=data['Swollen_Tonsils']
    HIV_Infection=data['HIV_Infection']
    Sexually_Transmitted_Infection=data['Sexually_Transmitted_Infection']
    Fever=data['Fever']
    Pains=data['Pains']
    Lymph_Nodes=data['Lymph_Nodes']
    prediction=model.predict([[Rectal_Pain,Sore_Throat,Penile_Oedema,Oral_Lesions,Solitary_Lesion,Swollen_Tonsils,HIV_Infection,Sexually_Transmitted_Infection,Fever,Pains,Lymph_Nodes]])  
    print(prediction)
        
    if prediction[0]==0:
        prediction="Congratulations you dont have any monkey-pox symptoms"
    else:
        prediction="Sorry you are like to have Monkey-pox please check with doctor"
    
if __name__ == '__main__':
    uvicorn.run(app, host='192.168.0.37', port=61622)