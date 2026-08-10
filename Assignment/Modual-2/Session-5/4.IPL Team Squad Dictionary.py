team = {
    'CSK': {'captain': 'Dhoni', 'players': 18},
    'MI': {'captain': 'Rohit', 'players': 17}
}

team['GT'] = {'captain': 'Hardik', 'players': 16}

for team_name, info in team.items():
    print(f"{team_name} Captain: {info['captain']}")