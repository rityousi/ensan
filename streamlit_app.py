# Streamlitライブラリをインポート
import streamlit as st
import random

st.title("分野決定ガチャ")
if st.button("分野を決める"):
   results = ["代数学","解析学","幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学"]
   result = random.choice(results)
   st.write(f"結果:位相幾何学")