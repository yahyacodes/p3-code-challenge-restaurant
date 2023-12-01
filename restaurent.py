class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(self)

    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def methods(rest):
        return rest.customers
    
    def customer_reviews(self):
        return list(set([review.restaurant() for review in Review.methods() if review.customers() == self]))
    
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)

class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.restaurants.append(self)

    @classmethod
    def rest(chefs):
        return chefs.restaurants
    
    def reviews(self):
        return [review for review in Review.rest() if review.restaurant() == self]
    
    def customers(self):
        return list(set([review.customer() for review in self.reviews()]))
    
    def average_ratings(self):
        ratings = [review.rating() for review in self.reviews()]
        return sum(ratings) / len(ratings) if ratings else 0
    
class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)

    def rating(self):
        return self.rating

    @classmethod
    def rev(clients):
        return clients.reviews

    def customer(self):
        return self.customer
    
    def resta(self):
        return self.resta