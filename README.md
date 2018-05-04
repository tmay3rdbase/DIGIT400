# [Memeline.win](https://www.memeline.win) for DIGIT 400
## Penn State Behrend
### Digital Media, Arts, and Technology

This is a scholarly site about memes made by **Taylor May** a student at [Penn State Behrend](http://behrend.psu.edu/).

The Motivation for this site came from my desire to make a more simple site than [knowyourmeme](http://knowyourmeme.com/) and [memebase](http://memebase.cheezburger.com/).

## Site Functionality

The site is a vertical timeline that allows first tells the user what a meme is. 

It then goes on to show the most popular meme for each time period from 1996 to 2017. 

As you scroll down the page there will be a **"TOP"** button that appears on the bottom right side of the page that returns the user to the top of the site.

The Navbar is fixed to the top of the page and displays each page upon **Click**.

The ***SEARCH MEMES*** tab takes the user to a page where they search a keyword and it displays a thumbnail image of a meme to them.

The ***TOPICS*** tab is a dropdown menu that shows each date to take you to the page that will expand on various scholarly pages.

The ***UPDATES*** page will display updates that happen to the site.

The ***ABOUT*** page is the last page that will also explain the site and me as the creator.

## Libraries Used!

On the site memeline.win there are two main python libraries used in `search.py`:

`from bs4 import BeautifulSoup`

`import requests`

## Python Libraries
[Memeline.win](https://www.memeline.win) is hosted by the usual `__init__.py` file.

**However** above this it also incorporates two other python files:

`pages.py`

Which is my content management file that links all the webpages to the auto populated tab list in my `navbar.html`.

***AND***

`search.py`

Which incorporates the two python libraries to allow the user to input a word and search it on google images to bring back the image.

## Acknowledgements
I could not have accomplished all of this by myself. I want to personally thank my professor [Aaron Mauro](https://github.com/aaronmauro) and the [bootsnipp](https://bootsnipp.com/) user *_[andrewnite](https://bootsnipp.com/andrewnite)_* for the timeline layout that I tweaked.
Along with this, a huge helper in this has been the [getbootstrap site](https://getbootstrap.com/) for obvious basic page layout and navbar usage.
