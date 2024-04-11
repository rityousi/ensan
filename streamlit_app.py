# Streamlitライブラリをインポート
import streamlit as st

def display_timetable():
    st.title("時間割")
    days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]
    periods = ["1限", "2限", "3限", "4限", "5限", "6限"]

    timetable = [
        ["数学", "英語", "物理", "化学", "体育", ""],
        ["国語", "歴史", "地理", "情報", "家庭", ""],
        ["数学", "英語", "物理", "化学", "体育", ""],
        ["国語", "歴史", "地理", "情報", "家庭", ""],
        ["数学", "英語", "物理", "化学", "体育", ""],
    ]

    for day, timetable_day in zip(days, timetable):
        st.subheader(day)
        for period, subject in zip(periods, timetable_day):
            st.write(f"{period}: {subject}")

def main():
    display_timetable()

if __name__ == "__main__":
    main()
