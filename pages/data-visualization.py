import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("데이터 시각화 예시")

st.sidebar.header("데이터 입력 방법 선택")

data_option = st.sidebar.selectbox(
    "데이터를 어떻게 입력하시겠습니까?",
    ("샘플 데이터", "텍스트 입력 (CSV)", "파일 업로드 (CSV)")
)

df = None

if data_option == "샘플 데이터":
    # 샘플 데이터 생성
    data = {
        '제품': ['A', 'B', 'C', 'D', 'E'],
        '판매량': [23, 45, 56, 78, 32],
        '가격': [100, 150, 200, 250, 300],
        '카테고리': ['전자제품', '의류', '식품', '전자제품', '의류']
    }
    df = pd.DataFrame(data)
    st.write("샘플 데이터를 사용합니다:")
    st.dataframe(df)

elif data_option == "텍스트 입력 (CSV)":
    csv_text = st.text_area("CSV 데이터를 입력하세요 (헤더 포함):", height=200)
    if csv_text:
        try:
            from io import StringIO
            df = pd.read_csv(StringIO(csv_text))
            st.write("입력된 데이터를 사용합니다:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"데이터 파싱 오류: {e}")

elif data_option == "파일 업로드 (CSV)":
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("업로드된 데이터를 사용합니다:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"파일 읽기 오류: {e}")

if df is not None:
    st.header("시각화 예시")

    # 1. 막대 차트 (Bar Chart)
    if '판매량' in df.columns:
        st.subheader("막대 차트: 판매량")
        st.bar_chart(df.set_index('제품')['판매량'])

    # 2. 선 차트 (Line Chart)
    if len(df) > 1:
        st.subheader("선 차트: 가격 추이")
        if '가격' in df.columns:
            st.line_chart(df['가격'])

    # 3. 산점도 (Scatter Plot) - Plotly 사용
    if '판매량' in df.columns and '가격' in df.columns:
        st.subheader("산점도: 판매량 vs 가격")
        fig = px.scatter(df, x='판매량', y='가격', title='판매량 vs 가격')
        st.plotly_chart(fig)

    # 4. 히스토그램 (Histogram)
    if '판매량' in df.columns:
        st.subheader("히스토그램: 판매량 분포")
        fig, ax = plt.subplots()
        ax.hist(df['판매량'], bins=10, edgecolor='black')
        ax.set_xlabel('판매량')
        ax.set_ylabel('빈도')
        st.pyplot(fig)

    # 5. 박스 플롯 (Box Plot) - Plotly 사용
    if '카테고리' in df.columns and '판매량' in df.columns:
        st.subheader("박스 플롯: 카테고리별 판매량")
        fig = px.box(df, x='카테고리', y='판매량', title='카테고리별 판매량 분포')
        st.plotly_chart(fig)

    # 6. 파이 차트 (Pie Chart) - Plotly 사용
    if '카테고리' in df.columns:
        st.subheader("파이 차트: 카테고리 분포")
        category_counts = df['카테고리'].value_counts()
        fig = px.pie(values=category_counts.values, names=category_counts.index, title='카테고리 분포')
        st.plotly_chart(fig)

else:
    st.info("데이터를 입력하거나 선택하세요.")
