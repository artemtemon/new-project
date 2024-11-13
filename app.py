import streamlit as st
from display import App

def main()->None:
    """
    Точка запуска приложения
    :Возвращает:
    """
    st.title("Валютные кросс-пары")
    app = App()
    app.display_sidebar()
    app.display_currency_pairs()

if __name__ == "__main__":
    main()