import streamlit as st
import plotly.express as px
from get_data import GetData
from config import CURRENCY_PAIRS

class App:
    """Класс для отображения приложения Streamlit, боковой панели и графиков"""

    def __init__(self):
        self.start_date = None
        self.end_date = None

    def display_sidebar(self)->None:
        """
        Отображает боковую панель для выбора периода валютных пар

        :Возвращает:
        """

        st.sidebar.header("Выбор дат")
        self.start_date = st.sidebar.date_input(label="Дата начала")
        self.end_date = st.sidebar.date_input(label="Дата конца")
        if self.start_date > self.end_date:
            st.sidebar.error("Ошибка: Дата конца должна быть меньше, чем дата начала!")

    def display_currency_pairs(self)->None:
        """
        Отображает график выбранной валютной пары в выбранном диапазоне дат

        :Возвращает:
        """

        with st.expander("Валютные кросс-пары"):
            pairs = CURRENCY_PAIRS
            for pair in pairs:
                if st.button(pair):
                    data_f = GetData(pair)
                    data = data_f.get_real_data(pair, self.start_date, self.end_date)
                    if not data.empty:
                        fig = px.line(data, x="Date", y="Close", title=f"График {pair}")
                        st.plotly_chart(fig)
                    else:
                        st.error("Для пары которую вы выбрали, нет сейчас данных! Пожалуйста, выберите другую пару")




