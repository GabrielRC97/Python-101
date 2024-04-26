matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

def winner_team(list_matches):
    new_list = list_matches.copy()
    if new_list['home_team_result'] == 'Win':
        return new_list

new_matches = list(filter(winner_team,matches))
new_matches_2 = list(filter(lambda i:i['home_team_result'] == 'Win',matches ))

print('vieja lista')
print(len(matches))
print(matches)
print('nueva lista')
print(len(new_matches))
print(new_matches)
print('nueva lista 2')
print(len(new_matches_2))
print(new_matches_2)


    
