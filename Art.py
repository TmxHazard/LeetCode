import mysql.connector;
mb=mysql.connector.connect(host="192.168.56.1",user="adithya",password="svnsa",database="artgallery")
cursor=mb.cursor()
def add_painting(no,painting,artist,painted_year,purchase_price):
    sql="insert into arts(no,painting,artist,painted_year,purchase_price) values(%s,%s,%s,%s,%s)"
    val=(no,painting,artist,painted_year,purchase_price)
    cursor.execute(sql,val)
    mb.commit()
    print(cursor.rowcount,"recorded")
def update_painting(sell_price, sell_date, painting):
    sql = "UPDATE arts SET sell_price=%s, sell_date=%s WHERE painting=%s"
    val = (sell_price, sell_date, painting)
    cursor.execute(sql, val)
    mb.commit()
    print(cursor.rowcount, "updated")
def display_paintings():
    cursor.execute("select * from arts")
    result = cursor.fetchall()
    if cursor.rowcount>0:
        for row in result:
            print("no : ",row[0])
            print("painting : ",row[1])
            print("artist : ",row[2])
            print("painted_year : ",row[3])
            print("purchased_year : ",row[4])
            print("sell_price : ",row[5])
            print("sell_date : ",row[6])
            print("==========x END x==========")
    else :
        print("There are no arts to display.")
def delete_painting(painting):
    sql = "DELETE FROM arts WHERE painting = %s"
    val = (painting,)
    cursor.execute(sql, val)
    mb.commit()
    print(cursor.rowcount, "record(s) deleted")
def main_menu():
    while True:
        print("===== ART GALLERY =====")
        print("1. Add new painting")
        print("2. Update paintings")
        print("3. Display paintings")
        print("4. Delete paintings")
        print("5. Exit")
        choice = input("enter your choice : ")
        
        if choice == '1':
            no = int(input("Enter no : "))
            painting= input("Enter painting name : ")
            artist = input("Enter artist name : ")
            painted_year = int(input("enter the painted year : "))
            purchase_price = int(input("enter the price of the painting : "))
            add_painting(no,painting,artist,painted_year,purchase_price)
        elif choice == '2':
            painting = input("Enter the painting name: ")
            sell_price = int(input("Enter painting selling price: "))
            sell_date = input("Enter painting selling date (YYYY-MM-DD): ")
            update_painting(sell_price, sell_date, painting)
        elif choice == '3':
            display_paintings()
        elif choice == '4':
            painting =input("Enter painting to be deleted: ")
            delete_painting(painting)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main_menu()
cursor.close()
mb.close()
