# Book Club
Developer: <a href='https://www.linkedin.com/in/omurilolima/' target='_blank'>Murilo Lima</a>

Visit the [live site](https://pp4-book-club.herokuapp.com/)

This is my fourth milestone project for the Full-Stack Software Development Course at Code Institute / University College Dublin

![Book-Club](/media/BookClub_readme_image.png)

## Table of Contents

- [Introdution](#introdution)
    - [Business goals addressed with this site](#business-goals-addressed-with-this-site)
    - [Customer needs](#customer-needs)
- [UX](#ux)
    - [Project goals](#project-goals)
    - [Ideal client](#ideal-client)
    - [Strategy](#strategy)
    - [User stories](#user-stories)
    - [Colour scheme](#colour-scheme)
    - [Typography](#typography)
    - [Images and Post Content](#images-and-post-content)
    - [Website pages](#website-pages)
    - [Wireframes](#wireframes)
- [Features](#features)
- [Database](#database)
- [Testing](#testing)
    - Code Validation
    - Manual testing of user stories
    - Performing tests on various devices
    - Browser compatibility
- [Technologies Used](#technologies-used)
- [Configuration](#configuration)
    - Forking the GitHub Repository
    - PostgreSQL Database
    - Deploy with Heroku
    - Pre Production Deployment
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Introdution

The Book Club is a comprehensive Django website specialized in books. There, users can create a profile and manage a personal catalogue of their reading Books. Also, the site has blog posts where readers can find content about books and interact adding a comment or liking a post.

### Business goals addressed with this site
- Build brand awareness;
- Prensent the business value proposition with high-quality content;
- Catch customer's attention and offer a good experience on managing their readings.

### Customer needs
- Understand the purpose of the Book Club;
- Interact with content about books;
- Manage their readings.

Back to [top](#table-of-contents)

## UX

### Project Goals

The primary goal of this project is to create an environment that enables full CRUD functionality to registered users, so that they can CREATE, READ, UPDATE and DELETE books directly on the site without intermediaries.

The second goal is to provide a blog in which registered users can read, like and comment.

### Ideal client
- English speaking;
- Has interest about books and reading;
- Want to create a list of their readinds.

### Strategy

 This project uses Agile Methodology. A Kanban board in GitHub was created to support the development process. A planning session generated 18 User Stories within 6 Epics, each one with their acceptance criterias. 2 of then was not implemented and they are listed in the "Features to Implement in the Future" session. The development process was based on iterative incremental philosophy, adopting 1 week sprints with the following goals:

- <strong>Week 1</strong>: Basic structure and blog features running with boilerplate design and content.
- <strong>Week 2</strong>: CRUD functionalities of Books section running with boilerplate design and content.
- <strong>Week 3</strong>: Final version of the design and content + Messages.
- <strong>Week 4</strong>: Testing, final deploy and documentation.

For more information: [View the Kanban Board here](https://github.com/users/omurilolima/projects/3).

Back to [top](#table-of-contents)

### User Stories
<strong>Epic: Account</strong>

1. As a User, I want to create my account so that I can comment, like and add my books.
2. As a returning user, I want to log in to the app to see my current books.
3. I want to be able to log out of my account
4. I want to see feedback messages to know that my book was created or edited successfully.

<strong>Epic: Admin</strong>

5. As a Site Admin, I want to create, read, update and delete posts so that I can manage my blog content.

<strong>Epic: Home page</strong>

6. As a User, I want to see the home page with the purpose of the site.
7. As a User, I want to view a list of posts so that I can select one to read.

<strong>Epic: Post</strong>

8. As a User, I want to read the full content of a post.
9. As a User, I want to view the number of likes on each post.
10. As a User, I want to like a post.

<strong>Epic: Comments</strong>

11. As a User, I want to view comments on a post.
12. As a User, I want to leave a comment on a post.

<strong>Epic: Book</strong>

13. As a User, I want to add a book to my bookshelf.
14. As a user, I want to see my books
15. As a User, I want to be able to edit my current book information.
16. I want to delete a book from my bookshelf.

Back to [top](#table-of-contents)

### Colour scheme

I used [mycolor.space](https://mycolor.space/) to choose a colour scheme that would be easily readable and visually appealing to users.

![Colour scheme](/media/mycolor.jpg)

### Typography

I used Google Fonts to select and import the font Poppins, including for main headers and the logo because it is modern but easily readable at the same time.

![Typography - Poppins font](/media/Poppins%20-%20Google%20Fonts.jpg)

### Images and Post Content

All the book images on the site were gathered on Amazon website.
The blog posts were oginaly published by [Bill Gates](https://www.gatesnotes.com/) on his personal blog.

Back to [top](#table-of-contents)

## Features

### Existing Features

<strong>Navbar:</strong>

The navbar is displayed in all the pages. On the left side you can find the logo with the name of the site and linked to the homepage. On the right side you can find the link to the main sections depending if you are logged in or not.

- Not logged in: Home, Login and Register.

![Navbar Not Logged](/media/bookClub_navbar.png)

- Logged in: Home, My Books, Add Books and Logout.

![Navbar Not Logged](/media/bookClub_navbar_logged.png)

The navbar is fully responsive. Therefore, when on smaller devices the it will collapse and the navigation links are accessed using a ”hamburger menu”.


![Navbar Not Logged](/media/bookClub_navbar_mobile.png)

<strong>Home Page:</strong>

The home page presents a main banner with the value proposition of the site (Discover new books and manage you reading list) and a button with a call to action to register. This banner only appears to not logged users.

There is also a section with the blog posts cards and a footer with the signature and social icons.

![Home Page](/media/bookClub_home.png)

<strong>Post:</strong>

The post details (or full post) features the title and image on top, followed by the author, date and the main content.

![Post details](/media/bookClub_postDetail.png)

<strong>Likes and Comments:</strong>

At the end of the blog post, the user can like the post or leave a comment, only if have logged in.

![Post details](/media/bookClub_postDetail_footer.png)

<strong>Add Books:</strong>

Through a simple form, the user can easily add books to their profile to manage their readings.

![Add Book](/media/BookClub_%20Add%20Book.png)

<strong>My Books:</strong>

On this page, the user can find all the books their add (books someone else added are not displayed). Each book is displayed on a card with some info. Every card has a button 'View details' which redirects the user to the Book details page. 

![My Books](/media/bookClub_Mybooksl.png)

<strong>Book details:</strong>

The book page show all the information about the book, including dates of start and end of the reading and the rating/score like stars. From there, the user can also edit the book info or delete the book. Before deleting, a pop-up is displayed for confirmation.

![Book details](/media/bookClub_bookDetail.png)

### Features to Implement in Future

- Contact form: Allows the user to send a message to the Site Admin [#18](https://github.com/omurilolima/book-club/issues/18)
- Delete account: Allows the user to delete their account [#15](https://github.com/omurilolima/book-club/issues/15)
- List 'My book' by status (reading, want to read, read).
- Add review to book info.
- Make 'My Books' public to allows user sharing their reading list with other users.

Back to [top](#table-of-contents)

## Wireframes

As part of the planning phase, before start the devopment, the wireframes for the main features were created using Figma. The wireframes were used to get a basic idea on how the site might look when finished.

### Home Page

![Home Page](/media/wireframe_home.png)


### Post Details

![Post details](/media/wireframe_post.png)

Back to [top](#table-of-contents)

## Database

The Book Club is hosted on Heroku and the database used is Heroku PostgreSQL. The images of the books and posts are hosted using Cloudinary.

Django User Model was used for creating the Post, Comment and Book models for the database. Below are the Entity-Relationship Tables:

### Post model
| Name | Type | Extra Info |
| --- | --- | --- |
| Title (Unique) | CharField | max_length=200, unique=True |
| Author | ForeignKey |  |
| Created_on | DateTimeField | auto_now_add=True |
| Updated date | DateTimeField | auto_now=True |
| Content | TextField |  |
| Featured Image | CloudinaryField | default='placeholder’ |
| Excerpt | TextField | blank=Tru |
| Likes | Many to many | related_name='blog_likes', blank=True |
| Slug | SlugField | max_length=200, unique=True |
| Status | Integer | STATUS = ((0, 'Draft'), (1, 'Published')) |


### Comment model
| Name | Type | Extra Info |
| --- | --- | --- |
| post | ForeignKey | Cascade on delete |
| name | CharField | Max length 80 |
| email | EmailField |  |
| body | TextField |  |
| created_on | DateTimeField | auto_now_add True |
| approved | BooleanField | default False |


### Book model
| Name | Type | Extra Info |
| --- | --- | --- |
| Title | CharField | max_length: 200 |
| Image_url | CharField | max_length: 200 |
| Slug | SlugField | max_length=200, unique=True |
| Author | CharField | max_length=80, unique=True |
| Status | integer | BOOK_STATUS = ((0, 'Read'), (1, 'Currently Reading'), (
2, 'Want to Read'), (3, 'Abandoned')) |
| Number of pages | Integer |  |
| Category | CharField | max_length: 80 |
| About | TextField |  |
| Rating | Integer | RATING = ((0, 'unread'), (1, 'Very bad'), (2, 'Bad'), (
3, 'Ok'), (4, 'Good'), (5, 'Very good')) |
| Date started reading | DateTimeField |  |
| Date finished reading  | DateTimeField | ` |
| created_on | DateTimeField | auto_now_add True |
| user | ForeignKey |  |

Back to [top](#table-of-contents)

## Testing

### HTML Code Validation

The W3C Markup Validation Service was used to validate the HTML of the website. All Django template tags were manually removed with the HTML code copied and inserted to the base template.

<details>
<summary><strong>base.html</strong> </summary>

![base.html](/media/Html_Checker.png)
</details>

<details>
<summary> <strong>add-book.html</strong></summary>

![base.html](/media/addbook_html_Checker.png)
</details>

<details>
<summary> <strong>book_detail.html</strong></summary>

![base.html](/media/book_detail_html_hecker.png)
</details>

<details>
<summary> <strong>books.html</strong></summary>

![base.html](/media/books_html_checker.png)
</details>

<details>
<summary> <strong>edit_books.html</strong></summary>

![base.html](/media/edit_book_html_checker.png)
</details>

<details>
<summary> <strong>index.html</strong></summary>

![base.html](/media/index_html_checker.png)
</details>

<details>
<summary> <strong>post_detail.html</strong></summary>

![base.html](/media/post_detail_html_hecker.png)
</details>

### CSS Code Validation

No errors were found when passing the CSS file through the The W3C CSS Validator.

<details>
<summary> <strong>CSS file validation results</strong></summary>

![base.html](/media/css_validator.png)
</details>

### Manual testing

| Test Label | Test Action | Expected Outcome | Test Outcome |
| --- | --- | --- | --- |
| Site loading | Navigate to the “home page”, “login”, “Register”, “Add a book”, “logout” and “My books” page. | All the pages and elements are loaded according. | PASS |
| Read a blog post | On the homepage, click on one of the cards presented in the “read our blog posts” section. | All the elements of post_detail are loaded according. | PASS |
| Leave a comment without logging | On the “post page”, without having logged in, go to the comment section. | A message informing that “To see the comments and leave a comment, please log in or create an account.” must be presented followed by the buttons “login” and “register”. | PASS |
| Leave a comment being logged in. | On the “post page”, having logged in, go to the comment section. Write some text and hit the “submit” button. | A message informing that “Your comment is awaiting approval” must be displayed. | PASS |
| Like a post | On the “post page”, click on the heart icon. | The counter of likes must increase by 1. | PASS |
| Add a book | On the navbar, click the “Add Books” option, fill out the form and hit the “Submit” button. | A success message must be displayed and the book must be listed on the “My books” page. | PASS |
| Edit a book | On the book page, click the “Edit” button, change some info on the form and hit the “Submit” button. | A success message must be displayed and the book info must be updated. | PASS |
| Delete a Book | On the book page, click the “Delete” button and click the “Delete” button in the confirmation popup. | The book must be deleted. | PASS |


### Browser Testing

I have tested this application works on the following installed browsers, using a Dell laptop on Windows OS:

- Microsoft Edge 112.0.1722.68
- Google Chrome Version 112.0.5615.138
- Firefox Browser 112.0.1

I have tested this application works on the following Android devices using Chrome browser 112.0.5615.138:

- Samsung Galaxy S20FE with Android 13.
- Samsung Galaxy S22 with Android 13.

### Responsiveness

I used Chrome developer tool to check the responsiveness on different screen sizes:
- 375px (Mobile)
- 728px (Tablet)
- 1024px (laptop)
- 4k (Monitor resolution)

### Automatic Testing

Django testing tools have been used to perform basic automatic testing on Book Club Python code for validating the main logical thing. Tests were run using the local SQLite3 database as opposed to the production PostgreSQL database.

Test scripts were written for the following blog app files;

models.py
views.py
forms.py

Those tests achieve 90% coverage. The results so far are highlighted in the summary report below:

![Coverage report](/media/Coverage%20report.png)

### Forms

| Test Label | Test Action | Expected Outcome | Test Outcome |
| --- | --- | --- | --- |
| BookForm - Title | Input empty value and click submit | Error message: “This field is required” | PASS |
| BookForm - Slug | Input empty value and click submit | Error message: “This field is required” | PASS |
| BookForm - Category | Input empty value and click submit | Error message: “This field is required” | PASS |
| BookForm - Image_url | Input empty value and click submit | No error message is displayed | PASS |
| BookForm - Fields displayed | Check if the 'title', 'slug', 'image_url',' author', 'number_of_pages', 'category',' about', 'status', 'rating', 'data_started_reading', and 'date_finished_reading', fields are explicit in comment metaclass | Only the listed fields in the test are shown for the user. | PASS |
| CommentForm - Body | Input empty value and click submit | Error message: “This field is required” | PASS |
| BookForm - Field displayed | Check if the body field is explicit in comment metaclass | Only the listed field in the test is shown for the user. | PASS |


### Views

| Test Label | Test Action | Expected Outcome | Test Outcome |
| --- | --- | --- | --- |
| Home | Testing load homepage | Page loaded with index.html template | PASS |
| Books page | Testing load books page | Page loaded with books.html template | PASS |
| Edit book | Testing edit a book | Book information id updated | PASS |
| Create Book | Testing create a book | Book is created | PASS |
| Delete Book | Testing delete a book | Book is deleted | PASS |

### Models

| Test Label | Test Action | Expected Outcome | Test Outcome |
| --- | --- | --- | --- |
| Comment | Creating a comment | __str__( ) method called by str() return the default f-string. | PASS |

Back to [top](#table-of-contents)

## Technologies Used

### Languages:

- HTML5
- CSS3
- Javascript
- Python

### Frameworks and Libraries

- [Bootstrap](https://getbootstrap.com/): Styling and responsiveness.
- [Cloudinary](https://cloudinary.com/): Hosting images.
- [Coverage](https://coverage.readthedocs.io/en/latest/index.html): Measuring automated test coding coverage.
- [Django](https://www.djangoproject.com/): Python web development framework.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html): Authentication and account registration.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Control the rendering behavior of Django forms.
- [Gunicorn](https://gunicorn.org/): Web Server to run Django on Heroku.
- [psycopg2](https://pypi.org/project/psycopg2/): PostgreSQL database adapter.
- [Summernote](https://github.com/summernote/django-summernote): To provide a WYSIWYG editor for add and customize blog content.

### Software and Web Applications

- [Figma](http://figma.com): Creating wireframes.
- [Git](https://github.com/omurilolima): Version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [Github](https://github.com/omurilolima): Store the projects code after being pushed from Git.
- [Gitpod](https://gitpod.io/): Cloud development environment.
- [Heroku](https://heroku.com/): Deployment and hosting of the application.
- [Heroku PostgreSQL](https://www.heroku.com/postgres): The database used for this application.
- [JSHint](https://jshint.com/): Javascript code validation.
- [Lighthouse](https://developer.chrome.com/docs/devtools/) Testing site performance on desktop and mobile devices.
- [My Color](https://mycolor.space/): Choosing a color pallete.
- [Notion](https://www.notion.so/): Documenting.
- [Pomodoro Tracker](https://pomodoro-tracker.com/): Measuring my effort.
- [W3C HTML](https://validator.w3.org/): HTML code valitadion service.
- [W3C CSS](https://jigsaw.w3.org/css-validator/): CSS code valitadion service.

Back to [top](#table-of-contents)

## Configuration

<details>
<summary><strong>Forking the GitHub Repository</strong></summary>

To fork this website to either propose changes or to use as an idea for another website, follow these steps:

If you haven't yet, you should first set up Git. Don't forget to set up authentication to GitHub.com from Git as well.
1. Navigate to the [Book Club](https://github.com/omurilolima/book-club) page on GitHub.
2. Click the 'Fork' button on the upper right part of the page. It's in between 'Watch' and 'Star'.
3. You will now have a fork of the Book Club repository added to your GitHub profile. Navigate to your own profile and find the forked repository to add the required files.
5. Above the list of forked files click the 'Code' button.
6. A drop-down menu will appear providing a choice of cloning options. Select the one which is applicable to your setup.

Further details can be found on GitHub's [Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) page.

To deploy locally with GitHub, follow these steps:

1. Log into your GitHub repository, create a GitHub account if necessary.
2. Click 'Settings' in the main Repository menu.
3. Click 'Pages' from the left-hand side navigation menu.
4. Within the Source section, click the "Branch" button and change from 'None' to 'Main'.
5. The page should automatically refresh with a url displayed.
6. Test the link by clicking on the url.


To push code using GitPod, following the steps:

1. With the application open, open the command line terminal (CLI).
2. Stage any changes using the command 'git add .' or by specifying the file with changes i.e 'git add settings.py'
3. Commit the changes to GitHub by adding a commit message describing the changes i.e. 'git commit -m "Update docbook dependency and generate epub".
4. Finally add the command 'git push' which will push all the code to GitHub.
5. Additionally if you would like to run the application locally pre/post any changes, from the terminal type 'python3 manage.py runserver'.
6. A dialog box should open asking you to open port 8000, click 'Open' and navigate to the opened tab/window which should allow you to view the running application.
7. If the dialog box does not automatically appear, find the 'Remote Explorer' section of the left hand navbar within GitPod and click on the port '8000' and the internet/globe icon to the right which should open the running application.
</details>

<details>
<summary><strong>PostgreSQL Database</strong></summary>

ElephantSQL replaced the originally selected free Heroku add-on PostgreSQL database due to the Heroku version becoming a chargeable service. Post MVP release I followed steps provided by the Code Institute to migrate the database from the Heroku version to Elephant. Dependant on your circumstances you may wish to use Heroku, Elephant or another service for your database.

1. If using Elephant, navigate to elephantsql.com and click 'Get a managed database today'. When presented with options for differing plans, I chose the free 'Tiny Turtle' plan.
2. Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account.
3. In the Create new team form:
    - Add a team name (your own name is fine).
    - Read and agree to the Terms of Service.
    - Select Yes for GDPR.
    - Provide your email address.
    - Click “Create Team”.
4. Your account should now be created.
5. Now you will need to create your database. Navigate to your elephantsql.com dashboard, and click "Create New Instance".
6. Set up your plan:
    - Give your plan a Name (this is commonly the name of the project).
    - Select the Tiny Turtle (Free) plan.
    - You can leave the Tags field blank.
7. Select a data center near you.
8. Click "Review".
9. Check your details are correct and then click "Create Instance".
10. Return to the ElephantSQL dashboard and click on the database instance name for this project.
11. You will return to this projects dashboard as part of the steps to 'Deploy with Heroku' as you will need the DATABASE_URL.
</details>

<details>
<summary><strong>Deploy with Heroku</strong></summary>

1. Log in to Heroku at https://heroku.com - create an account if needed.

2. From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.

3. On the Create New App page, enter a unique name for the application and select region. Then click Create app.

4. On the Application Configuration page for the new app, click on the Resources tab.

5. Next, click on Settings on the Application Configuration page and click on "Reveal Config Vars".

6. Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1, and click Add to save it. Remove this when releasing for Production.

7. Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols, and click Add to save it.

8. Add a new Config Var called DATABASE_URL and paste in the value for your ElephantSQL database, and click Add to save it.

9. The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :
```
DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

SECRET_KEY = os.environ.get('SECRET_KEY')
```
10. In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate

11. Update the requirements.txt file with all necessary supporting files by entering the command : 
```
pip freeze > requirements.txt
```
12. Commit and push any local changes to GitHub.

13. In order to be able to run the application on localhost, add SECRET_KEY and DATABASE_URL and their values to env.py

Connect GitHub Repo to Heroku App

1. Navigate to Application Configuration page for the application on Heroku and click on the Deploy tab.
2. Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter and search for the required repository, then click on Connect to link them up.
3. Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy.
4. The application can be run from the Application Configuration page by clicking on the Open App button.
5. Each time you push code from your GitHub Repo it will be automatically reflected in your Heroku App.

The url for this website can be found here https://pp4-book-club.herokuapp.com/
</details>

<details>
<summary><strong>Pre Production Deployment</strong></summary>

When the project be ready to move to production, the following steps must be taken to ensure your site works correctly and is secure.

In GitPod:

1. Set DEBUG flag to False in settings.py
2. Check the following line exists in settings.py to enable Summernote to work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
3. Update the requirements.txt file with all necessary supporting files by entering the command:
```
pip freeze > requirements.txt
```
In the Heroku App:

1. Go to Settings menu > Config Vars : Delete environment variable : DISABLE_COLLECTSTATIC
2. Go to Deploy menu: Click on deploy branch
</details>

Back to [top](#table-of-contents)

## Credits
### Code
In addition to the knowledge acquired in the [Professional Academy Diploma in Full Stack Software Development](https://www.ucd.ie/professionalacademy/findyourcourse/professional_diploma_in_software_development/) by [University College Dublin](https://www.ucd.ie/) and [Code Institute](https://codeinstitute.net/ie/), I also used the following sources to deal with specific points of this project:

- [Writing on Github](https://docs.github.com/en/get-started/writing-on-github)
- [Bootstrap Documentation](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- A Designer Who Codes
    - [Bootstrap 5 HORIZONTAL Cards](https://www.youtube.com/watch?v=1x6M8dvUJgU)
    - [Bootstrap 5 Navbar](https://www.youtube.com/watch?v=akXfF066MY0)
- [StackOverflow](https://stackoverflow.com/) for fixing date formating on models and forms

### Content

- All the icons were taken from [Font Awesome](https://fontawesome.com/icons).
- All the blog content was taken from the [GatesNotes](https://www.gatesnotes.com/)
- All the books content were taken from [Amazon Books](https://www.amazon.co.uk/books-used-books-textbooks/b?ie=UTF8&node=266239)
- README Documenting was inspired by [FishTales](https://github.com/mittnamnkenny/fishtales) and [FreshCats](https://github.com/RickofManc/fresh-casts)

Back to [top](#table-of-contents)

### Acknowledgements

- Thanks my mentor Brian Macharia for the guide and feedback throughout the project lifecycle.

- This project was inspired by my own experience of building digital products for tech companies as a Product Manager / Product Owner for the previous 10 years.

### Disclaimer
The content of this Website is for educational purposes only.

Back to [top](#table-of-contents)