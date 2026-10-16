import pandas as pd
df = pd.read_csv('data/dataset.csv')
target_artists = [
    "Ariana Grande",
    "Drake",
    "Brent Faiyaz",
    "J. Cole",
    "Sade"
]
target_df = df[df['artists'].isin(target_artists)]
target_df = target_df.drop_duplicates(subset=['track_name', 'artists'])
target_df.to_csv("data/cleaned_dataset.csv", index=False)
print(f"cleaned dataset created with {len(target_df)} songs")

