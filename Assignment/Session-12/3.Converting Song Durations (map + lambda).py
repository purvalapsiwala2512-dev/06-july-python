durations_in_minutes = [3.5, 4.2, 2.5, 5.0]
durations_in_seconds = list(map(lambda m: int(m * 60), durations_in_minutes))

print(f"--- Task 3 ---")
print(f"Durations in minutes: {durations_in_minutes}")
print(f"Durations in seconds: {durations_in_seconds}\n")