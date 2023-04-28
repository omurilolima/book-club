# Book Club
Developer: <a href='https://www.linkedin.com/in/omurilolima/' target='_blank'>Murilo Lima</a>
Visit the live site

 IMAGE with different screen sizes

This is my fourth milestone project for the Full-Stack Software Development Course at Code Institute / University College Dublin

## Table of Contents

- Introdution
- User Goals
- Business goals addressed with this site
- Customer needs
- UX
    - Ideal client
    - User Stories
    - Colour scheme
    - Typography
    - Website pages
    - Wireframes
- Database
- Technologies Used
- Features
- Features to Implement in Future
- Testing
    - Validation
    - Manual testing of user stories
    - Performing tests on various devices
    - Browser compatibility
- Bugs
- Configuration
    - Forking the GitHub Repository
    - Making a Local Clone
- Credits
- Acknowledgements

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

## UX

### Project Goals

The primary goal of this project is to create an environment that enables full CRUD functionality to registered users so that they can CREATE, READ, UPDATE and DELETE books directly on the site without intermediaries.

The second goal is to provide a blog in which registered users can read, like and comment.

### Strategy

 This project uses Agile Methodology. A Kanban board in GitHub was created to support development process. A planning session generated 18 User Stories within 5 Epics, each one with their acceptance criterias. The development process was based on iterative incremental philosophy, adopting 1 week sprints with the following goals:
- <strong>Week 1</strong>: Basic structure and blog features running with boilerplate design and content.
- <strong>Week 2</strong>: CRUD functionalities of Books section running with boilerplate design and content.
- <strong>Week 3</strong>: Final version of the design and content + Messages.
- <strong>Week 4</strong>: Bugfix, final deploy and documentation.

For more information: View the Kanban Board here.

### Ideal client
- English speaking;
- Has interest about books and reading;
- Want to create a list of their readinds.

### User Stories
Epic: Account

1. As a User, I want to create my account so that I can comment, like and add my books.
2. As a returning user, I want to log in to the app to see my current books.
3. I want to be able to log out of my account
4. I want to see feedback messages to know that my book was created or edited successfully.

Epic: Admin

5. As a Site Admin, I want to create, read, update and delete posts so that I can manage my blog content.

Epic: Home page
6. As a User, I want to see the home page with the purpose of the site.
7. As a User, I want to view a list of posts so that I can select one to read.

Epic: Post

8. As a User, I want to read the full content of a post.
9. As a User, I want to view the number of likes on each post.
10. As a User, I want to like a post.

Epic: Comments

11. As a User, I want to view comments on a post.
12. As a User, I want to leave a comment on a post.

Epic: Book

13. As a User, I want to add a book to my bookshelf.
14. As a user, I want to see my books
15. As a User, I want to be able to edit my current book information.
16. I want to delete a book from my bookshelf.


### Colour scheme
I used [mycolor.space](https://mycolor.space/) to choose a colour scheme that would be easily readable and visually appealing to users.

![Colour scheme](/media/mycolor.jpg)

### Typography

![Typography - Poppins font](/media/Poppins%20-%20Google%20Fonts.jpg)

- Website pages
- Wireframes

## Database

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


- Technologies Used
- Features
- Features to Implement in Future
- Testing
    - Validation
    - Manual testing of user stories
    - Performing tests on various devices
    - Browser compatibility

## Automatic Testing

### Forms

| Test Label | Test Action | Expected Outcome | Test Outcome | Screenshot |
| --- | --- | --- | --- | --- |
| BookForm - Title | Input empty value and click submit | Error message: “This field is required” | PASS |  |
| BookForm - Slug | Input empty value and click submit | Error message: “This field is required” | PASS |  |
| BookForm - Category | Input empty value and click submit | Error message: “This field is required” | PASS |  |
| BookForm - Image_url | Input empty value and click submit | No error message is displayed | PASS |  |
| BookForm - Fields displayed | Check if the 'title', 'slug', 'image_url',' author', 'number_of_pages', 'category',' about', 'status', 'rating', 'data_started_reading', and 'date_finished_reading', fields are explicit in comment metaclass | Only the listed fields in the test are shown for the user. | PASS |  |
| CommentForm - Body | Input empty value and click submit | Error message: “This field is required” | PASS |  |
| BookForm - Field displayed | Check if the body field is explicit in comment metaclass | Only the listed field in the test is shown for the user. | PASS |  |

- Bugs
- Configuration
    - Forking the GitHub Repository
    - Making a Local Clone
- Credits
- Acknowledgements