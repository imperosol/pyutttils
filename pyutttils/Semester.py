class Semester:
    def __init__(self, identifier):
        if identifier[0] not in ('A', 'P'):
            raise ValueError
        self.short_season = identifier[0]
        self.full_season = ["Automne", "Printemps"][identifier[0] == "P"]
        
        # work with "P22" and "P2022" and "Printemps 2022"
        self.short_year = int(identifier.strip()[-2:])
        self.full_year = 2000 + self.short_year
        
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
