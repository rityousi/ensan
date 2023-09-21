# Streamlitライブラリをインポート
import streamlit as st
import random

st.title("おみくじアプリ")
if st.button("おみくじを引く"):
   results = ["代数学","解析学","幾何学","幾何学","幾何学","幾何学"]
   result = random.choice(results)
   st.write(f"結果:{result}")