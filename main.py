
import streamlit as st 
st.set_page_config(page_title='Trắc nghiệm tính cách', page_icon=':question:', layout='wide')

st.title('Hãy chọn một con vật bạn yêu thích')
col1, col2, col3, col4, col5 = st.columns(5)
col6,col7=st.columns([2,1])




with col1:
    b1 = st.button('Con mèo')
with col2:
    b2 = st.button('Con chó')
with col3:
    b3 = st.button('Con khỉ')
with col4:
    b4 = st.button('Con đại bàng')
with col5:
    b5 = st.button('con gà')

if b1:
    with col6:
        st.write('Âm thanh')
        audio=open('_Cat Meow Sound Effect . Attract Cats, Sounds Cats Love.mp3','rb')
        st.audio(audio,format='audio/mp3')
        
        st.write('Video')
        st.video('https://www.youtube.com/watch?v=suaCbX5ji24')
    with col7:
        image='https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg'
        st.image(image,caption='Con mèo')
if b2:
    with col6:
        st.write('Âm thanh')
        audio=open('Dog barking sound continuously mp3 -- bhaiya choudlhary2635 - YouTube.mp3','rb')
        st.audio(audio,format='audio/mp3')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=mXvCjXaTCkA')
    with col7:
        image='https://upload.wikimedia.org/wikipedia/commons/9/99/Brooks_Chase_Ranger_of_Jolly_Dogs_Jack_Russell.jpg'
        st.image(image,caption='Con chó')
if b3:
    with col6:
        st.write('Âm thanh')
        audio=open('Monkey Noises SFX - YouTube.mp3','rb')
        st.audio(audio,format='audio/mp3')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=YfUMeMw1kY4')
    with col7:
        image='https://upload.wikimedia.org/wikipedia/commons/4/43/Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg'
        st.image(image,caption='Con khỉ')
if b4:
    with col6:
        st.write('Âm thanh')
        audio=open('Eagle Sound Effect - YouTube.mp3','rb')
        st.audio(audio,format='audio/mp3')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=K3oIF-SJCvI')
    with col7:
        image='https://upload.wikimedia.org/wikipedia/commons/6/60/Eagles_together.jpg'
        st.image(image,caption='Con đại bàng')
if b5:
    with col6:
        st.write('Âm thanh')
        audio=open('Hen Sound To Attract Roosters - Chicken Sound Effects Free - YouTube.mp3','rb')
        st.audio(audio,format='audio/mp3')

        st.write('Video')
        st.video('https://www.youtube.com/watch?v=d3i7a6S0TFc')
    with col7:
        image='https://upload.wikimedia.org/wikipedia/commons/b/b2/Male_and_female_chicken_sitting_together.jpg'
        st.image(image,caption='Con gà')
