# Streamlitライブラリをインポート
import streamlit as st
import random

st.title("志望校ガチャ")
if st.button("志望校を決める"):
   results = ["代数学","解析学","幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学","位相幾何学"]
   result = random.choice(results)
   st.write(f"結果:日本文理大学")