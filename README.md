# Overview

### Purpose

Test site for exploring Django, TastyPie, and the Heroku Python build pack

### Setup

- **Environment**
    - Install Python 3.7.3
    - Install pip 19.2.2
- **Dependecies**
    - run:
      - `pip install -r requirements.txt`
- **Create and migrate database** 
    - For local development, use sqlite3
    - Create an `.env` file in the root of the project. You can use `.env.example` as an example.
    - run:
      - `python manage.py migrate`
- **Populate test records**
    - Working on a seed file for the database
    - To manually create reacords run:
      - `python manage.py shell`
    - Within the python shell run
      - `from api.models import Organization`
      - `from api.models import Event`
      - Right now, events are dependant on the existence of an organization, so create orgs first
      - Create a few organizations using the following commands
        - `org = Organization(name = YOUR_CHOSEN_NAME, organization_id=INTEGER)`
        - `org.save()`
      - Create a few events using the following commands
        - `event = Event(event_name = YOUR_CHOSEN_NAME, organization_name=A_STRING_IDENTIFIER, event_start_date=YYYY-MM-DD HH:MM, ticket_cost=DECIMAL_VALUE)`
        - `Event.save()`
      - Once you have created a few orgs and events run:
        - `exit()`
- **Start the server**
    - Run:
      - `python manage.py runserver`


### Endpoints
- **Testing the endpoints**
  - In the root of the directory is a Postman collection
  - This collection will provide templates for testing the endpoints locally as well on Heroku

- **`GET /api/events`**
    - Fetch events
    - Pass query paremeters for event_name, organization_name, event_start_date, and ticket_cost to narrow search
    - ticket_cost and event_start_date will accept gte and lte query parameters
- **`PUT /api/events/{:id}`**
    - Updates event information as long as appropriate fields exist and the organization exists.
    - Payload example:
      - {
          "event_name" : "updated name",
          "organization_name" :"updated org",
          "ticket_cost": "500.00",
          "event_start_date": "2019-09-02 14:00:00.00"
        }

### Heroku Application

- Endpoints can be found at:
  - `https://gb-django-api-test.herokuapp.com/api/events`
