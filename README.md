# Sleeping Dragon Hobby Shop

![Image]

### [See live site.](https://sleeping-dragon-hobby-shop.herokuapp.com/)

## Table of Contents

> -	[Overview](#overview)
> -	[Description](#description)
> -	[UX](#ux)
> -	[Features](#features)
> -	[Technologies Used](#technologies-used)
> -	[Testing](#testing)
> - [Deployment](#deployment)
> -	[Credits](#credits)
> - [Acknowledgements](#acknowledgements)

## Overview

Sleeping Dragon Hobby Shop is an e-commerce store for an existing company selling modelling and hobby supplies for wargaming, intended to replace the [current online presence](https://www.sleepingdragonhobbyshop.co.uk/) with a new web application. It also aims to reduce the company's reliance on third-party apps/plugins for site design and store management by providing internal control of those elements to site super users.  

## Description


## User Experience (UX)

### User stories
**User classes:**

- Site User - General user
- Shopper - A user wishing to purchase products
- Store Owner - Site super user

<table>
    <tr>
        <th>STORY ID</th>
        <th>AS A</th>
        <th>I WANT TO BE ABLE TO</th>
        <th>SO THAT I CAN</th>
    </tr>
    <tr>
        <td colspan="4"><b>Viewing and Navigation</b></td>
    </tr>
    <tr>
        <td>US01</td>	
        <td>Shopper</td>	
        <td>View a list of products</td>	
        <td>Select some to purchase</td>
    </tr>
    <tr>
        <td>US02</td>
        <td>Shopper</td>
        <td>View a specific category of products</td>
        <td>Quickly find products I'm interested in without having to search through all products</td>
    </tr>	
    <tr>
        <td>US03</td>
        <td>Shopper</td>
        <td>View individual product details</td>
        <td>Identify the price, description, product rating and product image</td>
    </tr>
    <tr>
        <td>US04</td>
        <td>Shopper</td>
        <td>Easily view the total of my purchases at any time</td>
        <td>Avoid spending too much</td>
    </tr>
    <tr>
        <td colspan="4"><b>Registration and User Accounts</b></td>
    </tr>
    <tr>
        <td>US05</td>
        <td>Site User</td>
        <td>Register for an account</td>
        <td>Have a personal account and be able to view my profile</td>
    </tr>
    <tr>
        <td>US06</td>
        <td>Site User</td>
        <td>Login or logout</td>
        <td>Access my personal account information</td>
    </tr>
    <tr>
        <td>US07</td>
        <td>Site User</td>
        <td>Reset my password</td>
        <td>Recover access to my account</td>
    </tr>
    <tr>
        <td>US08</td>
        <td>Site User</td>
        <td>Receive an email confirmation after registering</td>
        <td>Verify that my account registration was successful</td>
    </tr>
    <tr>
        <td>US09</td>
        <td>Site User</td>
        <td>Have a personalised user profile</td>
        <td>View my personal order history and order confirmatons, and save my payment information</td>
    </tr>
    <tr>
        <td>US10</td>
        <td>Site User</td>
        <td>Login using a social media account</td>
        <td>Quickly access my account using social media credentials with one click</td>
    </tr>
    <tr>
        <td colspan="4"><b>Sorting and Searching</b></td>
    </tr>
    <tr>
        <td>US11</td>
        <td>Shopper</td>
        <td>Sort the list of available products</td>
        <td>Easily identify the best rated, best priced and categorically sorted products</td>
    </tr>
    <tr>
        <td>US12</td>
        <td>Shopper</td>
        <td>Sort a specific category of products</td>
        <td>Find the best priced or best rated product in a specific category, or sort products in that category by name</td>
    </tr>
    <tr>
        <td>US13</td>
        <td>Shopper</td>
        <td>Sort multiple categories of products simultaneously</td>
        <td>Find the best priced or best rated products across broad categories, such as "paints" or "materials"</td>
    </tr>
    <tr>
        <td>US14</td>
        <td>Shopper</td>
        <td>Sort products by specific brands</td>
        <td>Find all products from a particular brand or manufacturer</td>
    </tr>
    <tr>
        <td>US15</td>
        <td>Shopper</td>
        <td>Search for a product by name or description</td>
        <td>Find a specific product I'd like to purchase</td>
    </tr>
    <tr>
        <td>US16</td>
        <td>Shopper</td>
        <td>Easily see what I've searched for and the number of results</td>
        <td>Quickly decide whether the product I want is available</td>
    </tr>
    <tr>
        <td colspan="4"><b>Purchasing and Checkout</b></td>
    </tr>
    <tr>
        <td>US17</td>
        <td>Shopper</td>
        <td>View items in my cart to be purchased</td>
        <td>Identify the total cost of my purchase and all items I will receive</td>
    </tr>
    <tr>
        <td>US18</td>
        <td>Shopper</td>
        <td>Adjust the quantity of individual items in my cart</td>
        <td>Easily make changes to my purchase before checkout</td>
    </tr>
    <tr>
        <td>US19</td>
        <td>Shopper</td>
        <td>Easily enter my payment information</td>
        <td>Checkout quickly and with no hassle</td>
    </tr>
    <tr>
        <td>US20</td>
        <td>Shopper</td>
        <td>Feel my personal and payment information is safe and secure</td>
        <td>Confidently provide the needed information to make a purchase</td>
    </tr>
    <tr>
        <td>US21</td>
        <td>Shopper</td>
        <td>View an order confirmation after checkout</td>
        <td>Verify that I haven't made any mistakes</td>
    </tr>
    <tr>
        <td>US22</td>
        <td>Shopper</td>
        <td>Receive an email confirmation after checkout out</td>
        <td>Keep the confirmation of what I've purchase for my records</td>
    </tr>
    <tr>
        <td colspan="4"><b>Sales and Reports</b></td>
    </tr>
    <tr>
        <td>US23</td>
        <td>Store Owner</td>
        <td>Get sales reports</td>
        <td>See individual orders and sales totals over time</td>
    </tr>
    <tr>
        <td>US24</td>
        <td>Store Owner</td>
        <td>Get product reports</td>
        <td>See product sales and manage stock levels</td>
    </tr>
    <tr>
        <td>US25</td>
        <td>Store Owner</td>
        <td>Search for individual orders by name or unique ID</td>
        <td>Verify order information</td>
    </tr>
    <tr>
        <td colspan="4"><b>Admin and Store Management</b></td>
    </tr>
    <tr>
        <td>US26</td>
        <td>Store Owner</td>
        <td>Add a product or category</td>
        <td>Add new items or categories to my store</td>
    </tr>
    <tr>
        <td>US27</td>
        <td>Store Owner</td>
        <td>Edit/Update a product or category</td>
        <td>Change product prices, descriptions, images and other product criteria</td>
    </tr>
    <tr>
        <td>US28</td>
        <td>Store Owner</td>
        <td>Delete a product or category</td>
        <td>Remove items that are no longer for sale</td>
    </tr>
</table>


## Structure

- ### Data Structure
![Image](data-structure.png)


## Skeleton



## Surface

### Images


### Colours


### Typography


### Icons


## Features


### Existing Features

### Features Left to Implement


## Technologies Used

#### Languages:
* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


#### Database 
* Development - [SQLite](https://docs.djangoproject.com/en/3.2/ref/databases/#sqlite-notes)
* Deployed site - [Heroku PostgreSQL](https://www.heroku.com/postgres)

#### Storage 
* [Amazon AWS S3](https://aws.amazon.com/) - used to store static files.

#### Payments 
* [Stripe](https://stripe.com/docs/api) - fully integrated payments platform.

#### Libraries & Frameworks:
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
* [Balsamiq](https://balsamiq.com/) - Used for the creation of wireframes.
* [FontAwesome](https://fontawesome.com/) - Used for all site icons.
* [dbdiagram.io](https://dbdiagram.io/home) - Used to map out data structure. 
* [JQuery](https://jquery.com) - The project uses JQuery to simplify DOM manipulation.
* [GoogleFonts](https://fonts.google.com/) - 'Syncopate' and 'Raleway' fonts.
* [Bootstrap v5.0](https://getbootstrap.com/) - A mobile-first responsive library used to construct various parts of the project
* [Popper](https://popper.js.org/) - Included as a requirement of Bootstrap.
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - Used for user authentication
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - **Amazon Web Services SDK** for python. Used to configure **Amazon Web Services S3** storage of static files.
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - enables enhanced rendering of Django forms including integration with **Bootstrap**.
* [dj-database-url](https://pypi.org/project/dj-database-url/) - Django database configuration utility. Used to configure connection to the **Heroku** deployed postgres database.
* [django-countries](https://pypi.org/project/django-countries/) - Django application providing country choices for use with forms etc. Used to populate country choices on the **Country** dropdowns.
* [django-storages](https://django-storages.readthedocs.io/en/latest/) - Custom storage backends for **Django**. Used to configure **Amazon Web Services S3** storage of static files.
* [gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server for UNIX. Used as part of the **Heroku** deployment process.
* [pillow](https://pillow.readthedocs.io/en/stable/) - Python imaging library.
* [psycopg2](https://pypi.org/project/psycopg2/) - **PostgreSQL** database adapter for Python. Used as part of the **Heroku** deployment process.

#### Version Control:
* [Github](https://github.com/) - Used to store the code 
* [Gitpod](https://gitpod.io/) - Used as the primary version control IDE for development to further push and commit code to GitHub.
* [Heroku](https://www.heroku.com/home) - Used to deploy the live site

#### Other:
* [Code Institute Course Content](https://courses.codeinstitute.net/) - Primary source of learning code.
* [Stack Overflow](https://stackoverflow.com/) - Used for general troubleshooting and examples.
* [W3Schools](https://www.w3schools.com/) - Used for examples and tutorials.
* [ChromeDevTools](https://developers.google.com/web/tools/chrome-devtools) - Used frequently to detect any issues/bugs or layout differences.
* [Coolors](https://coolors.co/) - Used to help define the site colour scheme.
* [ami.responsive](http://ami.responsivedesign.is/) - Used to generate multi-device mockup image.
* [ResizeImage](https://resizeimage.net/) - Used to resize images to web-optimised sizes
* [Unsplash](https://unsplash.com) - Used to find suitable background and images throughout the project.

---

## Testing


## Deployment
The project has been developed using [Gitpod](https://www.Gitpod.io/) and [GitHub](https://github.com/). 
The project was regularly committed to [GitHub](https://github.com/) during the initial development phase.  
The website resides as a repository in [GitHub](https://github.com/), and has been been deployed 
using [Heroku](https://dashboard.heroku.com/).  
Static files are stored using [Amazon AWS](https://aws.amazon.com/) in an **Amazon Web Services S3 Bucket**.

In order to make a *Fork* or *Clone* of the project, a [GitHub](https://www.Gitpod.io/) account is required. 
The [Gitpod Browser Extension](https://www.Gitpod.io/docs/browser-extension/) is also recommended.  

<details>
<summary>GitHub</summary>

* Go to [GitHub](https://github.com/) and sign in, or sign up for an account.
* Once a Github account was created, I opened a new repository by clicking the green button "new". To create this project, I used the Code Institute's student 
[template](https://github.com/Code-Institute-Org/gitpod-full-template).
* Click on the green "gitpod" button to open [Gitpod](https://gitpod.io/), a cloud-based version control software or IDE, which was used to write all code for this project.
* It was then pushed or saved in the terminal to Github where it is stored in a [repository](https://github.com/NickChapman1988/sleeping-dragon-hobby-shop)
</details>

<details>
<summary>Heroku</summary>
The project was deployed to Heroku using the following steps:

* IF NOT USING FIXTURE FILES - to dump the data from your mysql development database to a json file, use the following command at the terminal *note - manage.py must be connected to your local mysql development database*:
`python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`
* Log in to **Heroku**, and create a new **App** by clicking the *New* button in the top right of 
your *Dashboard* and selecting *Create new app*. Give the new **App** a name (one that closely matches your Django appname) and set the region to your closest geographical region, 
then click *Create app*.
* Provision a new **POSTGRES** database from the *Resources* tab.
* Confirm that the **App** is connected to the correct **GitHub** repository.
* Install `dj_database_url` and `psycopg2-binary` using the `pip3 install` command
* Use the `pip3 freeze > requirements.txt` terminal command to to create a `requirements.txt` file, 
which lists all the **Python** dependencies.
* Import dj_database_url in settings.py.
* In settings.py, connect the **POSTGRES** database by setting `DATABASES` to match the `DATABASE_URL` from the Heroku Config Variables (under Settings):
```
    DATABASES = {
        'default': dj_database_url.parse(database_url)
    }
```

* Run `python3 manage.py showmigrations` at the terminal to show migrations to be applied to the new POSTGRES database.
* Run `python3 manage.py migrate --plan` at the terminal to check the migrations.
* Run `python3 manage.py migrate` at the terminal to apply the migrations to the new POSTGRES database.
* Note - if you encounter `error: django.db.utils.OperationalError: FATAL:  role "xxxxxxxxxxx" during configuration of POSTGRESQL`, run `unset PGHOSTADDR` at the terminal.
* Run `python3 manage.py loaddata db.json` at the terminal to load the data from the local json created earlier 
* If using fixture files, run `python3 manage.py loaddata fixturefilename` for each fixture file, making sure to load in the correct order (i.e load any fixtures with dependencies *after* loading the files they depend on)
* Install `gunicorn` and re-run `pip freeze > requirements.txt` at the terminal.
* Create a `Procfile`, declaring the process type in the root of the project. 
* The `Procfile` should have only one line that reads `web: gunicorn appname.wsgi:application`, with no empty white space or lines, where `appname` is the application name.
* Login to **Heroku** at the terminal using `heroku login -i`
* Run the command `heroku config:set DISABLE_COLLECTSTATIC=1 --app appname` at the terminal, where `appname` is the Heroku application name.
* Add `ALLOWED_HOSTS = ['appname.herokuapp.com', 'localhost']` to `settings.py` where where `appname` is the Heroku application name.
* Add, commit and push the newly created `requirements.txt` and `Procfile` files to the **GitHub**
repository using the `git add`, `git commit` and `git push` commands.
* Set the git remote using `heroku git:remote -a appname`, where `appname` is the application name.
* Deploy the app to heroku using `git push heroku branchname`, where `branchname` is the github branch name.
* In the *Dashboard* for the new application, click on *Settings* menu > *Reveal Config Vars*.
* Generate a Django secret key using [miniwebtool.com](https://miniwebtool.com/django-secret-key-generator/) and add it to the environment variables.
* In the Heroku Config Variables, add DISABLE_COLLECTSTATIC and set the value to 1, and add DJANGO_SECRET_KEY setting the value to the generated secret key.
* From your **App** *Dashboard*, click on the *Deploy* menu > *Deployment method* section and select *GitHub*.
* Search for your **GitHub** repository then click *Connect* to connect.
* Confirm that the **App** is connected to the correct **GitHub** repository.
* Enable **Automatic Deploys** from the correct **GitHub** branch.
* Update, commit and push the code to **GitHub** and **Heroku** using the 
`git add`, `git commit` and `git push` commands.
* **Heroku** will receive the code from **GitHub** and build the **App** with the required packages and dependencies.
* Once complete, you should see the message *Your app was successfully deployed*.
* Confirm that the application is automatically deploying to **Heroku** by checking the *Build Log* in the *Activity* tab.
* **Heroku** is now successfully connected to **GitHub** and any changes made in the **GitHub** repository 
will be automatically pushed to **Heroku**.
</details>

<details>
<summary>Forking the GitHub Repository</summary>
Forking the GitHub repository creates a copy of the original repository on your own GitHub account to view and/or make changes without affecting the original repository; use the following steps to fork:

1. Log in to GitHub and locate the GitHub [repository](https://github.com/NickChapman1988/game-shelf)
2. At the top of the repository above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the repository in your own GitHub account.

For further information on *Forking* a [GitHub](https://github.com/) repository, 
see the [GitHub Documentation](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).
</details>

<details>
<summary>Making a local Clone</summary>
* Go to the [Project Code Repository Location](https://github.com/NickChapman1988/sleeping-dragon-hobby-shop) on [GitHub](https://github.com/).
* Select the *Code* dropdown and choose *GitHub CLI* under *Clone*. This will give you a *URL* that may be copied into the clipboard. 
* Open the Git Bash command line interface in [Gitpod](https://www.Gitpod.io/).
* Change the current working directory to the location where you would like the cloned directory to reside.
* Type `git clone`, and then paste the *URL* copied earlier, eg:  
`$ git clone https://github.com/NickChapman1988/sleeping-dragon-hobby-shop`
* Press Enter to create the local clone.
* Any required **Python** dependencies should be installed locally using `$ pip install -r requirements.txt`.

For further information on *Cloning* a [GitHub](https://github.com/) repository, see the 
[GitHub Documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
</details>


## Credits


## Acknowledgements
