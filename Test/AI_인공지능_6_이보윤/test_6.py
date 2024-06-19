import folium
import webbrowser

m = folium.Map(location = [35.1347223, 129.107886],
               zoom_start = 12)

latlon=[
    [35.1347223, 129.107886],
]
   
for i in range(len(latlon)):
     folium.Marker(latlon[i],
                   popup = 'marker',
                   tooltip="부경대학교").add_to(m)


m.save('filename.html')
webbrowser.open_new_tab('filename.html')