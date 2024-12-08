import pandas as pd
from pathlib import Path

class Animal:
    """
    Base class for all animals.
    """
    def __init__(self, name, growth_time, product, artisan, product_price, artisan_price):
        self.name = name
        self.growth_time = growth_time
        self.product = product
        self.artisan = artisan
        self.product_price = product_price
        self.artisan_price = artisan_price

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Growth Time: {self.growth_time}\n"
                f"Product: {self.product} (Price: {self.product_price})\n"
                f"Artisan Product: {self.artisan} (Price: {self.artisan_price})")


class BarnAnimal(Animal):
    """
    Represents animals that live in barns.
    """
    def __init__(self, name, growth_time, product, artisan, product_price, artisan_price):
        super().__init__(name, growth_time, product, artisan, product_price, artisan_price)
        self.animal_type = "Barn"

    def __str__(self):
        return f"{super().__str__()}\nType: {self.animal_type}"


class CoopAnimal(Animal):
    """
    Represents animals that live in coops.
    """
    def __init__(self, name, growth_time, product, artisan, product_price, artisan_price):
        super().__init__(name, growth_time, product, artisan, product_price, artisan_price)
        self.animal_type = "Coop"

    def __str__(self):
        return f"{super().__str__()}\nType: {self.animal_type}"


class AnimalDatabase:
    """
    Manages a collection of Animal objects.
    """
    def __init__(self, csv_file):
        self.animals = {}
        self.load_data_from_csv(csv_file)

    def load_data_from_csv(self, csv_file):
        # Resolve the path to the current script's directory
        base_path = Path(__file__).parent
        csv_path = base_path / csv_file

        data = pd.read_csv(csv_path)
        for _, row in data.iterrows():
            if row["type"].lower() == "barn":
                animal = BarnAnimal(
                    name=row["name_animal"],
                    growth_time=row["growth_animal"],
                    product=row["product_animal"],
                    artisan=row["artisan_animal"],
                    product_price=row["product_animal_price"],
                    artisan_price=row["artisan_animal_price"]
                )
            elif row["type"].lower() == "coop":
                animal = CoopAnimal(
                    name=row["name_animal"],
                    growth_time=row["growth_animal"],
                    product=row["product_animal"],
                    artisan=row["artisan_animal"],
                    product_price=row["product_animal_price"],
                    artisan_price=row["artisan_animal_price"]
                )
            else:
                continue  # Skip unknown types
            self.animals[animal.name] = animal

    def search_by_name(self, name):
        """
        Finds an animal by name.
        """
        animal = self.animals.get(name)
        return str(animal) if animal else "Animal not found."

    def search_by_type(self, animal_type):
        """
        Filters animals by type (Barn/Coop).
        """
        filtered_animals = [
            animal for animal in self.animals.values()
            if getattr(animal, "animal_type", "").lower() == animal_type.lower()
        ]
        return "\n\n".join(str(animal) for animal in filtered_animals) if filtered_animals else f"No animals found for type '{animal_type}'."

def input_animal():
    """
    Interactive function for searching animals via a menu.
    """
    # Initialize the database
    db = AnimalDatabase("data/Animals.csv")

    while True:
        print("\nAnimal Search Menu:")
        print("1. Search by Name")
        print("2. Search by Type (Barn/Coop)")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter the name of the animal: ").strip()
            print("\nSearch Result:")
            print(db.search_by_name(name))
        elif choice == "2":
            animal_type = input("Enter the type of animal (Barn/Coop): ").strip()
            print("\nSearch Result:")
            print(db.search_by_type(animal_type))
        elif choice == "3":
            print("Exiting Animal Search...")
            break
        else:
            print("Invalid choice. Please try again.")