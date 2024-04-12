# Streamlitライブラリをインポート
import streamlit as st

import datetime

# 曜日ごとの時間割を定義

timetables = {

"Monday":["9:00-10:00 Math", "10:00-11:00 Science", "11:00-12:00 English"],

"Tuesday":["9:00-10:00 History", "10:00-11:00 Math", "11:00-12:00 Art"],

"Wednesday":["9:00-10:00 Science", "10:00-11:00 English", "11:00-12:00 Math"],

"Thursday":["9:00-10:00 Math", "10:00-11:00 Art", "11:00-12:00 Science"],

"Friday":["9:00-10:00 English", "10:00-11:00 Math", "11:00-12:00 History"],

"Saturday":["No classes"],

"Sunday":["No classes"]

}

# 現在の日時を取得し、曜日を取得

now = datetime.datetime.now()

weekday = now.strftime("%A")

# Streamlitアプリの構築

st.title("今日の時間割")

if weekday in timetables:

st.write("今日は{weekday}です。")

st.write("今日の時間割:")

for item in timetables[weekday]:

st.write(item)

else:

st.write("今日は授業がありません。")