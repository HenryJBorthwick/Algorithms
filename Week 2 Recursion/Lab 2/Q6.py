def num_rushes(slope_height, rush_height_gain, backsliding):
    """DOCSTRING"""

    if slope_height <= rush_height_gain:
        return 1
    else:
        return 1 + num_rushes(slope_height - rush_height_gain + backsliding, rush_height_gain*0.95, backsliding*0.95)
    
ans = num_rushes(100, 15, 7)
print(ans)

ans = num_rushes(10, 10, 9)
print(ans)