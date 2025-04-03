# Coleon

#### Description:
Coleon is an application designed for collectors who want to efficiently organize and plan their collections. It allows users to create, customize, and track the progress of their collections, whether they are stamps, records, trading cards, or other valuable items.

The app features a customizable table-based interface where each item is represented as a row. Users can add custom columns to record any necessary information, such as price, acquisition date, origin, store, images, and more.  

Additionally, Coleon automatically generates charts to visualize collection progress, money spent, price trends, and other relevant analytics. Users can also share collection templates with others and export data in multiple formats.

## Key Features:

- **Automatic Chart Generation:** If the collection includes predefined columns like "price" or "status," Coleon generates insightful charts, such as:
  - "Most Expensive Items"
  - "Purchase History"
  - "Collection Progress"

- **Custom Column Creation:** Users can add columns with different data types:
  - Text (string)
  - Number (number)
  - Date (date)
  - Status (boolean or enum)

- **Card and Table Views:** Users can switch between a table view and a card view, ideal for visually appealing collections.

- **Collection Export:** Collections can be exported in CSV format for easy sharing and data backup.

- **Advanced Filtering:** Users can filter the collection based on any column.

- **User Management and Security:** Secure user registration and login with password protection for personal collections.

- **Item Management:** Easy addition and removal of items with pagination support for large collections.

- **Image Link Verification:** Ensures images are not broken by validating URLs.

- **Sensitive Data Deletion Alerts:** Notifications appear before deleting items or columns containing significant data.

## Technologies Used:

- **Backend:** Python with Django
- **Database:** SQL with JSON storage (for custom columns)
- **Frontend:** HTML and CSS


Initiate the server --> $ python3 manage.py runserver
