import folium
import folium as g
import webbrowser
import base64
from folium.plugins import MiniMap
import os
import time

m = folium.Map(location=[35.134032, 129.1031735],zoom_start=12)
minimap = MiniMap()
minimap.add_to(m)

latlon=[
    [35.100095132250054,  129.02695924043655] #중구
]

latlon1=[
    [35.1581383, 129.0612467] #진구
]

latlon2=[
    [35.1381094, 129.1042361] #남구
]

latlon3=[
    [35.1561336, 129.1243101] #수영구
]

latlon4=[
    [35.0711451, 129.0669395] #영도구
]

latlon5=[
    [35.118278, 129.0407564] #동구
]

latlon6=[
    [35.1617421, 129.1597712] #해운대구
]

latlon7=[
    [35.1042357, 129.0205093] #서구
]

latlon8=[
    [35.2057237, 129.0793501] #동래구
]

latlon9=[
    [35.140293, 129.1084256] #수영구
]

latlon10=[
    [35.1380363, 129.0924108] #남구
]

pic = base64.b64encode(open('1.png', 'rb').read()).decode()
image_tag = '<img src="data:image/jpeg;base64,{}">'.format(pic)
iframe = folium.IFrame(image_tag, width=420, height=450)
popup = folium.Popup(iframe, max_width=650)

pic1 = base64.b64encode(open('2.png', 'rb').read()).decode()
image_tag1 = '<img src="data:image/jpeg;base64,{}">'.format(pic1)
iframe1 = folium.IFrame(image_tag1, width=420, height=450)
popup1 = folium.Popup(iframe1, max_width=600)

pic2 = base64.b64encode(open('3.png', 'rb').read()).decode()
image_tag2 = '<img src="data:image/jpeg;base64,{}">'.format(pic2)
iframe2 = folium.IFrame(image_tag2, width=420, height=450)
popup2 = folium.Popup(iframe2, max_width=600)

pic3 = base64.b64encode(open('4.png', 'rb').read()).decode()
image_tag3 = '<img src="data:image/jpeg;base64,{}">'.format(pic3)
iframe3 = folium.IFrame(image_tag3, width=420, height=450)
popup3 = folium.Popup(iframe3, max_width=600)

pic4 = base64.b64encode(open('5.png', 'rb').read()).decode()
image_tag4 = '<img src="data:image/jpeg;base64,{}">'.format(pic4)
iframe4 = folium.IFrame(image_tag4, width=420, height=450)
popup4 = folium.Popup(iframe4, max_width=600)

pic5 = base64.b64encode(open('6.png', 'rb').read()).decode()
image_tag5 = '<img src="data:image/jpeg;base64,{}">'.format(pic5)
iframe5 = folium.IFrame(image_tag5, width=420, height=450)
popup5 = folium.Popup(iframe5, max_width=600)

pic6 = base64.b64encode(open('7.png', 'rb').read()).decode()
image_tag6 = '<img src="data:image/jpeg;base64,{}">'.format(pic6)
iframe6 = folium.IFrame(image_tag6, width=420, height=450)
popup6 = folium.Popup(iframe6, max_width=600)

pic7 = base64.b64encode(open('8.png', 'rb').read()).decode()
image_tag7 = '<img src="data:image/jpeg;base64,{}">'.format(pic7)
iframe7 = folium.IFrame(image_tag7, width=420, height=450)
popup7 = folium.Popup(iframe7, max_width=600)

pic8 = base64.b64encode(open('9.png', 'rb').read()).decode()
image_tag8 = '<img src="data:image/jpeg;base64,{}">'.format(pic8)
iframe8 = folium.IFrame(image_tag8, width=420, height=450)
popup8 = folium.Popup(iframe8, max_width=600)

pic9 = base64.b64encode(open('10.png', 'rb').read()).decode()
image_tag9 = '<img src="data:image/jpeg;base64,{}">'.format(pic9)
iframe9 = folium.IFrame(image_tag9, width=420, height=450)
popup9 = folium.Popup(iframe9, max_width=600)

pic10 = base64.b64encode(open('11.png', 'rb').read()).decode()
image_tag10 = '<img src="data:image/jpeg;base64,{}">'.format(pic10)
iframe10 = folium.IFrame(image_tag10, width=420, height=450)
popup10 = folium.Popup(iframe10, max_width=600)

for i in range(len(latlon)):
    folium.Marker(latlon[i],
                  icon=g.Icon(icon='heart',color='blue'),
                  popup = popup,
                  tooltip="왕대박숯불갈비").add_to(m)
    
for i in range(len(latlon1)):
    folium.Marker(latlon1[i],
                  icon=g.Icon(icon='heart',color='blue'),
                  popup = popup1,
                  tooltip="그집곱도리탕").add_to(m)
    
for i in range(len(latlon2)):
    folium.Marker(latlon2[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup2,
                  tooltip="온더야드").add_to(m)
    
for i in range(len(latlon3)):
    folium.Marker(latlon3[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup3,
                  tooltip="민생주").add_to(m)
    
for i in range(len(latlon4)):
    folium.Marker(latlon4[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup4,
                  tooltip="와글와글").add_to(m)
    
for i in range(len(latlon5)):
    folium.Marker(latlon5[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup5,
                  tooltip="송원감자탕").add_to(m)
    
for i in range(len(latlon6)):
    folium.Marker(latlon6[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup6,
                  tooltip="해목").add_to(m)

for i in range(len(latlon7)):
    folium.Marker(latlon7[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup7,
                  tooltip="바사케").add_to(m)

for i in range(len(latlon8)):
    folium.Marker(latlon8[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup8,
                  tooltip="이십칠").add_to(m)
    
for i in range(len(latlon9)):
    folium.Marker(latlon9[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup9,
                  tooltip="뉴러우멘관즈").add_to(m)
    
for i in range(len(latlon10)):
    folium.Marker(latlon10[i],
                  icon=g.Icon(icon='heart', color='blue'),
                  popup = popup10,
                  tooltip="홈베이킹").add_to(m)

m.save('filename.html')
webbrowser.open_new_tab('filename.html')
time.sleep(5)
os.system("taskkill /im msedge.exe /f")
time.sleep(0.1)