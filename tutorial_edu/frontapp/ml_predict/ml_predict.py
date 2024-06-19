import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

class ML_Predict :
    ### 클래스 생성시 미리 처리할 함수 호출
    def __init__(self) :
        self.model_Load()
    
    ### 저장된 훈련모델 파일 불러들이기
    def model_Load(self) :
        save_path = "./frontapp/ml_predict/model/rf_model_joblib.md"
        self.rf_model = joblib.load(save_path)
        
    ### 임의 데이터로 예측하기
    def getModelPredict(self, random_data) :
        pred_Y = self.rf_model.predict(random_data)
        return pred_Y