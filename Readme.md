# A BOOKSTORE WEBSITE BUILT WITH DJANGO AND DOCKER

---

## DESCRIPTION: A bookstore website where users can buy books, write reviews, add to wishlist... nothing much.
1. User Registration by email or by Google OAuth.
2. Email Verification is optional.
3. A wishlist is created for every user after sign up, with the help of Signals.
3. Genres of the bookstore are: 'comedy', 'horror', 'fiction', 'romance'
4. Users can add to their wishlist, add/delete from cart, create orders.
5. Users can pay for orders
6. Users can write and view reviews.

_Yeah, so that's basically everything about this project_

***

### TECHNOLOGIES AND LIBRARIES USED:

django = "==3.0.1"
psycopg2-binary = "==2.8.4"
django-crispy-forms = "==1.8.1"
django-allauth = "==0.41.0"
pillow = "==6.2.1"
djangorestframework = "==3.11.0"
django-utils-six = "*"
dj-rest-auth = "==1.0.4"
pyyaml = "==5.3"
drf-yasg = "==1.17.1"
whitenoise = "==5.0.1"
gunicorn = "==20.0.4"
flutterwave payment gateway
django-anymail
django-storages

***
### Challenges faced:
1. Marking orders as paid, by tring to get the order id
2. As of this moment of writing, haven't added an email transaction service. I had to host it first to get a domain name.
3. Cart session gave little issues.
4. Frontend pages, since I'm no frontend dev... used templates :)
5. Difficulty with setting up dropbox storage, which was later done


***



#### For Api Documentation:
1. With Sawgger:  [swagger](swagger/doc/)
2. With Redoc: [redoc](redoc/doc/)


