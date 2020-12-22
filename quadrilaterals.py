import numpy as np
from random import choice as ch
from matplotlib import pyplot as plt


class Rectangle:
    def __init__(self):
        self.x1 = np.random.randint(-10, 10)
        self.y1 = np.random.randint(-10, 10)
        self.delta_x = np.random.randint(-10, 10)
        self.delta_y = np.random.randint(-10, 10)
        self.x2 = self.x1 + self.delta_x
        self.y2 = self.y1 + self.delta_y
        self.coords = [[self.x1, self.y1], [self.x1, self.y2],
                [self.x2, self.y2], [self.x2, self.y1]]
        self.coords.append(self.coords[0])


class Quadrilateral:
    def __init__(self):
        # Create vertices of bounding box
        self.x_start = np.random.randint(-10, 10)
        self.y_start = np.random.randint(-10, 10)

        self.bounding_box_width = np.random.randint(1, 10)
        self.bounding_box_height = np.random.randint(1, 10)

        self.box_vertices = [[self.x_start, self.y_start],
                            [self.x_start, self.y_start + self.bounding_box_height],
                            [self.x_start + self.bounding_box_width,
                            self.y_start + self.bounding_box_height],
                            [self.x_start + self.bounding_box_width, self.y_start]]
        self.box_vertices.append(self.box_vertices[0])


        self.width_choices = [x for x in
                                range(self.x_start, self.x_start + self.bounding_box_width)]
        self.height_choices = [y for y in
                                range(self.y_start, self.y_start + self.bounding_box_height)]

        print('x_start',self.x_start,'bounding_box_width', self.bounding_box_width, sep='\t')
        print('y_start',self.y_start,'bounding_box_height', self.bounding_box_height, sep='\t')
        print('width_choices',self.width_choices, sep='\t')
        print('height_choices', self.height_choices, sep='\t')
        self.coords = [[self.x_start, self.y_start
                                        + ch(self.height_choices)],

                                        [self.x_start + ch(self.width_choices),
                                        self.y_start + self.bounding_box_height],

                                        [self.x_start + self.bounding_box_width,
                                        self.y_start + ch(self.height_choices)],

                                        [self.x_start + ch(self.width_choices),
                                        self.y_start]]

        self.coords.append(self.coords[0])
#         self.bounding_box_start = [np.random.randint(-10, 10),
#                             np.random.randint(-10, 10)]
#         self.x_start = self.bounding_box_start[0]
#         self.bounding_box_width = np.random.randint(1, 10)
#         self.bounding_box_height = np.random.randint(1, 10)
# 
#         self.width_choices = [x for x in
#                                 range(self.x_start, self.x_start + bounding_box_width)]
#         self.height_choices = [y for y in
#                                 range(self.y_start, self.x_start + bounding_box_height)]
# 
#         self.bounding_box_vertices = [[self.x_start, self.y_start
#                                         + self.height_choices],
# 
#                                         [self.width_choices,
#                                         self.y_start + self.bounding_box_height],
# 
#                                         [self.x_start + bounding_box_width,
#                                         self.height_choices],
# 
#                                         [self.x_start + bounding_box_width,
#                                         self.y_start]]
#         self.scalars = [1/np.random.randint(1, 10),
#                 1/np.random.randint(1, 10),
#                 1/np.random.randint(1, 10),
#                 1/np.random.randint(1, 10)]
#
#
#         self.coords = [
#             [self.x_start,
#             np.floor(self.scalars[0] * self.bounding_box_height)
#             + self.bounding_box_start[1]],
# 
#             [np.floor(self.scalars[1] * self.bounding_box_width)
#                 + self.bounding_box_start[0],
#             self.bounding_box_start[1] + self.bounding_box_height],
# 
#             [self.bounding_box_start[0] + self.bounding_box_width,
#             np.floor(self.scalars[2] * self.bounding_box_height)
#             + self.bounding_box_start[1]],
# 
#             [np.floor(self.scalars[3] * self.bounding_box_width)
#                 + self.bounding_box_start[0],
#             self.bounding_box_start[1]]
# 
#             ]
#         self.coords.append(self.coords[0])




for count in range(10):
    print('Quadrilateral', count, sep='\t')
    q1 = Quadrilateral()

    print('Coords of Bounding Box', q1.box_vertices, sep='\t')
    print('Coords of Quadrilateral',q1.coords, sep='\t')
    print()
    box_x = [q1.box_vertices[i][0] for i in range(len(q1.box_vertices))]
    box_y = [q1.box_vertices[i][1] for i in range(len(q1.box_vertices))]
    x = [q1.coords[i][0] for i in range(len(q1.coords))]
    y = [q1.coords[i][1] for i in range(len(q1.coords))]

    plt.figure()
    plt.plot(box_x, box_y, x, y)
    plt.savefig('fig' + str(count) + '.png')
    # plt.show()

