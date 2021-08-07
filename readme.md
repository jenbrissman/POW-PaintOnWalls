![POW](static/images/powheader.png "POW")

by [Jen Brissman](https://www.linkedin.com/in/jenbrissman/) | [brissman514@gmail.com](mailto:brissman514@gmail.com?subject=[GitHub]%20Pow)

## <a name="#About"></a>What is POW? - [Demo Video](https://www.youtube.com/watch?v=alTthz7xCLs)
POW - otherwise known as “Paint on Walls” is a communal photo sharing platform for lovers of street art.

![DemoGIF](static/images/gallery.GIF "DemoGIF")

Table of Contents
------
- [Tech Stack](#Tech)
- [Testing](#Testing)
- [Features](#Features)
- [Install](#Install)
- [Meet the Developer](#Meet)
- [Looking Ahead](#Future)

## <a name="#Tech"></a>Tech Stack

- **Frontend**: JavaScript | HTML5 | CSS | Bootstrap
- **Backend**: Python3 | Flask | SQLAlchemy | Jinja2
- **APIs**: Cloudinary | GoogleMaps
- **Database**: PostgreSQL

## <a name="#Testing"></a>Testing

For my tests, I used [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/) as it allows you to see your test coverage.

1. To run coverage, run this command:
```shell
$ coverage run -m unittest discover.
```

2. To see the coverage report, run: 
```shell
$ coverage report -m.
```

## <a name="#Features"></a>Features
[Login](#Login) | [Gallery](#Gallery) | [Location](#Location) | [View](#View) | [Search](#Search) | [Upload](#Upload) | [Logout](#Logout) | [Database](#SQLDBM)

## <a name="#Login"></a>Login and Registration
Users can register and create an account which will give them access to the public street art gallery, as well as the option to upload photos of their own. I have hashed the user's credentials with sha256 to add security for the user. I built Pow with Flask - creating a service that uses a Postgres database interfaced with the SQLAlchemy ORM.

![Login](static/images/login.GIF)

## <a name="#Gallery"></a>Gallery
After logging in, the user will be brought to the public street art gallery. This gallery represents the full database of photos uploaded by the POW community of users. Each photo is displayed on a responsive card that I have styled using Bootstrap and CSS. Hover over an image and the card flips to display information about the specific street art piece on the back. This information is being dynamically displayed using Jinja templating and includes the title and artist, as well as links to a full-size image of the piece, and its locatio   n.

![Gallery](static/images/gallery.GIF)

## <a name="#Location"></a>Location
Clicking on the "location" button opens Google Maps to show exactly where that piece of art is located.

![Location](static/images/location.gif)

## <a name="#View"></a>View Image
Clicking on the "view image" button opens a full size view of the particular piece of art.

![Search](static/images/view.gif)

## <a name="#Search"></a>Search
To filter through the cards, I developed a search feature by adding a JavaScript event listener that evaluates keystrokes to hide the cards that do not contain text matching the query string.

![View](static/images/search.gif)

## <a name="#Upload"></a>Upload Image
To upload a photo to the community library, I built a form which takes in the title, the artist, and the location using Google’s Map & Places API with their Place Autocomplete service. For the image file itself I implemented Cloudinary’s media management API, which returns the url for the image uploaded to my database.

![Upload](static/images/upload.GIF)

## <a name="#Pics"></a>My Pics
Clicking 'my pics' in the nav bar will apply a filter on the galley that shows on your uploads, where you can see the specific photos you have added to the Pow community.

![Pics](static/images/mypics.gif)

## <a name="#Logout"></a>Log Out
![Logout](static/images/logout.GIF)

## <a name="#Data"></a>Data Model

![SQLDBM](static/images/SQLDBM.png)

## <a name="#Future"></a>Looking Ahead
I really loved making this app. It was my first experience creating a public community based application. Moving forward, I want to implement Amazon’s Rekognition feature so that the search function can search characteristics of the images, not just a string search of the information in the database/information displayed on the cards. Thank you for taking the time to learn a bit about POW, I really look forward to connecting with you!

## <a name="#Install"></a>Install

### Running POW

1. Clone this repository:
```shell
git clone https://github.com/jenbrissman/POW-PaintOnWalls.git
```

***Optional***: Create and activate a virtual environment:
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

2. Install dependencies: 
```shell
pip3 install -r requirements.txt
```

3. Create environmental variables to hold your API keys in a `secrets.sh` file. You'll need to create your own Cloudinary API keys:
```
export cloud_name="create your own cloudindary name/account"
export cloud_api_key="once you do this they will provide you a key which you will put here"
export cloud_api_secret="use your own secret of course, shhh"
```
Here are some relevant docs for creating and set up an account with Cloudinary:
[Create account](https://cloudinary.com/users/register/free) | 
[Get API Key and Secret](https://cloudinary.com/documentation/how_to_integrate_cloudinary)


4. Create your database & seed sample data:
```shell
createdb pow
python3 seed.py
```

5. Run the app on localhost:
```shell
source secrets.sh
python3 server.py
```

## <a name="#Meet"></a>Meet the Developer
A tenacious multi-hyphenate, I am a driven and focused problem solver who has a knack for seeing the bigger picture in any situation. I currently work for Cloudinary as a Software Engineering Tutorial Producer. From 2013-2021, I was the Senior Operations Manager at a private investment office in NYC, where I was promoted twice within the company.

I have also had a successful career as a theatre, television, film, voiceover, commercial actress and model in New York City. I hold a BFA from the highly competitive UC College-Conservatory of Music. This is one of the country's leading arts institutions which accepts only the top 1% of applicants.
I am a proud, contributing member and co-founder of the mentorship program within Artists Who Code, an online community of artists in tech.
In my free time, I am an adventurous world traveler who enjoys mountain biking, snowboarding, running, scuba diving, pickleball, cooking, and am happiest in hiking boots :)

Connect with [Jen Brissman](https://www.linkedin.com/in/jenbrissman/) on LinkedIn!