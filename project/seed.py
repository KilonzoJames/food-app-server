from datetime import datetime
from .app import app  # Import the Flask app
from .models.Config import db
from .models.Orders import Order
from .models.Restaurant import Restaurant
from .models.Food import FoodItem

def seed_data():
    print("🌱 Seeding orders data...")

    restaurants_data = [
        {
            "name": "The Injera Place",
            "description": "Injera inspired cuisine in a cozy setting",
            "contact": "542-222-2133",
            "image": "https://images.pexels.com/photos/2923034/pexels-photo-2923034.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "The Kienyeji House",
            "description": "Sizzling steaks and grilled meats",
            "contact": "333-222-3333",
            "image": "https://images.pexels.com/photos/15378105/pexels-photo-15378105/free-photo-of-well-done-rib.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "La Diaspora Kinshasa",
            "description": "Fine dining with a focus on fresh ingredients",
            "contact": "544-222-3311",
            "image": "https://images.pexels.com/photos/4551832/pexels-photo-4551832.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "Oteeri Mbale",
            "description": "Ugandan meals in a casual setting",
            "contact": "555-424-3333",
            "image": "https://images.pexels.com/photos/8523166/pexels-photo-8523166.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "Fufuville",
            "description": "Freshly made fufu and palm wine available",
            "contact": "555-222-1111",
            "image": "https://images.pexels.com/photos/4947396/pexels-photo-4947396.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "The Deli",
            "description": "Freshly made sandwiches and salads",
            "contact": "123-222-3333",
            "image": "https://images.pexels.com/photos/2253643/pexels-photo-2253643.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "The Green house",
            "description": "A variety of dishes in a cozy atmosphere",
            "contact": "555-868-3333",
            "image": "https://images.pexels.com/photos/17513578/pexels-photo-17513578/free-photo-of-restaurant-food-on-wall.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "The Brunch",
            "description": "Delicious brunch options served all day",
            "contact": "568-222-3333",
            "image": "https://images.pexels.com/photos/239975/pexels-photo-239975.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "Eat Spot",
            "description": "A trendy spot for delicious eats",
            "contact": "111-222-5533",
            "image": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "The British Tea House",
            "description": "Traditional British tea and treats",
            "contact": "445-222-3333",
            "image": "https://images.pexels.com/photos/33275/tea-party-tea-black-and-white-teapot.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "45 Degrees Kitchen",
            "description": "Organic and sustainable ingredients in a French and Italian influenced menu",
            "contact": "444-222-2223",
            "image": "https://images.pexels.com/photos/6058325/pexels-photo-6058325.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
        },
        {
            "name": "Saffron Indian Cuisine",
            "description": "Authentic North Indian cuisine",
            "contact": "555-123-4567",
            "image": "https://tinyurl.com/yck6w8t7"
        }
    ]

    # Create Restaurant objects and add them to the database
    restaurants = [Restaurant(**restaurant) for restaurant in restaurants_data]
    db.session.add_all(restaurants)
    db.session.commit()

    print("🌱 Restaurant data seeding completed!")
    
    orders_data = [
        {
            "food_id": 1,
            "table_no": 2,
            "timestamp": "2023-08-01",
            "restaurant_id": 1
        },
        {
            "food_id": 2,
            "table_no": 1,
            "timestamp": "2023-08-01",
            "restaurant_id": 2
        },
        {
            "food_id": 4,
            "table_no": 3,
            "timestamp": "2023-08-02",
            "restaurant_id": 8
        },
        {
            "food_id": 5,
            "table_no": 5,
            "timestamp": "2023-08-02",
            "restaurant_id": 9
        },
        {
            "food_id": 6,
            "table_no": 1,
            "timestamp": "2023-08-03",
            "restaurant_id": 7
        },
        {
            "food_id": 8,
            "table_no": 2,
            "timestamp": "2023-08-03",
            "restaurant_id": 5
        },
        {
            "food_id": 9,
            "table_no": 4,
            "timestamp": "2023-08-04",
            "restaurant_id": 9
        },
        {
            "food_id": 10,
            "table_no": 1,
            "timestamp": "2023-08-04",
            "restaurant_id": 8
        },
        {
            "food_id": 3,
            "table_no": 3,
            "timestamp": "2023-08-05",
            "restaurant_id": 6
        },
        {
            "food_id": 7,
            "table_no": 2,
            "timestamp": "2023-08-05",
            "restaurant_id": 3
        }
    ]

    # Convert the timestamp strings to datetime objects
    for order in orders_data:
        order["timestamp"] = datetime.strptime(order["timestamp"], "%Y-%m-%d")

    # Create Order objects and add them to the database
    orders = [Order(**order) for order in orders_data]
    db.session.add_all(orders)
    db.session.commit()

    print("🌱 Orders data seeding completed!")

    food_data = [
  {
    "id": 1,
    "food": "Ma-andazi",
    "description": "Local sweet bread",
    "price": 1000,
    "restaurant_id": 1,
    "origin": "Kenyan",
    "image": "https://lh3.googleusercontent.com/0NJ0tSWXxVAev3eL_S2yVN7VpWOxmxAbCH5nEm6zcAU3UAzyHILoBNVrshv6Oo-gFMxZxPLfPl_InXUwQR3wOHJ8fQ1EAFRiAZVjeQuz0NI=s750"
  },
  {
    "id": 2,
    "food": "Ugali",
    "description": "Maize porridge",
    "price": 850,
    "restaurant_id": 2,
    "origin": "Kenyan",
    "image": "https://www.willflyforfood.net/wp-content/uploads/2021/06/kenyan-food-ugali.jpg.webp"
  },
  {
    "id": 3,
    "food": " Poulet à la Moambé ",
    "description": " Poulet à la Moambé ",
    "price": 1200,
    "restaurant_id": 3,
    "origin": "Congolese",
    "image": "https://flavorverse.com/wp-content/uploads/2018/11/Poulet-%C3%A0-la-Moamb%C3%A9-Congolese-Food-640x521.jpg"
  },
  {
    "id": 4,
    "food": "Matooke",
    "description": "Matooke",
    "price": 950,
    "restaurant_id": 4,
    "origin": "Ugandan",
    "image": "https://afrifoodnetwork.com/wp-content/uploads/2021/08/Matoke-Ugandan-dish-scaled.jpg"
  },
  {
    "id": 5,
    "food": "Jollof Rice",
    "description": "Jollof Rice",
    "price": 750,
    "restaurant_id": 5,
    "origin": "Nigerian",
    "image": "https://allnigerianfoods.com/wp-content/uploads/Jollof-rice-recipe.jpg"
  },
  {
    "id": 6,
    "food": "Gelato",
    "description": "Italian-style ice cream with various flavors",
    "price": 500,
    "restaurant_id": 6,
    "origin": "Italian",
    
  },
  {
    "id": 7,
    "food": "Tiramisu",
    "description": "Classic Italian dessert made with ladyfingers, coffee, and mascarpone",
    "price": 650,
    "restaurant_id": 7,
    "origin": "Italian",
    "image": "",
  },
  {
    "id": 8,
    "food": "Bruschetta",
    "description": "Toasted bread topped with tomatoes, garlic, and olive oil",
    "price": 400,
    "restaurant_id": 8,
    "origin": "Italian",
    "image": "",
  },
  {
    "id": 9,
    "food": "Osso Bucco",
    "description": "Braised veal shanks with vegetables and gremolata",
    "price": 1200,
    "restaurant_id": 9,
    "origin": "Italian",
    "image": "",
  },
  {
    "id": 10,
    "food": "Ravioli",
    "description": "Stuffed pasta pockets with various fillings",
    "price": 900,
    "restaurant_id": 10,
    "origin": "Italian",
    "image": "",
  },
  {
    "id": 11,
    "food": "Cannoli",
    "description": "Italian pastry filled with sweet ricotta cream",
    "price": 550,
    "restaurant_id": 11,
    "origin": "Italian",
    "image": ""
  },
  {
    "id": 12,
    "food": "Prosciutto and Melon",
    "description": "Thinly sliced dry-cured ham with ripe cantaloupe",
    "price": 800,
    "restaurant_id": 12,
    "origin": "Italian",
    "image": "prosciutto_melon.jpg"
  },
  {
    "id": 13,
    "food": "Gnocchi",
    "description": "Soft dough dumplings typically made with potatoes and flour",
    "price": 700,
    "restaurant_id": 13,
    "origin": "Italian",
    "image": "gnocchi.jpg"
  },
  {
    "id": 14,
    "food": "Spaghetti Bolognese",
    "description": "Spaghetti with rich meat sauce",
    "price": 850,
    "restaurant_id": 14,
    "origin": "Italian",
    "image": "spaghetti_bolognese.jpg"
  },
  {
    "id": 15,
    "food": "Focaccia",
    "description": "Flat oven-baked bread topped with herbs and olive oil",
    "price": 500,
    "restaurant_id": 15,
    "origin": "Italian",
    "image": "focaccia.jpg"
  },
  {
    "id": 16,
    "food": "Panna Cotta",
    "description": "Creamy Italian dessert with sweetened cream and gelatin",
    "price": 550,
    "restaurant_id": 16,
    "origin": "Italian",
    "image": "panna_cotta.jpg"
  },
  {
    "id": 17,
    "food": "Caprese Salad",
    "description": "Fresh salad with tomatoes, mozzarella, basil, and olive oil",
    "price": 600,
    "restaurant_id": 17,
    "origin": "Italian",
    "image": "caprese_salad.jpg"
  },
  {
    "id": 18,
    "food": "Arancini",
    "description": "Fried rice balls typically stuffed with cheese or ragù",
    "price": 500,
    "restaurant_id": 18,
    "origin": "Italian",
    "image": "arancini.jpg"
  },
  {
    "id": 19,
    "food": "Minestrone Soup",
    "description": "Hearty vegetable soup with pasta or rice",
    "price": 450,
    "restaurant_id": 19,
    "origin": "Italian",
    "image": "minestrone_soup.jpg"
  },
  {
    "id": 20,
    "food": "Pesto Pasta",
    "description": "Pasta with a sauce made from basil, pine nuts, and cheese",
    "price": 750,
    "restaurant_id": 20,
    "origin": "Italian",
    "image": "pesto_pasta.jpg"
  },
  {
    "id": 21,
    "food": "Ethiopian Coffee",
    "description": "Ethiopian Coffee",
    "price": 550,
    "restaurant_id": 1,
    "origin": "Ethiopian",
    "image": "https://theplanetd.com/images/Facts-About-Brazil-Coffee.jpg"
  },
  {
    "id": 22,
    "food": "Sukuma Wiki",
    "description": "Collard greens",
    "price": 850,
    "restaurant_id": 2,
    "origin": "Kenyan",
    "image": "https://www.willflyforfood.net/wp-content/uploads/2021/06/kenyan-food-sukuma-wiki.jpg.webp"
  },
  {
    "id": 23,
    "food": "Fufu",
    "description": "Fufu",
    "price": 900,
    "restaurant_id": 3,
    "origin": "Congolese",
    "image": "https://flavorverse.com/wp-content/uploads/2018/11/Congolese-Food-Fufu-640x426.jpg"
  },
  {
    "id": 24,
    "food": "Posho",
    "description": "Posho",
    "price": 1200,
    "restaurant_id": 4,
    "origin": "Ugandan",
    "image": "https://afrifoodnetwork.com/wp-content/uploads/2021/08/Posho-Ugandan-dish-scaled.jpg"
  },
  {
    "id": 25,
    "food": "Pounded Yam",
    "description": "Pounded Yam",
    "price": 700,
    "restaurant_id": 5,
    "origin": "Nigerian",
    "image": "https://www.chefspencil.com/wp-content/uploads/Pounded-Yam-4-1-960x800.jpg.webp"
  },
  {
    "id": 26,
    "food": "Amatriciana Sauce",
    "description": "Tomato-based pasta sauce with guanciale or bacon",
    "price": 800,
    "restaurant_id": 6,
    "origin": "Italian",
    "image": "amatriciana_sauce.jpg"
  },
  {
    "id": 27,
    "food": "Cacio e Pepe",
    "description": "Spaghetti with Pecorino Romano cheese and black pepper",
    "price": 750,
    "restaurant_id": 7,
    "origin": "Italian",
    "image": "cacio_e_pepe.jpg"
  },
  {
    "id": 28,
    "food": "Trenette al Pesto",
    "description": "Pasta similar to linguine with basil pesto",
    "price": 700,
    "restaurant_id": 8,
    "origin": "Italian",
    "image": "trenette_al_pesto.jpg"
  },
  {
    "id": 29,
    "food": "Vitello Tonnato",
    "description": "Chilled veal with tuna and caper sauce",
    "price": 1100,
    "restaurant_id": 9,
    "origin": "Italian",
    "image": "vitello_tonnato.jpg"
  },
  {
    "id": 30,
    "food": "Tagliatelle Bolognese",
    "description": "Ribbon pasta with traditional Bolognese sauce",
    "price": 850,
    "restaurant_id": 10,
    "origin": "Italian",
    "image": "tagliatelle_bolognese.jpg"
  },
  {
    "id": 31,
    "food": "Farinata",
    "description": "Savory chickpea pancake",
    "price": 400,
    "restaurant_id": 11,
    "origin": "Italian",
    "image": "farinata.jpg"
  },
  {
    "id": 32,
    "food": "Cioppino",
    "description": "Italian-American fish stew with various seafood",
    "price": 1000,
    "restaurant_id": 12,
    "origin": "Italian",
    "image": "cioppino.jpg"
  },
  {
    "id": 33,
    "food": "Cassata Siciliana",
    "description": "Sicilian sponge cake with ricotta and candied fruit",
    "price": 700,
    "restaurant_id": 13,
    "origin": "Italian",
    "image": "cassata_siciliana.jpg"
  },
  {
    "id": 34,
    "food": "Braciola",
    "description": "Stuffed meat rolls cooked in tomato sauce",
    "price": 900,
    "restaurant_id": 14,
    "origin": "Italian",
    "image": "braciola.jpg"
  },
  {
    "id": 35,
    "food": "Ribollita",
    "description": "Tuscan vegetable and bread soup",
    "price": 500,
    "restaurant_id": 15,
    "origin": "Italian",
    "image": "ribollita.jpg"
  },
  {
    "id": 36,
    "food": "Saltimbocca alla Romana",
    "description": "Roman-style veal with prosciutto and sage",
    "price": 850,
    "restaurant_id": 16,
    "origin": "Italian",
    "image": "saltimbocca_alla_romana.jpg"
  },
  {
    "id": 37,
    "food": "Frittata",
    "description": "Italian omelette with various fillings",
    "price": 600,
    "restaurant_id": 17,
    "origin": "Italian",
    "image": "frittata.jpg"
  },
  {
    "id": 38,
    "food": "Stracciatella Soup",
    "description": "Egg drop soup with parmesan and spinach",
    "price": 450,
    "restaurant_id": 18,
    "origin": "Italian",
    "image": "stracciatella_soup.jpg"
  },
  {
    "id": 39,
    "food": "Acquacotta",
    "description": "Vegetable soup from the Tuscany region",
    "price": 500,
    "restaurant_id": 19,
    "origin": "Italian",
    "image": "acquacotta.jpg"
  },
  {
    "id": 40,
    "food": "Pasta Puttanesca",
    "description": "Pasta with tomatoes, olives, capers, and anchovies",
    "price": 700,
    "restaurant_id": 20,
    "origin": "Italian",
    "image": "pasta_puttanesca.jpg"
  },
  {
    "id": 41,
    "food": "Injera",
    "description": "Spongy flatbread",
    "price": 200,
    "restaurant_id": 1,
    "origin": "Ethiopian",
    "image": "https://theplanetd.com/images/Ethiopian-Food-Injira-640x960.jpg"
  },
  {
    "id": 42,
    "food": "Githeri",
    "description": "Githeri",
    "price": 200,
    "restaurant_id": 2,
    "origin": "Kenyan",
    "image": "https://www.willflyforfood.net/wp-content/uploads/2021/06/kenyan-food-githeri.jpg.webp"
  },
  {
    "id": 43,
    "food": "Fumbwa",
    "description": "Fumbwa",
    "price": 200,
    "restaurant_id": 3,
    "origin": "Congolese",
    "image": "https://flavorverse.com/wp-content/uploads/2018/11/Fumbwa-Congolese-Food.jpg"
  },
  {
    "id": 44,
    "food": "Nswaa",
    "description": "Nswaa",
    "price": 200,
    "restaurant_id": 4,
    "origin": "Ugandan",
    "image": "https://afrifoodnetwork.com/wp-content/uploads/2021/08/nswaa-taste-atlas.jpg"
  },
  {
    "id": 45,
    "food": " Egusi Soup",
    "description": " Egusi Soup",
    "price": 200,
    "restaurant_id": 5,
    "origin": "Nigerian",
    "image": "https://www.chefspencil.com/wp-content/uploads/Egusi-Soup-1-1.jpg.webp"
  },
  {
    "id": 46,
    "food": "Misir Wat",
    "description": "Red lentil stew",
    "price": 200,
    "restaurant_id": 6,
    "origin": "Ethiopian",
    "image": "https://example.com/misir-wat.jpg"
  },
  {
    "id": 47,
    "food": "Key Wat",
    "description": "Spicy beef stew",
    "price": 200,
    "restaurant_id": 7,
    "origin": "Ethiopian",
    "image": "https://example.com/key-wat.jpg"
  },
  {
    "id": 48,
    "food": "Gomen",
    "description": "Collard greens",
    "price": 200,
    "restaurant_id": 8,
    "origin": "Ethiopian",
    "image": "https://example.com/gomen.jpg"
  },
  {
    "id": 49,
    "food": "Atkilt Wot",
    "description": "Cabbage and carrots",
    "price": 200,
    "restaurant_id": 9,
    "origin": "Ethiopian",
    "image": "https://example.com/atkilt-wot.jpg"
  },
  {
    "id": 50,
    "food": "Ayib",
    "description": "Fresh cheese",
    "price": 200,
    "restaurant_id": 10,
    "origin": "Ethiopian",
    "image": "https://example.com/ayib.jpg"
  },
  {
    "id": 51,
    "food": "Fitfit",
    "description": "Torn injera with sauce",
    "price": 200,
    "restaurant_id": 11,
    "origin": "Ethiopia",
    "image": "https://example.com/fitfit.jpg"
  },
  {
    "id": 52,
    "food": "Kik Alicha",
    "description": "Yellow split pea stew",
    "price": 200,
    "restaurant_id": 12,
    "origin": "Ethiopian",
    "image": "https://example.com/kik-alicha.jpg"
  },
  {
    "id": 53,
    "food": "Awaze Tibs",
    "description": "Spicy meat",
    "price": 200,
    "restaurant_id": 13,
    "origin": "Ethiopian",
    "image": "https://example.com/awaze-tibs.jpg"
  },
  {
    "id": 54,
    "food": "Fosolia",
    "description": "Green beans and carrots",
    "price": 200,
    "restaurant_id": 14,
    "origin": "Ethiopian",
    "image": "https://example.com/fosolia.jpg"
  },
  {
    "id": 55,
    "food": "Gored Gored",
    "description": "Raw meat cubes",
    "price": 200,
    "restaurant_id": 15,
    "origin": "Ethiopian",
    "image": "https://example.com/gored-gored.jpg"
  },
  {
    "id": 56,
    "food": "Yetsom Beyaynetu",
    "description": "Vegetarian platter",
    "price": 200,
    "restaurant_id": 16,
    "origin": "Ethiopian",
    "image": "https://example.com/yetsom-beyaynetu.jpg"
  },
  {
    "id": 57,
    "food": "Genfo",
    "description": "Hot cereal",
    "price": 200,
    "restaurant_id": 17,
    "origin": "Ethiopian",
    "image": "https://example.com/genfo.jpg"
  },
  {
    "id": 58,
    "food": "Kolo",
    "description": "Roasted barley",
    "price": 200,
    "restaurant_id": 18,
    "origin": "Ethiopian",
    "image": "https://example.com/kolo.jpg"
  },
  {
    "id": 59,
    "food": "Tikil Gomen",
    "description": "Cabbage and potatoes",
    "price": 200,
    "restaurant_id": 19,
    "origin": "Ethiopian",
    "image": "https://example.com/tikil-gomen.jpg"
  },
  {
    "id": 60,
    "food": "Dulet",
    "description": "Tripe and liver dish",
    "price": 200,
    "restaurant_id": 20,
    "origin": "Ethiopian",
    "image": "https://example.com/dulet.jpg"
  },
  {
    "id": 61,
    "food": "Doro Wat",
    "description": "Doro Wat",
    "price": 200,
    "restaurant_id": 1,
    "origin": "Ethiopian",
    "image": "https://theplanetd.com/images/Ethiopian-food-Doro-Wot.jpg"
  },
  {
    "id": 62,
    "food": "Nyama Choma",
    "description": "Nyama Choma",
    "price": 200,
    "restaurant_id": 2,
    "origin": "Kenyan",
    "image": "https://www.willflyforfood.net/wp-content/uploads/2021/06/kenyan-food-nyama-choma.jpg.webp"
  },
  {
    "id": 63,
    "food": "Kwanga",
    "description": "Kwanga",
    "price": 200,
    "restaurant_id": 3,
    "origin": "Congolese",
    "image": "https://flavorverse.com/wp-content/uploads/2018/11/Kwanga-Congolese-Food-640x360.jpg"
  },
  {
    "id": 64,
    "food": "Groundnut Sauce (Binyebwa)",
    "description": "Groundnut Sauce (Binyebwa)",
    "price": 200,
    "restaurant_id": 4,
    "origin": "Ugandan",
    "image": "https://afrifoodnetwork.com/wp-content/uploads/2021/08/Uganda-G-nut-Sauce6S-scaled.jpg"
  },
  {
    "id": 65,
    "food": "Iyan (Pounded Yam)",
    "description": "Iyan (Pounded Yam)",
    "price": 200,
    "restaurant_id": 5,
    "origin": "Nigerian",
    "image": "https://cdn-bmalj.nitrocdn.com/uirOOtSrYrqqUksKHkiSCjZGZlPeXsmk/assets/images/optimized/rev-c3635d7/images/Nigerian-Food-Pounded-Yam.jpg"
  },
  {
    "id": 66,
    "food": "Ambasha",
    "description": "Slightly sweet bread",
    "price": 200,
    "restaurant_id": 6,
    "origin": "Ethiopian",
    "image": "https://example.com/ambasha.jpg"
  },
  {
    "id": 67,
    "food": "Mesir Kik Wat",
    "description": "Spicy red lentils",
    "price": 200,
    "restaurant_id": 7,
    "origin": "Ethiopian",
    "image": "https://example.com/mesir-kik-wat.jpg"
  },
  {
    "id": 68,
    "food": "Asa Tibs",
    "description": "Fried fish",
    "price": 200,
    "restaurant_id": 8,
    "origin": "Ethiopian",
    "image": "https://example.com/asa-tibs.jpg"
  },
  {
    "id": 69,
    "food": "Timatim Fitfit",
    "description": "Tomato salad",
    "price": 200,
    "restaurant_id": 9,
    "origin": "Ethiopian",
    "image": "https://example.com/timatim-fitfit.jpg"
  },
  {
    "id": 70,
    "food": "Doro Tibs",
    "description": "Sautéed chicken",
    "price": 200,
    "restaurant_id": 10,
    "origin": "Ethiopian",
    "image": "https://example.com/doro-tibs.jpg"
  },
  {
    "id": 71,
    "food": "Gored Gored",
    "description": "Ethiopian raw beef",
    "price": 200,
    "restaurant_id": 11,
    "origin": "Ethiopian",
    "image": "https://example.com/gored-gored-2.jpg"
  },
  {
    "id": 72,
    "food": "Minchet Abish",
    "description": "Spiced ground beef",
    "price": 200,
    "restaurant_id": 12,
    "origin": "Ethiopian",
    "image": "https://example.com/minchet-abish.jpg"
  },
  {
    "id": 73,
    "food": "Yebeg Alicha",
    "description": "Mild lamb stew",
    "price": 200,
    "restaurant_id": 13,
    "origin": "Ethiopian",
    "image": "https://example.com/yebeg-alicha.jpg"
  },
  {
    "id": 74,
    "food": "Shiro Fitfit",
    "description": "Chickpea stew with injera",
    "price": 200,
    "restaurant_id": 14,
    "origin": "Ethiopian",
    "image": "https://example.com/shiro-fitfit.jpg"
  },
  {
    "id": 75,
    "food": "Yetsom Beyaynetu",
    "description": "Vegetarian combo",
    "price": 200,
    "restaurant_id": 15,
    "origin": "Ethiopian",
    "image": "https://example.com/yetsom-beyaynetu-2.jpg"
  },
  {
    "id": 76,
    "food": "Tegabino Shiro",
    "description": "Chickpea porridge",
    "price": 200,
    "restaurant_id": 16,
    "origin": "Ethiopian",
    "image": "https://example.com/tegabino-shiro.jpg"
  },
  {
    "id": 77,
    "food": "Yebeg Tibs",
    "description": "Sautéed lamb",
    "price": 200,
    "restaurant_id": 17,
    "origin": "Ethiopian",
    "image": "https://example.com/yebeg-tibs.jpg"
  },
  {
    "id": 78,
    "food": "Kik Alicha",
    "description": "Yellow split pea stew",
    "price": 200,
    "restaurant_id": 18,
    "origin": "Ethiopian",
    "image": "https://example.com/kik-alicha-2.jpg"
  },
  {
    "id": 79,
    "food": "Gomen Be Siga",
    "description": "Collard greens with beef",
    "price": 200,
    "restaurant_id": 19,
    "origin": "Ethiopian",
    "image": "https://example.com/gomen-be-siga.jpg"
  },
  {
    "id": 80,
    "food": "Atakilt Wat",
    "description": "Cabbage, potatoes, and carrots",
    "price": 200,
    "restaurant_id": 20,
    "origin": "Ethiopian",
    "image": "https://example.com/atakilt-wat.jpg"
  },
  {
    "id": 81,
    "food": "Kik Alicha",
    "description": "Kik Alicha",
    "price": 220,
    "restaurant_id": 1,
    "origin": "Ethiopian",
    "image": "https://theplanetd.com/images/Ethiopian-Food-Kik-Alicha.jpg"
  },
  {
    "id": 82,
    "food": "Bhajias",
    "description": "Bhajias",
    "price": 150,
    "restaurant_id": 2,
    "origin": "Kenyan",
    "image": "https://www.willflyforfood.net/wp-content/uploads/2021/06/kenyan-food-bajias.jpg.webp"
  },
  {
    "id": 83,
    "food": "Mikate",
    "description": "Mikate",
    "price": 300,
    "restaurant_id": 3,
    "origin": "Congolese",
    "image": "https://flavorverse.com/wp-content/uploads/2018/11/Mikate-Congolese-Traditional-Food.jpg"
  },
  {
    "id": 84,
    "food": "Chickennat",
    "description": "Chickennat",
    "price": 250,
    "restaurant_id": 4,
    "origin": "Ugandan",
    "image": "https://afrifoodnetwork.com/wp-content/uploads/2021/08/chickennat-Ugandan-dish.jpg"
  },
  {
    "id": 85,
    "food": "Beef Suya (Thin Strips Of Seasoned, Grilled Beef)",
    "description": "Beef Suya (Thin Strips Of Seasoned, Grilled Beef)",
    "price": 180,
    "restaurant_id": 5,
    "origin": "Nigerian",
    "image": "https://cdn-bmalj.nitrocdn.com/uirOOtSrYrqqUksKHkiSCjZGZlPeXsmk/assets/images/optimized/rev-c3635d7/images/Nigerian-Food-Beef-Suya.jpg"
  },
  {
    "id": 86,
    "food": "Salsa",
    "description": "Various types - salsa verde, salsa roja, etc.",
    "price": 70,
    "restaurant_id": 6,
    "origin": "Mexican",
    "image": "https://example.com/salsa.jpg"
  },
  {
    "id": 87,
    "food": "Chilaquiles",
    "description": "Corn tortillas with salsa, cheese, and toppings",
    "price": 200,
    "restaurant_id": 7,
    "origin": "Mexican",
    "image": "https://example.com/chilaquiles.jpg"
  },
  {
    "id": 88,
    "food": "Tamales",
    "description": "Steamed corn dough with filling",
    "price": 170,
    "restaurant_id": 8,
    "origin": "Mexican",
    "image": "https://example.com/tamales.jpg"
  },
  {
    "id": 89,
    "food": "Pozole",
    "description": "Traditional soup with hominy and meat",
    "price": 250,
    "restaurant_id": 9,
    "origin": "Mexican",
    "image": "https://example.com/pozole.jpg"
  },
  {
    "id": 90,
    "food": "Ceviche",
    "description": "Citrus-marinated seafood salad",
    "price": 280,
    "restaurant_id": 10,
    "origin": "Mexican",
    "image": "https://example.com/ceviche.jpg"
  },
  {
    "id": 91,
    "food": "Mole",
    "description": "Various types - mole poblano, mole negro, etc.",
    "price": 300,
    "restaurant_id": 11,
    "origin": "Mexican",
    "image": "https://example.com/mole.jpg"
  },
  {
    "id": 92,
    "food": "Chiles en Nogada",
    "description": "Stuffed poblano chiles with walnut sauce",
    "price": 280,
    "restaurant_id": 12,
    "origin": "Mexican",
    "image": "https://example.com/chiles-en-nogada.jpg"
  },
  {
    "id": 93,
    "food": "Sopes",
    "description": "Thick tortillas with toppings",
    "price": 190,
    "restaurant_id": 13,
    "origin": "Mexican",
    "image": "https://example.com/sopes.jpg"
  },
  {
    "id": 94,
    "food": "Churros",
    "description": "Fried dough pastries",
    "price": 120,
    "restaurant_id": 14,
    "origin": "Mexican",
    "image": "https://example.com/churros.jpg"
  },
  {
    "id": 95,
    "food": "Flautas",
    "description": "Rolled and fried tortillas with filling",
    "price": 210,
    "restaurant_id": 15,
    "origin": "Mexican",
    "image": "https://example.com/flautas.jpg"
  },
  {
    "id": 96,
    "food": "Tortas",
    "description": "Mexican sandwiches",
    "price": 240,
    "restaurant_id": 16,
    "origin": "Mexican",
    "image": "https://example.com/tortas.jpg"
  },
  {
    "id": 97,
    "food": "Menudo",
    "description": "Tripe soup",
    "price": 270,
    "restaurant_id": 17,
    "origin": "Mexican",
    "image": "https://example.com/menudo.jpg"
  },
  {
    "id": 98,
    "food": "Birria",
    "description": "Spiced meat stew",
    "price": 280,
    "restaurant_id": 18,
    "origin": "Mexican",
    "image": "https://example.com/birria.jpg"
  },
  {
    "id": 99,
    "food": "Carnitas",
    "description": "Slow-cooked pork",
    "price": 260,
    "restaurant_id": 19,
    "origin": "Mexican",
    "image": "https://recipetineats.com/wp-content/uploads/2018/05/Pork-Carnitas-1000px.jpg"
  },
  {
    "id": 100,
    "food": "Cochinita Pibil",
    "description": "Yucatan-style slow-roasted pork",
    "price": 290,
    "restaurant_id": 20,
    "origin": "Mexican",
    "image": "https://example.com/cochinita-pibil.jpg"
  },
  {
    "id": 101,
    "food": "Tibs",
    "description": "Sautéed meat",
    "price": 320,
    "restaurant_id": 1,
    "origin": "Ethiopian",
    "image": "https://theplanetd.com/images/Ethiopian-food-Tibs.jpg"
  },
  {
    "id": 102,
    "food": "CHAPATI",
    "description": "CHAPATI",
    "price": 240,
    "restaurant_id": 2,
    "origin": "Kenyan",
    "image": "https://mayuris-jikoni.com/wp-content/uploads/2022/11/kenyan-chapati-1-copy.jpg"
  },
  {
    "id": 103,
    "food": " Loso na Madesu",
    "description": " Loso na Madesu",
    "price": 350,
    "restaurant_id": 3,
    "origin": "Congolese",
    "image": "https://flavorverse.com/wp-content/uploads/2018/11/Loso-na-Madesu-Congolese-Food.jpg"
  },
  {
    "id": 104,
    "food": "Muchomo",
    "description": "Muchomo",
    "price": 260,
    "restaurant_id": 4,
    "origin": "Ugandan",
    "image": "https://ugandaliveandtravel.com/wp-content/uploads/2022/04/Copy-of-post-photo-template-2022-05-06T103416.610.jpg"
  },
  {
    "id": 105,
    "food": "Ogbono Soup (Mango Seed Soup)",
    "description": "Ogbono Soup (Mango Seed Soup)",
    "price": 280,
    "restaurant_id": 5,
    "origin": "Nigerian",
    "image": "https://cdn-bmalj.nitrocdn.com/uirOOtSrYrqqUksKHkiSCjZGZlPeXsmk/assets/images/optimized/rev-c3635d7/images/Nigerian-Food-Pounded-Yams.jpg"
  },
  {
    "id": 106,
    "food": "Tostadas",
    "description": "Fried tortillas with toppings",
    "price": 190,
    "restaurant_id": 6,
    "origin": "Mexican",
    "image": "https://example.com/tostadas.jpg"
  },
  {
    "id": 107,
    "food": "Gorditas",
    "description": "Thick stuffed tortillas",
    "price": 210,
    "restaurant_id": 7,
    "origin": "Mexican",
    "image": "https://example.com/gorditas.jpg"
  },
  {
    "id": 108,
    "food": "Pambazos",
    "description": "Mexican sandwiches dipped in chili sauce",
    "price": 220,
    "restaurant_id": 8,
    "origin": "Mexican",
    "image": "https://example.com/pambazos.jpg"
  },
  {
    "id": 109,
    "food": "Papadzules",
    "description": "Yucatecan dish",
    "price": 260,
    "restaurant_id": 9,
    "origin": "Mexican",
    "image": "https://example.com/papadzules.jpg"
  },
  {
    "id": 110,
    "food": "Empanadas",
    "description": "Fried pastry filled with meat or sweet fillings",
    "price": 200,
    "restaurant_id": 10,
    "origin": "Mexican",
    "image": "https://example.com/empanadas.jpg"
  },
  {
    "id": 111,
    "food": "Chiles Rellenos",
    "description": "Stuffed poblano peppers",
    "price": 280,
    "restaurant_id": 11,
    "origin": "Mexican",
    "image": "https://example.com/chiles-rellenos.jpg"
  },
  {
    "id": 112,
    "food": "Capirotada",
    "description": "Mexican bread pudding",
    "price": 180,
    "restaurant_id": 12,
    "origin": "Mexican",
    "image": "https://example.com/capirotada.jpg"
  },
  {
    "id": 113,
    "food": "Picadillo",
    "description": "Ground meat dish with vegetables and spices",
    "price": 260,
    "restaurant_id": 13,
    "origin": "Mexican",
    "image": "https://example.com/picadillo.jpg"
  },
  {
    "id": 114,
    "food": "Agua Fresca",
    "description": "Various fruit-infused beverages",
    "price": 120,
    "restaurant_id": 14,
    "origin": "Mexican",
    "image": "https://example.com/agua-fresca.jpg"
  },
  {
    "id": 115,
    "food": "Camotes",
    "description": "Candied sweet potatoes",
    "price": 90,
    "restaurant_id": 15,
    "origin": "Mexican",
    "image": "https://example.com/camotes.jpg"
  },
  {
    "id": 116,
    "food": "Coctel de Camarones",
    "description": "Mexican shrimp cocktail",
    "price": 300,
    "restaurant_id": 16,
    "origin": "Mexican",
    "image": "https://example.com/coctel-de-camarones.jpg"
  },
  {
    "id": 117,
    "food": "Atole",
    "description": "Traditional hot drink made from masa",
    "price": 150,
    "restaurant_id": 17,
    "origin": "Mexican",
    "image": "https://example.com/atole.jpg"
  },
  {
    "id": 118,
    "food": "Tinga de Pollo",
    "description": "Shredded chicken in chipotle sauce",
    "price": 260,
    "restaurant_id": 18,
    "origin": "Mexican",
    "image": "https://example.com/tinga-de-pollo.jpg"
  },
  {
    "id": 119,
    "food": "Cochinita Pibil Tacos",
    "description": "Tacos with Yucatan-style slow-roasted pork",
    "price": 280,
    "restaurant_id": 19,
    "origin": "Mexican",
    "image": "https://example.com/cochinita-pibil-tacos.jpg"
  },
  {
    "id": 120,
    "food": "Elotes",
    "description": "Mexican street corn",
    "price": 150,
    "restaurant_id": 20,
    "origin": "Mexican",
    "image": "https://example.com/elotes.jpg"
  },
  {
    "id": 121,
    "food": "Kitfo",
    "description": "Kitfo",
    "price": 150,
    "restaurant_id": 1,
    "origin": "Ethiopian",
    "image": "https://theplanetd.com/images/Ethiopian-Food-Kitfo.jpg"
  },
  {
    "id": 122,
    "food": "Wali wa Nazi",
    "description": "Wali wa Nazi",
    "price": 300,
    "restaurant_id": 2,
    "origin": "Kenyan",
    "image": "https://www.willflyforfood.net/wp-content/uploads/2021/06/kenyan-food-wali-wa-nazi.jpg.webp"
  },
  {
    "id": 123,
    "food": "Mbika",
    "description": "Mbika",
    "price": 100,
    "restaurant_id": 3,
    "origin": "Congolese",
    "image": "https://www.chefspencil.com/wp-content/uploads/Mbika.jpg.webp"
  },
  {
    "id": 124,
    "food": "Boo",
    "description": "Boo",
    "price": 180,
    "restaurant_id": 4,
    "origin": "Ugandan",
    "image": "https://ugandaliveandtravel.com/wp-content/uploads/2022/04/Copy-of-post-photo-template-2022-05-06T103913.706.jpg"
  },
  {
    "id": 125,
    "food": " Akara (Fried Black-Eyed Peas Cake)",
    "description": " Akara (Fried Black-Eyed Peas Cake)",
    "price": 50,
    "restaurant_id": 5,
    "origin": "Nigerian",
    "image": "https://cdn-bmalj.nitrocdn.com/uirOOtSrYrqqUksKHkiSCjZGZlPeXsmk/assets/images/optimized/rev-c3635d7/images/Akara-Nigerian-food.jpg"
  },
  {
    "id": 126,
    "food": "Mandazi",
    "description": "African donuts",
    "price": 60,
    "restaurant_id": 6,
    "origin": "Kenyan",
    "image": "https://example.com/mandazi.jpg"
  },
  {
    "id": 127,
    "food": "Pilau",
    "description": "Spiced rice",
    "price": 250,
    "restaurant_id": 7,
    "origin": "Kenyan",
    "image": "https://example.com/pilau.jpg"
  },
  {
    "id": 128,
    "food": "Samosa",
    "description": "Stuffed pastry",
    "price": 40,
    "restaurant_id": 8,
    "origin": "Kenyan",
    "image": "https://example.com/samosa.jpg"
  },
  {
    "id": 129,
    "food": "Matoke",
    "description": "Green banana stew",
    "price": 180,
    "restaurant_id": 9,
    "origin": "Kenyan",
    "image": "https://example.com/matoke.jpg"
  },
  {
    "id": 130,
    "food": "Irio",
    "description": "Mashed potatoes, peas, and corn",
    "price": 200,
    "restaurant_id": 10,
    "origin": "Kenyan",
    "image": "https://example.com/irio.jpg"
  },
  {
    "id": 131,
    "food": "Kenyan Pilipili",
    "description": "Hot sauce",
    "price": 30,
    "restaurant_id": 11,
    "origin": "Kenyan",
    "image": "https://example.com/kenyan-pilipili.jpg"
  },
  {
    "id": 132,
    "food": "Wali wa Nazi",
    "description": "Coconut rice",
    "price": 180,
    "restaurant_id": 12,
    "origin": "Kenyan",
    "image": "https://example.com/wali-wa-nazi.jpg"
  },
  {
    "id": 133,
    "food": "Maharagwe",
    "description": "Bean stew",
    "price": 160,
    "restaurant_id": 13,
    "origin": "Kenyan",
    "image": "https://example.com/maharagwe.jpg"
  },
  {
    "id": 134,
    "food": "Kachumbari",
    "description": "Tomato and onion salad",
    "price": 50,
    "restaurant_id": 14,
    "origin": "Kenyan",
    "image": "https://example.com/kachumbari.jpg"
  },
  {
    "id": 135,
    "food": "Roast Maize",
    "description": "Grilled corn on the cob",
    "price": 40,
    "restaurant_id": 15,
    "origin": "Kenyan",
    "image": "https://example.com/roast-maize.jpg"
  },
  {
    "id": 136,
    "food": "Mukimo",
    "description": "Mashed potatoes, corn, peas, and greens",
    "price": 180,
    "restaurant_id": 16,
    "origin": "Kenyan",
    "image": "https://example.com/mukimo.jpg"
  },
  {
    "id": 137,
    "food": "Omena",
    "description": "Small fish, often dried and fried",
    "price": 120,
    "restaurant_id": 17,
    "origin": "Kenyan",
    "image": "https://example.com/omena.jpg"
  },
  {
    "id": 138,
    "food": "Biryani",
    "description": "Spiced rice with meat or vegetables",
    "price": 250,
    "restaurant_id": 18,
    "origin": "Kenyan",
    "image": "https://example.com/biryani.jpg"
  },
  {
    "id": 139,
    "food": "Bhajia",
    "description": "Deep-fried potato fritters",
    "price": 70,
    "restaurant_id": 19,
    "origin": "Kenyan",
    "image": "https://example.com/bhajia.jpg"
  },
  {
    "id": 140,
    "food": "Fish Stew",
    "description": "with Tilapia or Nile Perch",
    "price": 280,
    "restaurant_id": 20,
    "origin": "Kenyan",
    "image": "https://example.com/fish-stew.jpg"
  },
  {
    "id": 141,
    "food": "Siga Wat",
    "description": "Siga Wat",
    "price": 90,
    "restaurant_id": 1,
    "origin": "Ethiopia",
    "image": "https://theplanetd.com/images/Ethiopian-Food-Siga-Wot.jpg"
  },
  {
    "id": 142,
    "food": "Kenyan Pilau",
    "description": "Kenyan Pilau",
    "price": 200,
    "restaurant_id": 2,
    "origin": "Kenyan",
    "image": "https://www.willflyforfood.net/wp-content/uploads/2021/06/kenyan-food-pilau.jpg.webp"
  },
  {
    "id": 143,
    "food": "Mbala",
    "description": "Mbala",
    "price": 180,
    "restaurant_id": 3,
    "origin": "Congolese",
    "image": "https://www.chefspencil.com/wp-content/uploads/Boiled-Sweet-Potato.jpg.webp"
  },
  {
    "id": 144,
    "food": "Nsenene",
    "description": "Nsenene",
    "price": 60,
    "restaurant_id": 4,
    "origin": "Ugandan",
    "image": "https://toptenuganda.com/ezoimgfmt/i0.wp.com/toptenuganda.com/wp-content/uploads/2022/04/Nsenene-wpp1650783571956.webp?w=858&is-pending-load=1#038;ssl=1&ezimgfmt=rs:700x300/rscb1/ng:webp/ngcb1"
  },
  {
    "id": 145,
    "food": "Suya – Nigerian food",
    "description": "Suya – Nigerian food",
    "price": 280,
    "restaurant_id": 5,
    "origin": "Nigerian",
    "image": "https://allnigerianfoods.com/wp-content/uploads/suya.jpg"
  },
  {
    "id": 146,
    "food": "Fried Tilapia",
    "description": "Fried whole tilapia fish",
    "price": 230,
    "restaurant_id": 6,
    "origin": "Kenyan",
    "image": "https://example.com/fried-tilapia.jpg"
  },
  {
    "id": 147,
    "food": "Chicken Stew",
    "description": "Chicken cooked in a flavorful stew",
    "price": 220,
    "restaurant_id": 7,
    "origin": "Kenyan",
    "image": "https://example.com/chicken-stew.jpg"
  },
  {
    "id": 148,
    "food": "Mahamri",
    "description": "Sweet fried bread",
    "price": 60,
    "restaurant_id": 8,
    "origin": "Kenyan",
    "image": "https://example.com/mahamri.jpg"
  },
  {
    "id": 149,
    "food": "Mkate wa Ufuta",
    "description": "Sesame seed bread",
    "price": 70,
    "restaurant_id": 9,
    "origin": "Kenyan",
    "image": "https://example.com/mkate-wa-ufuta.jpg"
  },
  {
    "id": 150,
    "food": "Mukimo na Nyama",
    "description": "Mashed potatoes with meat",
    "price": 250,
    "restaurant_id": 10,
    "origin": "Kenyan",
    "image": "https://example.com/mukimo-na-nyama.jpg"
  },
  {
    "id": 151,
    "food": "Kuku Paka",
    "description": "Chicken in coconut curry",
    "price": 280,
    "restaurant_id": 11,
    "origin": "Kenyan",
    "image": "https://example.com/kuku-paka.jpg"
  },
  {
    "id": 152,
    "food": "Sukuma Ndiyo",
    "description": "Collard greens with peanut sauce",
    "price": 150,
    "restaurant_id": 12,
    "origin": "Kenyan",
    "image": "https://example.com/sukuma-ndiyo.jpg"
  },
  {
    "id": 153,
    "food": "Pilipili ya Kukaanga",
    "description": "Fried chili sauce",
    "price": 40,
    "restaurant_id": 13,
    "origin": "Kenyan",
    "image": "https://example.com/pilipili-ya-kukaanga.jpg"
  },
  {
    "id": 154,
    "food": "Ugali and Fish",
    "description": "Ugali served with fish",
    "price": 280,
    "restaurant_id": 14,
    "origin": "Kenyan",
    "image": "https://example.com/ugali-and-fish.jpg"
  },
  {
    "id": 155,
    "food": "Githeri and Fried Chicken",
    "description": "Githeri served with fried chicken",
    "price": 300,
    "restaurant_id": 15,
    "origin": "Kenyan",
    "image": "https://example.com/githeri-and-fried-chicken.jpg"
  },
  {
    "id": 156,
    "food": "Mutura",
    "description": "Kenyan sausage",
    "price": 120,
    "restaurant_id": 16,
    "origin": "Kenyan",
    "image": "https://example.com/mutura.jpg"
  },
  {
    "id": 157,
    "food": "Irio and Fried Tilapia",
    "description": "Irio served with fried tilapia",
    "price": 300,
    "restaurant_id": 17,
    "origin": "Kenyan",
    "image": "https://example.com/irio-and-fried-tilapia.jpg"
  },
  {
    "id": 158,
    "food": "Kenyan Biriani",
    "description": "Kenyan-style biryani",
    "price": 260,
    "restaurant_id": 18,
    "origin": "Kenyan",
    "image": "https://example.com/kenyan-biriani.jpg"
  },
  {
    "id": 159,
    "food": "Mbaazi",
    "description": "Pigeon peas in coconut sauce",
    "price": 160,
    "restaurant_id": 19,
    "origin": "Kenyan",
    "image": "https://example.com/mbaazi.jpg"
  },
  {
    "id": 160,
    "food": "Uji",
    "description": "Porridge made from millet or maize flour",
    "price": 70,
    "restaurant_id": 20,
    "origin": "Kenyan",
    "image": "https://example.com/uji.jpg"
  }
    ]


    # Create Restaurant objects and add them to the database
    foods = [FoodItem(**food) for food in food_data]
    db.session.add_all(foods)
    db.session.commit()

    print("🌱 Restaurant data seeding completed!")

    print("🌱 Orders data seeding completed!")


if __name__ == '__main__':
    with app.app_context():  # Update with your actual Flask app instance
        seed_data()
