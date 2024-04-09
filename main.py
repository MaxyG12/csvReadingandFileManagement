import os
import csv

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    print(row["Artist(s)"])
    if not os.path.exists(row["Artist(s)"]):
      os.mkdir(row["Artist(s)"])
    with open(f"{row['Artist(s)']}/{row['Song']}.txt", "w") as song:
      song.write(row["Song"])


