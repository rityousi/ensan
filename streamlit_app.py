import streamlit as st

# ページのタイトルを設定
st.title("アークナイツダメージシミュレータ")

# 選択可能な項目のリストを作成
options = ["スカジ", "スペクター", "チェン"]

# 選択された項目を受け取るセレクトボックスを表示
selected_option = st.selectbox("キャラクターを選択してください", options)

# 選択された項目に応じて対応する内容を表示
if selected_option == "アンジェリーナ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
    elif selected_option == "波濤の裂刃":
        st.write("配置後30秒間、攻撃力+170%")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
    elif selected_option == "海嘯の悲歌":
        st.write("攻撃力、防御力、最大HP+130%")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "イフリータ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "エイヤフィヤトラ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "エクシア":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "サリア":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "シルバーアッシュ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "シージ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "ホシグマ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","兵士","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)

