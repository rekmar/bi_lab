import csv
from pathlib import Path

films = []
file_path = Path("IMDB-Movie-Data.csv")
if file_path.exists():
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            films.append({'title': row['Title'], 'year': row['Year'], 'rating': row['Rating']})
    file.close()
else:
    print("File not exists")

top_rat = []
for film in films:
    top_rat.append({'title': film['title'], 'rating': film['rating']})
top_rat.sort(key=lambda films: films['rating'], reverse=True)

with open('top250_movies.csv', 'w', newline='') as top250file:
    fieldnames = ['title', 'rating']
    writer = csv.DictWriter(top250file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(top_rat[:250])
top250file.close()

years = {}

for film in films:
    year = years.get(film["year"], [0, 0.0])
    year[0] += 1
    year[1] += float(film["rating"])
    years[film["year"]] = year

avg_years = {}
for year, values in years.items():
    avg_years[year] = round(values[1]/values[0], 1)

with open('rating.csv', 'w', newline='') as rat_file:
    fieldnames = ['Year', 'Avg_rating']
    writer = csv.DictWriter(rat_file, fieldnames=fieldnames)
    writer.writeheader()
    for year, value in avg_years.items():
        writer.writerow({"Year": year, "Avg_rating": value})
rat_file.close()
