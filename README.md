# Product Management System

## Overview

This script provides a simple command-line interface for managing a product inventory stored in a CSV file. Users can add, update, delete, and view product information, as well as sort products by quantity or name. 

## Features

- **Add Product:** Allows users to add new products to the inventory.
- **Update Product:** Enables updating existing product details such as name, quantity, and brand.
- **Fetch Product:** Retrieves and displays information for a specific product based on its SKU.
- **Delete Product:** Permanently removes a product from the inventory.
- **Sort Products:** Sorts the product list by quantity or name, and displays the sorted list.

## Requirements

- Python 3.x
- CSV file named `products.csv` in the same directory as the script (will be created if not present).

## How to Use

1. **Run the Script:**
   ```bash
   python product_management.py
   ```

2. **Interactive Menu:**
   - **Enter 1:** Add a new product
   - **Enter 2:** Update an existing product
   - **Enter 4:** Fetch product details
   - **Enter 5:** Delete a product
   - **Enter 6:** Sort and display products
   - **Enter 0:** Exit the application

## Functions

### `addproduct()`
Prompts the user for product details (SKU, name, quantity, and brand) and appends this data to `products.csv`.

### `search(sku)`
Searches for a product by its SKU and returns the product details if found.

### `updateproduct()`
Allows the user to update product information based on SKU. Updates are saved back to `products.csv`.

### `readproduct()`
Fetches and displays product information for a specified SKU.

### `deleteproduct()`
Deletes a product from `products.csv` based on the given SKU.

### `sortproducts()`
Sorts the products either by quantity or name in ascending or descending order and displays the sorted list.

## Error Handling

- **File Operations:** Handles exceptions that may occur while reading from or writing to the CSV file.
- **User Input:** Validates user input for choices and quantities to ensure correct operations.

## Notes

- Deleting a product is irreversible. Ensure that you want to permanently remove the product before proceeding.
- If the CSV file does not exist, it will be created automatically when a new product is added.

## Example

Here's a typical session with the product management script:

```
Enter 1 to add data of new product
Enter 2 to update an existing product's data
Enter 4 to fetch data of a particular product
Enter 5 to delete the data of a particular product (IRREVERSIBLE OPERATION)
Enter 6 to display products sorted by quantity or name
Enter 0 to close this dialog box
```

**Adding a Product:**
```
Enter 1
Enter SKU: 123
Enter name: Widget
Enter Quantity: 10
Enter Brand: Acme
```

**Updating a Product:**
```
Enter 2
Enter the SKU of the product to update: 123
Current data: ['123', 'Widget', 10, 'Acme']
Enter 1 to update name
Enter 2 to update quantity
Enter 3 to update brand
Enter your choice (1/2/3): 2
Enter new quantity: 20
```

**Fetching a Product:**
```
Enter 4
Enter the SKU of the product to fetch: 123
Name: Widget, Quantity: 20, Brand: Acme
```

**Deleting a Product:**
```
Enter 5
Enter the SKU of the product to delete: 123
```

**Sorting Products:**
```
Enter 6
Enter 1 to sort by quantity
Enter 2 to sort by name
Enter your choice (1/2): 1
Enter 1 for ascending or 2 for descending order:
```

