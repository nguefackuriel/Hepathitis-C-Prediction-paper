import numpy as np
import streamlit as st
import pickle
#from GDA import GDA


# Load our mnodel
model_load = pickle.load(open('my_model_LGBM_hepatitisC.sav', 'rb'))

# Define a prediction function

def prediction_model(input_data):
    
    input_data_as_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_array.reshape(1,-1)

    prediction = model_load.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The patient is the Blood Donor"
    elif prediction[0] == 1:
        return 'The patient is a 0s=suspect Blood Donor'
    elif prediction[0] == 2:
        return 'The patient has 1=Hepatitis'
    elif prediction[0] == 3:
        return 'The patient has 2=Fibrosis'
    elif prediction[0] == 4:
        return 'The patient has 3=Cirrhosis'



def main():

    # Give a title to the App
    st.title('Hepatitis C prediction App')


    # Getting the Input from the user
    Age = st.text_input('Age of the patient')
    Sex = st.text_input('Sex of the patient(m/f)')
    ALB = st.text_input('ALB(Albumin) value')
    ALP = st.text_input('ALP(ALkaline Phosphatase) value')
    ALT = st.text_input('ALT(ALanine aminoTransferase) value')
    AST = st.text_input('AST(ASpartate aminotransferase) value')
    BIL = st.text_input('BIL(Bilirubin) Value')
    CHE = st.text_input('CHE(Choline Esterase) value')
    CHOL = st.text_input('CHOL(CHOLesterol) value')
    CREA = st.text_input('CREA(CREAtinine Blood test) value')
    GGT = st.text_input('GGT(Gamma-Glutamyl-Transferase) value')
    PROT = st.text_input('PROT(Total protein test) value')
    
    if Sex == 'm':
        Sex = '1'
    elif Sex == 'f':
        Sex == '0'
    

    # variable of prediction

    result = ''

    if st.button('Hepatitis C test result'):
        result = prediction_model([float(Age),str(Sex),float(ALB),float(ALP),float(ALT),float(AST),float(BIL),float(CHE),float(CHOL),float(CREA),float(GGT),float(PROT)])

    # Display the result
    st.success(result)

if __name__ == '__main__':
    main()
