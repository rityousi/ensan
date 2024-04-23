import streamlit as st

# キャラクターのパラメータ
CHARACTER_PARAMS = {
    "アンジェリーナ": {"オリジムシ": 0, "機動盾隊長": 300, "軽装隊長": 500, "重装隊長": 1000, "遊撃隊盾兵隊長": 1500, "「最後の蒸気騎士」": 2000},
    "イフリータ": {"オリジムシ": 0, "機動盾隊長": 300, "軽装隊長": 500, "重装隊長": 1000, "遊撃隊盾兵隊長": 1500, "「最後の蒸気騎士」": 2000},
    "エイヤフィヤトラ": {"オリジムシ": 0, "機動盾隊長": 300, "軽装隊長": 500, "重装隊長": 1000, "遊撃隊盾兵隊長": 1500, "「最後の蒸気騎士」": 2000},
    "エクシア": {"オリジムシ": 0, "機動盾隊長": 300, "軽装隊長": 500, "重装隊長": 1000, "遊撃隊盾兵隊長": 1500, "「最後の蒸気騎士」": 2000},
    "シルバーアッシュ": {"オリジムシ": 0, "機動盾隊長": 300, "軽装隊長": 500, "重装隊長": 1000, "遊撃隊盾兵隊長": 1500, "「最後の蒸気騎士」": 2000},
    "シージ": {"オリジムシ": 0, "機動盾隊長": 300, "軽装隊長": 500, "重装隊長": 1000, "遊撃隊盾兵隊長": 1500, "「最後の蒸気騎士」": 2000},
    "ホシグマ": {"オリジムシ": 0, "機動盾隊長": 300, "軽装隊長": 500, "重装隊長": 1000, "遊撃隊盾兵隊長": 1500, "「最後の蒸気騎士」": 2000}
}

# ダメージ計算関数
def calculate_damage(character, skill, enemy, attack_power):
    if skill == "秘杖・急収束":
        attack_power *= 1.1
        damage_reduction = max(attack_power * 0.05, attack_power - CHARACTER_PARAMS[character][enemy])
        return damage_reduction
    elif skill == "秘杖・微粒子":
        # 秘杖・微粒子の処理
        pass
    elif skill == "秘杖・反重力":
        # 秘杖・反重力の処理
        pass
    # 他のスキルの処理も同様に追加

# ページのタイトルを設定
st.title("アークナイツダメージシミュレータ")

# 選択可能なキャラクターのリスト
options = list(CHARACTER_PARAMS.keys())

# 選択されたキャラクターを受け取るセレクトボックスを表示
selected_character = st.selectbox("キャラクターを選択してください", options)

# 選択されたキャラクターに応じて対応する内容を表示
if selected_character:
    # キャラクターのスキルを選択
    skills = ["秘杖・急収束", "秘杖・微粒子", "秘杖・反重力"]  # 他のキャラクターのスキルもここに追加
    selected_skill = st.selectbox("スキルを選択してください", skills)

    # 敵の選択
    enemies = ["オリジムシ", "機動盾隊長", "軽装隊長", "重装隊長", "遊撃隊盾兵隊長", "「最後の蒸気騎士」"]
    selected_enemy = st.selectbox("敵を選択してください(上から術耐性の低い順です)", enemies)

    # 攻撃力の入力
    attack_power = st.number_input("攻撃力を入力してください", value=1)

    # ダメージ計算と結果の表示
    if st.button("ダメージを計算する"):
        damage = calculate_damage(selected_character, selected_skill, selected_enemy, attack_power)
        st.write("ダメージ:", damage)
