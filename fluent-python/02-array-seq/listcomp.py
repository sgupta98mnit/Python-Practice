colors = ['red', 'black']

sizes = ['S', 'M', 'L', 'X']

tshirts = [(color, size) for size in sizes
                        for color in colors]

print(tshirts)

tshirts = [(color, size) for size in sizes
           for color in colors]