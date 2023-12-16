# Suan Choi - She Codes News Project

## About This Project

- Create your own story, or simply allow others to write their story after creating their accounts. You can add, edit, delete stories and comment on others.

## How To Run This Code

- Clone this repo to your local machine
- Creating a virtual environment
- Migrate the database run by following command
  `python manage.py makemigration`
  `python manage.py migrate`
- Start development server
  `python manage.py runserver`

## Database Schema

![My ERD] (./she_codes_news/static/images/erm-diagram.png)

## Project Features

- [ ] Order stories by date
      ![order by date screenshot] (./she_codes_news/static/images/orderbydate.png)
- [ ] Styled "new story" form
      ![new story form screenshot] (./she_codes_news/static/images/newstoryform.png)
- [ ] Story images
      ![story image screenshot] (./she_codes_news/static/images/storyimage.png)
- [ ] Log-in/log-out
      ![login screenshot] (./she_codes_news/static/images/login.png)
      ![logout screenshots] (./she_codes_news/static/images/logout.png)
- [ ] "Account view" page
      ![account view screenshot] (./she_codes_news/static/images/myaccount.png)
- [ ] "Create Account" page
      ![create account screenshot] (./she_codes_news/static/images/createaccount.png)
- [ ] View stories by author
      ![stories by author screenshot] (./she_codes_news/static/images/storybyauthor.png)
- [ ] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user _is_ logged in
      _see log-in and log-out screenshots_
- [ ] "Create Story" functionality only available when user is logged in
      ![log in to create screenshot] (./she_codes_news/static/images/logintocreate.png)

## Additional Features:

- [ ] Add the ability to update and delete stories (consider permissions - who should be allowed to update or and/or delete stories).
  ![edit delete screenshot] (./she_codes_news/static/images/editdelete.png)
