import streamlit as st

# ページのタイトルを設定
st.title("項目選択サンプル")

# 選択可能な項目のリストを作成
options = ["項目1", "項目2", "項目3"]

# 選択された項目を受け取るセレクトボックスを表示
selected_option = st.selectbox("項目を選択してください", options)

# 選択された項目に応じて対応する内容を表示
if selected_option == "項目1":
    st.write("項目1が選択されました。ここに項目1の内容を表示します。")
elif selected_option == "項目2":
    st.write("項目2が選択されました。ここに項目2の内容を表示します。")
elif selected_option == "項目3":
    st.write("項目3が選択されました。ここに項目3の内容を表示します。")



