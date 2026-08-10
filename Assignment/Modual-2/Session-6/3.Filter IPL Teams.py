teams = ["CSK", "MI", "GT", "RCB", "KKR"]
points = [14, 8, 16, 12, 10]

team_points = dict(zip(teams, points))

print("Teams with more than 10 points:")
for team, pts in team_points.items():
    if pts > 10:
        print(f"{team}: {pts} points")