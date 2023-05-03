# Book Club
Developer: <a href='https://www.linkedin.com/in/omurilolima/' target='_blank'>Murilo Lima</a>
Visit the live site

 IMAGE with different screen sizes

This is my fourth milestone project for the Full-Stack Software Development Course at Code Institute / University College Dublin

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
    - Validation
    - Manual testing of user stories
    - Performing tests on various devices
    - Browser compatibility
- [Technologies Used](#technologies-used)
- [Configuration](#configuration)
    - Forking the GitHub Repository
    - Making a Local Clone
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
- Validation
- Manual testing of user stories
- Performing tests on various devices
- Browser compatibility

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

- Forking the GitHub Repository
- Making a Local Clone

Back to [top](#table-of-contents)

## Credits

Back to [top](#table-of-contents)

### Acknowledgements

Back to [top](#table-of-contents)