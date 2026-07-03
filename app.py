import streamlit as st
import pickle
import numpy as np

# load model and scaler
model = pickle.load(open("ckd_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Chronic Kidney Disease Prediction")
st.header("Enter Patient Details")

# -------- Numerical Inputs --------
age = st.number_input("Age")
bp = st.number_input("Blood Pressure")

sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
al = st.selectbox("Albumin", [0,1,2,3,4,5])

bgr = st.number_input("Blood Glucose Random")
bu = st.number_input("Blood Urea")
sc = st.number_input("Serum Creatinine")

sod = st.number_input("Sodium")
pot = st.number_input("Potassium")

hemo = st.number_input("Hemoglobin")
pcv = st.number_input("Packed Cell Volume")

wbcc = st.number_input("White Blood Cell Count")
rbcc = st.number_input("Red Blood Cell Count")

# -------- Categorical Inputs --------
rbc = st.selectbox("Red Blood Cells", ["Normal","Abnormal"])
rbc = 1 if rbc == "Normal" else 0

pc = st.selectbox("Pus Cell", ["Normal","Abnormal"])
pc = 1 if pc == "Normal" else 0

pcc = st.selectbox("Pus Cell Clumps", ["Present","Not Present"])
pcc = 1 if pcc == "Present" else 0

ba = st.selectbox("Bacteria", ["Present","Not Present"])
ba = 1 if ba == "Present" else 0

htn = st.selectbox("Hypertension", ["Yes","No"])
htn = 1 if htn == "Yes" else 0

dm = st.selectbox("Diabetes Mellitus", ["Yes","No"])
dm = 1 if dm == "Yes" else 0

cad = st.selectbox("Coronary Artery Disease", ["Yes","No"])
cad = 1 if cad == "Yes" else 0

appet = st.selectbox("Appetite", ["Good","Poor"])
appet = 1 if appet == "Good" else 0

pe = st.selectbox("Pedal Edema", ["Yes","No"])
pe = 1 if pe == "Yes" else 0

ane = st.selectbox("Anemia", ["Yes","No"])
ane = 1 if ane == "Yes" else 0

# -------- Prediction --------
if st.button("Predict"):

    input_data = np.array([[
        age, bp, sg, al, rbc, pc, pcc, ba,
        bgr, bu, sc, sod, pot, hemo, pcv,
        wbcc, rbcc, htn, dm, cad, appet, pe, ane
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    if prediction == 0:
        st.error("CKD Detected")
    else:
        st.success("Not CKD")