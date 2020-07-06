import constants
import copy

total_players_per_team = len(constants.PLAYERS)/len(constants.TEAMS)
players_copy = copy.deepcopy(constants.PLAYERS)


def clean_PLAYERS_height(players):
    for player in players:
        for key, value in player.items():
            if key == 'height':
                new_height = value.split(" ")
                new_height[0] = int(new_height[0])
                player['height'] = new_height[0]


def clean_PLAYERS_experience(players):
    for player in players:
        for key, value in player.items():
            if key == 'experience':
                if value == 'YES':
                    player['experience'] = True
                else:
                    player['experience'] = False


def clean_PLAYERS_guardians(players):
    for player in players:
        for key, value in player.items():
            if key == 'guardians':
                new_guardian = value.split(" and ")
                player['guardians'] = new_guardian


def balanced_teams(team1, team2, team3):
    team1_total_players = 1
    team2_total_players = 1
    experienced_players = 1
    non_experienced_players = 1
    for player in players_copy:
        if (team1_total_players <= total_players_per_team and player['experience'] == True and experienced_players <= 3):
            team1.append(player)
            team1_total_players += 1
            experienced_players += 1
        elif (team1_total_players <= total_players_per_team and player['experience'] == False and non_experienced_players <= 3):
            team1.append(player)
            team1_total_players += 1
            non_experienced_players += 1
        elif (team2_total_players <= total_players_per_team and player['experience'] == True and experienced_players <= 6):
            team2.append(player)
            team2_total_players += 1
            experienced_players += 1
        elif (team2_total_players <= total_players_per_team and player['experience'] == False and non_experienced_players <= 6):
            team2.append(player)
            team2_total_players += 1
            non_experienced_players += 1
        else:
            team3.append(player)


def start():
    print("BASKETBALL TEAM STATS TOOL \n")
    print('----MENU----' + '\n')
    
    
def menu():
    print("""
Here are your choices:
1) Display Team Stats
2) Quit
    """)


def end():
    print("See you next time!")


def team_number():
    print("""
----Teams----

1) Panthers
2) Bandits
3) Warriors
    """)
    while True:
        number = int(input("Enter an option >  "))
        if number == 1:
            return team1
        elif number == 2:
            return team2
        elif number == 3:
            return team3
        else:
            print('Invalid entry, please try again.')
            continue


def print_team_stats(team):
    num_players = 0
    num_experienced_players = 0
    num_non_experienced_players = 0
    height_value = 0
    name_list = list()
    guardian_list = list()
    for current_team in team:
        for key, value in current_team.items():
            if key == 'name':
                name_list.append(value)
            elif key == 'guardians':
                guardian_list.append(', '.join (value))
            elif key == 'experience' and value == True:
                num_experienced_players += 1
            elif key == 'experience' and value == False:
                num_non_experienced_players += 1
            elif key == 'height':
                height_value += value
                num_players += 1
    print(', '.join(name_list) + '\n')
    print('Guardians on Team:')
    print(', '.join(guardian_list) + '\n')
    print(f'Total Experienced Players: {num_experienced_players}')
    print(f'Total Non-Experienced Players: {num_non_experienced_players}')
    print('Average Height: {}'.format(height_value/num_players) + '\n')
    while True:
        see_more = input("Would you like to see more team stats? Y/N ")
        if see_more.lower() == 'y':
            print_team(team_number())
        elif see_more.lower() == 'n':
            end()
            break
        else:
            print('That is not a valid entry, please try again')
            continue


def print_team(team):
    if team == team1:
        print("Team: Panthers Stats")
        print('-' * 20)
        print(f"Total Players: {total_players_per_team} \n")
        print(f"Players on Team:")
    elif team == team2:
        print("Team: Bandits Stats")
        print('-' * 20)
        print(f"Total Players: {total_players_per_team} \n")
        print(f"Players on Team:")
    elif team == team3:
        print("Team: Warriors Stats")
        print('-' * 20)
        print(f"Total Players: {total_players_per_team} \n")
        print(f"Players on Team:")
    else:
        print("Invalid entry, please try again")
    print_team_stats(team)


if __name__ == "__main__":
    start()
    menu()
    while True:
        answer = int(input("Enter an option > "))
        if answer == 1:
            clean_PLAYERS_height(players_copy)
            clean_PLAYERS_experience(players_copy)
            clean_PLAYERS_guardians(players_copy)
            team1 = list()
            team2 = list()
            team3 = list()
            balanced_teams(team1, team2, team3)
            print_team(team_number())
        elif answer == 2:
            end()
            break
        else:
            print("Invalid entry, please try again.")
            continue
        