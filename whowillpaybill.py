import streamlit as st
import random
friends=st.text_input("enter your friends names")
pay_bill=random.choice(friends)
st.write(pay_bill+" will pay the bill today")
