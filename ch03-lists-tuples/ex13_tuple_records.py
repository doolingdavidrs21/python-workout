PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(records):
    formatted = []
    for first, last, travel_time in sorted(records, key=lambda r: (r[1], r[0])):
        formatted.append(f"{last:<10} {first:<10} {round(travel_time, 2)}")
    return formatted

if __name__ == "__main__":
    for line in format_sort_records(PEOPLE):
        print(line)
