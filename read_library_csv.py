import csv
from library import Library


libraries = []

# load data from the csv file to the libraries list
def load_csv():
    with open("Calgary_Public_Library_Locations_and_Hours.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
# [W.R. Castell Central Library,T2G 2M2,177532,.....]
# [[W.R. Castell Central Library,T2G 2M2,177532,.....]]
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')

            else:
                library = Library(row[0], row[1], row[2])
                libraries.append(library)

            line_count += 1
    print(f'Processed {line_count} lines.')



# sort libraries by their names in descending order
def sort_library_by_name_asc():
     libraries.sort(key=lambda x: x.name, reverse = True)


# find all libraries that starts with letter "A"
def find_a_libraries():
    for library in libraries:
        if library.name.startswith("A"):
            print(library)

def format_libraries():
    for library in libraries:
        print(library)




def find_nearest(post_code, library):
    matched_letters = []
    print('post', library.post_code, 'code', post_code)
    print('list', list(zip(library.post_code, post_code)))
    for f, b in zip(library.post_code, post_code):
        print('f', f)
        print('b', b)
        if(f == b):
            matched_letters.append(f)
        else:
            return len(matched_letters)

nearby_libraries = {}
def find_nearest_library():
    # post_code = "T2K 4Y1"
    post_code = input(print('Please input the postal code(i.e. T2K 4Y1) so that we can help you find the nearest location:\n'))
    for i, library in enumerate(libraries):
        matched_letters = find_nearest(post_code, library)
        print('matched_letters', matched_letters)
        library.matched_letters = matched_letters
        print('i', i)
        print('library', library)
        nearby_libraries[i] = library
        print('nearby_libraries[i]', type(nearby_libraries))



load_csv()
sort_library_by_name_asc()
print()
# format_libraries()
# find_a_libraries()

def sorted_function(x):
     print('3333', x[1])
     print('xxxxxx', x[1].matched_letters)
     return x[1].matched_letters



find_nearest_library()
sorted_matched_libraries = sorted(nearby_libraries.items(), key =sorted_function, reverse = True)
print('sorted_matched_libraries', sorted_matched_libraries)
print("The closest library is", sorted_matched_libraries[0][1].name)
