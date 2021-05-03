"use strict";

// #######################LOGIN####################################

$('.message a').click(function(){
  $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
  });

$('#register-form').on('submit', (evt) => {
  evt.preventDefault();
  const formInputs = {
      'first_name': $('#first_name').val(),
      'last_name': $('#last_name').val(),
      'email': $('#email').val(),
      'password': $('#password').val(),
  }

  $('.flashes').empty()

  // $.post('/api/register', formInputs, (res) => {
  //     if (res != 'None') {
  //         $('#display-message').text(`Hi ${res.first_name} ${res.last_name}! You have successfully created an account. Please Log In!`)
  //     } else {
  //         $('#display-message').text(`An account with the email ${res.email} already exists. Please try again with a different email`)
  //     }
  // });
});

// #######################ADD IMAGE####################################

async function addImage() {
    const url = "/upload-cloudinary";
    const fileList = document.querySelectorAll("[type=file]");

    //iterate over the image files
    for (let i = 0; i < fileList.length; i++) {
        const formData = new FormData();
      
        let file = fileList[i];
        formData.append("file", file.files[0]);
        //this is where we send the data to the /upload-cloudinary end point
        let cloud_res = await fetch(url, {
            method: "POST",
            body: formData
        })
        //we are waiting for cloudinary to return the image object 
        let cloud_res_json = await cloud_res.json();

        //this is where we store the image in the database
        let flask_resp = await fetch('/submit-image', {
            method: "POST",
            body: JSON.stringify({
                'artist': $('#artist').val(),
                "image_url": cloud_res_json.url,
                'location': $('#autocomplete').val(),
                'image_title': $('#image_title').val(),
            }),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });
        
        if (!flask_resp.ok) {
            alert(`Unable to load files. ${flask_resp.statusText}`)
            break 
        }   
    }
    //once function has completed, we reroute to the gallery
    window.location = '/gallery'
}

// #######################ON SUBMIT####################################

const form = document.querySelector(".upload-art");

form.addEventListener("submit", (evt) => {
    evt.preventDefault();
    addImage()
        })
        
// ###################################GOOGLE MAPS#######################################

var placeSearch, autocomplete;
      var componentForm = {
        street_number: 'short_name',
        route: 'long_name',
        locality: 'long_name',
        administrative_area_level_1: 'short_name',
        country: 'long_name',
        postal_code: 'short_name'
      };

      function initAutocomplete() {
        autocomplete = new google.maps.places.Autocomplete(
            /** @type {!HTMLInputElement} */(document.getElementById('autocomplete')),
            {types: ['geocode', 'establishment']});
        }

      function geolocate() {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var geolocation = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            var circle = new google.maps.Circle({
              center: geolocation,
              radius: position.coords.accuracy
            });
            autocomplete.setBounds(circle.getBounds());
          });
        }
      }

// // #######################SEARCH FEATURE####################################

// const searchBar = document.getElementById('searchBar');
// const text = document.getElementsByClassName("flip-card-back");

// function searchCards(queryString) {
//     console.log(Object.values(text).filter((t) => !t.outerText.toLowerCase().includes(queryString)))
//     console.log(Object.values(text).map((t) => console.log(t.outerText.toLowerCase())))
//     return Object.values(text).filter((t) => !t.outerText.toLowerCase().includes(queryString))
// }

// searchBar.addEventListener('keyup', (evt) => {
//     const searchString = evt.target.value;
//     let searchResults = searchCards(searchString.toLowerCase())
//     for (let i = 0; i < text.length; i++) {
//         searchResults.includes(text[i]) ? text[i].style.display = "none" : text[i].style.display = "block"    
//     }
// });