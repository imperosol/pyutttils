class Semester:
    def __init__(self, identifier):
        self.short_season = identifier[0]
        if self.short_season == "A":
            self.full_season = "Automne"
        if self.short_season == "P":
            self.full_season = "Printemps"

        if len(identifier) == 3:  # "P22"
            self.short_year = int(identifier[1:3])
            self.full_year = 2000 + self.short_year
        elif len(identifier) == 5:  # "P2022"
            self.full_year = int(identifier[1:])
            self.short_year = int(identifier[3:])
        else:  # "Printemps 2022"
            self.full_year = int(identifier.split(" ")[1])
            self.short_year = int(identifier.split(" ")[1][2:])
        self.long_code = self.short_season + str(self.full_year)
        self.full_name = self.full_season + " " + str(self.full_year)

    def __str__(self):
        return self.full_name

    def get_next(self):
        if self.short_season == "A":
            return Semester("P"+str(self.full_year+1))
        else:
            return Semester("A" + str(self.full_year))

    def get_previous(self):
        if self.short_season == "A":
            return Semester("P"+str(self.full_year))
        else:
            return Semester("A" + str(self.full_year - 1))
