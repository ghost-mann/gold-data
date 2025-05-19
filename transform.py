def transform(df):
    df['close'] = df['close'].astype(float)
    df['SMA1O'] = df['close'].rolling(window=10).mean()
    df['candle'] = df.apply(lambda row: 'Bullish' if row['close'] < row['SMA1O'] else 'up', axis=1)
    return df