import csv
import sqlite3

class Product:
    count = 0
    
    def __init__(self):
        Product.count += 1
        self.conn = sqlite3.connect('products.db')
        self.create_table()
        
        while True:
            print("Enter 1 to add data of new product")
            print("Enter 2 to update an existing product's data")
            print("Enter 4 to fetch data of a particular product")
            print("Enter 5 to delete the data of a particular product (IRREVERSIBLE OPERATION)")
            print("Enter 6 to display products sorted by quantity or name")
            print("Enter 0 to close this dialog box")
            choice = int(input())
            if choice == 0:
                break
            elif choice == 1:
                self.addproduct()
            elif choice == 2:
                self.updateproduct()
            elif choice == 4:
                self.readproduct()
            elif choice == 5:
                self.deleteproduct()
            elif choice == 6:
                self.sortproducts()
            else:
                print("Invalid choice. Please enter a valid option.")
                
        self.conn.close()

    def create_table(self):
        try:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCTS
                                (SKU TEXT PRIMARY KEY NOT NULL,
                                NAME TEXT NOT NULL,
                                QTY INT NOT NULL,
                                BRAND TEXT NOT NULL);''')
        except Exception as e:
            print(f"Error creating table: {e}")

    def addproduct(self):
        sku = input("Enter SKU: ")
        name = input("Enter name: ")
        qty = int(input("Enter Quantity: "))
        brand = input("Enter Brand: ")
        prod = [sku, name, qty, brand]
        
      
        try:
            with open('products.csv', 'a', newline='') as f_object:
                writer_object = csv.writer(f_object)
                writer_object.writerow(prod)
        except Exception as e:
            print(f"Error adding product to CSV: {e}")
     
        try:
            self.conn.execute("INSERT INTO PRODUCTS (SKU, NAME, QTY, BRAND) VALUES (?, ?, ?, ?)", prod)
            self.conn.commit()
            print("Product added successfully.")
        except Exception as e:
            print(f"Error adding product to SQLite: {e}")

    def search(self, sku):
       
        try:
            with open('products.csv', mode='r') as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    if lines[0] == sku:  # if SKU is the same then return that particular list
                        return lines
        except Exception as e:
            print(f"Error searching for product in CSV: {e}")
      
        try:
            cursor = self.conn.execute("SELECT SKU, NAME, QTY, BRAND FROM PRODUCTS WHERE SKU = ?", (sku,))
            data = cursor.fetchone()
            if data:
                return list(data)
        except Exception as e:
            print(f"Error searching for product in SQLite: {e}")
        return None

    def updateproduct(self):
        sku = input("Enter the SKU of the product to update: ")
        data = self.search(sku)
        
        if data is None:
            print("Product not found.")
            return
        
        print(f"Current data: {data}")
        print("Enter 1 to update name")
        print("Enter 2 to update quantity")
        print("Enter 3 to update brand")
        update_choice = int(input("Enter your choice (1/2/3): "))

        if update_choice == 1:
            new_name = input("Enter new name: ")
            data[1] = new_name
        elif update_choice == 2:
            try:
                new_qty = int(input("Enter new quantity: "))
                data[2] = new_qty
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                return
        elif update_choice == 3:
            new_brand = input("Enter new brand: ")
            data[3] = new_brand
        else:
            print("Invalid choice.")
            return
        
        newlist = []
        with open('products.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if lines[0] != sku:
                    newlist.append(lines)
                else:
                    newlist.append(data)
        
        try:
            with open('products.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(newlist)
            print("Product updated successfully in CSV.")
        except Exception as e:
            print(f"Error updating product in CSV: {e}")
        
       
        try:
            self.conn.execute("UPDATE PRODUCTS SET NAME = ?, QTY = ?, BRAND = ? WHERE SKU = ?", (data[1], data[2], data[3], sku))
            self.conn.commit()
            print("Product updated successfully in SQLite.")
        except Exception as e:
            print(f"Error updating product in SQLite: {e}")

    def readproduct(self):
        sku = input("Enter the SKU of the product to fetch: ")
        data = self.search(sku)
        if data:
            print(f"Name: {data[1]}, Quantity: {data[2]}, Brand: {data[3]}")
        else:
            print("Product not found.")

    def deleteproduct(self):
        sku = input("Enter the SKU of the product to delete: ")
        data = self.search(sku)
        
        if data is None:
            print("Product not found.")
            return
        
        newlist = []
        with open('products.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                if lines[0] != sku:
                    newlist.append(lines)
        
        try:
            with open('products.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(newlist)
            print("Product deleted successfully from CSV.")
        except Exception as e:
            print(f"Error deleting product from CSV: {e}")
        
      
        try:
            self.conn.execute("DELETE FROM PRODUCTS WHERE SKU = ?", (sku,))
            self.conn.commit()
            print("Product deleted successfully from SQLite.")
        except Exception as e:
            print(f"Error deleting product from SQLite: {e}")

    def sortproducts(self):
        print("Enter 1 to sort by quantity")
        print("Enter 2 to sort by name")
        sort_choice = int(input("Enter your choice (1/2): "))

        if sort_choice not in [1, 2]:
            print("Invalid choice.")
            return
        
        try:
            with open('products.csv', mode='r') as file:
                csvFile = csv.reader(file)
                data = list(csvFile)

            if sort_choice == 1:
                data.sort(key=lambda x: int(x[2]))
            elif sort_choice == 2:
                data.sort(key=lambda x: x[1])

            print("Enter 1 for ascending or 2 for descending order:")
            order_choice = int(input())
            if order_choice == 2:
                data.reverse()

            print("Sorted product list (from CSV):")
            for row in data:
                print(f"SKU: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Brand: {row[3]}")
        except Exception as e:
            print(f"Error sorting products from CSV: {e}")
        
        try:
            order = "ASC" if order_choice == 1 else "DESC"
            if sort_choice == 1:
                cursor = self.conn.execute(f"SELECT SKU, NAME, QTY, BRAND FROM PRODUCTS ORDER BY QTY {order}")
            elif sort_choice == 2:
                cursor = self.conn.execute(f"SELECT SKU, NAME, QTY, BRAND FROM PRODUCTS ORDER BY NAME {order}")
            
            print("Sorted product list (from SQLite):")
            for row in cursor:
                print(f"SKU: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Brand: {row[3]}")
        except Exception as e:
            print(f"Error sorting products from SQLite: {e}")

c1 = Product()
print("The number of products that you have is", Product.count)
