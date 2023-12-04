#%% #lembre-se dessa hashtag com porcentagem para incializar o jupyternotebooks
import folium
from folium import plugins
from folium.plugins import Draw
from folium.plugins import MousePosition

MapaIFPBCG = folium.Map(location = [-7.23999, -35.91571], 
                        zoom_start = 19, 
                        control_scale = True,
                        tiles= None)

folium.TileLayer(
		        tiles= 'https://{s}.tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token={acesstoken}',
                attr='<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                acesstoken = 'WvNMjK391KKRnUXspyFJXkHEPLsKaEP5F4biz9wjidz4bUZu4uYyNH2y23cleO4z',
                max_zoom= 22,
                min_zoom= 0,
                name='Modo Escuro').add_to(MapaIFPBCG)

folium.TileLayer(
		        tiles= 'https://tile.jawg.io/jawg-light/{z}/{x}/{y}{r}.png?access-token=WvNMjK391KKRnUXspyFJXkHEPLsKaEP5F4biz9wjidz4bUZu4uYyNH2y23cleO4z',
                attr='<a href=\"https://www.jawg.io?utm_medium=map&utm_source=attribution\" target=\"_blank\">&copy; Jawg</a> - <a href=\"https://www.openstreetmap.org?utm_medium=map-attribution&utm_source=jawg\" target=\"_blank\">&copy; OpenStreetMap</a>&nbsp;contributors',
                acesstoken = 'Su1RQRhG7TMz3hpWCkcf4VfDCPLNH1YllY5VTVgYhLDxbWH7mgngnOJDhsN7cDgz',
                max_zoom= 22,
                min_zoom= 0,
                name='Modo Claro').add_to(MapaIFPBCG)


folium.LayerControl().add_to(MapaIFPBCG)










MapaIFPBCG
#%%