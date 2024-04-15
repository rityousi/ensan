import streamlit as st
import markovify

# Streamlitアプリのタイトルを設定
st.title("テキスト生成アプリ")

# テキスト入力ボックスを作成
user_input = st.text_input("テキストを入力してください:")

# テキスト生成のボタンを作成
generate_button = st.button("新しいテキストを生成する")

# テキスト生成関数
def generate_text(input_text):
    try:
        # 入力テキストからモデルを作成
        text_model = markovify.Text(input_text)
        # ランダムなテキストを生成
        generated_text = text_model.make_sentence()
        return generated_text
    except:
        return None

# ボタンがクリックされた場合
if generate_button:
    # 入力されたテキストを取得
    input_text = user_input.strip()  # 先頭と末尾の空白を削除
    # 入力されたテキストがある場合
    if input_text:
        # テキストを生成して表示
        generated_text = generate_text(input_text)
        if generated_text:
            st.write("生成されたテキスト:", generated_text)
        else:
            st.write("テキストを生成できませんでした。入力テキストの品質を確認してください。")
    else:
        st.write("入力されたテキストがありません。")


