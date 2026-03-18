import streamlit as st

st.set_page_config(page_title="자기소개 페이지", layout="centered")

st.title("👋 자기소개 페이지")

st.header("이름")
st.write("김태경")

st.header("소개")
st.write("안녕하세요! 저는 Streamlit을 사용한 웹 인터랙티브 앱을 만들고 있는 개발자입니다. 데이터 시각화와 UI 설계에 관심이 많습니다.")

st.header("기술 스택")
st.write("- Python\n- Streamlit\n- Pandas\n- NumPy\n- Plotly")

st.header("취미")
st.write("- 독서\n- 사이클링\n- 오픈소스 기여")

st.header("연락처")
st.write("- 이메일: example@example.com\n- 깃허브: [github.com/example](https://github.com/example)")

st.info("페이지는 간단히 수정 가능합니다. 이 내용을 실제 정보로 바꿔 사용하세요.")
