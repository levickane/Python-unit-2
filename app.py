import constants
import copy
import sys

total_players_per_team = len(constants.PLAYERS)/len(constants.TEAMS)
players_copy = copy.deepcopy(constants.PLAYERS)


def clean_PLAYERS_info(players):
    """this function takes the value of the key, 'height' and splits it at the space.
        then we take the first object of the list [0] and convert that to an integer.
        then we define that the player['height'] is now equal to that integer. then we 
        convert the 'experience' from YES or NO to TRUE or FALSE. then we split the 'guardians'
        values at the ' and ' and store them as lists
    """
    for player in players:
        for key, value in player.items():
            if key == 'height':
                new_height = value.split(" ")
                new_height[0] = int(new_height[0])
                player['height'] = new_height[0]
            elif key == 'experience':
                if value == 'YES':
                    player['experience'] = True
                else:
                    player['experience'] = False
            elif key == 'guardians':
                new_guardian = value.split(" and ")
                player['guardians'] = new_guardian


def balanced_teams(team1, team2, team3):
    """this function blanceses the teams and starts with a count of players on each team and a count of experienced 
    and non experienced. you can't start with 0 people, it has to start with at least 1 person. We iterate for players 
    in player_copy (which is the copy of the constants PLAYERS, that we made at the top) and we add a player unitl we 
    reach 3 for experienced_players and 3 players for non_experienced_players. then we do the same for team 2 until we 
    reach 6 for experienced and non_experienced. from there, that's 12 total players assigned to 2 teams (team1 and team2), 
    which means theres only 6 players left over and they will be asigned to team3. these teams will be called on later.
    """
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


def team_number():
    print("""
----Teams----

1) Panthers
2) Bandits
3) Warriors
    """)
    while True:
        try:
            number = int(input("Enter a team number >  "))
            if number == 1:
                return team1
            elif number == 2:
                return team2
            elif number == 3:
                return team3
            else:
                print('Invalid entry, please try again.')
                continue
        except ValueError:
            print("That's not a TEAM NUMBER. Try again")
            continue


def print_team_stats(team):
    """this function prints the team stats. starting with a count of 0 for number of players, experienced
    and non-experienced, and height. We also start with a blank list of names and guardians. for each player
    we're going to look at the current player and iterate over each item for the current_player as it relates
    to the Key:Value pairs. if key is equal to 'name' then that name is added to name_list list. if key is
    equal to 'guardians' then the guardians are added to the guardian_list (if there are multiple guardians
    then they are separated by a comma , ). exeperienced and non-experienced are added to their respective counts
    based on their boolean value. then the height is added to the count along with the number of players that
    this for loop has iterated over. Next we're going to print the name_list and guardians_list joined together 
    yet separated by commas. We're also going to print the number of experienced and non-experienced players on the
    team. then we're going to print the average height, which is the height_value/num_players. Finally we'll
    have a while loop that will ask if you want to see more stats, y/n?
    """
    num_players = 0
    num_experienced_players = 0
    num_non_experienced_players = 0
    height_value = 0
    name_list = list()
    guardian_list = list()
    for current_player in team:
        for key, value in current_player.items():
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
    """this function will print the team and the total number of players per team followed by
        the team stats - this is all dependant on whatever team is selected.
    """
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


def end():
    """using sys.exit to exit the program or else it keeps looping and asking
    for the same entry over and over again.
    """
    print("See you next time!")
    sys.exit()


if __name__ == "__main__":
    start()
    menu()
    while True:    
        try:
            answer = int(input("Enter an option > "))
            if answer == 1:
                clean_PLAYERS_info(players_copy)
                team1 = list()
                team2 = list()
                team3 = list()
                balanced_teams(team1, team2, team3)
                print_team(team_number())
                """this will trigger the team_number function, and based on the the team selected,
                it will then trigger the print_team function which will also trigger the print_team_stats
                function, which will then ask if you want to see more or if you want to quit
                """
            elif answer == 2:
                end()
                break
            else:
                print("Invalid entry, please try again.")
                continue
        except ValueError:
            print("It's either the number 1 or the number 2. Nothing else.")
            
        
            
        