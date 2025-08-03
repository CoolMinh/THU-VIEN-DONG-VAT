
import streamlit as st 
st.set_page_config(page_title='Trắc nghiệm tính cách', page_icon=':question:', layout='wide')

st.title('Hãy chọn một con vật bạn yêu thích')
col1, col2, col3, col4, col5 = st.columns(5)

Personality = {
    'con mèo': 'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, bạn khao khát được nghỉ.',
    'con chó': 'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề xảy ra.',
    'con sư tử': 'Có thể thấy bạn là người có vẻ bề ngoài nổi bật. Bạn thu hút mọi người bằng vẻ bề ngoài hào nhoáng.',
    'con ngựa': 'Có điều gì đó đang hạn chế sự tự do của bạn.',
    'thiên nga': 'Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó nhé.'
}

with col1:
    b1 = st.button('Con mèo')
with col2:
    b2 = st.button('Con chó')
with col3:
    b3 = st.button('Con sư tử')
with col4:
    b4 = st.button('Con ngựa')
with col5:
    b5 = st.button('Thiên nga')

if b1:
    with st.expander('Con mèo'):
        st.write(Personality['con mèo'])
if b2:
    with st.expander('Con chó'):
        st.write(Personality['con chó'])
if b3:
    with st.expander('Con sư tử'):
        st.write(Personality['con sư tử'])
if b4:
    with st.expander('Con ngựa'):
        st.write(Personality['con ngựa'])
if b5:
    with st.expander('Thiên nga'):
        st.write(Personality['thiên nga'])

with st.sidebar:
    st.title('Trắc nghiệm tính cách')
    if b1:
        st.write('Con vật bạn chọn là con mèo')
    if b2:
        st.write('Con vật bạn chọn là con chó')
    if b3:
        st.write('Con vật bạn chọn là con sư tử')
    if b4:
        st.write('Con vật bạn chọn là con ngựa')
    if b5:
        st.write('Con vật bạn chọn là thiên nga')
