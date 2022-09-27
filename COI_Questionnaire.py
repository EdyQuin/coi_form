import streamlit as st
from deta import Deta
st.image('./SLP_LOGO.png')
# Data to be written to Deta Base
with st.form("form"):
    age = st.number_input("Your age")
    email = st.text_input("Your email")
    phone_number = st.text_input("Your phone number")
    one = st.text_input("Does your spouse agree on how you want to dispose of your home?")
    two = st.text_input("Does your spouse agree on how you want to dispose of your bank accounts?")
    three = st.text_input("Does your spouse agree on how you want to dispose of your jewelry?")
    four = st.text_input("Does your spouse agree on how you want to dispose of your personal property?")
    five = st.text_input("Does your spouse agree on how you want to dispose of your property?")
    six = st.text_input("Do you agree with how your spouse wants to dispose of his/her home?")
    seven = st.text_input("Do you agree with how your spouse wants to dispose of his/her bank accounts")
    eight = st.text_input("Do you agree with how your spouse wants to dispose of his/her jewelry")
    nine = st.text_input("Do you agree with how your spouse wants to dispose of his/her personal property")
    ten = st.text_input("Do you agree with how your spouse wants to dispose of his/her property")
    submitted = st.form_submit_button("Save in database")
    clear_on_submit=True
# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("LawTech_COI")
# If the user clicked the submit button
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "age": age, "email": email, "telephone": telephone, 
            "qe": qe, "qf": qf, "qg": qg, "qh": qh, "qi": qi,
           "qj": qj, "qk": qk, "ql": ql, "qm": qm, "qn": qn})
    if submitted:
        st.write("Your answers have been successfully received. For any questions or concerns please contact the office @ asanchez@sanchezlp.com. Please close your browser when you are finished.")
"---"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(query=None, limit=None, last=None).items

