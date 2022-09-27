import streamlit as st
from deta import Deta
st.image('./SLP_LOGO.png')
# Data to be written to Deta Base
with st.form("form"):
    aname = st.text_input("Your name")
    bage = st.number_input("Your age")
    cemail = st.text_input("Your email")
    dphone_number = st.text_input("Your phone number")
    eone = st.text_input("Does your spouse agree on how you want to dispose of your home?")
    ftwo = st.text_input("Does your spouse agree on how you want to dispose of your bank accounts?")
    gthree = st.text_input("Does your spouse agree on how you want to dispose of your jewelry?")
    hfour = st.text_input("Does your spouse agree on how you want to dispose of your personal property?")
    ifive = st.text_input("Does your spouse agree on how you want to dispose of your property?")
    jsix = st.text_input("Do you agree with how your spouse wants to dispose of his/her home?")
    kseven = st.text_input("Do you agree with how your spouse wants to dispose of his/her bank accounts")
    leight = st.text_input("Do you agree with how your spouse wants to dispose of his/her jewelry")
    mnine = st.text_input("Do you agree with how your spouse wants to dispose of his/her personal property")
    nten = st.text_input("Do you agree with how your spouse wants to dispose of his/her property")
    submitted = st.form_submit_button("Save in database")
    clear_on_submit=True
# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])
db = deta.Base("LawTech_COI")
# If the user clicked the submit button
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "age": age, "email": email, "phone number": phone_number, 
            "one": eone, "two": ftwo, "three": gthree, "four": hfour, "five": ifive,
           "six": jsix, "seven": kseven, "eight": leight, "nine": mnine, "ten": nten})
    if submitted:
        st.write("Your answers have been successfully received. For any questions or concerns please contact the office @ asanchez@sanchezlp.com. Please close your browser when you are finished.")
"---"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(query=None, limit=None, last=None).items

