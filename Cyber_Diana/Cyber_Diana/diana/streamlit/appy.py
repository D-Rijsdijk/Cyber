import streamlit as st
import pandas as pd

num_a = st.number_input('Número A',value = 0)
num_b = st.number_input('Número B', value = 0)

arredondar = st.checkbox('Arredondar resultado')
op = st.radio('Operação:', ['Soma', 'Subtração', 'Multiplicação', 'Divisão'])

if op == 'Soma':
    st.write(num_a + num_b)
elif op =='Subtração':
    st.write(num_a - num_b)
elif op =='Multiplicação':
    st.write(num_a * num_b)
else:
    if arredondar:
        st.write(round(num_a / num_b, 1))
    else:
        st.write(num_a / num_b)

tabela = pd.DataFrame({
    'dados_x' : [0, 1, 2, 3, 4],
    'dados_y' : [0, 1, 2, 3, 8]

})

st.write(tabela)
st.line_chart(tabela, x = 'dados_x', y = 'dados_y',) #não ta terminado


'''
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button('Somar'):
        st.write(f'A + B = {num_a + num_b}')

with col2:
    if st.button('Subtrair'):
        st.write(f'A - B = {num_a - num_b}')

with col3:
    if st.button('Multiplicar'):
        st.write(f'A * B = {num_a * num_b}')

with col4:
    if st.button('Dividir'):
        st.write(f'A / B = {num_a / num_b}')
'''