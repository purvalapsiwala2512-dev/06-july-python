call_durations = (12, 5, 0, 20, 7, 3, 15)

filtered_list = [minutes for minutes in call_durations if minutes >= 5]

filtered_durations = tuple(filtered_list)

print("Filtered Call Durations (5+ mins):", filtered_durations)