class Club:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points

    def __repr__(self):
        return f"Club({self.name}, Points: {self.points})"


class Match:
    def __init__(self, home_team, away_team, home_goals, away_goals):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = home_goals
        self.away_goals = away_goals

    def get_winner(self):
        if self.home_goals > self.away_goals:
            return self.home_team
        elif self.home_goals < self.away_goals:
            return self.away_team
        return None  # Indicates a draw

    def __repr__(self):
        return (
            f"Match({self.home_team.name} vs {self.away_team.name}, "
            f"Score: {self.home_goals}-{self.away_goals})"
        )


class League:
    def __init__(self):
        self.clubs = {}
        self.matches = []

    def add_club(self, club):
        if club.name not in self.clubs:
            self.clubs[club.name] = club

    def add_match(self, match):
        self.matches.append(match)
        self.update_points(match)

    def update_points(self, match):
        winner = match.get_winner()
        if winner:
            winner.add_points(3)
        else:
            match.home_team.add_points(1)
            match.away_team.add_points(1)

    def get_standings(self):
        return sorted(self.clubs.values(), key=lambda club: club.points, reverse=True)

    def __repr__(self):
        return "\n".join(str(club) for club in self.get_standings())


def main():
    league = League()
    barcelona = Club("Barcelona")
    real_madrid = Club("Real Madrid")
    league.add_club(barcelona)
    league.add_club(real_madrid)

    match1 = Match(barcelona, real_madrid, 2, 1)
    match2 = Match(real_madrid, barcelona, 3, 3)
    league.add_match(match1)
    league.add_match(match2)

    print(league)
    # Output:
    # Club(Barcelona, Points: 4)
    # Club(Real Madrid, Points: 1)


# Example usage
if __name__ == "__main__":
    main()