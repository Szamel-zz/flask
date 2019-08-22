from flask_examples.basic_db import db, Puppy


# Create
my_puppy = Puppy('Rufus', 5)

db.session.add(my_puppy)
db.session.commit()


# Read
all_pupies = Puppy.query.all()  # ist of puppies object in the table
print(all_pupies)


# Select id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)


# Filters
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())


# Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


# Delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()


# Check the results
all_puppies = Puppy.query.all()
print(all_puppies)

'''
You can not run this code multiple time, because it can delete id=2 once
1. delete data.sqlite
2. run setupdatabase.py
3. run crud.py
'''