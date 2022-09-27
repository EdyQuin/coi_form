import streamlit as st
from deta import Deta
st.image('./SLP_LOGO.png')
# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    qa = st.number_input("Your age")
    qb = st.text_input("Your email")
    qc = st.text_input("Your phone number")
    qd = st.text_input("Does your spouse agree on how you want to dispose of your home?")
    qe = st.text_input("Does your spouse agree on how you want to dispose of your bank accounts?")
    qf = st.text_input("Does your spouse agree on how you want to dispose of your jewelry?")
    qg = st.text_input("Does your spouse agree on how you want to dispose of your personal property?")
    qh = st.text_input("Does your spouse agree on how you want to dispose of your property?")
    qi = st.text_input("Do you agree with how your spouse wants to dispose of his/her home?")
    qj = st.text_input("Do you agree with how your spouse wants to dispose of his/her bank accounts")
    qk = st.text_input("Do you agree with how your spouse wants to dispose of his/her jewelry")
    ql = st.text_input("Do you agree with how your spouse wants to dispose of his/her personal property")
    qm = st.text_input("Do you agree with how your spouse wants to dispose of his/her property")
    submitted = st.form_submit_button("Save in database")
    clear_on_submit=True
# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("LawTech_COI")
# If the user clicked the submit button
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"qa": qa, "qb": qb, "qc": qc, "qd": qd, 
            "qe": qe, "qf": qf, "qg": qg, "qh": qh, "qi": qi,
           "qj": qj, "qk": qk, "ql": ql, "qm": qm, "qn": qn})
    if submitted:
        st.write("Your answers have been successfully received. For any questions or concerns please contact the office @ asanchez@sanchezlp.com. Please close your browser when you are finished.")
"---"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(query=None, limit=None, last=None).items

