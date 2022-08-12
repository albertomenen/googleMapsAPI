import os
import googlemaps # pip install googlemaps
import win32com.client as win32com

API_KEY = open("API_KEY.txt").read()
map_client = googlemaps.Client(API_KEY)

#def get_place_info()
