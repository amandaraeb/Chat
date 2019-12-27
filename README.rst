Chat
====

Setup
-----

This application is written using Python3 and Django. Before running the application, you need to install the dependencies in a Python virtual environment within the application's home directory as follows:

.. code-block:: bash

    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

To set up an initial database, run:

.. code-block:: bash

    $ python manage.py migrate

This will create a sqlite database in the application's home directory. 

To populate the sqlite database with initial users, run:

.. code-block:: bash

    $ python manage.py loaddata initial_users.json

This will create two users, user1 and user2, both with the password 'pass'. 

Running the Application
-----------------------

To run application, ensure you have sourced your virtual environment and run:

.. code-block:: bash

    $ python manage.py runserver

This will run the application at http://localhost:8000.

Before sending any messages, you  must log in through Django's admin interface at  http://localhost:8000/admin.

Tests
-----

Run tests with the command:

.. code-block:: bash

    $ python manage.py test

There is one functional test that utilizes Selenium. Selenium requires `Geckodriver`_ to be installed. The functional test also assumes that the application is running at http://localhost:8000.

To run only the message unit tests, specify the message app in the testing command as follows:

.. code-block:: bash

    $ python manage.py test message

.. _`Geckodriver`: https://github.com/mozilla/geckodriver

Future Work
-----------

With more time, I would have liked to make the following changes:

* Better testing for the Compose Form; I think currently the functional test tests that the form successfully sends messages, but I'd like to figure out how to add a unit test for the actual form.
* When fetching received messages, instead of fetching all messages, fetch only the latest messages. This way, instead of having to rewrite all the messages on the page, you can just add the latest messages to the list of messages.
* Show an entire conversation rather than just the received message. This would include adding another filter to the received endpoint to get only the messages sent by a particular user, as well as showing the messages that the current user sent. This would also involve sorting the messages based on the 'sent' time stamps, and maybe also showing the time stamp next to the message.
* I'd also like to do more research into whether Ajax is the best tool for periodically checking the received messages. It may be better to use React component and to reset its state every time a message is sent.
* Currently the only way to log in is through the Django admin interface. There is also no authorization for viewing the home page. This means you can view the app and try to send a message without logging in, which will fail due to the requesting user being anonymous. This can be fixed by either checking if the user is anonymous and sending back an error message, or by rerouting to a log in page before showing the home page. 
