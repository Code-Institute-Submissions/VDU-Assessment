<h1 align="center">VDU Assessment</h1>

[View the live project here.]( https://bridcourtney.github.io/Business-Travel-Guide/)

To create an online application that allows user to complete & submit their VDU (Visual Display Unit) Assessment.  Assessments will be categorised per user submission for further analysis and follow up by Accessor

<h2>Table of Contents</h2>

- [UX](#heading)
  * [Goals](#sub-heading)
    + [Visitor Goals](#sub-sub-heading)
    + [Business Goals](#sub-sub-heading)
- [Heading](#heading-1)
  * [Sub-heading](#sub-heading-1)
    + [Sub-sub-heading](#sub-sub-heading-1)
- [Heading](#heading-2)
  * [Sub-heading](#sub-heading-2)
    + [Sub-sub-heading](#sub-sub-heading-2)




## UX



### Goals



#### Visitor Goals

The central target audience for VDU Assessment Manager are:
 - All Employees
 - All Contactors 
 
User Goals are:
 - Register / Login to VDU Assessment Manager
 - Complete my VDU Assessment
 - View Completed VDU Assessments
 - Edit my Completed VDU Assessments
 - Delete my Completed VDU Assessments
 
 Manager Goals are:
 - Register / Login to VDU Assessment Manager
 - View my reports VDU Assessments

Admin Goals are:
 - Register / Login to VDU Assessment Manager
 - Access Maintenance Section to maintain Department and Manager Dropdowns
 - Access Maintenance Section to maintain is_admin & is_manager rights

## Heading

This is an h1 heading

### Sub-heading

This is an h2 heading

#### Sub-sub-heading

This is an h3 heading

## Heading

This is an h1 heading

### Sub-heading

This is an h2 heading

#### Sub-sub-heading

This is an h3 heading



## User Experience (UX)

-   ### User stories

    -   #### Visitor Goals

        1. As Visitor, I want to find the Abbot site I am visiting and learn more about the site e.g. is it Manufacturing, Commercial etc
        2. As Visitor, I want to easily find out more about the area I am visiting e.g What Hotels, Restaurants and Attractions are in the vicinity
        3. As Visitor, I want to be able to look for information from the Team managaging the Portal
        
-   ### Structure
    -   #### Multi Image Carousal
         -  By mousing over the Site Image the User instantly is shown the site information and location on map.  The User can then move on to the next location and new details are loaded
           -   The multi image carousal improves the user experience as it allow the user to view site information and location on map without scrolling down.
       -   ### Design
    -   #### Colour Scheme
        -   Color is fundamental in the way we express the Abbott brand. The color palette I used includes, Dark in the header and light in the footer of each page.  The                   vibrant images in the Abbott Site carousal blend well with the background image.

    -   #### Typography.
        -   The 'Josefin Sans' font is the main font used throughout the whole website with sans-serif as the fallback font in case for any reason the font isn't being imported into the site correctly. The 'Josefin Sans'gives the Site an unified appearance throughtout. 
    -   #### Imagery 
        -   I selected vibrant images for each Site in the carousal that work well with the background image. 

*   ### Skeleton.

    -   Index Page Wireframe - [View](Business-Travel-Guide_Lgr&Med_Devices.pdf)

    -   Mobile / small device Wireframe - [View](Business-Travel-Guide_SM_Devices.pdf)


## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [jQuery](https://jqueryui.com)


### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Josefin Sans' font into the style.css file which is used on all pages throughout the project.
3. [jQuery:](https://jquery.com/)
    - jQuery used to hide Site information on page open, and then mouseover & mouseout to show/hide
4. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
5. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
6. [GIMP:](https://developer.gimp.org/)
    - GIMP was used resizing images and editing photos for the website.
7. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
8. [Places API:](https://developers.google.com/maps/documentation/javascript/examples/places-autocomplete-hotelsearch#maps_places_autocomplete_hotelsearch-javascript)
    - Place Autocomplete Hotel Search Tutorial
9. Maps JavaScript API
10. [Geocoding API:](https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse#maps_geocoding_reverse-javascript)
    - Reverse Geocoding Tutorial
11. [unsplash:](https://unsplash.com/)
    - I used upsplash to find good quality images of countries and landmarks
12. [EmailJS:](https://www.emailjs.com/)
    - In the Contact Us page I used EmailJS to Send Email Directly From JavaScript 



## Testing

The W3C Markup Validator, W3C CSS Validator and jshint Services were used to validate every page and js files of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
-   [jshint](https://jshint.com/) 
### Test Script
-   Link below is Test Script performed.
-   Test Scripts - [View](Test Scripts performed.docx)
     
### Further Testing
-   During testing it was found the 'Geocoder failed due to: INVALID_REQUEST' error was appearing on startup, to fix this I added a default value to #latlng.
-   During testing users reported it was confusing that there was no response when Comment was submitted on Contact page, I fixed this by added a success and fail Alert.
-   The Website was tested on Google Chrome, Internet Explorer & Microsoft Edge.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   Sometimes the user needs to hit the refresh button to load the map
-   It is not a bug, but the Geocode API reaches usage limit very quckly

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly     to make site responsive using the Bootstrap Grid System.

-   The Navbar code was taken from https://www.w3schools.com/bootstrap4/bootstrap_navbar.asp, and taylored to meet my requirements
-   The Carousal code was taken from https://azmind.com/bootstrap-carousel-multiple-items/
-   Geocode API https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse#maps_geocoding_reverse-javascript)
-   Places API https://developers.google.com/maps/documentation/javascript/examples/places-autocomplete-hotelsearch#maps_places_autocomplete_hotelsearch-javascript


### Content

-   All content was written by the developer.


 
### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.
