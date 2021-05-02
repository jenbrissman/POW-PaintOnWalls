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

jb_1 = crud.create_image(user_id=1,
                        image_title="We The Youth ",
                        location="Point Breeze, Philadelphia, PA, USA",
                        image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619932052/mxfnawmcjclmcfu7m6hz.jpg",
                        artist="Keith Haring ")

jb_2 = crud.create_image(user_id=1,
                        image_title="Nobody Likes Me",
                        location="Stanley Park Drive, Vancouver, BC, Canada",
                        image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619932267/dgzi2f2pntycxshkmkj5.jpg",
                        artist="Iheart")


jb_3 = crud.create_image(user_id=1,
                        image_title="Part I",
                        location="Ribeira Grande, Portugal",
                        image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619932936/wrunm2bl7ztdocquec5s.jpg",
                        artist="Vhils")

jb_4 = crud.create_image(user_id=1,
                        image_title="Visual Disobedience",
                        location="The Pulse, Beach Road, Repulse Bay, Hong Kong",
                        image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619933271/lx8g3tlccrbzppngefqt.jpg",
                        artist="Shepard Fairey")

jb_5 = crud.create_image(user_id=1,
                        image_title="Sailor's Kiss",
                        location="The High Line, West 30th Street, New York, NY, USA",
                        image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619933391/meq168zr4pglkskc8oge.jpg",
                        artist="Kobra")

jb_6 = crud.create_image(user_id=1,
                        image_title="Women Are Heroes",
                        location="Kibera slum, Nairobi, Kenya",
                        image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619933572/xydacpgcz6l9mjrxwwbr.png",
                        artist="JR")

jb_7 = crud.create_image(user_id=1,
                        image_title="First Love",
                        location="Berlin, Germany",
                        image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619934247/hun3z6salup2dodkeyfy.jpg",
                        artist="Tavar Zawacki - Above")

jb_8 = crud.create_image(user_id=1,
                        image_title="Untitled",
                        location="Wynwood Walls, Northwest 2nd Avenue, Miami, FL, USA",
                        image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619934537/occpxh9tpozbzrzanp64.jpg",
                        artist="Martin Whatson")


# jb_9 = crud.create_image(user_id=1,
#                         image_title="Favorite Image Ever",
#                         location="123 Main Street",
#                         image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619895594/imdb23bcwvo7xu1f7ldy.jpg",
#                         artist="Shepard Fairey")



# jb_10 = crud.create_image(user_id=1,
#                         image_title="Favorite Image Ever",
#                         location="123 Main Street",
#                         image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619895594/imdb23bcwvo7xu1f7ldy.jpg",
#                         artist="Shepard Fairey")

# jb_11 = crud.create_image(user_id=1,
#                         image_title="Favorite Image Ever",
#                         location="123 Main Street",
#                         image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619895594/imdb23bcwvo7xu1f7ldy.jpg",
#                         artist="Shepard Fairey")



# sm_m = crud.create_image(user_id=2,
#                         image_title="Sean Street",
#                         location = "555 Sean",
#                         image_url="http://res.cloudinary.com/jenbrissman/image/upload/v1619895594/imdb23bcwvo7xu1f7ldy.jpg",
#                         artist="Kaws")