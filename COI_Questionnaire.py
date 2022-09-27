import streamlit as st
from deta import Deta
st.image('./SLP_LOGO.png')
# Data to be written to Deta Base
with st.form("form"):
    a_name = st.text_input("Your name")
    b_age = st.number_input("Your age")
    c_email = st.text_input("Your email")
    d_phone_number = st.text_input("Your phone number")
    e_one = st.text_input("Does your spouse agree on how you want to dispose of your home?")
    f_two = st.text_input("Does your spouse agree on how you want to dispose of your bank accounts?")
    g_three = st.text_input("Does your spouse agree on how you want to dispose of your jewelry?")
    h_four = st.text_input("Does your spouse agree on how you want to dispose of your personal property?")
    i_five = st.text_input("Does your spouse agree on how you want to dispose of your property?")
    j_six = st.text_input("Do you agree with how your spouse wants to dispose of his/her home?")
    k_seven = st.text_input("Do you agree with how your spouse wants to dispose of his/her bank accounts")
    l_eight = st.text_input("Do you agree with how your spouse wants to dispose of his/her jewelry")
    m_nine = st.text_input("Do you agree with how your spouse wants to dispose of his/her personal property")
    n_ten = st.text_input("Do you agree with how your spouse wants to dispose of his/her property")
    submitted = st.form_submit_button("Save in database")
    clear_on_submit=True
# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("LawTech_COI")
# If the user clicked the submit button
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": a_name, "age": b_age, "email": c_email, "phone number": d_phone_number, 
            "one": e_one, "two": f_two, "three": g_three, "four": h_four, "five": i_five,
           "six": j_six, "seven": k_seven, "eight": l_eight, "nine": m_nine, "ten": n_ten})
    if submitted:
        st.write("Your answers have been successfully received. For any questions or concerns please contact the office @ asanchez@sanchezlp.com. Please close your browser when you are finished.")
"---"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(query=None, limit=None, last=None).items

