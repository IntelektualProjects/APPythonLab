import requests
from bs4 import BeautifulSoup


class HypixelStats:

    def data_type_choice(self):
        answer = input("Please choose a specific game (Ex. Bed Wars, SkyWars): ").lower()
        if answer == "bed wars":
            return "BedWars"
        if answer == "blitz survival games":
            return "BSG"
        if answer == "cops and crims":
            return "CaC"
        if answer == "mega walls":
            return "MW"
        if answer == "tnt games":
            return "TNTGames"
        if answer == "uhc champions":
            return "UHC"
        if answer == "skywars":
            return "SkyWars"

        string = ""
        for x in answer.split(" "):
            if x == "uhc":
                string += "UHC"
            else:
                string += x[0].upper() + x[1:]
        return string

    def data_retrieval(self, gamer_tag, game):
        response = requests.get("https://plancke.io/hypixel/player/stats/" + gamer_tag)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find(id=f"stat_panel_{game}")
        basic = result.find('div', class_="panel-collapse collapse").find('ul', class_="list-unstyled")
        basic = [x.replace(' ', "") for x in basic.prettify().split("\n")]

        vals = []
        values = []
        keys = []
        i = 0
        for x in basic:
            if x != '' and x[0] != '<':
                vals.append(x)
        while i < len(vals):
            if i == 0:
                keys.append(vals[i])
            elif i % 2 == 1:
                values.append(vals[i])
            else:
                keys.append(vals[i])
            i += 1
        finalized = list(zip(keys, values))
        print(finalized)


HypixelStats().data_type_choice()
