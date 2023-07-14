import numpy as np
from itertools import chain

# #{ class Pixel

class Pixel:

    def __init__(self, x, y, value):

        self.x = x
        self.y = y
        self.value = value

# #}

# #{ class Cluster

class Cluster:

    def __init__(self, pos_x, pos_y, pixels, class_name, class_index):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pixels = pixels
        self.class_name = class_name
        self.class_index = class_index

    def __str__(self):
        return '[' + str(self.pos_x) + ',' + str(self.pos_y) + ']: ' + self.class_name + ', ' + str(len(self.pixels)) + ' pixels'

# #}

# #{ clas Metadata

class Metadata:

    # #{ __init__()

    def __init__(self, unfiltered_metadata):

        tmp = unfiltered_metadata['latitude, longitude, altitude, tle_time']
        tmp = tmp.split(', ')
        self.latitude = [float(tmp[0])]
        self.longitude = [float(tmp[1])]
        self.altitude = [float(tmp[2])]
        self.tle_time = [tmp[3]]
        self.minimal_pixel_value = float(unfiltered_metadata['Minimal pixel value (Original)'])
        self.maximal_pixel_value = float(unfiltered_metadata['Maximal pixel value (Original)'])
        self.pixel_count = int(unfiltered_metadata['Pixel count (Original)'])
        self.acquisition_time = [float(unfiltered_metadata['Acquisition time'])]
        self.time = [unfiltered_metadata['Time']]
        self.readable_time = [unfiltered_metadata['Human readable time']]
        self.image_number = [int(unfiltered_metadata['Image number'])]
        self.temperature = [float(unfiltered_metadata['Temperature'])]

    # #} end of __init__()

    # #{ __str__()

    def __str__(self):

        ret = 'Latitude: ' + str(self.latitude) + '\n'
        ret += 'Longitude: ' + str(self.longitude) + '\n'
        ret += 'Altitude: ' + str(self.altitude) + '\n'
        ret += 'TLE Time: ' + str(self.tle_time) + '\n'
        ret += 'Minimal pixel value: ' + str(self.minimal_pixel_value) + '\n'
        ret += 'Maximal pixel value: ' + str(self.maximal_pixel_value) + '\n'
        ret += 'Pixel count: ' + str(self.pixel_count) + '\n'
        ret += 'Acquisition time: ' + str(self.acquisition_time) + '\n'
        ret += 'Time: ' + str(self.time) + '\n'
        ret += 'Readable time: ' + str(self.readable_time) + '\n'
        ret += 'Image number : ' + str(self.image_number) + '\n'
        ret += 'Temperature : ' + str(self.temperature)

        return ret

    # #} end of __str__()

    # #{ __iadd__()

    def __iadd__(self, other):

        self.latitude = list(chain(self.latitude, other.latitude))
        self.longitude = list(chain(self.longitude, other.longitude))
        self.tle_time.append(other.tle_time)
        self.minimal_pixel_value = min(self.minimal_pixel_value, other.minimal_pixel_value)
        self.maximal_pixel_value = max(self.maximal_pixel_value, other.maximal_pixel_value)
        self.pixel_count += other.pixel_count
        self.acquisition_time = list(chain(self.acquisition_time, other.acquisition_time))
        self.time = list(chain(self.time, other.time))
        self.readable_time = list(chain(self.readable_time, other.readable_time))
        self.image_number = list(chain(self.image_number, other.image_number))
        self.temperature = list(chain(self.temperature, other.temperature))

        return self

    # #} end of __iadd__()

    # #{ getGpsCoordinates()

    def getGpsCoordinates(self):

        points = zip(self.latitude, self.longitude)
        return points

    # #} end of getGpsCoordinates()

# #}

# #{ fullresFromClusters()

def fullresFromClusters(clusters, filter=None):

    image = np.zeros(shape=[256, 256])

    for c in clusters:
        if filter is not None:
            if c.class_name not in filter:
                continue
        cluster_start = (c.pos_x, c.pos_y)
        for p in c.pixels:
            image[c.pos_x + p.x][c.pos_y + p.y] = p.value

    return image

# #} end of fullresFromClusters()
