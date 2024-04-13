#Name: Jeffrey Guaman
#Date: October 28th, 2023
#email: JEFFREY.GUAMAN18@myhunter.cuny.edu
#This program makes a map and adds a pop for Hunter College Main Campus
import folium

data = folium.Map((40.75, -74.125))
Hunter = folium.Marker((40.75, -74.125), popup= 'Hunter College')
data.add_child(Hunter)

data.save("nycMap.html")
