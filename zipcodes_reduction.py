from math import radians, cos, sin, asin, sqrt
from string import whitespace
import sys

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# def find_min_dist(list, index, direction):
#     lat1 = float(list[index][5].strip(whitespace))
#     lon1 = float(list[index][6].strip(whitespace))
#
#     next = index + direction
#     min_dist = sys.float_info.max
#     while next >= 0 and next < len(list):
#
#         lat2 = float(list[next][5].strip(whitespace))
#         lon2 = float(list[next][6].strip(whitespace))
#         dist = haversine(lon1, lat1, lon2, lat2)
#         min_dist = min(dist, min_dist)
#         if ()


def main():
    filtered_zipcodes = list()

    with open('us_postal_codes.csv', 'r') as zipcodes_file:
        # last = None
        for line in zipcodes_file:
            line = line.split(',')
            print (line[0])
            try:
                lat1 = float(line[5].strip(whitespace))
                lon1 = float(line[6].strip(whitespace))

                if len(filtered_zipcodes) > 0:
                    min_dist = sys.float_info.max
                    for entry in filtered_zipcodes:
                        lat2 = float(entry[5].strip(whitespace))
                        lon2 = float(entry[6].strip(whitespace))
                        dist = haversine(lon1, lat1, lon2, lat2)

                        min_dist = min(dist, min_dist)
                        # print ("Distance from {0} {1} to {2} {3} is {4}".format(lat1, lon1, lat2, lon2, dist))

                    # are all registered at a distance grater than 9 km ?
                    if min_dist > 30:
                        filtered_zipcodes.append(line)
                else:
                    filtered_zipcodes.append(line)
            except Exception as e:
                print e

    # lat_ordered = sorted(all_zipcodes, key=lambda x: x[5])
    # lon_ordered = sorted(all_zipcodes, key=lambda x: x[6])
    #
    # filtered_zipcodes = list()
    #
    # for entry in all_zipcodes:
    #     min_dist = sys.float_info.max
    #
    #
    #
    #     if len(filtered_zipcodes) == 0:
    #         filtered_zipcodes.append(entry)
    #     else:
    #         lat_i = lat_ordered.index(entry)
    #         # lat up
    #         while ()
    #         # lat down
    #         pass
    #         # lon up
    #         # lon down

    with open('us_postal_codes_reduced_more.csv', 'w') as zipcodes_file:
        for line in filtered_zipcodes:
            zipcodes_file.write(','.join(line))

main()


# if len(store) > 0:
#     min_dist = sys.float_info.max
#     for entry in store:
#         lat2 = float(entry[5].strip(whitespace))
#         lon2 = float(entry[6].strip(whitespace))
#         dist = haversine(lon1, lat1, lon2, lat2)
#
#         min_dist = min(dist, min_dist)
#         # print ("Distance from {0} {1} to {2} {3} is {4}".format(lat1, lon1, lat2, lon2, dist))
#
#     if min_dist > 9:
#         store.append(line)
# else: