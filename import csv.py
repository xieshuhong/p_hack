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
    for f, b in zip(library.post_code, post_code):
        if(f == b):
            matched_letters.append(f)
        else:
            return len(matched_letters)


nearby_libraries = {}
#  find the nearest library the users wants
def find_nearest_library():
    post_code = input('please input your postal code(i.e. T2W 4N1) so we find the nearest library for you:\n')
    for i, library in enumerate(libraries):
        matched_letters = find_nearest(post_code, library)
        library.matched_letters = matched_letters
        nearby_libraries[i] = library




load_csv()
# sort_library_by_name_asc()
# print()
# format_libraries()
# find_a_libraries()

def sorted_function(x):
     return x[1].matched_letters



find_nearest_library()
sorted_matched_libraries = sorted(nearby_libraries.items(), key =sorted_function, reverse = True)
# print('sorted_matched_libraries', sorted_matched_libraries)
print("The closest library is", sorted_matched_libraries[0][1].name)
