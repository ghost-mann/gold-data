import pandas as pd


def transform_data(df):
    # parsing datetime for sma calculation in chronological order
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.sort_values('datetime')

    df['close'] = df['close'].astype(float)
    df['SMA1O'] = df['close'].rolling(window=10).mean()
    df['candle'] = df.apply(lambda row: 'Bullish' if row['close'] > row['SMA1O'] else 'Bearish', axis=1)

    return df