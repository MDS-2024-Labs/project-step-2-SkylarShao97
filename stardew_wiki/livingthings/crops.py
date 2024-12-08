import pandas as pd
from pathlib import Path

class Crop:
    def __init__(self, name, season, growth_time, regrowth_time, price, craft_product, craft_price):
        """
        Initialize a Crop instance.
        """
        self.name = name
        self.season = season
        self.growth_time = growth_time
        self.regrowth_time = regrowth_time
        self.price = price
        self.craft_product = craft_product
        self.craft_price = craft_price

    def __str__(self):
        regrowth = f"Regrowth Time: {self.regrowth_time}" if not pd.isna(self.regrowth_time) else "No regrowth"
        craft = (f"Crafting Product: {self.craft_product} (Price: {self.craft_price})"
                   if not pd.isna(self.craft_product) else "No crafting product")
        return (f"Name: {self.name}\n"
                f"Season: {self.season}\n"
                f"Growth Time: {self.growth_time}\n"
                f"{regrowth}\n"
                f"Price: {self.price}\n"
                f"{craft}")


class CropDatabase:
    def __init__(self, csv_file):
        """
        Initialize the crop database by loading data from a CSV file.
        """
        self.crops = {}
        self.load_data_from_csv(csv_file)

    def load_data_from_csv(self, csv_file):
        """
        Load crop data from the provided CSV file.
        """
        # Resolve the path to the current script's directory
        base_path = Path(__file__).parent
        csv_path = base_path / csv_file

        data = pd.read_csv(csv_path)
        for _, row in data.iterrows():
            crop = Crop(
                name=row["name_crop"],
                season=row["season"],
                growth_time=row["growth_crop"],
                regrowth_time=row.get("regrowth_crop", None),
                price=row["crop_price"],
                craft_product=row.get("craft_crop", None),
                craft_price=row.get("craft_crop_price", None)
            )
            self.crops[crop.name] = crop

    def search_by_name(self, name):
        """
        Finds a crop by name.
        """
        crop = self.crops.get(name)
        return str(crop) if crop else "Crop not found."

    def search_by_season(self, season):
        """
        Lists crops for a specific season.
        """
        filtered_crops = [
            crop.name for crop in self.crops.values()
            if season.lower() in [s.strip().lower() for s in crop.season.split("/")]
        ]
        if filtered_crops:
            return "\n".join(filtered_crops)
        else:
            return f"No crops found for {season}."


def input_crop():
    """
    Interactive function for searching crops via a menu.
    """
    db = CropDatabase("data/Crops.csv")

    while True:
        print("\nCrop Search Menu:")
        print("1. Search by Name")
        print("2. Search by Season")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            name = input("Enter the name of the crop: ").strip()
            print("\nSearch Result:")
            print(db.search_by_name(name))
        elif choice == "2":
            season = input("Enter the season (Spring/Summer/Fall/Tropical): ").strip()
            print("\nSearch Result:")
            print(db.search_by_season(season))
        elif choice == "3":
            print("Exiting Crop Search...")
            break
        else:
            print("Invalid choice. Please try again.")