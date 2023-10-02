import sqlite3

"""
This class is used for handling all of the database methods and keeping track of the SQLite3 Database that will be used to hold all of the team colors
UPDATE: THIS CLASS IS NOT NECESSARY
It's easier just to use the downloaded copy of teh excel file, and constantly pull data from there
Cuts down on complexity, only dealing with one class instead of two, only pulling data from one source instead of passing it into SQLite and then into the config.json file
"""
class database():
    def __init__(self):
        # __init__ details the initialization protocol whenever the class is generated
        data = sqlite3.connect("./python_startup/colors_database")
        # There's probably an easier way to store the rgb values for each, but it's really not going to change a whole lot in terms of speed
        # Since this is going to be a relatively small database
        data.execute(
            "CREATE TABLE IF NOT EXISTS colors (id INTEGER PRIMARY KEY, name STRING, primary_red INTEGER, primary_green INTEGER, primary_blue INTEGER, second_red INTEGER, second_green INTGER, second_blue INTEGER);"
            )
        osu_param = ["OSU", 215, 63, 9, 0, 0, 0]
        tuple_osu = tuple(osu_param)
        data.execute(
            "INSERT or REPLACE INTO colors (name, primary_red, primary_green, primary_blue, second_red, second_green, second_blue) VALUES (?, ?, ?, ?, ?, ?, ?)",
            tuple_osu
        )
        data.commit()
        data.close()

    @staticmethod    
    def get_colors(name):
        """
        This method uses the paramter 'name' to pull the rgb values for the primary and secondary colors,
        Then it sets them into a list, and returns that list
        """
        port = sqlite3.connect("./python_startup/colors_database")
        datalist = []
        datalist.append(database.format_data(port.execute("SELECT primary_red FROM colors WHERE name = ?", (name, ))))
        datalist.append(database.format_data(port.execute("SELECT primary_green FROM colors WHERE name = ?", (name, ))))
        datalist.append(database.format_data(port.execute("SELECT primary_blue FROM colors WHERE name = ?", (name, ))))

        port.close()

        print(datalist)
        return datalist
    
    @staticmethod
    def format_data(data):
        """
        Trimming all of the excess fat off of the data that's pulled from the SQLite Database
        """
        slice1 = str(data.fetchone()).strip('([])').rstrip(',')
        slice2 = slice1.replace("'", '')
        return slice2