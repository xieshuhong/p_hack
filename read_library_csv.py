import csv
import copy
from library import Library
# from rich.progress import track
# import time

# for counter in track(range(5), description="Completion..."):
#    print(f"Loading data")
#    time.sleep(0.5)

libraries = []
title_info = '\n{:<30} {:<20} {:<20} {:<20}\n'.format('Library', 'Postal Code', 'Square Feet', 'Phone Number')

# load data from the csv file to the libraries list
def load_csv():
    with open("Calgary_Public_Library_Locations_and_Hours.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                library = Library(row[0], row[1], row[2], row[3])
                libraries.append(library)
            line_count += 1



# display and sort libraries by their names in ascending order
def display_and_sort():
    #  deep copy of the list
     copy_libraries = [x for x in libraries]
     copy_libraries.sort(key=lambda x: x.name)
     print(title_info)
     for library in copy_libraries:
        print(library)


# find the library you want to find
def find_a_library():
    library_bool = False
    library_name = input("Please enter the name of the library that you want to find information on:\n")
    for library in libraries:
        if library.name == library_name:
            library_bool = True
            print(f'\nWe have found that library, here is all the relevant information:\n{title_info}{library}\n')
    if not library_bool:
            print('\nSorry, please enter valid library name!')




def find_nearest(post_code, library):
    matched_letters = []
    for f, b in zip(library.post_code, post_code):
        if(f == b):
            matched_letters.append(f)
        else:
            return len(matched_letters)


nearby_libraries = {}
#  find the nearest library the users wants
def find_nearest_library():
    # reverse it back first
        post_code = input('\nplease input your postal code(i.e. T2W 4N1) so we find the nearest library for you:\n')
        for i, library in enumerate(libraries):
            try:
                matched_letters = find_nearest(post_code, library)
                library.matched_letters = matched_letters
                nearby_libraries[i] = library
            except:
                print('\nPlease input the right postal code!')



# get the data from the library csv
load_csv()
# display and sort libraries by their names in ascending order
display_and_sort()

# find_a_libraries()

def sorted_function(x):
     return x[1].matched_letters


# find the nearest library according to the postal code
find_nearest_library()
sorted_matched_libraries = sorted(nearby_libraries.items(), key =sorted_function, reverse = True)
print("The closest library is", sorted_matched_libraries[0][1].name + '\n')


# find the library info according to the library's name
find_a_library()
