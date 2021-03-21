import matplotlib.colors as mc
def NonLinCdict(steps, hexcol_array):
    cdict = {'red': (), 'green': (), 'blue': ()}
    for s, hexcol in zip(steps, hexcol_array):
        rgb =mc.hex2color(hexcol)
        cdict['red'] = cdict['red'] + ((s, rgb[0], rgb[0]),)
        cdict['green'] = cdict['green'] + ((s, rgb[1], rgb[1]),)
        cdict['blue'] = cdict['blue'] + ((s, rgb[2], rgb[2]),)
    return cdict

# Create an array with the colors you want to use
hc = ["#1c4279", "#2aabb7"]
th = [0, 1]

cdict = NonLinCdict(th, hc)
cm = mc.LinearSegmentedColormap('test', cdict)