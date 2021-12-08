hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]


def get_score(team_name, teams):
    for index, item in enumerate(teams):
        if item == team_name:
            return f"A {item} ficou classificada em {index + 1}"


get_score_3 = get_score("Team Mirum", hackathon_3)
print(get_score_3)

get_score_1 = get_score("Team Ateliware", hackathon_1)
print(get_score_1) 

get_score_2 = get_score("Team Kenzie", hackathon_1)
print(get_score_2)

get_score_4 = get_score("Team VHSYS", hackathon_1)
print(get_score_4)

get_score_5 = get_score("Team Mirum", hackathon_2)
print(get_score_5)