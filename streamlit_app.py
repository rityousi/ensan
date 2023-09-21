# Streamlitライブラリをインポート
import streamlit as st
import random

st.title("分野ガチャ")
if st.button("分野を決める"):
   results = ["代数学","解析学","幾何学"]
   result = random.choice(results)
   st.write(f"結果:幾何学")