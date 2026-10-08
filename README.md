# Python OOP Lab: Bookstore



This project has two classes that model items in a bookstore.



## Book (`lib/book.py`)



- Attributes: `title` and `page_count`

- `page_count` must be an integer. If it isn't, the class prints a message.

- `turn_page()` prints a message about flipping the page.



## Coffee (`lib/coffee.py`)



- Attributes: `size` and `price`

- `size` must be Small, Medium, or Large. If it isn't, the class prints a message.

- `tip()` prints a thank-you message and raises the price by 1.



## Running the tests



```

pipenv install

pipenv shell

pytest -x lib/testing/book_test.py

pytest -x lib/testing/coffee_test.py

```



## Screenshot



![Passing tests](tests.png)

