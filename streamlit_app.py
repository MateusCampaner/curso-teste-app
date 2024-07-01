import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import math
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title='Streamlit', page_icon='🔴')

st.sidebar.header("🔴 Streamlit")

if st.sidebar.button("❄"):
    st.snow()

pagina = st.sidebar.selectbox(
    "Escolha",
    ('Lista de compras', 'Calculadora', 'Visualizar CSV', 'Classificação')
)

if pagina == 'Lista de compras':
    st.header("📜 Lista de compras")

    produtos = st.multiselect(
     'Produtos para comprar',
     ['Arroz', 'Feijão', 'Batata', 'Tomate']
    )

    st.write('Sua lista de compras')
    for i in produtos:
        st.checkbox(i)


    
if pagina == "Calculadora":
    st.header("📐 Calculadora")
    st.write("Calculadora de equação de 2º grau")

    st.write("Fórmula de Bhaskara")
    st.latex(r'''
    x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    ''')

    a = st.number_input('Digite o valor de a', min_value=-100, max_value=100, value=0, step=1)
    b = st.number_input('Digite o valor de b', min_value=-100, max_value=100, value=0, step=1)
    c = st.number_input('Digite o valor de c', min_value=-100, max_value=100, value=0, step=1)

    def calcular_bhaskara(a, b, c):
        delta = b**2 - 4*a*c
        if delta < 0:
            return "A equação não possui raízes reais"
        elif delta == 0:
            x = -b / (2*a)
            return f"A equação possui uma raiz real: x = {x}"
        else:
            x1 = round((-b + math.sqrt(delta)) / (2*a), 3)
            x2 = round((-b - math.sqrt(delta)) / (2*a), 3)
            return f"Resultados x1 = {x1} x2 = {x2}"

    if st.button("✔ Calcular"):
        resultado = calcular_bhaskara(a, b, c)
        st.write(resultado)



if pagina == "Visualizar CSV":
    st.header("📊 Visualizar CSV")

    st.subheader('Upload de CSV')
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.write("Dados do arquivo CSV:")

        selected_columns = st.multiselect(
            'Selecione as colunas para exibir',
            options=df.columns.tolist(),
            default=df.columns.tolist()
        )

        st.write(df[selected_columns])

        

if pagina == 'Classificação':
    st.header("🤖 Classificação")

    #pip install scikit-learn
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn import tree
    from sklearn.metrics import accuracy_score

    iris = load_iris()

    dados = iris.data
    especies = iris.target

    porcentagem = st.slider(
        'Escolha a porcentagem de treino',
        0.01, 0.99, (0.30)
    )
    
    criterios = st.selectbox(
        'Escolha o seu critério',
        ('gini', 'entropy', 'log_loss')
    )

    if st.button("Treinar modelo"):
        x_train, x_test, y_train, y_test = train_test_split(dados, especies, test_size=porcentagem, random_state=42)
        clf = tree.DecisionTreeClassifier(criterion=criterios)
        clf.fit(x_train, y_train)
        prev = clf.predict(x_test)
        
        acuracia = round(((accuracy_score(prev, y_test))*100), 3)

        st.write(f"Sua acurácia é de {acuracia}")