#pip install folium
import folium 
  
# Map method of folium return Map object 
  
# Here I pass coordinates of Rishikesh  
# and starting Zoom level = 15 



my_map = folium.Map(location = [Latitude, Longitude], 
                                        zoom_start = 15) 
  
# Pass a string in popup parameter 
folium.Marker([Latitude, Longitude], 
               popup = 'Rishikesh').add_to(my_map) 
  
  
my_map.save(" my_map.html ") 
