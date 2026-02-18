def map_range(x, in_min, in_max, out_min, out_max):
    return int(out_min + (float(x - in_min)/float(in_max-in_min) * (out_max) - out_min))
