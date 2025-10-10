import models
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class ClientData(BaseModel):
    atm_trn_cnt_1: float = 5.0
    atm_trn_cnt: float = 3.0
    bt_trn_cnt_1: float = 2.0
    bt_trn_cnt: float = 1.0
    chq_trn_cnt_1: float = 0.0
    chq_trn_cnt: float = 0.0
    cc_trn_cnt_1: float = 8.0
    cc_trn_cnt: float = 10.0
    elt_trn_cnt_1: float = 1.0
    elt_trn_cnt: float = 2.0
    ht_trn_cnt_1: float = 0.0
    ht_trn_cnt: float = 0.0
    it_trn_cnt_1: float = 0.0
    pos_trn_cnt_1: float = 15.0
    pos_trn_cnt: float = 12.0
    trd_trn_cnt_1: float = 3.0
    trd_trn_cnt: float = 4.0
    acc_credit: float = 50000.0
    acc_funds: float = 15000.0
    cc_appr_amt: float = 100000.0
    cc_avg_bal: float = 25000.0
    cc_avg_bal_1: float = 23000.0
    cc_min_bal: float = 5000.0
    chq_acc_ind: float = 1.0
    cust_age: float = 45.0
    days_brtday: float = 120.0
    cc_ea_open_mth: float = 24.0
    sa_ea_open_mth: float = 36.0
    tr_ea_open_mth: float = 18.0
    enq_trn_cnt: float = 2.0
    equity_amt: float = 500000.0
    recency: float = 30.0
    fol_l_clos_mth: float = 0.0
    fol_l_open_mth: float = 2.0
    sa_la_clos_mth: float = 0.0
    sa_la_open_mth: float = 6.0
    tr_la_clos_mth: float = 0.0
    tr_la_open_mth: float = 3.0
    cust_class: float = 2.0
    dep_max_amt: float = 20000.0
    ch_addr: float = 0.0
    ch_marital: float = 0.0
    npv_savings: float = 150000.0
    npv_trans: float = 50000.0
    depos_count: float = 5.0
    joint_acc_cnt: float = 1.0
    prod_count: float = 8.0
    sav_acc_count: float = 2.0
    tra_acc_count: float = 1.0
    wthdr_count: float = 20.0
    avg_bal: float = 30000.0
    rel_age: float = 45.0
    sav_avg_bal_1: float = 15000.0
    sav_avg_bal: float = 18000.0
    avg_bal_1: float = 28000.0
    npv_total: float = 200000.0
    tra_avg_bal_1: float = 12000.0
    tra_avg_bal: float = 15000.0
    tr_min_bal: float = 5000.0
    tra_auth_no: float = 2.0
    tra_auth_yes: float = 18.0
    call_trn_cnt_1: float = 3.0
    Change_In_ATM_TR: float = 0.5


model = joblib.load("models/best_churn_model.pkl")

@app.post("/predict")
def predict_churn(data: ClientData):
    try:
        input_data = {
             "atm_trn_cnt_1": [data.atm_trn_cnt_1],
            "atm_trn_cnt": [data.atm_trn_cnt],
            "bt_trn_cnt_1": [data.bt_trn_cnt_1],
            "bt_trn_cnt": [data.bt_trn_cnt],
            "chq_trn_cnt_1": [data.chq_trn_cnt_1],
            "chq_trn_cnt": [data.chq_trn_cnt],
            "cc_trn_cnt_1": [data.cc_trn_cnt_1],
            "cc_trn_cnt": [data.cc_trn_cnt],
            "elt_trn_cnt_1": [data.elt_trn_cnt_1],
            "elt_trn_cnt": [data.elt_trn_cnt],
            "ht_trn_cnt_1": [data.ht_trn_cnt_1],
            "ht_trn_cnt": [data.ht_trn_cnt],
            "it_trn_cnt_1": [data.it_trn_cnt_1],
            "pos_trn_cnt_1": [data.pos_trn_cnt_1],
            "pos_trn_cnt": [data.pos_trn_cnt],
            "trd_trn_cnt_1": [data.trd_trn_cnt_1],
            "trd_trn_cnt": [data.trd_trn_cnt],
            "acc_credit": [data.acc_credit],
            "acc_funds": [data.acc_funds],
            "cc_appr_amt": [data.cc_appr_amt],
            "cc_avg_bal": [data.cc_avg_bal],
            "cc_avg_bal_1": [data.cc_avg_bal_1],
            "cc_min_bal": [data.cc_min_bal],
            "chq_acc_ind": [data.chq_acc_ind],
            "cust_age": [data.cust_age],
            "days_brtday": [data.days_brtday],
            "cc_ea_open_mth": [data.cc_ea_open_mth],
            "sa_ea_open_mth": [data.sa_ea_open_mth],
            "tr_ea_open_mth": [data.tr_ea_open_mth],
            "enq_trn_cnt": [data.enq_trn_cnt],
            "equity_amt": [data.equity_amt],
            "recency": [data.recency],
            "fol_l_clos_mth": [data.fol_l_clos_mth],
            "fol_l_open_mth": [data.fol_l_open_mth],
            "sa_la_clos_mth": [data.sa_la_clos_mth],
            "sa_la_open_mth": [data.sa_la_open_mth],
            "tr_la_clos_mth": [data.tr_la_clos_mth],
            "tr_la_open_mth": [data.tr_la_open_mth],
            "cust_class": [data.cust_class],
            "dep_max_amt": [data.dep_max_amt],
            "ch_addr": [data.ch_addr],
            "ch_marital": [data.ch_marital],
            "npv_savings": [data.npv_savings],
            "npv_trans": [data.npv_trans],
            "depos_count": [data.depos_count],
            "joint_acc_cnt": [data.joint_acc_cnt],
            "prod_count": [data.prod_count],
            "sav_acc_count": [data.sav_acc_count],
            "tra_acc_count": [data.tra_acc_count],
            "wthdr_count": [data.wthdr_count],
            "avg_bal": [data.avg_bal],
            "rel_age": [data.rel_age],
            "sav_avg_bal_1": [data.sav_avg_bal_1],
            "sav_avg_bal": [data.sav_avg_bal],
            "avg_bal_1": [data.avg_bal_1],
            "npv_total": [data.npv_total],
            "tra_avg_bal_1": [data.tra_avg_bal_1],
            "tra_avg_bal": [data.tra_avg_bal],
            "tr_min_bal": [data.tr_min_bal],
            "tra_auth_no": [data.tra_auth_no],
            "tra_auth_yes": [data.tra_auth_yes],
            "call_trn_cnt_1": [data.call_trn_cnt_1],
            "Change_In_ATM_TR": [data.Change_In_ATM_TR]
        }

        df = pd.DataFrame(input_data)
        df = df.fillna(0)

        probability = model.predict_proba(df)[0,1]
        prediction = probability > 0.5
        return{
            "churn_probability": round(probability,2),
            "will_churn": bool(prediction),
            "status": "success"
        }
    except Exception as e:
        return{
            "churn_probability": 0.0,
            "will_churn": False,
            "status": "error",
            "error": str(e)
        }

@app.get("/features")
def get_features():
    return {
        "total_features": 63,
        "features": list(ClientData.__fields__.keys())
    }

@app.get("/")
def health_check():
    return {"status": "API is working", "model_loaded": True}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)