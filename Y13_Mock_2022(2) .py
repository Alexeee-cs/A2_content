class Team():
    def __init__(self,player1,player2,player3,player4,player5,ranking):
        self.__Player1 = player1 #Player1 : STRING
        self.__Player2 = player2 #Player2 : STRING
        self.__Player3 = player3 #Player3 : STRING
        self.__Player4 = player4 #Player4 : STRING
        self.__Player5 = player5 #Player5 : STRING
        self.__TeamName = player1[0] + player2[0] + player3[0] + player4[0] + player5[0] #TeamName : STRING
        self.__Ranking = ranking #Ranking: INTEGER
    def getRanking(self):
        return self.__Ranking
    def getTeamName(self):
        return self.__TeamName
def ConvertRanking(ranking):
    categories = {
        "Iron": 1,
        "Bronze": 5,
        "Silver": 9,
        "Gold": 13,
        "Platinum": 17,
        "Diamond": 21,
        "Master": 25,
        "Grandmaster": 29,
        "Challenger": 33
    }
    roman_numerals = {
        "I": 0,
        "II": 1,
        "III": 2,
        "IV": 3
    }
    category, sub_level = ranking.split(' ')
    if category in categories and sub_level in roman_numerals:
        return categories[category] + roman_numerals[sub_level]
    else:
        raise ValueError("Invalid ranking category or sub-level.")
def ReadData():
    try:
        with open("Gamers.txt") as f:
            lines = f.readlines()
            for i in range (0,len(lines),5):
                players = []
                total_ranking = 0
                for j in range(5):
                    player_data = lines[i+j].strip().split(",")
                    player_name = player_data[0].strip()
                    player_ranking = player_data[1].strip()
                    players.append(player_name)
                    total_ranking += ConvertRanking(player_ranking)
                new_team = Team(*players, total_ranking)
                arrayTeams.append(new_team)
            print(f"Succesfully added {len(arrayTeams)} teams.")
    except OSError:
        print("File not found")
def displayTeams():
    for teams in arrayTeams:
        print(f"Team: {teams.getTeamName()}, Ranking: {teams.getRanking()}")

arrayTeams = [] # to store information for all teams

def InsertionSort(arr):
    for i in range(1,len(arr)):
        Current_team = arr[i]
        Current_ranking = Current_team.getRanking()
        j=i-1
        while j>-1 and Current_ranking>arr[j].getRanking(): #decending order
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=Current_team


def CreateBrackets(arr):
    print("\nMatchups:")
    num_teams = len(arr)
    for i in range(num_teams // 2):
        team1 = arr[i]
        team2 = arr[num_teams - 1 - i]
        print(
            f"Match {i + 1}: Team {team1.getTeamName()} (Rank {team1.getRanking()}) vs Team {team2.getTeamName()} (Rank {team2.getRanking()})")

def FindLargestGaps(arr):
    gaps = []
    for i in range(0, len(arr)-1):
        gap = arr[i].getRanking() - arr[i+1].getRanking()
        gaps.append((gap, i, i+1))

    gaps.sort(reverse=True)
    print("\nTop 5 largest gaps in seeding:")
    for gap, team1_num, team2_num in gaps[:5]:
        team1 = arr[team1_num]
        team2 = arr[team2_num]
        print(f"Gap:{gap}")
        print(f" Team {team1_num+1}: {team1.getTeamName()} (Members: {team1._Team__Player1}, {team1._Team__Player2}, {team1._Team__Player3}, {team1._Team__Player4}, {team1._Team__Player5})")
        print(f" Team {team2_num+1}: {team2.getTeamName()} (Members: {team2._Team__Player1}, {team2._Team__Player2}, {team2._Team__Player3}, {team2._Team__Player4}, {team2._Team__Player5})")
        print()

ReadData()
InsertionSort(arrayTeams)
displayTeams()
CreateBrackets(arrayTeams)
FindLargestGaps(arrayTeams)
