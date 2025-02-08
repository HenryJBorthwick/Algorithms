def select_shows(show_list):
    # Convert show durations to end times
    shows_with_end_times = [(title, start, start + duration) for title, start, duration in show_list]

    # Sort shows by end times
    sorted_shows = sorted(shows_with_end_times, key=lambda x: x[2])

    # Sort shows by their end times
    sorted_shows = sorted(shows_with_end_times, key=lambda x: x[2])

    # Initialize the list of selected shows and the end time of the last selected show
    selected_shows = []
    current_end_time = 0

    # Iterate through the sorted shows
    for show in sorted_shows:
        title, start_time, end_time = show

        # Check if the show starts after the last selected show ends
        if start_time >= current_end_time:
            selected_shows.append(show)
            current_end_time = end_time

    return selected_shows


def print_shows(show_list):
    selected_shows = select_shows(show_list)
    for title, start_time, end_time in selected_shows:
        print(f"{title} {start_time} {end_time}")


# Test
print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4),
    ('h', 8, 3)
])

# Output
# b 1 4
# e 4 7
# h 8 11
