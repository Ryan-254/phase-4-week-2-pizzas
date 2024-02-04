from random import choice, choices, sample, randint
import faker
from models import Restaurant,Pizza,RestaurantPizza, db

fake = faker.Faker()

from app  import app

with app.app_context():
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    Restaurant.query.delete()

    for n in range(20):
        fake_name=  fake.name()
        address= fake.address()

        
        restaurant = Restaurant(name=fake_name ,address=address)
        db.session.add(restaurant)
        db.session.commit()


    pizzas= ["Veggie", "Chicken tika","chicken pepperoni", "Magherita" , "Cheese", "Beef", "Hawaiian","BBQ Chicken"]
    sample_ingredients= ["Chicken","Spinach","Artichokes","Feta cheese","Ricotta cheese", "Parmesan cheese","Garlic", "Basil", "Oregano"]
   

    fake_pizzas= []
    for n in range(len(pizzas)):
        other_pizza = choices(sample_ingredients , k=3)
        random_ingedients= ','.join(str(ingredient) for ingredient in other_pizza)
        random_pizza= Pizza(name= choice(pizzas), ingredients= random_ingedients)
        fake_pizzas.append(random_pizza)
    db.session.add_all(fake_pizzas)
    db.session.commit()

    for record in range(40):
        restaurant=choice([x.id for x in Restaurant.query.all()])
        pizza=choice([p.id for p in  Pizza.query.all()])
        db.session.add(RestaurantPizza(restaurant_id=restaurant, pizza_id=pizza, price= randint(1,40)))
        db.session.commit()

   
