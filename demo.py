import streamlit as st

# text elements

if st.sidebar.button('Text Elements'):
    st.write('hello welcome to Value Laden')
    st.markdown('this is markdown')
    st.title('this is title')
    st.header('this is header')
    st.divider()
    st.subheader('this is subheader')
    st.caption('this is caption')
    st.code('this is code')
    st.text('this is text')
    st.latex('this is latex - (a+b)^2 = a^2 + b^2 + 2ab')

# input widgets
if st.sidebar.button('Input widget'):
    st.text_input('Name')
    st.number_input('Age')
    st.date_input('DOB')
    st.time_input('Time of Birth')
    st.radio('Gender',['Male','Female'])
    st.selectbox('Graduation',['12th','BTech','MTech'])
    st.multiselect('Skills',['C','Python','Java'])
    st.file_uploader('Upload your resume')
    st.toggle('Interested')
    st.text_area('Summary')
    st.checkbox('I agree to terms')
    st.button('Submit')
    st.link_button('go to page','https://www.google.com')

# layouts and containers
if st.sidebar.button('Other elements'):
        
    col1,col2,col3,col4 = st.columns(4)
    col1.write('this is col1')
    col2.write('this is col2')
    col3.write('this is col3')
    col4.write('this is col4')

    tab1,tab2 = st.tabs(['tab1','tab2'])
    tab1.write('this is tab1')
    tab2.write('this is tab2')

    with st.expander('click to know more'):
        st.write('this is expander')
    st.chat_input('Ask something')
    st.balloons()
    st.snow()
    st.success('successfully registered')
    st.error('this is error')
    st.warning('this is warning')