![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Hand-Crafted Designs E-Commerce

![am i responsive](readme_images/ami-responsive.png)
[Live Site Here &#127760;](https://handcrafteddesigns.herokuapp.com/)
## Introduction

This project is a e-commerce store that provides an online platform for a local hand-crafted paper
artist to sell their products. My name is **Jose Guerra** and I developed this site as My Personal Portafolio Project 5 (PP5) of my [**Fullstack Web Development Diploma (with e-commerce applications**](https://codeinstitute.net/courses) with the [**Code Institute**](https://codeinstitute.net). The website is built using Django 3.2 and Bootstrap 4 for the front-end design, with Stripe for secure payment processing, Cloudinary for storage of static and media files, and is hosted on Heroku with
ElephantSQL for database storage.

---

### **Project Goal**

The goal of this project is to help the artist reach a wider audience and make their work more
accessible to customers. With this platform, customers can easily browse and
purchase the artist's products, and the artist can manage their sales and inventory through
a simple and user-friendly interface.

---

### **Table of Content**

- Use the sticky-menu above to easily navigate the readme file.
- ![readme navigation](readme_images/readme-menu-icon.png)

---

## **Project Business Model**

 This is a **B2C** Business to Customer e-commerce business model for selling handcrafted paper flower shadow boxes and with a Stripe payment gateway that provides a seamless shopping experience for customers while enabling the business to efficiently manage its operations and grow its customer base.

**Product Offering**: The e-commerce application will offer a range of handcrafted paper flower shadow boxes and cards in various designs and sizes to its customers. These products will be showcased on the website with high-quality images and detailed descriptions.

**Customer Acquisition**: The e-commerce application will use various marketing channels such as social media, email marketing, search engine optimization to attract potential customers to the website.

**Ordering Process**: Customers will be able to browse the product catalog, select the items they want to purchase, and add them to their cart. The ordering process will be easy to navigate and user-friendly. Once the customer is ready to checkout, they will be asked to provide their shipping information and payment details.

**Payment Gateway**: The e-commerce application will integrate with Stripe, a popular payment gateway that securely handles the payment process. Customers will be able to pay using various payment methods such as credit/debit cards, digital wallets, and bank transfers.

**Order Fulfillment**: Once the payment has been processed, the e-commerce application will notify the customer that their order has been received and is being prepared for shipment. The application will then handle the order fulfillment process, which includes packaging the product, generating a shipping label, and sending it to the carrier for delivery.

**Customer Support**: The e-commerce application will provide excellent customer support to ensure a positive shopping experience. Customers will be able to reach out to the support team via email for any inquiries or issues they may have with their order.

**Feedback and Reviews**: After receiving their order, customers will be encouraged to leave feedback and reviews on the e-commerce application's website. This feedback will help the business improve its products and services and attract new customers.

---

### **Note:**

When testing payments functionality in this project, use a card number,such as:

- **4242 4242 4242 4242** for successful payment or
- **4000 0027 6000 3184** for 3D secure authentication.
- Enter the card number in the payment form.
- Use a valid future date, such as 12/34.
- Use any three-digit CVC.
- Use any value you like for other form fields.

---

## Features

### **Navigation Bar**

- <details>
    <summary>The navigation bar is featured across all pages.</summary>

  Common navbar features:

  - Logo: Displays website brand name at the top left.
  - Search bar: The search bar allows users to easily find specific products.
  - My Account Icon: Dropdown menu to Login or Register.
  - Shopping Icon: Opens the Shopping cart page.
  - Menu:
    - Shop: Dropdown menu that sort products by price, category or all products.
    - Shadow Boxes: Displays a list of products of the shadow boxes category.
    - Cake Toppers: Displays a list of products of the cake toppers category.
    - Blog: Displays a list of blog articles.
    - Special Offers: Dropdown menu that sort products of the special offers category.
    - About: Provides information about the website.

  - ![main navbar](readme_images/main-navbar.png)

  For registered users:

  - My Profile: Provides a personalized overview of the user's account, including any recent activity or updates.
  - Wishlist: Display a the users wishlist products.
  - Logout: Allows the user to log out of their account.

  - ![navbar registered user](readme_images/main-navbar-registered-user.png)

  For authorize staff:

  - Product Management: Allows the user to create a new post.
  - My Profile: Provides a personalized overview of the user's account, including any recent activity or updates.
  - Wishlist: Display a the users wishlist products.
  - Logout: Allows the user to log out of their account.

  - ![navbar authorize staff](readme_images/main-navbar-authorize-staff.png)

- <details>
  <summary>Collapsed Navbar</summary>

  - ![navbar registered collapsed](readme_images/navbar-collapsed.png)

</details>

</details>

### **Home App**

- <details>
  <summary>Home Page</summary>

  - A Cover image welcome the user as they visit the site.
  - The call to action "SHOP NOW" button give the user a clear message on the purpose of site and goal of of the company.

  - ![home page](readme_images/homepage.png)

</details>

- <details>
    <summary>Contact Form</summary>

  Registered users that are logged in are allowed to contact the site owner via contact form.

  Form fields are:
  - Name
  - Email
  - Content

  - ![Contact form](readme_images/contact-form.png)

  Received email inbox detail

  - ![email inbox detail](readme_images/handcrafted-email-enquiry-png.png)

  </details>

- <details>
  <summary>About Page</summary>

  - Give the user an in depth information about how the company was conceived.

  - ![about page](readme_images/home-app-about-page.png)

</details>

- <details>
  <summary>FAQs Page</summary>

  - Question and answers are organized in an accordion component and answers user's frequently asked questions.

  - ![FAQs page](readme_images/faq-page.png)

</details>

### **Products App**

- <details>
  <summary>Product List Page</summary>

  - The list is displayed in cards and  will show an image of the product and details including name of the
    product, category, price and rating.
    The page has a pagination functionality in place displaying a set number of products per page for a better user
    experience.

  - ![products list  page](readme_images/produts-list-page.png)

</details>

- <details>
  <summary>Product Details Page</summary>

  - From the product list, by clicking on a product image or product name the user can access the Product
    Details page which will display the image, product name, price, category, average rating, description of a
    product, frame size dropdown menu, quantity input, add or remove from wishlist button, add to cart button.Below the user have the option to leave a review and rate the product.

  - ![products detail  page](readme_images/product-detail-page.png)

</details>

- <details>
  <summary>Product Edit Page</summary>

  - From the product list card or detail page authorized staff will have access to the edit product page.

  - ![edit product page](readme_images/edit-product-page.png)

</details>

- <details>
  <summary>Add Product Page</summary>

  - From My Account dropdown menu in the main navbar authorized staff will have access to the add product
  page by clicking in Product Management.

  - ![add product page](readme_images/add-product-page.png)

</details>

- <details>
  <summary>Delete a Product</summary>

  - From the product list card or detail page authorized staff will have access to the delete product
    confirmation page.

  - ![delete product page](readme_images/delete-product.png)

</details>

### **Cart App**

- <details>
  <summary>Add to Cart</summary>

  - From the product detail page when adding a product to the cart, a success message pops up
    with detail information about the product added,
    including the size, price, quantity of a product, amount to spend to get free delivery and
    secure checkout button.

  - ![add to cart toast](readme_images/cart-add-product.png)

</details>

- <details>
  <summary>Cart Page</summary>

  - The cart page will give the user a break down of all the products they have in their shopping cart,
    including the current quantity they wish to order, the user will also have the  ability to update the
    order quantity or remove a product from the cart entirely.

  - ![cart page](readme_images/cart-page.png)

</details>

### **Checkout App**

- <details>
  <summary>Checkout Page</summary>

  - Once in the secure checkout page, the user is presented with an order summary on the right,
    along with an order form where they have to fill in their details, name,    email address and
    delivery information. The user will have the option to save their delivery information to their
    profile (if they are signed in) or to login or create an account (if they are not signed in).

    Bellow the delivery information is the payment section for the user to enter their card details.
    At the bottom of page the user can complete or update their order by clicking in either complete order
    or adjust cart buttons.

    Order form and payment section are fully validated.

  - ![checkout page](readme_images/checkout-page.png)

</details>

- <details>
  <summary>Checkout Confirmation Page</summary>

  - After an order has been submitted and payment successfully processed, the user is shown a thank you page
    and a Confirmation Email with the order information will be sent to the user email address.

  - ![checkout success page](readme_images/checkout-success.png)

</details>

- <details>
  <summary>Order Confirmation Email</summary>

  - ![order confirmation email](readme_images/order-confirmation-email.png)

</details>

### **Profiles App**

- <details>
  <summary>My Profile Page</summary>

  - Registered users can save and update their default delivery information and order history.
    The profile information can easily be changed overwriting the pre-populated fields during the
    submission of an order or directly via the Profile Page.

  - ![my profile page](readme_images/profile-page.png)

</details>

### **Blog App**

- <details>
  <summary>Blog Article List</summary>

  - The list is displayed in cards and  will show the featured image of the article and title.
    The page has a pagination functionality in place displaying a set number of products per page for a better user
    experience.

  - ![blog article list](readme_images/blog-article-list-page.png)

</details>

- <details>
  <summary>Blog Article</summary>

  - From the blog article list, by clicking on an article image or title the user can access the Blog
    Article page which will display the image, title and article content.

  - ![blog article](readme_images/blog-article-page.png)

</details>

- <details>
    <summary>Blog Article Comment</summary>

  - Bellow the article registered users have the option to leave or delete a comment

  - ![blog article comment](readme_images/article-comment.png)

</details>

### **Search Functionality**

### **Stripe Payment Getaway**

- <details>
    <summary>Stripe Webhook</summary>

  - ![stripe webhook](readme_images/stripe-webhook-payment.png)

</details>

- <details>
    <summary>Stripe Events</summary>

  - ![stripe events](readme_images/stripe-events.png)

</details>

- <details>
    <summary>Stripe Endpoint</summary>

  - ![stripe endpoint](readme_images/stripe-endpoint-example.png)

</details>

### **WishList Functionality**

- <details>
    <summary>Product Wishlist</summary>

  - The product wishlist is displayed in cards and will show an image of the product and details
    including name of the product, category, price and rating.
    The user will have the option of removing the product from the wishlist or buying the product which will redirect the user to the product detail page.
    The page has a pagination functionality in place displaying a set number of products per page for a better user experience.

  - ![product wishlist](readme_images/product-wishlist.png)

</details>

### **Rate and Review Functionality**

- <details>
  <summary>Rate and Review Form</summary>

  - Authenticated users are allowed to leave a review and rate their favorite products.

  - ![product rate and review](readme_images/product-review-rate.png)

</details>

### **Footer**

The footer is featured across the application.

- <details>
    <summary>Footer</summary>

  For anonymous users:

  - Home: Takes the user to the homepage of the website.
  - Products: Display the products list page.
  - Blog: Displays a list of blog articles.
  - Sign in/Sign up: Allows users to create an account or log in to an existing account.
  - About: Provides information about the website.
  - Social links:
    - Facebook custom make account.
    - Github website repository.
    - Linkedin developer's account.
  - FAQs: Display a list of frequently asked questions.

  - ![footer anonymous user](readme_images/footer-anonymous-user.png)

  For registered users:

  - Home: Takes the user to the homepage of the website.
  - Profile: Provides a personalized overview of the user's account, including any recent activity or updates.
  - Products: Display the products list page
  - Wishlist: Display a list of the user's product wishlist.
  - Blog: Displays a list of blog articles.
  - Logout: Allows the user to log out of their account.
  - Social links:
    - Facebook custom make account.
    - Github website repository.
    - Linkedin developer's account.
  - About: Provides information about the website.
  - Contact: Users are allowed to send emails to the site's owner.
  - FAQs: Display a list of frequently asked questions.

  - ![footer registered user](readme_images/footer-registered-user.png)

</details>

---

### **Custom Error Pages**

Custom Error Pages are displayed in case an error occurs on client, server or database side. It provides a better user experience and give the user the ability to easily return to the shop area.
Each error page displays a specific error code in the title. The user can still use the main navbar to navigate or click the large button in the middle of the page to return to shop.

- 403 Forbidden Request
- 404 Page Not Found
  - <details>
    <summary>404 error page image</summary>

    ![404 error page](readme_images/404-page-not-found.png)

  </details>

- 405 Method Not Allowed
- 500 Internal Server Error
  - <details>
    <summary>500 error page image</summary>

    ![500 error page](readme_images/500-internal-server-error.png)

  </details>

---

### Future Features

- Account user registration using social media accounts such as Google, Facebook or Instagram.
- Discount coupons functionality within the checkout app.
- Recomendation system to recomend products based on previous purchases.

---

### **Wireframes**

- <details>
  <summary>Homepage wireframe</summary>

    ![homepage wireframe](readme_images/wireframes/wireframe-homepage.png)

  </details>

- <details>
  <summary>Product list wireframe</summary>

    ![product list wireframe](readme_images/wireframes/wireframe-product-list.png)

  </details>

- <details>
  <summary>Product detail wireframe</summary>

    ![product detail wireframe](readme_images/wireframes/wireframe-product-detail.png)

  </details>

- <details>
  <summary>Shopping Cart wireframe</summary>

    ![shopping cart wireframe](readme_images/wireframes/wireframe-shopping-cart.png)

  </details>

---
### **Database Diagram and Flowcharts**

- <details>
  <summary>dbDiagram</summary>

    ![database relationship diagram](readme_images/e-commerce-db-relationships.png)

  </details>

- <details>
  <summary>Admin / authorized staff flowchart</summary>

    ![admin / authorized staff flowchart](readme_images/ecommerce-admin-flowchart.png)

  </details>

- <details>
  <summary>Authenticated user flowchart</summary>

    ![authenticated user flowchart](readme_images/ecommerce-authenticated-flowchart.png)

  </details>

- <details>
  <summary>Unauthenticated user flowchart</summary>

    ![unauthenticated user flowchart](readme_images/ecommerce-unauthenticated-flowchart.png)

  </details>

---
## User Experience (UX)

### **User Stories**

- <details>
    <summary>Registration and User Accounts</summary>

    | User Story No. | AS A/AN | I WANT TO BE ABLE TO...  | SO THAT I CAN... |
    |---|---|---|---|
    |   |   | **Registration and User Accounts** |   |
    | 1 | Site User | register for an account | save my personal details information |
    | 2 | Site User | easily login and logout of my account | access my personal account information |
    | 3 | Site User | change or recover my password if I forget it | update or gain access to my account |
    | 4 | Site User | receive an email after registration |  verify that registration was succesful |
    | 5 | Site User | have a personal profile | save my payment information, my personal details and view my order history |

</details>

- <details>
    <summary>Viewing and Navigation</summary>

    | User Story No. | AS A/AN | I WANT TO BE ABLE TO...  | SO THAT I CAN... |
    |---|---|---|---|
    |   |   | **Viewing and Navigation** |   |
    | 6 | Buyer | view a list of products | select some to purchase |
    | 7 | Buyer | select individual product  | view more detail information |
    | 8 | Buyer | see items I have placed in my shopping cart easily | keep track of what I am buying |
    | 9 | Buyer | easily view the total of my purchases at any time | avoid spending too much |
    | 10 | Buyer | filter the products by categories | easily find the products I am looking for |
    | 11 | Buyer | view an about page | read about the store |
    | 12 | Site User | view a list of products in my wishlist | easily find the products I would like to purchase |
    | 13 | Site User | view a list of posts | select one to read the full text |
    | 14 | Site User | leave comments on a post | be involved in the conversation |
    | 15 | Site User | contact the site owner | make queries or ask question about the products |

</details>

- <details>
    <summary>Sorting and Searching</summary>

    | User Story No. | AS A/AN | I WANT TO BE ABLE TO...  | SO THAT I CAN... |
    |---|---|---|---|
    |   |   | **Sorting and Searching** |   |
    | 16 | Buyer |  sort the available products | easily identify the best priced and best rated products |
    | 17 | Buyer |  sort a category of products | easily identify the best priced and best rated products of a category |
    | 18 | Buyer |  search for a product by name, type or category | easily find what I am searching for |
    | 19 | Buyer |  see how many products are in the search results | quickly view if the product I want is available |

</details>

- <details>
    <summary>Purchasing and Checkout</summary>

    | User Story No. | AS A/AN | I WANT TO BE ABLE TO...  | SO THAT I CAN... |
    |---|---|---|---|
    |   |   | **Purchasing and Checkout** |   |
    | 20 | Buyer |  easily select the quantity of a product | add the right amount of a product to my shopping cart |
    | 21 | Buyer |  see the items in my shopping cart | identify the items, the total, the delivery cost and the grand total |
    | 22 | Buyer |  easily update the items in the shopping cart | change the quantities or delete the products from my cart  |
    | 23 | Buyer |  easily enter my payment information at checkout | safely make a purchase |
    | 24 | Buyer |  receive an email confirmation after checking out | verify my purchase was correct and keep confirmation for my records |

</details>

- <details>
    <summary>Admin and Store Management</summary>

    | User Story No. | AS A/AN | I WANT TO BE ABLE TO...  | SO THAT I CAN... |
    |---|---|---|---|
    |   |   | **Admin and Store Management** |   |
    | 25 | Admin / Owner |  add a product | add a new item to my store |
    | 26 | Admin / Owner |  edit or update a product | change the price, the description or the image of products |
    | 27 | Admin / Owner |  delete a product | delete items no longer for sale |
    | 28 | Admin / Owner |  create a post  | add content to the blog |
    | 29 | Admin / Owner |  edit or update a post I created | I can make changes or delete a post |
    | 30 | Admin / Owner |  approve or disapprove comments | I can filter out objectionable comments |
    | 31 | Admin / Owner |  send email to subscribers | send information about new products or new posts related to the business |

</details>

- <details>
    <summary>SEO and WeB Marketing</summary>

    | User Story No. | AS A/AN | I WANT TO BE ABLE TO...  | SO THAT I CAN... |
    |---|---|---|---|
    |   |   | **SEO and WeB Marketing** |   |
    | 32 | Site User | subscribe to a Newsletter | receive the latest news and offers from the store |

</details>

---

### **Colours**

- <details>
  <summary>Complementary colours palette</summary>

   Purple was chosen as the main colour to use throughout the project because it is associated with creativity.
   Golden colour is used as the main accent colour transmiting luxury, achievement and success.

  ![complementary color palette](readme_images/color-scheme.png)
  [https://colors.muz.li/palette/8860d0/544a92/e4e0ff/d0b360/927d43](https://colors.muz.li/palette/8860d0/544a92/e4e0ff/d0b360/927d43)

</details>

- <details>
  <summary>Typography colour palette</summary>

  Typography is based on the main theme colour, mix with black and with progressive decresed opacity.

</details>

### **Typography**

- <details>
  <summary>Montserrat font</summary>

  - The main font used for this project is [Montserrat](https://fonts.google.com/specimen/Montserrat). The old posters and signs in the traditional Montserrat neighborhood of Buenos Aires inspired Julieta Ulanovsky to create this font in 2010. It is a sans serif font with excellent readability.

  </details>

---

## Technologies

### **Languages**

- [Python3](https://www.python.org/)
  - Used to create the main application functionality
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - Used to create the interactive functionality of the website

### **Frameworks and Libraries**

- <details>
    <summary>List of Frameworks and Libraries</summary>

  - [Django:](https://www.djangoproject.com/)
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
  - [Bootstrap:](https://getbootstrap.com/)
    - The world’s most popular framework for building responsive, mobile-first sites.
  - [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html)
    - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
  - [Stripe](https://stripe.com/en-gb)
    - Online payments platform used for the shopping basket functionality.
  - [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Crispy Forms let you control the rendering behavior of your Django forms in a very elegant and DRY way.
  - [psycopg2:](https://pypi.org/project/psycopg2/)
    - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
  - [dj_database_url:](https://pypi.org/project/dj-database-url/)
    - This simple Django utility allows you to utilize the [12factor](https://www.12factor.net/backing-services) inspired DATABASE_URL environment variable to configure your Django application..
  - [dj3-cloudinary-storage:](https://cloudinary.com/)
    - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
  - [Gunicorn:](https://gunicorn.org/)
    - Green Unicorn, used as the Web Server to run Django on Heroku.
  - [Summernote:](https://github.com/summernote/django-summernote)
    - To provide a WYSIWYG editor for customizing new products description, blog content and add images.
  - [Pillow:](https://pillow.readthedocs.io/en/stable/)
    - The Python Imaging Library adds image processing capabilities to your Python interpreter.
  - [Coverage:](https://coverage.readthedocs.io/en/latest/index.html)
    - Used for measuring code coverage of Python test files. -->
  - [Jest:](https://jestjs.io/docs/28.x/getting-started)
    - A delightful JavaScript Testing Framework, used for automated tests.
  - [Mixer](https://mixer.readthedocs.io/en/latest/quickstart.html#django-orm)
    - Mixer is an object generation tool used for testing.

</details>

### **Software and Web Applications**

- <details>
    <summary>List Software and Web Applications</summary>

  - [Am I Responsive:](http://ami.responsivedesign.is)
    - Checking the responsiveness.
  - [Code Beautify:](https://codebeautify.org/)
    - Used to beautify html code.
  - [Balsamiq:](https://balsamiq.com/)
    - Used to create the wireframes.
  - [Chrome DevTools:](https://developer.chrome.com/docs/devtools/)
    - Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze page load.
  - [Font Awesome:](https://fontawesome.com/)
    - Used throughout the site to add icons for aesthetic and UX purposes.
  - [Git:](https://git-scm.com/)
    - Git open source software for distributed version control.
  - [GitHub:](https://github.com/)
    - Internet hosting service for software development and version control using Git.
  - [Cloudinary:](https://cloudinary.com/)
    - Used to store the application static files, images and uploaded images.
  - [Google Fonts:](https://fonts.google.com/)
    - Used to import fonts family [Montserrat](https://fonts.google.com/specimen/Montserrat+Alternates) which is used as main font throughout the site and [Lato](https://fonts.google.com/specimen/Lato) font used for headings.
  - [Heroku:](https://www.heroku.com/)
    - For deployment and hosting of the application.
  - [Elephant PostgreSQL:](https://www.elephantsql.com/)
    - The database used for this application.
  - [HTML Validator:](https://validator.w3.org/)
    - Check your code for HTML validation.
  - [JSHint:](https://jshint.com/)
    - Check code for JavaScript validation.
  - [CI Python Linter](https://pep8ci.herokuapp.com/)
    - Check code for python pep8 validation.
  - [Tiny PNG:](https://tinypng.com/)
    - Compressing images to smaller sizes.
  - [Unsplash:](https://unsplash.com/photos/NtkCemIfaiU)
    - Stock images.
  - [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/)
    - Check your code for CSS validation.
  - [Gauger:](https://gauger.io/fonticon/)
    - Used to create the favicon Logo, create beautiful favicon with ease.
  - [Contrast Checker](https://webaim.org/resources/contrastchecker/)
    - Tool to check the contrast ratio.
  - [xml sitemaps](https://www.xml-sitemaps.com/)
    - Used to create the xml sitemap.
  - [dbdiagrams.io](https://dbdiagram.io/home)
    - Used to create the database entity-relationship diagram.
  - [animate.css](https://animate.style/)
    - Animations
  - [Muzli Colors](https://colors.muz.li/)
    - Color palette

</details>

---

## **Installing The Project In Your Local Machine**

### Prerequisites

You will need the following software installed on your local machine:

- Python 3
- Django 3.2
- Bootstrap 4
- Stripe
- Heroku CLI
- ElephantSQL

- <details>
  <summary>Clone the repository to your local machine:</summary>

  - To clone a repository from GitHub, you will need to have Git installed on your computer. If you don't already have Git installed, you can download it from the [official website](https://git-scm.com/).

  - Once you have Git installed, open a terminal window and navigate to the location where you want to store the repository on your local machine. Then, use the following command to clone the repository:

          git clone https://github.com/USERNAME/(your_repository_name).git <where to clone> ( Note: replace <where to clone> with  .  and will clone it in the actual directory )

  Change into the project directory:

      cd (your_repository_name)

  Set up a virtual environment and activate it:

      python3 -m venv venv
      source venv/bin/activate

  Install the required packages:

      pip install -r requirements.txt

  Apply the migrations:

      python manage.py migrate

  Run the development server:

      python manage.py runserver

  Open a web browser and navigate to http://localhost:8000 to view the e-commerce store.

  </detail>

### **Project Setup**

- <details>
    <summary>To Setup a new Django Project, follow these steps:</summary>

  - To **Create a GitHub repository**, follow these steps:
    - Go to GitHub and log in to your account.
    - Click on the "`Repositorie's`" button and then click on the "`New`" button.
    - Enter a name for your repository and a description (optional).
    - Choose whether you want your repository to be public or private.
    - Click on the "`Create repository`" button.
    - Click the "`Gitpod`" button to create a workspace in gitpod.
  - To **initialize the new Git repository** if necessary, follow the these steps:
    - Once the workspace is open, navigate to your project's root directory.
    - Run the following command to initialize a new Git repository:

            git init
    - Run the following command to add the GitHub repository as a remote:

            git remote add origin [GitHub repository URL]
    - Run the following command to create the first commit:

            git add .
            git commit -m "Initial commit"

    - Run the following command to push the initial commit to the GitHub repository:

            git push -u origin main
    Your Django project is now under version control using Git and GitHub.

  - **Step 1** Create a Django Project:
    - Install Django using the command: (`$ pip3 install django==3.2`)
    - Create a Django project using the command: (`$ django-admin startproject [projectname eg: ecommerce] .`)  # using "." after the project name creates the project in the current directory
    - Create a basic gitignore file by typing: (`$ touch .gitignore`)
      - add the following:

            *.sqlite3 
            *.pyc
            __pycache__ (compile python code)
            env.py

    - Navigate into the project directory: (`$ cd ecommerce`)
    - Run the development server:(`$ python manage.py runserver`)
    - Open a web browser and navigate to http://localhost:8000 you’ll see a “Congratulations!” page, with a rocket taking off. It worked!
    - Set up the database running the command: (`$ python3 manage.py migrate`)
    - Create a superuser to access the admin panel using the command: (`$ python3 manage.py createsuperuser`)
    - Generate a new SECRET_KEY using this shell command:

            from django.core.management.utils import get_random_secret_key

            get_random_secret_key()

            output "my_new_secret_key" 

    - Create a env.py file using the command (`$ touch env.py`)
    - Add SECRET_KEY to env.py file:

            import os

            os.environ("SECRET_KEY") = "my_new_secret_key"

    - In the `settings.py` file of your project, add the following code:

            import os
            if os.path.isfile("env.py"):
              import env

            SECRET_KEY = os.environ.get('SECRET_KEY', "")
    - Commit and Push your changes to Github.
  - Once you have your project set up, to **create a new app within the project**, follow these steps:
    - Run the following command to create a new Django app:

        `$ python3 manage.py startapp [appname eg: home]`

    - Create a new directory called `templates` within your `home` app,
    then create a new directory called `home` within templates directory:

        `$ mkdir -p home/templates/home`  # make directory (mkdir), create parents as required (-p)

    - Create a new file called `index.html` within the `templates/home` directory:

      `$ touch home/templates/home/index.html`
    - Add the following code to the index.html file:

            <h1>Welcome to the home app</h1>
    - In the (`settings.py`) file of your project, add the app `home` to the INSTALLED_APPS list:

            INSTALLED_APPS = [
              # ...
              'home',
            ]
    - In the (`urls.py`) file of your project, add the following code to create a basic URL configuration:

            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('home.urls')),
            ]
    - Create a file called `urls.py` within your `home` app.

          `$ touch home/urls.py`
    - In the (`urls.py`) file of your `home` app, add the following code to create a basic URL configuration:

            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.index, name='index'),
            ]
    - In the (`views.py`) file of your `home` app, add the following code to create a basic view:

            from django.shortcuts import render

            def index(request):
                return render(request, 'home/index.html')

    - In the `settings.py` file of your project, add the following code to configure Django to use the templates directory:

            TEMPLATES = [
            {
                ...
                'DIRS': [os.path.join(BASE_DIR, 'templates')],
                ...
            },
        ]
    - Run the development server:(`$ python manage.py runserver`)
    - Open a web browser and navigate to http://localhost:8000 you'll see `Welcome to the home app`
    - Repeat these steps for each functional area of your application, such as the home, products, cart, checkout, profiles, and blog.
  - **Step 2** Creating Models

    - Models in Django are used to define the structure of the data that will be stored in your database.
    For this e-commerce application, you'll need to create models for products, carts, orders, and other data related to your e-commerce functionality.
    - Example of how to create a basic `Product` model:
      - Open the `models.py` file in the `products app` directory.
      - Import the necessary modules:

              from django.db import models
      - Define the Product model:

              class Product(models.Model):
                  name = models.CharField(max_length=254)
                  description = models.TextField()
                  price = models.DecimalField(max_digits=6, decimal_places=2)
                  image = models.ImageField(upload_to='media/images')
                  
                  def __str__(self):
                      return self.name
        - Save the changes to the `models.py` file and close it.
        - Run the following command to create the database tables for the models:

                python manage.py makemigrations
        - Run the following command to apply the migrations:

                python manage.py migrate
  - **Step 3** Define views and templates:
    - Views are Python functions that handle HTTP requests and return an HTTP response.
    They are responsible for querying the database for the data required by the page, processing that data, and passing it to a template for rendering.
    Templates are HTML files with placeholders for the dynamic data that will be filled in by the views.
    - For this e-commerce application, you'll need to create views to display product listings, product details, the shopping cart, and the checkout process.
    - Example of how you can create a basic view to display a `list of products`:
      - Open the `views.py` file in the `product app` directory
      - Import the necessary modules:

              from django.shortcuts import render
              from .models import Product
      - Define the view:

              def product_list(request):
                  """ A view to show all products """
                  products = Product.objects.all()
                  template = 'products/product_list.html'
                  context = {'products': products}
                  return render(request, , template, context)

      - Create a new directory called `templates` within your `products` app,
      then create a new directory called `products` within templates directory and
      create a new file called `product_list.html` within the `templates/products` directory.
      (`products/templates/products/product_list.html`)
      Add the following code to the product_list.html file:

            {% for product in products %}
              <h2>{{ product.name }}</h2>
              <p>{{ product.description }}</p>
              <p>{{ product.price }}</p>
              <img src="{{ product.image.url }}" alt="{{ product.name }}">
            {% endfor %}
      - Save the changes to the `product_list.html` file and close it.
      - Open the `urls.py` file in the `ecommerce app` directory.

              from django.contrib import admin
              from django.urls import path, include

              urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('products.urls')),
              ]

      - In the (`urls.py`) file of your `products` app, add the following code to create a basic URL configuration:

            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.product_list, name='products'),
            ]
      - Repeat these steps to create additional views and templates for your e-commerce application,
      such as product detail pages, shopping cart, and checkout process , profiles and blog.

</details>

---

### **Setting Up Django-Allauth for registration and authentication**

- <details>
    <summary>To Install django-allauth, follow these steps:</summary>
  
  - Install Python package:

          `$ pip3 install django-allauth==0.41.0`

  - In the `settings.py` file of your project, add the following code:

            TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    ...
                    # path to `allauth` templates 
                    os.path.join(BASE_DIR, "templates/allauth"),
                    ...
                    ],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        ...
                        # required by `allauth`
                        'django.template.context_processors.request',
                        ...
                    ],
                },
            },
          ]

            AUTHENTICATION_BACKENDS = [
            # Needed to login by username in Django admin, regardless of `allauth`
            'django.contrib.auth.backends.ModelBackend',

            # `allauth` specific authentication methods, such as login by e-mail
            'allauth.account.auth_backends.AuthenticationBackend',
          ]

            INSTALLED_APPS = [
              ...
              # The following apps are required:
              'django.contrib.auth',
              'django.contrib.messages',
              'django.contrib.sites',

              'allauth',
              'allauth.account',
              'allauth.socialaccount',
            ]
  - In the `urls.py` file of your project, add the following code:

          import include

          urlpatterns = [
          ...
          path('accounts/', include('allauth.urls')),
          ...
          ]
  - In your Django project root execute the command below to create the allauth database tables:

          python manage.py migrate

  - Add Development email backend to `setting.py`:

          EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

          ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
          ACCOUNT_EMAIL_REQUIRED = True
          ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
          ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
          ACCOUNT_USERNAME_MIN_LENGTH = 4
          LOGIN_URL = '/accounts/login/'
          LOGIN_REDIRECT_URL = '/'

  - Add Allauth templates to the project templates directory:
    - In the project root directory execute the following commands:

          mkdir templates
          mkdir templates/allauth
    - To make a copy of the allauth templates from the python site packages module into your templates/allauth directory we just created by running the following command:

          `$ cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/`  # copy (cp) recursively (-r) all (*) allauth templates into the root templates/allauth directory

</details>

---

### **Setting Up ElephantSQL as Database**

- <details>
    <summary>To Set Up ElephantSQL as Database, follow these steps:</summary>

  - Go to the [ElephantSQL website](https://www.elephantsql.com/) and create an account if you haven't do so already.

  - Log in to ElephantSQL.com to access your dashboard.

  - After creating an account, you will be able to create a new PostgreSQL database,  click "`Create new instance`".

  - Set up your plan
    - Give your plan a Name (this is usually the name of the project)
    - Select the Tiny Turtle (Free) plan
    - You can leave the Tags field blank

  - Select a region and data center near you eg:(EU-West-1 (Ireland)).

  - Then Click "`Review`"

  - Check your details are correct and then click “`Create instance`”

  - Once the database is created, you will see the database details page. Here, you can find the connection details for your database,
  including the hostname, port, database name, and username.

  - To connect to the database, you will need a PostgreSQL client. There are many different clients available, such as pgAdmin and psql.
  Choose a client and follow the instructions to connect to your database using the connection details provided.

  - Once you are connected to the database, you can start creating tables and inserting data. You can also use SQL commands to manage
  and query the data in your database.

</details>

---

### **Set Up Cloudinary**

- <details>
    <summary>To Set Up Cloudinary to host images and static files used by the application</summary>

  - Sign up for a Cloudinary account at https://cloudinary.com/users/register/free.

  - After you have signed up, you will be taken to the dashboard. In the dashboard, click on the "Settings" tab and then click on the "Security" tab.

  - In the "Security" tab, you will see your "Cloud Name", "API Key", and "API Secret". These will be needed later to authenticate your Django application with Cloudinary.

  - Install the Cloudinary Python library by running the following command:

        pip install dj3-cloudinary-storage
        pip install cloudinary

  - Add the following code to your Django settings file to configure the Cloudinary library with your account credentials:

        CLOUDINARY_CLOUD_NAME = "your_cloud_name"
        CLOUDINARY_API_KEY = "your_api_key"
        CLOUDINARY_API_SECRET = "your_api_secret"

  - Log in to Heroku and go to the Application Configuration page for the application. Click on Settings and click on the "Reveal Config Vars" button and add the following:
  
        CLOUDINARY_URL = "cloudinary://CLOUDINARY_API_KEY:CLOUDINARY_API_SECRET@CLOUDINARY_CLOUD_NAME"

  - Add the Cloudinary library to your Django project by adding 'cloudinary_storage' and 'cloudinary' to the INSTALLED_APPS list in your Django settings file:

        INSTALLED_APPS = [    
            ...
            'cloudinary_storage',
            'django.contrib.staticfiles',
            'cloudinary',
            ...
            ]

  - Run the following command to apply the changes to your Django project:

        python manage.py migrate

  - You are now ready to use Cloudinary in your Django project. To use Cloudinary to manage and serve your  media files, you can use the CloudinaryField field in your Django models.

  - For example, to create a model with a Cloudinary image field, you can do the following:

        from django.db import models
        from cloudinary.models import CloudinaryField

        class MyModel(models.Model):

        name = models.CharField(max_length=255)
        image = CloudinaryField('image')

  - You can then use the image field just like any other Django field to store and retrieve images from Cloudinary.

</details>

---

### **Setting Up Gmail as Django mail backend**

- <details>
    <summary>To Set Up Gmail as Django mail backend, follow these steps:</summary>

  - Install the django-email-backend package by running the following command:

          pip install django-email-backend

  - In your Django settings file (typically settings.py), add the following lines to configure the email backend:

          EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
          EMAIL_HOST = 'smtp.gmail.com'
          EMAIL_PORT = 587
          EMAIL_USE_TLS = True
          EMAIL_HOST_USER = 'your-gmail-username@gmail.com'
          EMAIL_HOST_PASSWORD = 'your-gmail-password'

  - Make sure that you have enabled "Less secure app access" in your Gmail account settings. To do this, go to your Google Account settings, click on "Security" and then scroll down to "Third-party apps with account access." Make sure that "Allow less secure apps" is turned on.

  - Test the email backend by sending a test email from your Django application. You can do this by using Django's built-in send_mail function, like this:

          from django.core.mail import send_mail

          send_mail(
          'Subject here',
          'Here is the message.',
          'from@example.com',
          ['to@example.com'],
          fail_silently=False,
          )

  - If everything is set up correctly, this should send a test email to the specified address using your Gmail account as the email backend.

</details>

---

### **Setting Up Search Functionality**

- <details>
  <summary>Adding Search Functionality</summary>
  - Import the `Q class` from the `django.db.models` module in your `products` views.py file:

          from django.db.models import Q

  - Create a search view to handle search requests:

          def search(request):
          """
          Search for a product based on a search query
          """
          query = request.GET.get("query", "")

          if query:
              products = Product.objects.filter(
                  Q(name__icontains=query) |
                  Q(description__icontains=query) |
                  Q(category__name__icontains=query) 
              )
          else:
              products = []

          template = "products/product/search.html"
          context = {
              "query": query,
              "products": products,
              }

          return render(request, template, context)
    - In the `base.html` template add a search form to the top of the page:

            <form action="{% url 'search' %}" method="get">
              <input type="search" name="query" placeholde="Find a product...">
              <button type="submit">Search</button>
            </form>

    - In the (`urls.py`) file of your `products` app, add the following code to create a basic URL configuration:

        from django.urls import path
        from . import views

        urlpatterns = [
            path('search/', views.search, name='search'),
        ]

  - create a new file called `search.html` within the `templates/products` directory.
  (`products/templates/products/search.html`)
  Add the following code to the `search.html` file:

            {% for product in products %}
              <h2>{{ product.name }}</h2>
              <p>{{ product.description }}</p>
              <p>{{ product.price }}</p>
              <img src="{{ product.image.url }}" alt="{{ product.name }}">
            {% endfor %}

</details>

---

### **Setting Up Pagination Functionality**

- <details>
  <summary>Add pagination to the `product list view`</summary>
  - To do this, you'll need to import the `Paginator class` and `PageNotAnInteger` from the `django.core.paginator` module:

          from django.core.paginator import Paginator, PageNotAnInteger

  - In the product_list view, modify the code to add pagination:

          def product_list(request):
          """ 
          A view to show all products, and pagination functionality 
          """
              products = Product.objects.all()
              paginator = Paginator(products, 6)
              page_number = request.GET.get('page')
              try:
                  page_obj = paginator.get_page(page_number)
              except PageNotAnInteger:
                  page_obj = paginator.get_page(1)

              template = 'products/product_list.html'
              context = {
                'products': products,
                'page_obj': page_obj,
                }
              return render(request, , template, context)
    - In this code, we create a Paginator object with the products queryset and specify that we want to display 6 products per page.
    The current page number is retrieved from the GET parameters in the request. The get_page() method is used to retrieve the current page of products.

  - In the product_list.html template, update the code to display the paginated products:

          {% for product in products %}
            <h2>{{ product.name }}</h2>
            <p>{{ product.description }}</p>
            <p>{{ product.price }}</p>
            <img src="{{ product.image.url }}" alt="{{ product.name }}">
          {% endfor %}
          {% with page_obj=prducts %}
            <div class="pagination">
              <a href="?page=1"><<</a>
              <a href="?page={{ page_obj.previous_page_number }}"><</a>
              <a href="?page={{ page_obj.number }}">{{ page_obj.number }}</a>
              <a href="?page={{ page_obj.next_page_number }}">></a>
              <a href="?page={{ page_obj.paginator.num_pages }}">>></a>
            </div>
          {% endwith %}
    - The pagination links are created by using the previous_page_number, next_page_number, number, and paginator.num_pages attributes of the page_obj object.

</details>

---

### **Deployment to Heroku**

- <details>
    <summary>To deploy the Django app with ElephantSQL to Heroku, follow these steps:</summary>

  - Set up a database with [Elephantsql](https://www.elephantsql.com/docs/index.html) - ([follow the instructions above](#setting-up-elephantsql-as-database))
  - Sign up for a Heroku account or log in if you already have one.
  - Click the "`New`" button in the top right corner of the dashboard and select "`Create new app`".
  - Choose a unique name for your app, select region (for example, United States or Europe) and click on `Create App`
  - In Heroku under the `Settings` tab click `Reveal Config Vars`  
    - Add all the environmant variables from your local `.env` file into the Heroku Config Vars:

      | Key | Value |
      | --- | --- |
      | SECRET_KEY | [YOUR SECRET KEY] |
      | CLOUDINARY_URL | [YOUR CLOUDINARY URL] |
      | STRIPE_PUBLIC_KEY | [YOUR STRIPE PUBLIC KEY] |
      | STRIPE_SECRET_KEY | [YOUR STRIPE SECRET KEY] |
      | STRIPE_WH_SECRET | [YOUR STRIPE WEBHOOK SECRET KEY] |
      | DATABASE_URL | [YOUR POSTGRESQL DATABASE URL] |
      | EMAIL_HOST_PASS | [YOUR GMAIL APP SIGN IN PASSWORD] |
      | EMAIL_HOST_USER | [YOUR ORDER CONFIRMATION EMAIL ADDRESS FROM GMAIL]

  - In your IDE terminal if you haven't do so:
    - Install [dj_database_url](https://pypi.org/project/dj-database-url/) and [psycopg2](https://pypi.org/project/psycopg2/) (`$ pip3 install dj_database_url==0.5.0 psycopg2`)
    - Create `requirements.txt` (`$ touch requirements.txt`)
    - Install the required packages (`$ pip3 install -r requirements.txt`)
    - Pip freeze the installed packages (`$ pip3 freeze --local > requirements.txt`)
    - In your `settings.py` file, import dj_database_url underneath the import for os
    - Connect the new DATABASE as follow:

          DATABASES = {
            default': dj_database_url.parse('DATABASE_URL')
          }
    - Migrate your database models to your new database (`$ python3 manage.py migrate`)
    - Load in the fixtures. We need to load categories first (`$ python3 manage.py loaddata categories`)
    - Then products, as the products require a category to be set (`$ python3 manage.py loaddata products`)
    - Create a superuser for your new database (`$ python3 manage.py createsuperuser`)
    - Create a `Procfile` (`$ echo web: gunicorn <app_name>.wsgi > Procfile`)
    - Create an env.py file and add all your environment variables.
    - Create a .gitignore file and add your env.py files
    - Set DEBUG to `False`
  - Commit and Push your changes to Github.
  - In Heroku `Deploy` Tab, the `deployment method` select Github,
    scroll down to Manual or Automatic deploy and deploy branch.
  - Once the build is complete, click on `Open App`

</details>

---

### **Web Marketing**

- <details>
    <summary>Newsletter Functionality</summary>

    As part of the web marketing strategy, a newsletter subscription functionality powered by
    [Mailchimp](https://mailchimp.com/) is provided.

  - ![newsletter form](readme_images/newsletter-form.png)

</details>

- <details>
    <summary>MailChimp Audience</summary>

  - ![newsletter form](readme_images/mailchimp-audience.png)

</details>

- <details>
    <summary>Facebook Business Page</summary>

  - ![facebook business page](readme_images/facebook-business-page.png)

</details>

### **Search Engine Optimization (SEO)**

In order to improve the visibility of the site in a search engine's unpaid results
the following has been implemented:

- html semantic tags
- meta keywords tag
- xml sitemap
- robots.txt

- <details>
    <summary>SEO detail</summary>

  - sitemap schema
  ![xml sitemaps schema](readme_images/xml-sitemap.png)

  - robots txt file

  ![robots txt file](readme_images/robots-txt.png)

  - seo meta tags

  ![seo meta tags](readme_images/seo-meta-tags.png)

  </details>

---

## Testing

- [TESTING.md](TESTING.md)

### **Running automated tests**

- <details>
    <summary>Unit test automated tests</summary>

  - The automated django/python tests are executed using unittest.
  - Test run using sqlite3 as Db, set DEBUG  to `True` before running tests.
  - Run the python tests using the command:

          python3 manage.py test

</details>

- <details>
    <summary>Coverage automated tests</summary>

  - Test coverage for the django/python tests can be reviewed using the coverage tool:

  - If coverage is not installed then run the command:

            pip3 install coverage
  - Test run using sqlite3 as Db, set DEBUG  to `True` before running tests.
  - Run the following series of commands to determine test coverage:

          coverage run --source=myapp manage.py test
          coverage report
          coverage html
          python3 -m http.server 
          (coverage results can be viewed in the browser in the htmlcov directory)

  - To exclude certain files or directories from running or from the coverage report, you can use the --omit option in the coverage command:

        coverage run --omit="myapp/migrations/*" manage.py test

  - Alternatively create a .coveragerc folder and add the following:

        [run]
        omit=
            *staticfiles*
            *migrations*
            *env*
            *manage.py*
            *settings.py*

        [report]
        omit =
            *staticfiles*
            *migrations*
            *env*
            *manage.py*
            *settings.py*

</details>

---

## **Debuging**

- <details>
    <summary>Checkout Form AttributeError</summary>

      Bug: AttributeError at /checkout/
          module 'django.forms.forms' has no attribute 'BoundField'

      https://github.com/django-crispy-forms

      Solution: `$ pip install crispy-bootstrap4`

      - Settings.py:

        INSTALLED_APPS = (
          ...
          "crispy_forms",
          "crispy_bootstrap4",
          ...
        )

        CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

        CRISPY_TEMPLATE_PACK = "bootstrap4"
  
---

## **Built With**

- Django 3.2 - The web framework used
- Bootstrap 4 - The front-end framework used
- Stripe - The payment processing service used
- Heroku - The cloud platform used for deployment
- ElephantSQL - The cloud-based PostgreSQL database used

## **Author**

Jose Guerra 2023

## **License**

The project is open-source and licensed under the MIT License, allowing other developers to
contribute and improve upon the code. The artist's work is protected by the Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License
ensuring that their work is used appropriately and with proper credit given - see the [LICENCE.md](LICENSE.md) file for details.

### **Credit**

- [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) for inspiration, which was customized to suit the project's objective.
- [ci-pp4-django-fsf](https://github.com/JoseMGuerra/ci-pp4-django-fsf/blob/main/README.md) for the README format.
- [Stack Overflow](https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django) for the test form validation snippet.
- [W3schools](https://www.w3schools.com/django/index.php) for Django tutorials.
- [Learn Django](https://learndjango.com/tutorials/django-testing-tutorial) for unit testing inspiration.
- [Unit testing framework documentation](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures) for skipping tests.
- [Django documentation](https://docs.djangoproject.com/en/3.2/topics/testing/tools/) for testing tools.
- [W3schools](https://www.w3schools.com/charsets/ref_emoji.asp) for readme emojis.
- [dequeuniversity.com](https://dequeuniversity.com/rules/axe/4.4/label?utm_source=lighthouse&utm_medium=devtools) for input label lighthouse error fix.
- [dequeuniversity.com](https://dequeuniversity.com/rules/axe/4.4/button-name?utm_source=lighthouse&utm_medium=devtools) for button name lighthouse error fix.
- [GitHub documentation](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/changing-a-commit-message) for changing a commit message.
- [privacypolicygenerator.info](https://www.privacypolicygenerator.info/) for the privacy policy HTML.
- [Font Awesome](https://fontawesome.com/) for icons.
- [Google Fonts](https://fonts.google.com/) for fonts.
- [Cloudinary](https://cloudinary.com/) for file storage.
- [Heroku](https://www.heroku.com/) for deployment.
- [PostgreSQL](https://www.postgresql.org/) for the database.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) for form rendering.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) for authentication.
- [Stripe](https://stripe.com/) for payment processing.
- [Pixabay](https://pixabay.com/) for the images.
- [Unsplash](https://unsplash.com/) for the images.
- [animate.css](https://animate.style/#utilities) for the animation.
- [hover.css](https://ianlunn.github.io/Hover/) for the hover effect.

## **Acknowledgments**

I would like to take a moment to acknowledge the immense support I have received from my coding mentor **Brian Macharia**, slack community, tutor support at [Code Institute](https://codeinstitute.net) and fellow cohort who have been instrumental in my growth and development as a programmer. My mentor's guidance and expertise have been invaluable in helping me hone my skills and deepen my understanding of programming concepts. The supportive and collaborative environment of the slack community and my fellow classmates have kept me motivated and inspired throughout my learning journey. Thank you for your unwavering support and encouragement. I could not have come this far without you all.

---

Happy coding!
