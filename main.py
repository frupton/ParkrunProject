import folium
import webbrowser
import os
import pandas as pd
import sounds
import numpy as np


def get_home(file):
    home = []
    raw_data = pd.read_csv(file)
    home += list(raw_data['Lat'])
    home += list(raw_data['Long'])
    return home


def get_full_list():

    place, lat, long, junior = ([] for i in range(4))
    raw_data = pd.read_csv('Parkrun-locations.csv')

    place += list(raw_data['Place'])
    long += list(raw_data['Latitude'])
    lat += list(raw_data['Longitude'])
    junior += list(raw_data['Junior'])

    return place, lat, long, junior


def get_run_list(file):

    done = []
    raw_data = pd.read_csv(file)
    done += list(raw_data['Place'])
    return done


def folium_func(name, lats, longs, types_list, home):
    """
        Adds locations onto a OSM map using Folium
            Parameters:
                lats (array) :  array of latitude points
                longs (array):  array of longitude points
                name (array of string values) :  Name will appear on each points popup marker
                types_list (array of string values) : Type of icon wanted
                home (list of float) : location for the home
            Returns:
                Saves map.html to the folder you are working in
        """

    # dictionary with keys = point type, values = icon
    icons_dict = {'done': 'check', 'not_done': 'star', 'junior': 'child'}
    colour_dict = {'done': 'green', 'not_done': 'lightgray', 'junior': 'beige'}

    # Folium Stuff - Make an empty map
    m = folium.Map(location=home, zoom_start=10, tiles='OpenStreetMap')

    # Add home to the map
    folium.Marker(
        location=home, popup='home', icon=folium.Icon(color='blue', icon='home', prefix='fa')).add_to(m)

    # Add marker one by one on the map
    for j in range(1, len(name)):
        if types[j] != 'no':
            folium.Marker(
                location=[lats[j], longs[j]],
                popup=name[j], icon=folium.Icon(color=colour_dict[types_list[j]], icon=icons_dict[types_list[j]],
                                                prefix='fa')).add_to(m)

    # Saves the map to folder
    m.save("map.html")
    message = 'Folium route saved'
    return message


if __name__ == '__main__':
    file_name_home = 'home_locations.csv'
    file_name_done = 'Parkrun-done.csv'
    juniors = 0
    alphabet_challenge = 1

    place, lat, long, junior = get_full_list()
    home = get_home(file_name_home)
    run = get_run_list(file_name_done)
    types = []
    alphabet = []

    # Label the locations for if they are jun
    for i in range(len(place)):
        if place[i] in run:
            types.append('done')
        else:
            if junior[i] == 1:
                types.append('junior')
            else:
                types.append('not_done')

    # Alphabet Challenge labels
    alphabet_done = []
    for i in range(len(run)):
        letter = run[i][0]
        if letter not in alphabet_done:
            alphabet_done.append(letter)
    for i in range(len(place)):
        letter = place[i][0]
        if letter not in alphabet_done:
            alphabet.append(1)
        else:
            alphabet.append(0)

    # Culling
    if juniors == 0:
        for i in range(len(types)):
            if types[i] == 'junior':
                types[i] = 'no'

    if alphabet_challenge == 1:
        for i in range(len(place)):
            if alphabet[i] == 0:
                types[i] = 'no'

    # Calling folium_func
    x = folium_func(place, lat, long, types, home)
    print(x)


filename = 'file:///' + os.getcwd() + '/' + 'map.html'
webbrowser.open_new_tab(filename)


sounds.buzz()
