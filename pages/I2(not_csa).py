import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="구입하지 않는 이유 시각화",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 간편식 구입하지 않는 이유 📈")
st.sidebar.markdown("# 간편식 관련 분석 데이터 📈")

st.write("""
### 2021년
""")


url21 = 'https://raw.githubusercontent.com/HyenC/AIS7MidProject/main/data/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%92%E1%85%A1%E1%84%8C%E1%85%B5_%E1%84%8B%E1%85%A1%E1%86%AD%E1%84%82%E1%85%B3%E1%86%AB_%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%B2_21.csv'


@st.cache
def load_data(url21):
    df_21 = pd.read_csv(url21, encoding='cp949')
    return df_21

df_21 = load_data(url21)

df_t21 = df_21.rename(columns=df_21.iloc[0])
df_t21 = df_t21.drop(df_t21.index[0])
df_t21 = df_t21.astype({i:"float" for i in df_t21.columns[2:]})


df21_a = df_t21[df_t21['특성별(1)'] == '가구주연령별']
df_21_a = df21_a.drop(['특성별(1)'], axis=1)
df_21_a = df_21_a.set_index(keys='특성별(2)')
df_21_a = df_21_a.rename_axis('연령별')

df21_c = df_t21[df_t21['특성별(1)'] == '가구원수별']
df_21_c = df21_c.drop(['특성별(1)'], axis=1)
df_21_c = df_21_c.set_index(keys='특성별(2)')
df_21_c = df_21_c.rename_axis('가구원수별')

df21_s = df_t21[df_t21['특성별(1)'] == '가구주성별']
df_21_s = df21_s.drop(['특성별(1)'], axis=1)
df_21_s = df_21_s.set_index(keys='특성별(2)')
df_21_s = df_21_s.rename_axis('성별')


fig = df_21_c.T.plot(kind='bar', figsize=(25,10), rot=35, fontsize=15)
plt.title("2021년 가구원수별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = df_21_s.T.plot(kind='bar', figsize=(25,10), rot=35, fontsize=15)
plt.title("2021년 성별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())

fig = df_21_a.T.plot(kind='bar', figsize=(25,10), rot=35, fontsize=15)
plt.title("2021년 연령별", fontsize=20)
plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(plt.show())
