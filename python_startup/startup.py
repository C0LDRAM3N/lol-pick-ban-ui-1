import json
import customtkinter as ctk
import tkinter as tk
from tkinter import *
import sqlite3
from database import database
import pandas as pd
from CTkScrollableDropdown import *
import subprocess
from pathlib import Path

class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoL Pick Ban UI Startup")
        window_width = 800
        window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(screen_height, screen_width)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        self.home_score = tk.IntVar()
        self.away_score = tk.IntVar()
        self.team_sheet = pd.read_excel("./python_startup/BROADCAST GFU Esports.xlsx", sheet_name="Validation! Schools", usecols="D:J")

        self.team_list = []
        for i in range(0, len(self.team_sheet)):
            self.team_list.append(self.team_sheet.at[i, "Top Team Logo"])

        self.create_widgets()

    def create_widgets(self):
        """
        Creating all of the widgets and handling the placement
        """
        away_label = ctk.CTkLabel(self, text="Away Team Data:")
        away_label.grid(row=0, column=2)
        self.away_selection = ctk.CTkComboBox(self, width=300, values=(self.team_list))
        self.away_selection.grid(row=1, column=2)
        CTkScrollableDropdown(self.away_selection, values=self.team_list) # Adds the scroll option to the self.away_selection ComboBox

        away_score_entry = ctk.CTkEntry(self, width=150)
        away_score_entry.grid(row=2, column=2)

        

        home_label = ctk.CTkLabel(self, text="Home Team Data:")
        home_label.grid(row=0, column=0)
        self.home_selection = ctk.CTkComboBox(self, width=300)
        self.home_selection.grid(row=1, column=0)
        CTkScrollableDropdown(self.home_selection, values=self.team_list) # Adds the scroll option to the self.home_selction ComboBox


        score_label = ctk.CTkLabel(self, text="Score")
        score_label.grid(row=2, column=1)

        name_label = ctk.CTkLabel(self, text="Team Name")
        name_label.grid(row=1, column=1)

        start = ctk.CTkButton(self, text="Start the UI", command=lambda: [self.start_ui()])
        start.grid(row=5, column=1)

        reloader = ctk.CTkButton(self, text="Reload new changes", command=lambda: [database.get_colors("OSU")])
        reloader.grid(row=4, column=1)

    def get_data(self):
        """
        Getting all of the data for the update_JSON method
        NOT FINISHED
        """
        print(self.away_selection.get())
        my_list = []
        my_list.append(self.away_selection.get())
        return my_list
    
    def get_colors(self, team_name):
        """
        This method uses the team_name parameter to try and find the hex color values of the same row
        """

    def update_JSON(self, home_name, away_name, home_score, away_score):
        """
        Updates config.json with the Home/Away Team Names, Colors, current Score
        """
        with open("backend/config.json", "r") as file:
            # Loading the variable 'data' with the config.json file
            data = json.load(file)
            print("JSON File Loaded")
            file.close()
        # Blue Team is the Home Team, and Red Team is the Away Team
        data['frontend']['blueTeam']['name'] = home_name
        data['frontend']['blueTeam']['score'] = home_score

        data['frontend']['redTeam']['name'] = away_name
        data['frontend']['redTeam']['score'] = away_score

        with open("backend/config.json", "w") as jsonfile:
            # Loading the updated data back into the config.json file
            json.dump(data, jsonfile)
            # print(myJSON)
            jsonfile.close()

    def start_ui(self):
        """
        Starts the UI successfully, it does open a bit too many terminal commands and tabs
        There's probably a way to get everything more simplified
        Close the frontend first, and then the backend
        """
        
        starting = Path.cwd()
        file = starting/'python_startup'/'batch_files'/'program-test.bat'
        subprocess.run([file])



    def push_data(self):
        print("Hello World!")


if __name__ == "__main__":
    # print("Starting Database")
    # data = database()
    # print("Database started")
    app = main()
    app.mainloop()







# json_update = {
#     "frontend": {
#         "scoreEnabled": True,
#         "spellsEnabled": True,
#         "coachesEnabled": True,
#         "blueTeam": {
#             "name": home_team,
#             "score": 0,
#             "coach": "Coach Blue",
#             "color": "rgb(0,151,196)"
#         },
#         "redTeam": {
#             "name": "Team Red",
#             "score": 0,
#             "coach": "Coach Red",
#             "color": "rgb(222,40,70)"
#         },
#         "patch": "9.19"
#     },
#     "contentPatch": "latest",
#     "contentCdn": "https://ddragon.leagueoflegends.com/cdn"
# }