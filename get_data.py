import requests
import pandas as pd
from config import ALPHA_VANTAGE_API_KEY

class GetData:
    """Класс который генерирует реальные данные"""

    def __init__(self, pair: str):
        self.pair = pair
        self.first_cross = pair[:3]
        self.second_cross = pair[3:]

    def get_real_data(self, pair, start_date: pd.Timestamp, end_date: pd.Timestamp)->pd.DataFrame:
        """
        Генерирует реальные данные для выбранной валютной пары
        Параметры:
            - pair (str): Название валютной пары
            - start_date: Начала даты для формировани графика (начало периода)
            - end_date: конец даты для формирования графика (конец периода)

        Возвращает:
            - DataFrame с датами от даты начала до даты конца и все даты между ними,
             а также реальные значения от API
        """
        url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={self.first_cross}&to_symbol={self.second_cross}&apikey={ALPHA_VANTAGE_API_KEY}&outputsize=full'
        response = requests.get(url)
        data = response.json()

        if 'Time Series FX (Daily)' in data:
            time_series = data['Time Series FX (Daily)']
            df = pd.DataFrame.from_dict(time_series, orient='index')
            df.index = pd.to_datetime(df.index)
            df = df[['4. close']].astype(float)
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
            filtered_df = df.loc[(df.index>=start_date)&(df.index<=end_date)].reset_index().\
                rename(columns={'index':'Date','4. close':'Close'})
            return filtered_df
        return pd.DataFrame()

    @staticmethod
    def get_fake_data(pair, start_date: pd.Timestamp, end_date: pd.Timestamp)->pd.DataFrame:
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
