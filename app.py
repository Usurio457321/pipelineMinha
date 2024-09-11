import streamlit as st
from contrato import Vendas
from datetime import datetime,time
from pydantic import ValidationError

#st.write("esse é meu dashboard")

def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do servidor")
    data = st.date_input("Data Compra",datetime.now())
    hora = st.time_input("Campo para selecionar a hora em que a venda foi realizada")
    valor = st.number_input("Valor da Venda")
    quantidade = st.number_input("Campo numérico para inserir a quantidade de produtos vendidos")
    produto = st.selectbox("Campo da seleção para escolher o produto vendido",["ZapFlow com Gemini","ZapFlow com ChatGPT","ZapFlow com LIama3.0"])

    if st.button("Salvar"):

        venda = Vendas(
            email = email,
            data = data_hora,
            valor = valor,
            quantidade = quantidade,
            produto = produto
        )
        data_hora = datetime.combine(data,hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email do vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")
        


if __name__=="__main__":
    main()    

