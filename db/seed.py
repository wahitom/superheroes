from app.app import db
from app.models import PowersModel, HeroModel, HeroPowersModel

# Seed powers
powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"},
]

for data in powers_data:
    power = PowersModel(**data)
    db.session.add(power)

# Seed heroes
heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"},
]

for data in heroes_data:
    hero = HeroModel(**data)
    db.session.add(hero)

# Commit the changes so that the IDs are available for HeroPower associations
db.session.commit()

# Seed hero powers
strengths = ["Strong", "Weak", "Average"]
for hero in HeroModel.query.all():
    for _ in range(1, 4):  # Assuming each hero has 1 to 3 powers
        power = PowersModel.query.order_by(db.func.random()).first()
        hero_power = HeroPowersModel(hero_id=hero.id, power_id=power.id, strength=strengths.pop())
        db.session.add(hero_power)

# Commit the final changes
db.session.commit()

print("🦸‍♀️ Done seeding!")