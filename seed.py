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
                      password="password1",
                      )

sm = crud.create_user(first_name="Sean",
                      last_name="Montgomery",
                      email="sean@sean.com",
                      password="sean",
                      )

jb_m = crud.create_image(user_id=1,
                        image_title="Bend Street",
                        location="123 Main Street",
                        url="http://res.cloudinary.com/followspotapp/image/upload/v1617853423/nhzyx0asj1272aqkjlx5.jpg",
                        artist="Shepard Fairey")

sm_m = crud.create_image(user_id=2,
                        image_title="Sean Street",
                        location = "555 Sean",
                        url="http://res.cloudinary.com/followspotapp/image/upload/v1617853423/nhzyx0asj1272aqkjlx5.jpg",
                        artist="Kaws")