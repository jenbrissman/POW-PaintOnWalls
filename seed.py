import os
import json
import crud
import model
import server

os.system('dropdb pow')
os.system('createdb pow')

model.connect_to_db(server.app)
model.db.create_all()

##############################USER#############################################

jb = crud.create_user(first_name="Jen",
                      last_name="Brissman",
                      email="brissman514@gmail.com",
                      password="239127e09157cbafb6212123b102aa1103241946b3684c232c44b8367c3a4d47",
                      )

sm = crud.create_user(first_name="Sean",
                      last_name="Montgomery",
                      email="sean@sean.com",
                      password="c278ec5a69c34aace42773e41b1163e6ce40c906f2a14f807d39d1b2a1c2dff5",
                      )

jb_m = crud.create_image(user_id=1,
                        image_title="Favorite Image Ever",
                        location="123 Main Street",
                        image_url="http://res.cloudinary.com/followspotapp/image/upload/v1617853423/nhzyx0asj1272aqkjlx5.jpg",
                        artist="Shepard Fairey")

sm_m = crud.create_image(user_id=2,
                        image_title="Sean Street",
                        location = "555 Sean",
                        image_url="http://res.cloudinary.com/followspotapp/image/upload/v1617853423/nhzyx0asj1272aqkjlx5.jpg",
                        artist="Kaws")