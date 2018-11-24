import matplotlib.pyplot as plt


def plotTSP(path, points):
    """
    path: List of lists with the different orders in which the nodes are visited
    points: coordinates for the different nodes
    """

    x = []
    y = []
    for i in path:
        y.append(points[i][0])
        x.append(points[i][1])

    plt.plot(x, y, 'ro', markersize=4)

    a_scale = float(max(x)) / float(200)

    # Draw the primary path for the TSP problem
    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width=a_scale,
              color='black', length_includes_head=True)
    for i in range(0, len(x) - 1):
        plt.arrow(x[i], y[i], (x[i + 1] - x[i]), (y[i + 1] - y[i]),
                  head_width=a_scale, color='black', length_includes_head=True)

    # Set axis too slightly larger than the set of x and y
    plt.xlim(min(x) - 100, max(x) + 100)
    plt.ylim(min(y) - 100, max(y) + 100)
    plt.show()
