import folium
import webbrowser
import os
import pandas as pd
import sounds
#import visual


def get_home(file):
    home_coord = []
    raw_data = pd.read_csv(file)
    home_coord += list(raw_data['Lat'])
    home_coord += list(raw_data['Long'])
    return home_coord


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


def done_labels(parkrun_places, parkrun_run):
    done = []
    for i in range(len(parkrun_places)):
        if parkrun_places[i] in parkrun_run:
            done.append(1)
        else:
            done.append(0)
    return done


def show_label(show, bin_label, label, type_label):
    if show:
        for i in range(len(place)):
            if bin_label[i]:
                type_label[i] = label
    return type_label


def alphabet_labels(parkrun_places, parkrun_run):
    alphabet_done = []
    for i in range(len(parkrun_run)):
        letter = parkrun_run[i][0]
        if letter not in alphabet_done:
            alphabet_done.append(letter)
    for i in range(len(parkrun_places)):
        letter = parkrun_places[i][0]
        if letter not in alphabet_done:
            alphabet_done.append(1)
        else:
            alphabet_done.append(0)
    return alphabet_done


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
    icons_dict = {'done': 'check', 'not_done': 'star', 'junior': 'child', 'alphabet': 'star'}
    colour_dict = {'done': 'green', 'not_done': 'lightgray', 'junior': 'beige', 'alphabet': 'orange'}

    # Folium Stuff - Make an empty map
    m = folium.Map(location=home, zoom_start=10, tiles='OpenStreetMap')

    # Add home to the map
    folium.Marker(
        location=home, popup='home', icon=folium.Icon(color='blue', icon='home', prefix='fa')).add_to(m)

    # Add marker one by one on the map
    for j in range(1, len(name)):
        if types_list[j] != 'no':
            folium.Marker(
                location=[lats[j], longs[j]],
                popup=name[j], icon=folium.Icon(color=colour_dict[types_list[j]], icon=icons_dict[types_list[j]],
                                                prefix='fa')).add_to(m)

    # Saves the map to folder
    m.save("map.html")
    message = 'Folium route saved'
    return message


if __name__ == '__main__':
    # This section will be replaced with info from the GUI
    file_name_home = 'home_locations.csv'
    file_name_done = 'Parkrun-done.csv'
    show_juniors = 0
    show_alphabet = 0
    show_done = 0
    show_not_done = 0

    # Set up
    place, lat, long, junior_bin = get_full_list()
    home = get_home(file_name_home)
    run = get_run_list(file_name_done)

    # 1s and 0s
    done_bin = done_labels(place, run)
    alphabet_bin = alphabet_labels(place, run)

    type_labels = ['no']*len(place)
    type_labels = show_label(show_juniors, junior_bin, 'junior', type_labels)
    type_labels = show_label(show_alphabet, alphabet_bin, 'alphabet', type_labels)
    type_labels = show_label(show_done, done_bin, 'done', type_labels)

    # Calling folium_func
    x = folium_func(place, lat, long, type_labels, home)
    print(x)

    filename = 'file:///' + os.getcwd() + '/' + 'map.html'
    webbrowser.open_new_tab(filename)

    sounds.buzz()
