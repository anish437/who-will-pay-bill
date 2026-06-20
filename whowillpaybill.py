import streamlit as st
import random

friends_input = st.text_input("Enter friends' names, separated by commas")
friends = [f.strip() for f in friends_input.split(',') if f.strip()]
if friends:
    pay_bill = random.choice(friends)
    st.write(f"{pay_bill} will pay the bill today")
else:
    st.write("Please enter at least one name.")
