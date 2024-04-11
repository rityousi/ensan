# Streamlitライブラリをインポート
import streamlit as st

def display_timetable():
    st.title("時間割")
    days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]
    periods = ["1限", "2限", "3限", "4限", "5限", "6限","7限"]

    timetable = [
        ["理数化学", "CⅢ", "論表Ⅲ", "理数物/生", "数BC", "論理国語"],
        ["古典探究", "数Ⅲ", "CⅢ", "理数物/生", "理数化学", "地理","論表Ⅲ"],
        ["論理国語", "数BC", "理数物/生", "体育", "地理", "数Ⅲ"],
        ["理数物/生", "数Ⅲ", "理数化学", "数学BC", "CⅢ", "古典探究","舞プロ"],
        ["理数物/生", "地理", "体育", "CⅢ", "数Ⅲ", "理数化学","HRA"],
    ]

    for day, timetable_day in zip(days, timetable):
        st.subheader(day)
        for period, subject in zip(periods, timetable_day):
            st.write(f"{period}: {subject}")

def main():
    display_timetable()

if __name__ == "__main__":
    main()

import streamlit as st
from datetime import datetime, timedelta, timezone

def get_jst_weekday():
    # 現在のUTC時間を取得
    utc_now = datetime.utcnow()

    # UTCからJSTに変換
    jst = timezone(timedelta(hours=9))
    jst_now = utc_now.astimezone(jst)

    # 曜日を取得（0: 月曜日, 1: 火曜日, ..., 6: 日曜日）
    weekday_index = jst_now.weekday()

    # 曜日のリスト
    weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

    return weekdays[weekday_index]

def main():
    st.title("現在の曜日（日本時間）")
    jst_weekday = get_jst_weekday()
    st.write(f"曜日：{jst_weekday}")

if __name__ == "__main__":
    main()
