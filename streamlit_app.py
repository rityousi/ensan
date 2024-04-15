import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

@st.cache
def find_similar_sentences(query, top_n=5):
    query_vector = tfidf_vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    similar_indices = cosine_similarities.argsort()[:-top_n:-1]
    return data.iloc[similar_indices]["text"].tolist()

def main():
    st.title("文章分析と生成アプリ")

    # データの読み込み
    data_file_path = "your_text_data.csv"  # テキストデータのファイルパスを指定
    data = load_data(data_file_path)

    # テキストデータの表示
    st.subheader("テキストデータ")
    st.dataframe(data)

    # TF-IDFベクトライザの作成
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(data["text"])

    # コサイン類似度の計算
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # 類似度の高い文章を表示
    st.subheader("類似度の高い文章を検索")
    query = st.text_input("検索クエリを入力してください:")
    if query:
        similar_sentences = find_similar_sentences(query)
        st.write(similar_sentences)

    # ランダムな文章の生成
    st.subheader("ランダムな文章の生成")
    generate_button = st.button("ランダムな文章を生成する")
    if generate_button:
        random_sentence = random.choice(data["text"].tolist())
        st.write(random_sentence)

if __name__ == "__main__":
    main()
