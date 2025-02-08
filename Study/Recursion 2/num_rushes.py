def num_rushes(slope_height, rush_height_gain, back_sliding):
    if slope_height <= rush_height_gain:
        return 1
    else:
        return 1 + num_rushes((slope_height - rush_height_gain + back_sliding), rush_height_gain, back_sliding)
    
ans = num_rushes(10, 10, 9)
print(ans)