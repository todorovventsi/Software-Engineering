class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player not in self.players and not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if not any([True for player in self.players if player.name == player_name]):
            return f"Player {player_name} is not in the guild."
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = [f"{player.player_info()}\n" for player in self.players]
        return f"Guild: {self.name}\n{''.join(players_info)}"
