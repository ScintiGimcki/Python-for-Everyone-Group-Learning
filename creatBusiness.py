import json
import sqlite3

file = open("yelp_academic_dataset_business.json", encoding = 'utf-8')

conn = sqlite3.connect('review.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Business
    (id INTEGER PRIMARY KEY UNIQUE, business_id TEXT UNIQUE,
    name TEXT, latitude FLOAT, longitude FLOAT, stars FLOAT,
    review_count INTEGER)''')

for item in file.readlines():
    each = json.loads(item)
    business_id = each["business_id"]
    name = each["name"]
    if each["latitude"] is not None:
        latitude = float(each["latitude"])
    if each["longitude"] is not None:
        longitude = float(each["longitude"])
    if each["stars"] is not None:
        stars = float(each["stars"])
    if each["review_count"] is not None:
        review_count = int(each["review_count"])

    cur.execute('''INSERT OR IGNORE INTO Business (business_id,
        name, latitude, longitude, stars, review_count) VALUES
        (?, ?, ?, ?, ?, ?)''', (business_id, name, latitude,
        longitude, stars, review_count))

conn.commit()
cur.close()
