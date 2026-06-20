import streamlit as st
import random
friends=["Anish","karthik","sai"]
pay_bill=random.choice(friends)
st.write(pay_bill+" will pay the bill today")
