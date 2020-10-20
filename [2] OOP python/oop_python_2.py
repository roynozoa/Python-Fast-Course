# Part 2 of my OOP python practical learning source code


# (3) Class cont.
# Create 2 class that have a relationship
# class Restaurant and Food


# Class Restaurant
class Restaurant:
    def __init__(self, id, name, rating, max_food):
        self.id = id  # integer data type
        self.name = name
        self.rating = rating  # float 0.0 - 5.0
        self.max_food = max_food
        self.foods = []
        self.chef = []
        self.is_open = True

    def get_rating(self):
        return self.rating

    def add_food(self, food):
        if len(self.foods) < self.max_food:
            self.foods.append(food)
            return True
        return False

    def get_average_rating(self):
        pass

    def get_average_food_price(self):
        value = 0
        for food in self.foods:
            value += food.get_price()
        return value / len(self.foods)


# Class Food
class Food:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


food_one = Food(1, 'Pizza', 100000)
food_two = Food(2, 'Bakso', 20000)
food_three = Food(3, 'Salad', 50000)
food_four = Food(4, 'Kebab', 20000)

restaurant_one = Restaurant(1, 'The Restaurant', 4.1, 3)

restaurant_one.add_food(food_one)
restaurant_one.add_food(food_two)
restaurant_one.add_food(food_three)
# restaurant_one.add_food(food_four)

print(restaurant_one.foods[0].name)
print(restaurant_one.get_average_food_price())
