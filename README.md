Features
Add New Product: Add a new product with SKU, name, quantity, and brand.
Update Existing Product: Update the name, quantity, or brand of an existing product.
Fetch Product Data: Retrieve and display details of a product using its SKU.
Delete Product: Permanently delete a product from the inventory using its SKU.
Sort Products: Sort the products either by quantity or name, and display the sorted list.
Usage
Add a New Product

Enter 1 when prompted.
Input the SKU, name, quantity, and brand of the product.
Update an Existing Product

Enter 2 when prompted.
Input the SKU of the product to be updated.
Choose which field (name, quantity, brand) to update and provide the new value.
Fetch Product Data

Enter 4 when prompted.
Input the SKU of the product you want to fetch.
Delete a Product

Enter 5 when prompted.
Input the SKU of the product to be deleted.
Sort Products

Enter 6 when prompted.
Choose to sort by quantity or name.
Decide on ascending or descending order.
Exit

Enter 0 to close the dialog box and terminate the script.
Code Breakdown
Initialization (__init__): Displays a menu and handles user choices in an infinite loop until 0 is entered.

Add Product (addproduct): Takes user input and appends the product details to products.csv.

Search Product (search): Searches for a product by SKU and returns its details if found.

Update Product (updateproduct): Updates the details of a product and rewrites the CSV file with the updated data.

Fetch Product Data (readproduct): Retrieves and displays the details of a product based on SKU.

Delete Product (deleteproduct): Removes a product from the CSV file based on SKU.

Sort Products (sortproducts): Sorts the product list either by quantity or name, and displays the sorted list.
