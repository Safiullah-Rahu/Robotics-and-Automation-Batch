import streamlit as st
import time

st.write("Hi, it's AI!")

st.title("This is Demo")

st.header("This is header")

st.markdown("This is Markdown")

st.subheader("This is subheader")

st.caption("This is caption")

st.code("import time")

st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.image("safi.jpg")

st.audio("audio.mp3")

st.video("video.mp4")

# Input Widgets

st.checkbox('Yes')

st.button('Click')

st.radio("Pick your gender", ["Male", "Female"])

st.selectbox("Choose a planet", ["Mars", "Earth", "Jupiter"])

st.multiselect("Pick a mark", ["Bad", 'Good', 'Excellent'])

st.select_slider("Pick a mark", ["Bad", 'Good', 'Excellent'])

st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0, 10)

st.text_input('Email address')

st.date_input("Travelling date")

st.time_input("Chhuti time")

st.text_area("Description")

st.file_uploader("Upload a photo")

st.color_picker("Choose your fav color")

# st.balloons()
# st.progress(100)
# with st.spinner("Wait for it...."):
#     time.sleep(10)
    
st.success("You did it !")
st.error("Error occurred!")
st.warning("Warning message")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))