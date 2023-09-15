import pandas as pd
import zipfile

zip_file_path = "data/winemag-data-130k-v2.csv.zip"

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    csv_file_name = zip_ref.namelist()[0]
    with zip_ref.open(csv_file_name) as csv_file:
        df = pd.read_csv(csv_file)

wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")
#country_points = wine_reviews[['country', 'points']]
avg_country_points = wine_reviews.groupby('country')['points'].mean().reset_index()
avg_country_points['points'] = avg_country_points['points'].round(1)
count_of_wines = (wine_reviews.country.value_counts())
#print(country_points, count_of_wines,)
answer = pd.merge(avg_country_points, count_of_wines, on='country')
print(answer)
answer.to_csv('data/reviews-per-country.csv')
