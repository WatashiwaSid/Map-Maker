# Imports 
import eel
import folium
import fontawesome as fa
import geocoder 
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='Map Maker')


# Variables
Latitude = 0
Longitude = 0
Address = 0
file_name = 0


# Main 
def latlong(n):
    print('Intializing Modules...')

    def my_location():
        global Latitude
        global Longitude
        print('Collecting Coordinates...') 
        g = geocoder.ip('me')
        if g == None:
            my_location()
        elif g != None:
            Latitude,Longitude = g.latlng[0],g.latlng[1]
                    

    def address():
        global Latitude
        global Longitude
        inp_address = input('Enter your address or PinCode : ')
        print('Collecting Coordinates...')
        location = geolocator.geocode(inp_address)
        if location == None:
            address()
        elif location != None:
            Latitude,Longitude = location.latitude,location.longitude

    def raw_cords():
        global Latitude
        global Longitude
        inp_lat = float(input('Enter your Latitude : '))
        inp_long = float(input('Enter your Longitude : '))
        Latitude,Longitude = inp_lat,inp_long


    if n == 'my_location':
        my_location()
    elif n == 'address':
        address()
    elif n == 'raw_cords':
        raw_cords()
    else:
        print('\nInvalid! Input. Please try again.')
        Invalid = input('Enter \"my_location\" to get your location.\nEnter \"address\" to enter your Address.\nEnter \"raw_cords\" to get your Coordinates.\nEnter here : ')
        latlong(Invalid)


def address_gen():
    global Address

    location = geolocator.reverse(f'{Latitude},{Longitude}')
    Address =  location.address


def map_generator():
    global Latitude
    global Longitude
    global Address
    global file_name

    print('Creating Map...')
    m = folium.Map(location=[Latitude,Longitude],zoom_start=12)

    tooltip = 'Click For More Info'

    print('Editing the Map...')
    folium.Marker([Latitude, Longitude],
            popup = folium.Popup(f'<strong>{Address}</strong>', max_width=300,min_width=300),
            tooltip=tooltip,
            icon=folium.Icon(color="red",icon="chevron-down ", prefix='fa')).add_to(m)

    print('Creating file...')
    file_name = Address.split(',')[0]
    file_name = f'{file_name}.html'
    m.save(f'web\{file_name}')

def html_runner():
    global file_name
    eel.init('web')

    try:
        try:
            print('Opening in Browser...')
            eel.browsers.set_path('chrome',r'C:\Program Files (x86)\Google\Application\chrome.exe' or r'%AppData%\Local\Google\Chrome\Application\chome.exe')
            eel.start(rf'{file_name}',size=(800,400))
        except Exception:
            print('Opening in Browser...')
            eel.start(rf'{file_name}',size=(800,400),mode='default')
    except Exception:
        try:
            brows = input('Plese enter the name of browser in which you want to open the file.\nEnter a valid name.\nExamples:\n\"edge\" \n\"chrome\" \n\"opera\"')
            print('Opening in Browser...')
            eel.start(rf'{file_name}',size=(800,400),mode=brows)
        except Exception as e:
            print(e)
            re_run = input('Enter \"try\" to try again or \"quit\" to quit.\nEnter here : ')
            if re_run == 'try':
                html_runner()
            elif re_run == 'quit':
                print('Exiting...')
                exit()
            else:
                print('Something went wrong!\nExiting...')



print('\nThis is a Map-Generator program.\nThat generates a Interactive Map in HTML format that can be opened in any browser.')
print('\nPlease follow the steps correctly.\nMake sure you have Internet connection.')

user_gen = input('\nEnter \"my_location\" to get your location.\nEnter \"address\" to enter your Address.\nEnter \"raw_cords\" to get your Coordinates.\nEnter here : ')

latlong(user_gen)
address_gen()
map_generator()

user_open = input('\nEnter \"open\" to open the map in browser.\nOr enter \"quit\" to Quit the program.\nEnter here : ')

if user_open == 'open':
    html_runner()
elif user_open == 'quit':
    quit()