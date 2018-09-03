import sqlite3
import folium

conn = sqlite3.connect('review.sqlite')
cur = conn.cursor()

cur.execute('''SELECT name, latitude, longitude, stars, review_count
    FROM Business
    WHERE longitude < -100 and latitude < 38 and review_count > 1000
    ORDER BY stars DESC, review_count DESC''')

count = 0

restaurantMap = folium.Map(location = [36.11, -115.17], zoom_start = 13)
for row in cur:
    count = count + 1
    if count < 6:
        folium.Circle(location = [row[1], row[2]],
            popup = row[0], fill_color = '#A020F0', color = '#000000',
            radius = row[4]/6, weight = 1).add_to(restaurantMap)
    elif count < 11:
        folium.Circle(location = [row[1], row[2]],
            popup = row[0], fill_color = '#BA55D3', color = '#000000',
            radius = row[4]/6, weight = 1).add_to(restaurantMap)
    elif count < 16:
        folium.Circle(location = [row[1], row[2]],
            popup = row[0], fill_color = '#DDA0DD', color = '#000000',
            radius = row[4]/6, weight = 1).add_to(restaurantMap)
    else:
        folium.Circle(location = [row[1], row[2]],
            popup = row[0], fill_color = '#FFF5EE', color = '#000000',
            radius = row[4]/6, weight = 1).add_to(restaurantMap)
    if count == 25: break

restaurantMap.save('restaurantMap.html')
