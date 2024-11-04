import streamlit as st
import pandas as pd
import plotly.express as px
import requests

ALPHA_VANTAGE_API_KEY = 'OEGYY6XXADTSPLIR'

def get_real_data(pair, start_date, end_date):
    """
    Генерирует реальные данные для выбранной валютной пары
    Параметры:
        - pair (str): Название валютной пары
        - start_date: Начала даты для формировани графика (начало периода)
        - end_date: коец даты для формирования графика (конец периода)

    Возвращает:
        - DataFrame с датами от даты начала до даты конца и все даты между ними,
         а также реальные значения от API
    """
    first_cross = pair[:3]
    second_cross = pair[3:]
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={first_cross}&to_symbol={second_cross}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=full'
    response = requests.get(url)
    data = response.json()

    if 'Time Series FX (Daily)' in data:
        time_series = data['Time Series FX (Daily)']
        # print(time_series)
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df.index = pd.to_datetime(df.index)
        df = df[['4. close']].astype(float)
        filtered_df = df.loc[(df.index>=start_date)&(df.index<=end_date)].reset_index().\
            rename(columns={'index':'Date','4. close':'Close'})
        return filtered_df
    return pd.DataFrame()


def get_dates(pair, start_date, end_date):
    """
    Генерирует фейковые данные для выбранной валютной пары
    Параметры:
        - pair (str): Название валютной пары
        - start_date: Начала даты для формировани графика (начало периода)
        - end_date: коец даты для формирования графика (конец периода)

    Возвращает:
        - DataFrame с датами от даты начала до даты конца и все даты между ними, а также рандомные значения
    """
    dates = pd.date_range(start = start_date, end=end_date)
    prices = pd.Series(1+(pd.Series(range(len(dates)))*0.01)).sample(frac=1).values

    return pd.DataFrame({"Date":dates,"Price":prices})



def display_currency_pairs():
    """
    Функция отобржает разворачивающуюся панель с валютными парами.
    Параметры:
        -
    Возвращает:
         None
    """
    with st.expander("Валютные кросс-пары"):
        pairs = ["EURUSD", "GBPUSD", "USDRUB" , "USDJPY","XAUUSD"]
        for pair in pairs:
            if st.button(pair):
                data = get_real_data(pair, start_date, end_date)
                if not data.empty:
                    fig = px.line(data, x = "Date", y="Close", title=f"График {pair}")
                    st.plotly_chart(fig)
                else:
                    st.error("Для пары которую вы выбрали, нет сейчас данных! Пожалуйста, выберите другую пару")



st.sidebar.header("Выбор дат")
start_date = st.sidebar.date_input(label="Дата начала")
end_date = st.sidebar.date_input(label="Дата конца")

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

if start_date > end_date:
    st.sidebar.error("Ошибка: Дата конца должна быть меньше, чем дата начала!")


display_currency_pairs()