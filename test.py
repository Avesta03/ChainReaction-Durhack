import random
from collections import defaultdict

class Product:
    def __init__(self, name):
        self.name = name
        self.local_price = random.uniform(1, 10)  # Random starting price
        self.consequences = defaultdict(list)  # Good and bad consequences

    def adjust_price(self, amount):
        self.local_price += amount
        self.local_price = max(0, self.local_price)  # Price cannot be negative

class Country:
    def __init__(self, name):
        self.name = name
        self.products = {name: Product(name) for name in ['Coffee', 'Bananas', 'Wheat', 'Rice', 'Fish']}
        self.needs = set()
        self.is_landlocked = False

    def add_need(self, product):
        self.needs.add(product)

class World:
    def __init__(self):
        self.countries = {}
        self.trades = defaultdict(list)
        self.setup_countries()

    def setup_countries(self):
        # Setting up some initial countries with needs
        for name in ["Brazil", "Japan", "Canada", "Germany", "Egypt", "India", "Australia", "Mexico", "Russia", "China"]:
            country = Country(name)
            self.countries[name] = country
            if random.choice([True, False]):  # Randomly decide if the country is landlocked
                country.is_landlocked = True

        # Assign needs to 10 random countries
        for _ in range(10):
            country_name = random.choice(list(self.countries.keys()))
            product = random.choice(list(self.countries[country_name].products.values()))
            self.countries[country_name].add_need(product.name)

    def trade(self, from_country, to_country, product_name, amount):
        from_country_obj = self.countries[from_country]
        to_country_obj = self.countries[to_country]
        product = from_country_obj.products[product_name]

        # Example consequences
        if amount > 0:
            product.adjust_price(-0.5)  # Price drops with excess supply
            print(f"{from_country} exports {amount} of {product_name} to {to_country}")
            self.trades[from_country].append((to_country, product_name, amount))
        else:
            product.adjust_price(0.5)  # Price rises with low supply
            print(f"{from_country} imports {abs(amount)} of {product_name} from {to_country}")
            self.trades[to_country].append((from_country, product_name, abs(amount)))

    def display_world_status(self):
        for country_name, country in self.countries.items():
            print(f"\nCountry: {country_name}")
            print(f"Products and Prices:")
            for product in country.products.values():
                print(f"- {product.name}: ${product.local_price:.2f}")
            if country.needs:
                print(f"Needs: {', '.join(country.needs)}")

    def run_game(self):
        while True:
            self.display_world_status()
            command = input("Enter a trade (format: from_country to_country product_name amount) or 'quit' to exit: ")
            if command.lower() == 'quit':
                break
            try:
                from_country, to_country, product_name, amount = command.split()
                amount = int(amount)
                if from_country in self.countries and to_country in self.countries:
                    self.trade(from_country, to_country, product_name, amount)
                else:
                    print("Invalid country names.")
            except ValueError:
                print("Invalid input format. Please try again.")

if __name__ == "__main__":
    world_game = World()
    world_game.run_game()
