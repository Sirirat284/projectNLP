import streamlit as st



sample_user = st.selectbox(
    'เลือกข้อมูลตัวอย่าง',
    ('นาย A', 'นาย B', 'นาย C'))
sex= st.selectbox(
    'เพศ',
    ('ชาย', 'หญิง'))
NATIONALITY_NAME= st.selectbox(
    'สัญชาติ',
    ('ไทย', 'พม่า','ลาว','กัมพูชา','อื่น'))
st.write('You selected:', sample_user)