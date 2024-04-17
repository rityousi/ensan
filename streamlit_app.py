import streamlit as st

# ページのタイトルを設定
st.title("アークナイツダメージシミュレータ")

# 選択可能な項目のリストを作成
options = ["アンジェリーナ", "イフリータ", "エイヤフィヤトラ","エクシア","サリア","シルバーアッシュ","シージ","ホシグマ"]

# 選択された項目を受け取るセレクトボックスを表示
selected_option = st.selectbox("キャラクターを選択してください", options)

# 選択された項目に応じて対応する内容を表示
if selected_option == "アンジェリーナ":
    options = ["秘杖・急収束","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "秘杖・急収束":
        st.write("攻撃力+110%")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
    elif selected_option == "秘杖・微粒子":
        st.write("通常攻撃の間隔を超大幅に短縮し、45%の攻撃力で術攻撃を行う")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
    elif selected_option == "秘杖・反重力":
        st.write("敵全員に反重力状態を付与し、攻撃範囲拡大、攻撃力+150%、敵最大5体を同時に攻撃")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
elif selected_option == "イフリータ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
elif selected_option == "エイヤフィヤトラ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "エクシア":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "サリア":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "シルバーアッシュ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "シージ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "ホシグマ":
    options = ["迅速攻撃γ","波濤の裂刃","海嘯の悲歌"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "迅速攻撃γ":
        st.write("攻撃力+45%,攻撃速度+45")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","	遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)

