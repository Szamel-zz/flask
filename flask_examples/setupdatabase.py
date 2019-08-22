from flask_examples.basic_db import db, Puppy


# Creates all the tables model
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

# None
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

db.session.commit()

# id's
print(sam.id)
print(frank.id)