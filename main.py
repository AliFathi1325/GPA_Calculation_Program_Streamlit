import streamlit as st

st.title('GPA Calculation')
st.write('Enter your grades')

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    English = st.number_input('English', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
    Mathematics = st.number_input('Mathematics', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
    Science = st.number_input('Science', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
with col2:
    History = st.number_input('History', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
    Geography = st.number_input('Geography', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
    Art_and_Design = st.number_input('Art and Design', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
with col3:
    Music = st.number_input('Music', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
    Physical_Education = st.number_input('Physical Education', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
    Information_Technology = st.number_input('Information Technology', min_value=0.0, max_value=20.0, value=1.0, step=0.1)

# Scores entered in the list
data = [English, Mathematics, Science, History, Geography, Art_and_Design, Music, Physical_Education, Information_Technology]

# Calculation of average scores
mean = sum(data) / len(data)

# Display GPA at the push of a button
if st.button('GPA calculation'):
    st.success(f'Your GPA is {mean:.2f}')