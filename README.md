# Django Delights
Deployed at: https://django-delights.herokuapp.com/  
This project is a simple website built using the Django framework in Python. Its main purpose is to simulate restaurant management. Here is a summary of the project's features and components:

## User Registration and Login
Users can register an account and log in to the website.

## Inventory Management
Users can add items to the inventory by specifying the item's name, quantity, unit, and unit price. The inventory items are associated with the user who added them. The inventory dynamically tracks the available quantity of each item.

## Menu Creation
Users can add items to the menu by providing a title and price for each menu item. The menu items are also associated with the user who added them.

## Recipe Management
Users can specify the recipe requirements for each menu item. The recipe requirements include the ingredients and their quantities needed to prepare a menu item.

## Purchase Tracking
Users can track purchases made for menu items. When a purchase is made, the system checks if there are sufficient ingredients in stock based on the recipe requirements. If there are not enough ingredients, an error is displayed. If the purchase is successful, the inventory stock is updated accordingly.

## Profit Tracking
The system calculates profit by subtracting total expenses from total revenue. The total revenue is calculated based on the prices of the purchased menu items, and the total expenses are calculated based on the quantity and unit price of the ingredients used.