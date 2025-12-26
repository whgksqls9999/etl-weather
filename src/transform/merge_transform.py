def merge_weather_dust(weather_df, dust_df):
    merged = weather_df.merge(
        dust_df,
        on="date",
        how="left"
    )
    
    if merged.isnull().any().any():
        print("[Warning] Missing values detected")
        
    print("[Transform] Weather + Dust merged")
    return merged