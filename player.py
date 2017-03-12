

class Player:

    def __init__(self, kit_num, name, position, DOB, nation, apps, goals, assists, mins_played):

        if ' ' in name:
            name = name.split()
            self.first_name = name[0]
            self.last_name = name[-1]
            self.name = self.first_name + ' ' + self.last_name
        else:
            self.name = name

        self.kit_num = kit_num
        self.position = position
        self.dob = DOB
        self.nation = nation
        self.goals = goals
        self.assists = assists
        self.mins_played = mins_played

        if '(' in apps:
            apps = apps.strip(')').split('(')
            self.starts = int(apps[0])
            self.substitutions = int(apps[1])
        else:
            self.starts = apps
            self.substitutions = 0

    def __str__(self):
        return "\n{}\nNo. {}, Position: {}, Mins played: {}, Starts(Subs): {}({}), Goals: {}, Assists: {}".format(self.name, self.kit_num, self.position, self.mins_played, self.starts, self.substitutions, self.goals, self.assists)

    def __repr__(self):
        return "".format()
