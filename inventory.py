import mysql.connector; # type: ignore
myab=mysql.connector.connect(host="192.168.56.1",user="adithya",password="svnsa",database="inventorysystem")
cursor=myab.cursor()
def add_item(name, quantity, price):
    sql = "INSERT INTO inventory (name, quantity, price) VALUES (%s, %s, %s)"
    val = (name, quantity, price)
    cursor.execute(sql, val)
    myab.commit()
    print(cursor.rowcount, "record inserted.")
def update_item(item_id, quantity):
    sql = "UPDATE inventory SET quantity = %s WHERE id = %s"
    val = (quantity, item_id)
    cursor.execute(sql, val)
    myab.commit()
    print(cursor.rowcount, "record(s) affected.")
def display_inventory():
    cursor.execute("SELECT * FROM inventory")
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print("ID:", row[0])
            print("Name:", row[1])
            print("Quantity:", row[2])
            print("Price:", row[3])
            print("--------------------")
    else:
        print("Inventory is empty.")
def delete_item(item_id):
    sql = "DELETE FROM inventory WHERE id = %s"
    val = (item_id,)
    cursor.execute(sql, val)
    myab.commit()
    print(cursor.rowcount, "record(s) deleted.")
def main_menu():
    while True:
        print("===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add new item")
        print("2. Update item quantity")
        print("3. Display inventory")
        print("4. Delete item")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_item(name, quantity, price)
        elif choice == '2':
            item_id = int(input("Enter item ID: "))
            quantity = int(input("Enter new quantity: "))
            update_item(item_id, quantity)
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            item_id = int(input("Enter item ID to delete: "))
            delete_item(item_id)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main_menu()
cursor.close()
myab.close()
