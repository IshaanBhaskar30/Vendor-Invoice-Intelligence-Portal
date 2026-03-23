def add_features(df):
    df = df.copy()

    df['unit_price'] = df['Dollars'] / df['Quantity']
    df['freight_ratio'] = df['Freight'] / df['Dollars']
    df['dollar_diff_ratio'] = abs(
        df['Dollars'] - df['total_item_dollars']
    ) / df['total_item_dollars']

    return df