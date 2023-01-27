players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
#
# team_a_members =[
#     player['name']
#     for player in players_dict.values()
#     if player['status'] == 'Rest' and player['team'] == 'A'
# ]
# print(f'Все члены команды А, которые отдыхают: \n{team_a_members}')
#
# team_b_members = [
#     player['name']
#     for player in players_dict.values()
#     if player['status'] == 'Training' and player['team'] == 'B'
# ]
#
# print(f'Все члены команды В, которые тренируются: \n{team_b_members}')
#
# team_c_members = [
#     player['name']
#     for player in players_dict.values()
#     if player['status'] == 'Travel' and player['team'] == 'C'
# ]
#
# print(f'Все члены команды С, которые путешествуют: \n{team_c_members}')

help_dict = {"Rest": "отдыхают",
             "Training": "тренируются",
             "Travel": "путешествуют"}

team_order = ["A", "B", "C"]

# Запустим цикл по словарю состояний и одновременно будем вести счёт состояний, чтобы на каждой итерации выбирать
# одну из команд:
index = 0
for state in help_dict:
    print(f"Все члены команды из команды {team_order[index]}, которые {help_dict[state]}:")
    for _, player in players_dict.items():
        if player["status"] == state and player["team"] == team_order[index]:
            print(player["name"])
    index += 1