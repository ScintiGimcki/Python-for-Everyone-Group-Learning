# Python-for-Everyone-Group-Learning

The dataset used in this project can be downloaded from [yelp.com](https://www.yelp.com/dataset) for free. And the file downloaded will have nearly 3GB data compressed and 7GB if uncompressed in .json format.

Since the dataset is so large and I am only interested in the top 25 most popular restaurants in Los Angeles, I only used the dataset *yelp_academic_dataset_user.json*.

The two code scripts will be included in the repo and you can downloaded them to reproduce what I have down.

## Files

- **createBusiness.py**: this file helps you to construct a SQLite database with table Business
- **top25Map.py**: this file helps you to make the interactive map as restaurantMap.html
- **restaurantMap.html**: the interactive map, where you can zoom in and out and if you click on the circle, the name of the restaurant will pop up.

## Notice

You have to install [*folium*] package for the Python, which can help you draw interactive maps based on Leaflet, one Javascript mapping tool. If you want to download this package, just type the following codes in the bash.
```
python3 -m pip install folium
```

**If you have made further results, hope you can share with me. I will appreciate it very much!**
