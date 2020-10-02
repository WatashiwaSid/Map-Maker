# import folium package 
import folium 
  
# Map method of folium return Map object 
  
# Here we pass coordinates of Gfg  
# and starting Zoom level = 12 



def Latitude():
    x = input(float("Latitude : \n"))
    return x

def Longitude():
    y = input(float("Longitude : \n"))
    return y

# def return_text():
#     global Latitude
#     global Longitude
#     coordinate_1 = 




my_map = folium.Map(location = [Latitude, Longitude], 
                                        zoom_start = 15) 
  
# Pass a string in popup parameter 
folium.Marker([Latitude, Longitude], 
               popup = ' Rishikesh').add_to(my_map) 
  
  
my_map.save(" my_map.html ") 
