# 간편식 사업 활성화 프로젝트
![image](https://github.com/HyenC/AIS7MidProject/assets/38906574/34774da2-8d7e-4201-9abe-a51398c83023)

## 인사이트

<div>
  <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/52168a42-a0a7-4949-8562-66495b5ef809">
  <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/87ab86ab-3969-4e10-9844-f486ea10adae">
</div>

<div>
  <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/8bbcfa4e-9064-4ebe-a618-e76f2451212e">
  <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/d07d6678-c52d-40d1-9525-edede1d3bf86">
</div>

<div>
  <img width="265" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/1a30d276-b2fc-4f4f-b864-0dcf31cd726d">
  <img width="265" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/7bbf8fe4-ef66-4c5a-9ec9-6182fc50ec94">
  <img width="265" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/2bfbfece-ba64-4a1b-b7ea-c8d253ddebcc">
</div>

</br>
  
# 1. 프로젝트 개요

## 1-1. 주제 : **유통데이터 분석을 통한 지속가능한 간편식 사업 활성화 프로젝트**

## 1-2. 주제 선정의 배경

### **주제 선정 과정**

- 유통데이터 활용 경진대회 주최측으로부터 상품데이터, 구매 데이터, 결제 데이터를 제공받았다. 주최측에서 제공한 데이터 외에도 공공데이터포털이나 공공기관에서 제공하는 데이터를 함께 활용해도 된다고 하였기 때문에 제공받은 데이터셋의 ‘어떤 사람’이 상품을 구매하는지와 연관을 지어보기 위해 KOSIS의 <가구주의 연령/가구유형/가구원수별 추계가구 데이터>를 분석해보기로 하였다.

<div>
    <img width="400" alt="image" margin='auto' src="https://github.com/HyenC/MealKit/assets/38906574/c00cb95c-0206-4969-95bf-425d173095f3">
    <img width="400" alt="image" margin='auto' src="https://github.com/HyenC/MealKit/assets/38906574/bc120d93-aa52-4c34-82c0-84086e960125">
</div>

그 결과 ‘인구의 고령화', ‘1인 가구의 증가’가 가장 눈에 띄었고 이를 인사이트로 하여 고령가구와 1인 가구의 소비 및 유통에 대한 주제를 선정하려고 했다.

 원래 적용하려던 '1인 가구 증가' 및 '고령 인구' 문제를 해결하기 위해서 사용하려고 했던 경진대회 데이터와 가구와 인구 데이터를 결합하는 것이 어려웠다. 또한 모의 분석 결과를 제공하는 데이터와 엮었을 때도 난점이 있었다. 그래서 경진대회 데이터를 간단히 분석하여 중요한 포인트를 찾아내기로 결정했다. 

</br></br>

- 제공받은 데이터로 간단한 EDA를 진행한 뒤 결과를 분석하여 주제를 구체화했다.
<div>
    <img width="260" alt="image" margin='auto' src="https://github.com/HyenC/MealKit/assets/38906574/dd64f7ce-631f-428b-8bad-b0346f789b43">
    <img width="260" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/0e9a512c-0e83-4fad-b69c-aab49f05948f">
    <img width="260" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/3f7b74ef-fc2a-457f-b749-ca35a30aee24">
</div>

- 주어진 데이터의 상품 목록은 대분류> 중분류> 소분류로 분류된다. 이때 소분류를 기준으로 삼게 되면 상품 유형이 너무 많아지므로 대분류를 기준으로 데이터 프레임을 보았다.
- 그 결과 상위 8개의 항목은 1. 생수, 과자, 라면, 커피 2. 우유, 냉장냉동, 간편식 3. 채소 4. 정육, 계란 5. 주방, 청소, 욕실용품, 6. 과일, 7. 생선, 건해산물, 8. 주류 였다. 이 중 다섯 번째로 많은 항목을 차지하는 주방, 청소, 욕실용품을 제외하고 모두 ‘식품’과 관련된 소비이므로 ‘식품’ 구매로 주제를 좁혔다.
- 따라서 경진대회에서 제공받은 데이터의 구체적인 EDA는 ‘식품’ 데이터로 하기로 결정하였고, 다른 종류의 공공데이터와 결합하여 인사이트를 도출하는 과정에서는 ‘식품 데이터’의 범위도 넓다고 생각하여 그 중에서 가장 눈에 띄는 지점으로 좁혀서 아이디어를 제안하기로 하였다.
- 생필품이라고 볼 수 있는 ‘생수, 라면, 커피'를 제외하고 ‘식품 데이터'라고 판단한 항목들의 절대량과 그 비율을 살펴보기 위해 막대 그래프와 도넛 차트를 그려보았더니 우유, 냉장냉동, 간편식의 비중이 가장 두드러졌다.

<details>
<summary>
    
### 배경 및 필요성 </summary>
<div markdown="1">
    
- 경진대회에서 제공받은 구매 데이터와 카드 결제 데이터의 시점은 2019, 2020, 2021, 2022년이다. 이 시기의 가장 큰 사회적 변화는 단연 코로나19이다. 코로나19는 비말(droplet)에 의한 사람 간 전파가 기본이기 때문에 특히 음식 섭취와 관련하여 많은 사람들의 인식 변화가 있었다. 그 중 대표적인 것이 간편식이다. 밀키트란 meal(식사)와 kit(키트)의 합성어로, 식사 키트라는 뜻이다. 이와 비슷한 가정간편식(HMR)은 Home Meal Replacement의 약어로서, 가정식 대체식품이라는 의미이다. 본고에서는 밀키트와 가정간편식(HMR), 냉동냉장 식품을 모두 포함하여 ‘간편식’으로 칭하기로 하였다.
- 코로나19 발생 이후 간편식과 관련된 인식 변화로는 먼저 중장년층의 인식 변화를 예시로 들 수 있다. 강혜정(2020)에 따르면 이전에는 간편식을 접해보지 못하여 간편식에 대해 막연히 부정적인 인식을 가지고 있었던 중장년층이 코로나19로 간편식을 접한 뒤 긍정적인 인식을 가지게 된 경우가 있다. 또 다른 변화는 코로나19 이후 냉동 간편식을 찾는 사람들이 급증했다는 것이다. 코로나19 이전에는 간편식을 구입하더라도 신선식품이나 레토르트(국탕류)를 찾고 냉동식품은 냉동고를 열어 꺼내야 하는 불편함 때문에 잘 이용하지 않았는데 마켓컬리 등 온라인 마트가 성장하면서 오히려 냉동 간편식이 성장한 것이다.
- 한국농어촌방송(2021)에 따르면 간편식 판매량이 코로나 이전년도 대비 8배 이상 급증했으며, 이러한 영향으로 한동안 너도나도 간편식 사업을 시작하는 ‘간편식 돌풍’이 있었다. 특히 창업 비용이 저렴한 ‘무인 밀키트 가게'가 우후죽순으로 생겨나기도 했다. 하지만 단계적 일상회복(위드 코로나)이후 다시 외식을 하는 사람들이 늘어나면서 밀키트 판매량이 감소했으며, 시사캐스트(2022)에 따르면 무인 밀키트 매장의 수익이 반토막 나며 장사를 접고 있는 점주들이 늘어나고 있다.
- 하지만 간편식은 사회적으로 다음과 같은 긍정적인 영향을 줄 수 있다는 점에서 2022 엔데믹 이후에도 간편식의 활성화에 대한 논의가 필요하다.
1. 연합뉴스(2022)에 따르면 최근 중부지방의 폭우로 인해 식료품 공급이 어려워지며 간편식 판매량이 30% 가까이 급증했다. 이번 폭우 뿐 아니라 각종 자연재해의 상황에서 간편식 시장이 다양화 되는 것은 재난 상황 속 균형 잡힌 영양 제공에 도움을 줄 수 있다.
2. 사람들마다 간편식을 찾는 이유가 각양각색이기 때문에 간편식은 여러 사회 계층에게 섬세하게 도움을 제공할 수 있다.

 예를 들어 학생의 경우 경제적인 문제를 해결하기 위해 간편식을 구매할 수 있다. 1인 가구의 경우 배달을 시켜 먹었을 때 배달음식의 양이 1인분을 초과하는 경우가 많고 배달비에 대한 부담을 느낄 수 있다는 문제가 있는데 이에 대한 해결방안이 될 수 있다.

 중장년층, 노년층의 경우 지자체에서 고독사 방지 사업의 일환으로 간편식을 제공하거나 복지관에서 간편식으로 식사를 대접하는 경우가 많다. 또한 장애인 등의 사회적 약자나 병원에 있는 환자, 간병인, 임산부 등 요리를 직접 해먹기 불편하지만 충분한 영양 섭취가 필요한 경우 간편식의 존재가 필수적이다.

 해외에서 한국 음식을 먹고 싶은 경우에도 간편식이 유용하다. 한식은 조리가 어렵고 해외에서 재료를 구하기 힘든 경우가 많기 때문이다. 또한 점심시간이나 저녁 시간이 빠듯한 바쁜 직장인은 간편식으로 끼니를 해결해야 하는 날이 많다.

1. 시장의 활성화는 사람들의 관심을 집중시키고 이는 해당 상품을 둘러싼 문제 해결 과정에 영향을 미친다. 예를 들어 어떤 상품과 관련된 산업이 도태된다면 문제 해결에 대한 의제 형성 자체가 불가능해진다.

 따라서 경진대회에서 제공받은 데이터와 공공데이터포털, 통계청의 데이터를 활용하여 유통, 식품, 간편식을 키워드로 한 EDA를 진행하고 간편식 시장의 지속적인 부흥을 위한 방안을 제시하고자 한다.
</div>
</details>

<details>
<summary>
    
### 분석 목적 </summary>
<div markdown="1">
    
1. ‘유통' 데이터로 주어진 3개의 데이터 중 구매, 카드결제 데이터를 제공받은 후 EDA를 통해 적합한 주제를 도출한다.
2. 주어진 데이터의 시점과 맞닿아 있는 사회적 이슈인 코로나19와 데이터에서 집중하고자 선정한 ‘간편식'의 연관성을 검증한다.
3. 2022년 위드 코로나가 진행되며 간편식의 장밋빛 미래를 예측하는 자료들도 있고, 외식의 증가로 인한 간편식의 쇠퇴를 예측하는 자료들도 존재하는 가운데 간편식 사업의 지속가능한 활성화를 위해 어떤 방안을 제시할 수 있을지 고안해본다.
4. 간편식을 이용하는 사람들을 연령, 성별, 가구 유형별로 분석하여 각 사회적 계층의 니즈를 확인한다.
5. 유통 트렌드가 빠르게 변화하고 있는 가운데 일반적인 유통 트렌드를 어떻게 간편식에 적용할 수 있을지 생각해본다.
6. 분석 과정에서 불필요한 정보를 빼고 보기 좋게 가공하는 데이터 전처리 과정을 거친 뒤 분석 목적에 맞는 그래프를 파이썬 라이브러리를 활용하여 그려 시각화하고 대시보드를 만들어 주장에 대한 설득을 시도한다.
   
</div>
</details>

</br>
    
# 2. 데이터

## 2-1. 사용 데이터

<details>
<summary> 

#### 유통데이터 활용 경진대회 데이터 [상품 데이터/ 구매 데이터/ 카드 결제 및 명세 데이터] </summary>
<div markdown="1">

> 개요: 산업통상자원부 '산업혁신기반구축' 사업으로 구축중인 '유통데이터 서비스 플랫폼'에서 제공받은 데이터이며, 경진대회 주관기관 중 ‘텐큐브’에서 전달했다. 전체 raw data는 외부 유출 금지이지만, 시각화 대시보드 발표는 가능하다는 허락을 받았다.

<img width="500" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/62ac1151-ac03-424d-ab2d-a71f5df95a71">
<img width="500" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/b7ff654a-4b9b-4f31-b4e8-2cfaa1e082d4">
<img width="500" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/3bcba404-01cb-4d73-843f-b57788de4995">

</div>
</details>

<details>
<summary> 

#### KOSIS 데이터 </summary>
<div markdown="1">

> 개요 및 목적: 식품기업의 마케팅 전략 수립에 필요한 정보를 제공하기 위해 가공식품에 대한 소비자 인식 및 라이프스타일에 대한 체계적인 조사를 실시하여 각 기업의 소비자 트렌드 정보 수요에 부응하고, 시장세분화를 위한 기초 자료를 제공한다.

- 최근 1년간 건강기능식품 품목별 구입경험 및 구입 변화
    
    [https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_057_2019&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_053&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
    
- 향후 1년 간편식(HMR) 구입 변화 예상
    
    [https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_053&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_065&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
    
- 간편식 구입 이유 데이터
    
    https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_057_2019&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE
    
- 월평균 간편식 지출액 데이터
    
    https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_059&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE
    
- 유기가공식품 구입 경험 및 인증 품질에 대한 신뢰도
    
    [https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_057_2019&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_082_2019&vw_cd=MT_ZTITLE&list_id=D2_114053_001_005&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
    
- 가공식품 가격에 대한 인식
    
    [https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_057_2019&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_091&vw_cd=MT_ZTITLE&list_id=D2_114053_001_006&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
    
- 식품소비 트렌드별 동조성(간편식)
    
    [https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_057_2019&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE](https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_125_2019_19&vw_cd=MT_ZTITLE&list_id=D2_114053_001_006&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
    
- 간편식을 구입하지 않는 이유 데이터
    
    https://kosis.kr/statHtml/statHtml.do?orgId=114&tblId=DT_114053_057_2019_01&vw_cd=MT_ZTITLE&list_id=D2_114053_001_003&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE

</div>
</details>

<details>
<summary> 

#### 그 외 데이터  </summary>
<div markdown="1">

> 개요: 식품소비행태조사(The Consumer Behavior Survey for Food, CBSF)는 가구 및 개인의 식품소비 및 외식행태와 식생활 파악을 목적으로 2013년부터 매년 실시하고 있다. 2020 식품소비행태조사는 가구 내 식품 주구입자(3,335가구), 성인(6,355명) 및 청소년 가구원(622명)을 대상으로 조사했다.

- 연도별 식품소비 행태조사
    
https://www.krei.re.kr/foodSurvey/index.do
    
https://www.krei.re.kr/foodSurvey/selectBbsNttView.do?key=1774&bbsNo=451&nttNo=158642&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=       

</br>
  
> 개요: 코로나 바이러스는 올해 초부터 정치, 경제, 사회, 문화를 통틀어 국가 전체에 큰 영향을 미쳤다. 바이러스는 사람을 매개로 전세계 곳곳까지 빠르게 확산되었지만, 혼란 속에서도 사람들의 노력으로 감염에 관한 여러 데이터가 확보되었다. 코로나 바이러스가 남긴 데이터의 패턴을 찾아 다양한 기법으로 분석을 통해 확산을 예측한다면, 최적의 방역 조치를 결정하는데 도움이 될 것이고, 우리는 좀 더 빠르게 코로나 바이러스를 극복할 수 있을 것이다. 코로나 바이러스의 확산 현황 데이터를 통해 코로나 바이러스의 특성을 분석하는 데이터이다.

- 코로나 바이러스 감염증 (COVID-19) 현황 데이터 시각화

https://www.bigdata-map.kr/datastory/new/story_17

</div>
</details>


<details>
<summary> 

## 2-2. 전처리 예시 </summary>
<div markdown="1">
    
- 로우 데이터셋은 특성별(1)에 가구원수별, 가구주성별, 가구주연령별이 모두 포함되어있어 카테고리별로 슬라이싱 했다.
    
![image](https://github.com/HyenC/MealKit/assets/38906574/ad3c4c3d-125e-4f8e-a811-cfbf63e60c71)

<details>
    <summary> 전처리 코드 </summary>
    <div markdown="2">

```Python
# 전처리 후
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import koreanize_matplotlib

%config InlineBackend.figure_format = 'retina'

from glob import glob
file_name1 = glob("식품소비_트렌드별_동조성_19.csv")[0]
df_t1 = pd.read_csv(file_name1, encoding='cp949')

# 컬럼의 이름을 첫 행(설문내용)으로 바꾸고 첫 행 삭제
df_t19 = df_t1.rename(columns=df_t1.iloc[0])
df_t19 = df_t19.drop(df_t19.index[0])

# 시각화를 위해 데이터 타입을 확인 후 object -> float 변환
df_t19.iloc[:, 2:].info()
df_t19 = df_t19.astype({i:"float" for i in df_t19.columns[2:]})

# 특성별(1)이 가구원수별인 데이터프레임 분리
df19_c = df_t19[df_t19['특성별(1)'] == '가구원수별']
df_19_c = df19_c.drop(['특성별(1)'], axis=1)
df_19_c = df_19_c.set_index(keys='특성별(2)')
df_19_c = df_19_c.rename_axis('가구원수별')

# 특성별(1)이 가구주성별에 해당하는 데이터프레임 분리
df21_g = df_t21[df_t21['특성별(1)'] == '가구주성별']
df_21_g = df21_g.drop(['특성별(1)'], axis=1)
df_21_g = df_21_g.set_index(keys='특성별(2)')
df_21_g = df_21_g.rename_axis('성별')

#특성별(1)이 가구주연령별에 해당하는 데이터프레임 분리
df19_a = df_t19[df_t19['특성별(1)'] == '가구주연령별']
df_19_a = df19_a.drop(['특성별(1)'], axis=1)
df_19_a = df_19_a.set_index(keys='특성별(2)')
df_19_a = df_19_a.rename_axis('연령별')
```
</div>
</details>

![image](https://github.com/HyenC/MealKit/assets/38906574/fd33771b-bb9b-4287-a0a8-cbaf0ccdd1fd)

</div>
</details>

</br>

## 3. 분석 결과
<details>
<summary>

#### [19~20년 구매데이터 품목군별 데이터(제공데이터)] (plotly, histogram) </summary>
<div markdown="1">

<div>
    <img width="400" alt="image" margin='auto' src="https://github.com/HyenC/MealKit/assets/38906574/3f132c19-8726-4643-9c6a-e16d2abc3baa">
    <img width="400" alt="image" margin='auto' src="https://github.com/HyenC/MealKit/assets/38906574/56321efc-5554-4b66-9a45-92cdc972c6d0">
</div>

- 19년 9월 경 부터 20년 10월까지 방대한 양의 구매데이터를 받고, 최우선적으로 진행한 것은 정제 작업이다. (39620, 16)의 데이터를 정제하기 위해 팀의 주제와 관련된 품목만을 남기기 위하여 MasterCategoryFullName 컬럼에서 식품 관련된 카테고리를 제외하고 모두 제거하는 작업을 거쳤다. 이후 추가적으로 필요없는 컬럼들을 제거한 후 연도별로 보기 좋게 나눈 결과, 우유, 냉장냉동, 간편식 카테고리가 가장 높다는 것을 확인할 수 있었다. 데이터를 보면 y축의 단위를 고려하였을 때 19년도 코로나 이전에 비해 20년도 코로나가 창궐한 이후 냉동식품 및 간편식의 소비가 크게 증가한 것을 확인할 수 있다.

</div>
</details>

<details>
<summary>

#### [21~22년 카드 결제데이터_카테고리_외식(제공데이터)과 코로나 확진자수 상관관계 비교] (matplotlib, lineplot) </summary>
<div markdown="1">

![image](https://github.com/HyenC/MealKit/assets/38906574/0dbf40ac-7c87-491f-9cdb-b20eb006856c)
![image](https://github.com/HyenC/MealKit/assets/38906574/fb62ee99-c919-4058-9439-3024d96d29c8)

- 구매 데이터처럼 2021, 2022년에도 코로나19와 식품 구매의 상관관계가 있을 것이라고 생각했다. 따라서 카드 결제데이터와 코로나 확진자수를 같은 그래프에 넣고 상관관계를 보기좋게 비교하기 위해 위 그래프처럼 시각화 하였다. 카드 결제 데이터는 식재료가 실제로 집에서 먹었는지, 어디에 사용했는지가 애매하여 외식 및 식당 등의 카테고리만을 남기고 전처리 하였고 '코로나 확진자 수' 데이터는 일일 확진자수만을 나타내도록 전처리한 데이터이다.
- 시각화 후 분석을 진행해보니 의외로 상관관계가 없었고 데이터를 분석하여 확인해본 결과 22년도 2월부터  위드코로나 시행인 3월, 그 이후에도 확진자수의 관계없이 외식의 수가 많아지는 것을 보면 확진자의 수보다 사회적 거리두기 단계, 정권 교체로 인한 위드 코로나 정책 등과 같은 제재나 사람들의 코로나에 대한 인식 변화가 더 큰 영향을 미쳤다는 것을 확인하였다.
- 따라서 코로나 확진자의 절대적인 수는 늘어났음에도 위드 코로나 정책로 인해 사람들이 외식을 많이 하게 되었고 이는 외식으로 인해 무인 밀키트 사업이 망하는 등 간편식의 위치가 애매하게 되었다라는 것을 뒷받침해줄 수 있다. 따라서 앞으로 간편식이 활성화될 수 있도록 간편식과 관련된 데이터를 분석해보기로 했다.

</div>
</details>

<details>
<summary>

#### [18~20년 간편식 구입변화(%) 데이터]  (seaborn, barplot) </summary>
<div markdown="1">

<div>
    <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/1dd35942-b35e-4a1e-a2d7-c39e308f6617">
    <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/ccecce4d-c2e2-4b20-b5ff-0ffcb5e13cf4">
</div>

- 간편식의 구입변화(%)를 매우감소, 약간감소, 비슷, 약간증가, 매우증가로 항목을 나눠 시각화 하였다.  먼저, 간편식에 대한 변화율만을 확인하기 위하여 그래프의 전체적인 추세를 확인하였다. ‘매우감소’ 부터 보면 전체적인 비율이 18년도에 비해 19년도에는 늘어나지만, 20년도에는 다시 줄어드는 것을 볼 수 있다.  간편식 구입을 이전에 비해 매우 적게 하게 되었다는 비율이 20년도에 줄어들어다는 것은 곧 간편식을 이전보다 많이 구입한다는 것이다. ‘약간감소’의 비율도 ‘매우감소’ 항목과 유사한 그래프를 형성하는 것을 볼 수 있다.
- 한편, ‘약간증가’ 항목을 살펴보면 18년도와 19년도가 비슷한 그래프 양상을 보이지만 20년도에 증가하는 추세를 보인다. ‘매우증가’ 항목에서 가장 눈에 띄는 흥미로운 결과가 나왔는데, 18, 19년도의 ‘매우증가' 수치가 굉장히 낮지만 20년도에 들어서 큰 폭으로 늘어난  모습을 보인다. 이와 비슷한 특징을 가지는 데이터가 하나 더 있다. 이를 통해 ‘감소' 항목에 대한 결과와 마찬가지로 20년도에 사람들이 이전보다 간편식을 많이 소비하게 되었다는 결론을 내릴 수 있었다.
- 다음으로 간편식의 세부 품목에 집중하여 분석해본다면, ‘면류'의 경우 ‘매우 감소'와 ‘감소'에서는 낮은 수치를 기록했지만 ‘약간 증가'에서 가장 높은 수치를 보였다. 이를 통해 ‘면류'는 연도의 변화에는 크게 영향을 받지 않지만 간편식을 섭취하는 사람들이 꾸준히 찾는 품목이라는 것을 알 수 있다. 따라서 추후 간편식 시장 개선방안을 제안할 때 스테디셀러인 ‘면류' 밀키트를 더욱 활성화시킬 수 있겠다는 인사이트를 도출할 수 있었다. 또한 연도의 변화를 고려했을 때 2020년에 ‘밥류'와 ‘찌개/ 탕류'의 ‘매우증가’ 수치가 매우 높은 것을 확인할 수 있다. 2020년은 코로나19가 창궐한 해로, 이전에는 많은 사람들이 밥과 찌개 등을 식당에서 먹었다면 코로나19 발생 이후에는 집에서 가정식을 먹어야 하기 때문에 수치가 급증하였다고 예측할 수 있다. 특히 간편식의 주 목적 중 하나가 조리하기 힘든 음식을 한번에 조리할 수 있는 키트를 제공하는 것이라는 것을 고려하면 조리가 어려운 찌개, 탕류 소비의 증가 더욱 쉽게 이해된다.

</div>
</details>

<details>
<summary>

#### [18~20년 간편식 구입경험] (matplotlib, pie) </summary>
<div markdown="1">

![image](https://github.com/HyenC/MealKit/assets/38906574/140d493b-cc68-470b-8448-0d1bcb0d37ca)

- 이 데이터는 18~20년 간편식 구입경험에 대한 설문 데이터인데, 위에서 살펴본 ‘간편식 구입변화(%)’ 데이터와 마찬가지로 간편식 시장의 성장 가능성을 보여주는 지표이다. 간편식을 구입해본 경험이 있는 사람들이 2018에는 구입 경험이 없는 사람들과 비슷한 수치를 보여주지만, 19, 20년도에 들어서 구입경험이 있는 사람의 수치가 더 높은 수치를 보인다. 평균 비율을 비교해보면 19, 20년도 기준으로 9:1 정도로 압도적이다. 이 지표를 보면 간편식 시장이 이미 대중화 되어있고, 간편식의 존재에 대해 대부분의 사람들이 알고 있다는 것을 알 수 있다. 따라서 간편식을 구입하지 않는 이유나 간편식에 대한 사람들의 인식 및 신뢰도를 분석하여  밀키트 시장을 더 성장 시킬 수 있는 인사이트를 얻고 경쟁력을 갖추고자 하였다.

</div>
</details>

<details>
<summary>

#### [월평균 간편식 지출액_가구원수별, 연령별] (matplotlib, barplot) </summary>
<div markdown="1">

- 지금까지 간편식 구입경험과 변화 및 유통데이터를 통해 구매추이를 보았다면, 더 다양한 관점으로 확인해보기 위해 사람들이 간편식에 지출하는 비용에 대한 데이터를 분석해보았다. 이 과정에서 좀 더 세부적으로 구분하여 보기 위해 가구원수별,  연령별로 구분지어 데이터를 시각화하였다. 우선 가구원수별로 나눠본 지표이다.

<div>
    <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/f3083150-94c7-4eaf-a861-bf994bc40e5f">
    <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/bc16ebd6-4a49-4807-bae6-15e9c4652b64">
</div>

- 1만원 미만으로 지출한 사람들의 비율을 보면 전체적으로 보아도 19, 20년도와 비교하여 21년도에 큰 증가를 보였다. 그중에서도 막대의 항목을 기준으로 보았을 때 1인가구와 2인가구의 지표가 엄청난 증가폭을 그리는 것을 확인할 수 있다. 이를 보면 경제적으로 여유가 없고 스스로 밥을 해먹어야 하는 1인가구(사회초년생, 자취생 및 독거노인 등)가 소액으로 간편하게 끼니를 해결할 수 있는 간편식을 선호한다고 볼 수 있고, 그 추세가 21년도에 들어서 급격히 증가되었다. 또 1만원에서 2만원 사이로 지출한 지표를 보면 2인가구가 크게 증가하는 경향을 보이는데, 이는  2인분의 식사를 해결하기 위한 적당한 금액이므로 자연스러운 현상이고 19, 20년도와 비교하여 21년도에 큰 증가폭을 보인다. 4인가구 이상에서는 가구원수에 따라 소액지출하는 경우는 낮다고 볼 수 있고, 지출금액이 증가함에 따라 4인가구 이상의 지표도 함께 증가한는 경향을 보인다. 특이사항은 10만원 이상에서 1인가구가 적지않은 지표를 보이는데, 한번에 대량으로 구매하여 조금 더 저렴한 가격으로 끼니를 해결하기 위한 전략이라고 유추할 수 있다. 다음은 연령별로 나누어 본 지출액별 지표이다.

<div>
    <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/325e46a8-3597-4d51-ad53-dfa98b7f4f61">
    <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/94b0e9a6-baa9-4196-95e3-48f767855a13">
</div>

- 1만원 미만 지출 데이터를 보면 21년도에 들어서 간편식 소비가 증가하였고, 60대 이상의 비율이 가장 높은 것을 확인할 수 있다. 1만원 미만 뿐만 아니라 60대 이상의 비율의 비율만을 보면 1만원 미만에서 6만원 까지의 지출금액 부분에서 전연령대를 통틀어 가장 높은 지표를 보인다. 6만원에서 10만원 까지의 상대적으로 높은 금액에서의 지출 비율은 낮은 지표를 보이지만 60대 이상의 소비자들이 간편식 시장에서 꽤 큰 비중을 차지한다는 것을 확인할 수 있다.

</div>
</details>

<details>
<summary>

#### [연도별 식품소비 트렌드별 동조성 데이터_성별] (matplotlib, pie)  </summary>
<div markdown="1">

- 간편식에 대한  인식을 확인하기 전,  전체적인 식품소비의 트렌드를 확인할 필요가 있다고 판단하였다. 따라서 간편식 뿐 아니라 전체적인 식품소비의 트렌드를 조사한 ‘연도별 식품소비 트렌드별 동조성 데이터’를 분석해보았다. 성별을 나누어 데이터를 시각화 하였고, 연도별로 그래프를 비교하여 코로나 전과 후의 식품소비에 대한 인식 변화를 확인할 수 있다.

<img width="500" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/c8825d02-3f23-4dec-b48b-057e6944158c">

- 데이터를 살펴보면 19년도와 20년도 데이터에서 주목해야할 항목은 ‘가격이 비싸도 건강에 좋은 원료 안전성이 확보된 제품을 구매하겠다’ 와 ‘가격이 비싸도 소포장 사용 및 취식/조리가 간편화된 제품을 구입하겠다’ 이다. 남성의 경우 여성보다 원료 안전성에 대해 민감하게 반응하고 여성의 경우 남성에 비해 소포장 사용 및 취식의 간편성을 더 고려하는 경향이 있긴 하지만, 전체적으로 보았을 때 남녀 모두 ‘원료 안전성’을 가장 우선으로 두고 식품을 소비하는 것을 알 수 있었다. 간편식의 경우 영양성분 함량과 유통기한을 자율적으로 적도록 하여 해당 정보를 명시하지 않는 경우가 많다. 이는 음식을 선택할 때 ‘원료 안전성'을 최우선적으로 고려하는 한국인들의 특성을 고려했을 때 판매율에 부정적인 영향을 끼칠 것이라고 예측할 수 있다.
- 21년도에는 특이하게 19, 20년도에는 5개 항목 중 모두 3위에 그쳤던 '다양하고 새로운 맛을 낸 제품 구입하겠다’에 대한 응답 비율이 가장 높은 것을 확인할 수 있다. 2021년과 2022년도의 ‘소비자 트렌드 보고서’ 의 분석에 따르면, 남들과의 동질성을 통해 소속감을 얻고 싶어했던 과거와는 달리 최근에는 자신만의 독특한 가치를 보여줄 수 있는 취향을 소비하는 문화가 왕성하다. 특히 다양한 종류의 SNS가 활성화되며 취향을 공유할 수 있는 경로가 많아졌다. 외식업 또한 SNS 인플루언서를 모델로 내세우고 라이브 방송을 통해 상품을 판매하기도 한다. 코로나 이후 많은 기업들이 간편식 시장에 뛰어들면서 특색을 구분할 수 없는 획일적인 간편식 제품들이 우후죽순으로 쏟아졌다. 따라서 설문 결과를 통해 간편식 소비자들이 이러한 행태에 신물이 났고, 집에서도 외식을 하는 것과 같이 특이한 음식 섭취 경험을 해보고 싶은 사람들이 많아진 것을 확인할 수 있었다.

</div>
</details>

<details>
<summary>

#### [간편식을 구입하지 않는 이유 설문 데이터] (matplotlib, barplot 전치) </summary>
<div markdown="1">

- 연도별 식품소비 트렌드별 동조성 데이터를 통해 성별에 관련없이 식품의 안전성, 즉 신선도나 유통기한과 소포장 및 간편한 조리를 원하는 것을 볼 수 있었다. 그렇다면 이러한 식품 소비 트렌드가 ‘간편식'에도 적용되는지 확인해보기 위해 ‘간편식을 구입하지 않는 이유' 라는 설문 데이터를 수집하였고, 가구원 수, 성별, 연령별로 나누어 분석해보았다.

<img width="500" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/a1f62e6a-e05d-444b-bc7b-ab43f9344cf9">

- 먼저 가구원수별로 ‘간편식을 구입하지 않는 이유’ 설문에 응답한 데이터를 분석해보면 ‘1인 가구'를 제외한 다인 가구는 모두 ‘가족의 식사는 직접 조리(요리)해야 한다고 생각해서'의 항목이 높은 것을 알 수 있다. ‘간편식'의 구성이나 맛, 가격 등을 차치하고서라도 ‘가족의 식사'라는 행위에 특별한 의미를 부여하는 한국인의 정서를 확인할 수 있었다. 따라서 이러한 인식에서 자유로운 1인 가구를 겨냥한 간편식을 구성하거나, ‘간편식’ 중에서도 특히 밀키트의 경우 재료 손질의 단계를 줄여준다는 점을 제외하면 직접 조리하는 것과 비슷하다고 볼 수 있는데 인식적으로도 밀키트 조리 행위가 ‘요리'라고 비춰질 수 있도록 제품의 완성도를 높이려는 작업이 필요하다.

<img width="500" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/66c7c011-4e25-414c-9bf2-601ef4933cb7">

- 다음으로 ‘연령별 간편식을 구입하지 않는 이유’를 살펴보면, 앞선 가구유형별 그래프에서 살펴본 인식적인 이유를 제외하고는 ‘안전성(신선도 유통기한 등)이 염려되어서'와 ‘원재료의 원산지와 품질이 의심스러워서'의 비율이 가장 높은 것을 알 수 있다. 특히 40대의 비율이 두드러지게 높았는데 이는 아이들을 키우는 부모의 입장에서 더욱 식품의 안전성을 고려하기 때문이라고 유추할 수 있다. 결론적으로 ‘가구원수별, 연령별 간편식을 구입하지 않는 이유'를 분석함으로써 소비자들이 간편식의 원재료와 원산지의 품질을 신뢰하지 못하고 안전하지 못한 상품이라고 인식하고 있는 것을 확인할 수 있었다.
- 특히 간편식 중에서도 냉장, 냉동 식품이나 이미 조리가 되어 데우기만 하면 되는 가정 간편식(HMR)과 달리 밀키트는 조리 전 식재료의 상태로만 제공된다. 따라서 밀키트의 경우 실제 유통기한이 길지 않은데 이 때문에 판매되지 못하고 쌓이는 재고 상태의 밀키트를 염려한 사업주들이 유통기한을 표기하지 않거나 영양성분을 표시하지 않는 경우가 빈번하다.
- 실제로 한국소비자원이 채소와 쌈 등을 주재료로 하는 밀키트 16개 제품을 조사한 결과, 영양 성분을 표시한 제품은 단 1개에 불과했다. 그 중 6개 제품은 유통기한의 안내가 없었고, 바깥과 안쪽 포장의 원재료명 표시가 다르기도 했다. YTN 기사에 따르면, 최근 3년간 접수된 밀키트 재료 관련 민원은 모두 76건이었고, 이 가운데 식중독 발생 사례는 51%에 달했다. 그동안 밀키트는 의무적으로 영양 성분 표시를 해야 하는 대상에서 제외되어 있었는데, 문제점들이 발생하자 정부는 의무 대상 품목을 단계적으로 확대한다고 입장을 밝혔다. 하지만 그 시기가 불명확하여 그때까지는 업체가 자율적으로 표시하도록 기대하는 수 밖에 없다. 따라서 이에 대한 개선방안도 결론 도출 부분에서 고안해보기로 하였다.

</div>
</details>

<details>
<summary>

#### [간편식을 구매하는 이유 설문 데이터] (matplotlib, donut) </summary>
<div markdown="1">

- 다음은 반대로 간편식을 구매하는 이유에 대해 분석해보았다. 처음에는 가구원수별, 성별별, 연령별로 나누어 인사이트를 각각 도출하고자 했지만 각 분류별 특이점을 찾을 수 없었고 모두 비슷한 추세를 보였기에 전반적인 추이를 살펴보기로 하였다.

<div>
    <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/151becf7-1f41-46e5-86cc-d5dfeef6628b">
    <img width="400" alt="image" src="https://github.com/HyenC/MealKit/assets/38906574/ff3dd0e8-b38e-4c9d-92bf-5ffd80cb7840">
</div>

- 2019년, 2020년, 2021년의 간편식 구입 이유를 살펴보니 ‘조리하기 번거롭고 귀찮아서'가 1위, ‘재료를 사서 조리하는 것보다 비용이 적게 들어서'가 2위를 꾸준히 기록하고 있었으며 ‘직접 조리할 시간이 없어서'와 ‘간편식이 맛있어서'가 각각 3위와 4위를 다투고 있었다. 이를 통해 간편식을 구입하는 이유는 시점의 변화에 크게 민감하게 반응하지 않으며, 조리의 번거로움을 줄이고 비용을 줄이려는 의도가 가장 큰 것으로 보였다. 따라서 차별화된 상품을 만드는 것을 시도한다고 하더라도 ‘조리의 간편성’과 ‘저렴한 비용'이라는 간편식의 가장 근본적인 목적을 잊어서는 안된다는 것을 알 수 있었다.

</div>
</details>

</br>

<details>
<summary> 
    
## 4. 참고자료 </summary>
<div markdown="1">
        
### **학술논문/ 학술지**
- 김도형, 전병륜, 이우영 and 김광용. (2021). 유통‧소비 빅데이터 플랫폼에 대한 사례연구. 한국IT정책경영학회 논문지, 13(4), 2561-2567.
- 김문기, 최희정 and 한상린. (2020). 빅데이터 분석을 활용한 유통 분야 연구동향 분석. 유통연구, 25(3), 85-103.
- 유성은 and 안동환. (2020). 가정간편식 및 외식 소비 영향 요인 분석
- 이유나, 장혜정, 최영우, 최윤솔 and 오지은. (2021). 채식 밀키트 개발을 위한 소비자 인식 및 중요도-수행도 조사 연구. 한국콘텐츠학회 논문지, 21(3), 324-335.
- 이현주. (2021). 코로나19 발생 이후 식품소비 방식별 지출액의 변화 수준에 따른 시장세분화: 20~50대 소비자를 중심으로. 소비자정책교육연구, 17(2), 1-28.
- 이홍승 and 김준환. (2021). 코로나19로 인한 식품 소비행태 변화분석: MZ세대를 중심으로. 디지털융복합연구, 19(3), 47-54.
- 정유빈, 황희원, 정효재 and 오지은. (2022). 식생활라이프스타일에 따른 중장년층과 노년층의 HMR 제품 구매행동과 선택속성에 대한 연구: 서울,경기지역을 중심으로. 한국콘텐츠학회 논문지, 22(2), 770-781.
- 황진수, 박권철, 윤영진 and 김현준. (2018). 가정간편식 시장에서 제품특성을 활용한 경영전략에 관한 연구. 호텔경영학연구, 27(8), 327-338.

### **학술대회 발표자료 및 보고서**
- 포스트코로나 시대 식품산업 전망과 과제 (이정희 교수)
- 2019 식품소비행태조사 결과발표대회: 친환경식품에 대한 관심과 실제 구매행위는 어떻게 다른가? (강혜정 교수)
- 2020 식품소비행태조사 결과발표대회: 코로나 19와 식품 소비행태 변화 (강혜정 교수)
- 2021 식품소비자행태조사 결과발표대회: 1인 가구의 세대별 식생활 특성에 관한 비교분석 및 시사점 (이현주 교수)
- [KREI] 2021년 가구의 가공식품 소비 지출 변화와 특징
- 월간유통산업동향 2022년 4~10월호: What's Next in Retail 2022
- 오픈 서베이 식료품 구매 트렌드 리포트 2019, 2020, 2021
- 식품소비행태조사 기초분석 보고서 2019, 2020, 2021

### **신문기사**
- 코로나 팬데믹으로 인한 기능성 성분이 함유된 식품 소비 증가
- [2021 핫한 음식] 가정간편식(HMR)과 밀키트 열풍, 차이점과 문제점은?
- '밀키트' 열풍, 다이어트 위해 '밀키트'로 삼시세끼 먹기
- 너도나도 뛰어드는 밀키트 시장…올해도 굳건할까
- 위드 코로나 이후 식생활: 집밥 대세 꺾였나…신선식품 덜 사먹고 외식 늘고
- [지구용]쓰레기 걱정 줄인 비건 밀키트가 왔어요
- [퍼스트펭귄] 영국 비건 밀키트 배달 스타트업이 사랑받는 이유
- 관악구, 중장년 1인가구에 밀키트 지원
- 노인을 위한 음식은 있다… ‘엔젤스 밀’ 사전 예약분 완판
- 간편한 한 끼 식사 ‘밀키트’ 영양성분 정보 제공 필요해요!
- 2022 식품•외식 전망
- [인터뷰] 코로나19가 가져온 캠핑 트렌드 변화는?
- "힙한 사찰음식" 간편식 잇달아 출시
- 중부지방 폭우로 편의점 간편식 수요 급증…수건·양초 매출도↑

## 5-2 출처
### **학술논문/ 학술지**
- 빅데이터 분석을 활용한 유통 분야 연구동향 분석
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002612228
    
- 유통**‧**소비 빅데이터 플랫폼에 대한 사례연구
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002748468
    
- 코로나19로 인한 식품 소비행태 변화분석: MZ세대를 중심으로
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002696205
    
- 코로나19 발생 이후 식품소비 방식별 지출액의 변화 수준에 따른 시장세분화: 20~50대 소비자를 중심으로
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002726296
    
- 가정간편식 및 외식 소비 영향 요인 분석
    https://www.krei.re.kr/foodSurvey/selectBbsNttView.do?key=1930&bbsNo=1024&nttNo=142838&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=
    
- 가정간편식 시장에서 제품특성을 활용한 경영전략에 관한 연구
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002421342
    
- 채식 밀키트 개발을 위한 소비자 인식 및 중요도-수행도 조사 연구
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002697300
    
- 식생활 라이프 스타일에 따른 중장년층과 노년층의 HMR 제품 구매행동과 선택속성에 대한 연구: 서울, 경기지역을 중심으로
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002814374
    

### **학술대회 발표자료 및 보고서**
- 포스트코로나 시대 식품산업 전망과 과제 (이정희 교수)
    https://www.mfds.go.kr/brd/m_59/down.do?brd_id=cmnt0019&seq=408&data_tp=A&file_seq=2
    
- 2019 식품소비행태조사 결과발표대회: 친환경식품에 대한 관심과 실제 구매행위는 어떻게 다른가? (강혜정 교수)
    https://www.krei.re.kr/foodSurvey/selectBbsNttView.do?key=807&bbsNo=450&nttNo=131571&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=
    
- 2020 식품소비행태조사 결과발표대회: 코로나 19와 식품 소비행태 변화 (강혜정 교수)
    https://www.krei.re.kr/foodSurvey/selectBbsNttView.do?key=807&bbsNo=450&nttNo=134424&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=
    
- 2021 식품소비자행태조사 결과발표대회: 1인 가구의 세대별 식생활 특성에 관한 비교분석 및 시사점 (이현주 교수)
    https://www.krei.re.kr/foodSurvey/selectBbsNttView.do?key=807&bbsNo=450&nttNo=155189&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=
    
- [KREI] 2021년 가구의 가공식품 소비 지출 변화와 특징
    https://www.atfis.or.kr/home/board/FB0003.do?act=read&bpoId=4209
    
- 월간유통산업동향 2022년 4~10월호: What's Next in Retail 2022
    https://retaildb.or.kr/use/board/bbs/detail/55?page=1&size=10&schType=&schCategory=&schText=
    
- 오픈 서베이 식료품 구매 트렌드 리포트 2019, 2020, 2021, 2022
    [https://blog.opensurvey.co.kr/trendreport/online-grocery-2022/#:~:text=소비자의 81.5%25는 온라인,무려 2.5배나 성장했습니다](https://blog.opensurvey.co.kr/trendreport/online-grocery-2022/#:~:text=%EC%86%8C%EB%B9%84%EC%9E%90%EC%9D%98%2081.5%25%EB%8A%94%20%EC%98%A8%EB%9D%BC%EC%9D%B8,%EB%AC%B4%EB%A0%A4%202.5%EB%B0%B0%EB%82%98%20%EC%84%B1%EC%9E%A5%ED%96%88%EC%8A%B5%EB%8B%88%EB%8B%A4).
    
- 식품소비행태조사 기초분석 보고서 2019, 2020, 2021
    https://www.krei.re.kr/foodSurvey/selectBbsNttList.do?bbsNo=448&key=805
    

### **신문기사**
- CULTURE&LIFESTYLE. (2021). [인터뷰] 코로나19가 가져온 캠핑 트렌드 변화는?https://cjnews.cj.net/%EC%9D%B8%ED%84%B0%EB%B7%B0-%EC%BD%94%EB%A1%9C%EB%82%9819%EA%B0%80-%EA%B0%80%EC%A0%B8%EC%98%A8-%EC%BA%A0%ED%95%91-%ED%8A%B8%EB%A0%8C%EB%93%9C-%EB%B3%80%ED%99%94%EB%8A%94/. CJ NEWSROOM
- 경민경. (2021). [2021 핫한 음식] 가정간편식(HMR)과 밀키트 열풍, 차이점과 문제점은?. https://www.mhns.co.kr/news/articleView.html?idxno=501777.  문화뉴스
- 그린매거진 편집부. (2022). 코로나 팬데믹으로 인한 기능성 성분이 함유된 식품 소비 증가. http://rda.go.kr/webzine/2022/06/sub2-4.html. 그린매거진
- 김다정. (2022). 집밥 대세 꺾였나…신선식품 덜 사먹고 외식 늘고. https://www.nongmin.com/news/NEWS/ECO/CMS/362227/view. 농민신문
- 김선정. (2021). 1인중년가구 위해 민·관이 손잡았다. http://www.tynewspaper.co.kr/news/articleView.html?idxno=20421. 통영신문
- 김은서. (2022). [이슈포커스] 엔데믹에 밀키트 무인매장 줄폐업...이유는?. http://www.sisacast.kr/news/articleView.html?idxno=34945. 시사CAST
- 김응구. (2022). 관악구, 중장년 1인가구에 밀키트 지원. http://www.sijung.co.kr/news/articleView.html?idxno=279445. 시정일보
- 남주원. (2022). [퍼스트펭귄] 영국 비건 밀키트 배달 스타트업이 사랑받는 이유. https://www.newspenguin.com/news/articleView.html?idxno=10408. 뉴스펭귄
- 변선진. (2022). 너도나도 뛰어드는 밀키트 시장…올해도 굳건할까. http://news.imaeil.com/page/view/2022041412260563661. 매일일보
- 이순용. (2020). '밀키트' 열풍, 다이어트 위해 '밀키트'로 삼시세끼 먹기. https://www.edaily.co.kr/news/read?newsId=02348486625831896&mediaCodeNo=257. 이데일리
- 이지윤. (2022). "힙한 사찰음식" 간편식 잇달아 출시. https://v.daum.net/v/Htn2qpzc6M
. 동아일보
- 이희승. (2022). "유행 끝나" vs "시장 강화 중" 엇갈린 HMR 업계 반응. http://www.newskr.kr/news/articleView.html?idxno=77144. 한국농어촌방송
- 임성현, 김시균, 한재범. (2021). 찬사받던 K방역 대혼돈...코로나 컨트롤타워만 4개, 지자체까지 가세. https://www.mk.co.kr/news/society/view/2021/07/684544/. 매일경제
- 팀지구용. (2021). [지구용]쓰레기 걱정 줄인 비건 밀키트가 왔어요. https://www.sedaily.com/NewsView/22RC0MQM1M. 서울경제
- 온라인뉴스부. (2021). 노인을 위한 음식은 있다… ‘엔젤스 밀’ 사전 예약분 완판. https://www.seoul.co.kr/news/newsView.php?id=20210323500113. 서울신문
- 전은희. (2022). 팬데믹 이후 성장하고 있는 ‘캠핑용 식품' 시장 동향. https://www.sommeliertimes.com/news/articleView.html?idxno=21270. SOMMELIER TIMES
- 황희정. (2022). 중부지방 폭우로 편의점 간편식 수요 급증…수건·양초 매출도↑. https://www.yna.co.kr/view/AKR20220815014300003. 연합뉴스
  </div>
  </details>
