import os
import csv
import datetime
def main():
    
    
    print(" " * 35, "WELCOME TO LETTUCE EAT   ")
    print("_" * 75, "\n\n")
    print("\t\t\t\t\tOPERATE AS:")
    print(" " * 10, "~" * 60)
    while True:
        try:
            x =int(input("\t\t\t\t\t1.ADMIN\n\t\t\t\t\t2.CUSTOMER\n\t\t\t\t\t3.EXIT: "))
            if x==1:
                admin=Admin()
                admin.admin_menu()
            elif x==2:
                customer=Customer()
                customer.customer_menu()
            elif x==3:
                break
            else:
                print("invalid input")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
class Menu():
    def __init__(self):
        self.new_no=0
    def item_exists(self, name):
        if not os.path.isfile("menu.csv"):
            print("Menu File Does Not Exist.")
            return False

        with open("menu.csv", "r", newline='') as obj:
            fobj = csv.reader(obj)
            next(fobj)
            for row in fobj:
                if row[1].strip() == name.strip():
                    return True

        return False
    def get_item_price(self, name):
        if not os.path.isfile("menu.csv"):
            print("Menu File Does Not Exist.")
            return None

        with open("menu.csv", "r", newline='') as obj:
            fobj = csv.reader(obj)
            next(fobj)
            for row in fobj:
                if row[1].strip() == name.strip():
                    return int(row[2])

        return None

    def add_item_menu(self, name, price):
        if not os.path.isfile("menu.csv"):
            with open("menu.csv","w",newline='') as obj:
                fobj=csv.writer(obj)
                fobj.writerow(["sl no","item","price"])
                self.new_no=1
        else:
            with open("menu.csv", "r", newline='') as obj:
                fobj = csv.reader(obj)
                lines = list(fobj)
                self.new_no = len(lines)
        with open("menu.csv","a",newline='') as obj:
            fobj=csv.writer(obj)
            fobj.writerow([self.new_no,name,price])
    def remove_item_menu(self, name):
        if not os.path.isfile("menu.csv"):
            print("Menu file does not exist.")
            return False
        temp_file = "temp_menu.csv"
        with open("menu.csv", "r", newline='') as obj, open(temp_file, "w", newline='') as temp_obj:
            fobj = csv.reader(obj)
            temp_fobj = csv.writer(temp_obj)
            found = False
            for row in fobj:
                if row[1].strip() == name.strip():
                    found = True
                else:
                    temp_fobj.writerow(row)
            if not found:
                print("Item Not Found In Menu.")
                return False

        os.remove("menu.csv")
        os.rename(temp_file, "menu.csv")
        return True
    def update_item_price(self, name, new_price):
        if not os.path.isfile("menu.csv"):
            print("Menu File Does Not Exist.")
            return False

        temp_file = "temp_menu.csv"
        with open("menu.csv", "r", newline='') as obj, open(temp_file, "w", newline='') as temp_obj:
            fobj = csv.reader(obj)
            temp_fobj = csv.writer(temp_obj)
            found = False
            for row in fobj:
                if row[1].strip() == name.strip():
                    found = True
                    row[2] = new_price
                temp_fobj.writerow(row)

            if not found:
                print("Item Not Found In Menu.")
                return False

        os.remove("menu.csv")
        os.rename(temp_file, "menu.csv")
        return True
    def display_menu(self):
        if not os.path.isfile("menu.csv"):
            print("Menu File Does Not Exist.")
            return

        with open("menu.csv", "r", newline='') as obj:
            fobj = csv.reader(obj)
            print("Menu:")
            for row in fobj:
                print("\t".join(row))
                
class Admin(Menu):
    def __init__(self):
        self.__password=1234
        #self.menu=Menu()
    def admin_menu(self):
        while True:
            attempt=int(input("Enter Password:"))
            if attempt==self.__password:
                print("Welcome To Admin Menu:")
                print("==========================")
                print("1.Add item to menu\n2.Remove item from menu\n3.Update Item\n4.View All Bills\n5.Menu")
                n=int(input("Enter Choice:"))
                if n==1:
                    self.add_item()
                    
                elif n==2:
                    self.remove_item()
                elif n==3:
                    self.update_menu()
                elif n==4:
                    self.read_all_bills()
                elif n==5:
                    self.view_menu()
                else:
                    print("invalid input")
                break
            else:
                print("Invalid Password,Try Again")
    def return_to_menu(self):
        y=int(input("type 1 to return to admin menu\ntype 2 for main menu:"))
        if y==1:
            self.admin_menu()
        elif y==2:
            main()
        else:
            print("invalid option")
    def user_input(self):
        num=0
        while num<3:
            try:
                dept:dept id ,dept name
                emp:empid,deptid,salary
                
                input1=int(input("enter a value"))
                return input1
            except:
                print("invalid value,input a digit")
            num+=1
        return 0
    def add_item(self):
        name=input("enter name of the item to add:")
        price=int(input("enter price of the item to add:"))
        self.add_item_menu(name,price)
        self.return_to_menu()
            
    def remove_item(self):
        name=input("enter name of the item to remove:")
        if self.remove_item_menu(name):
            print("item removed")
        else:
            print("failed to remove item to menu")
        self.return_to_menu()
    def update_menu(self):
        name=input("enter name:")
        price=int(input("enter price:"))
        self.update_item_price(name,price)
        self.return_to_menu()
    def read_all_bills(self):
        if not os.path.isfile("all_bills.csv"):
            with open("all_bills.csv", "w", newline='') as obj:
                fobj = csv.writer(obj)
                fobj.writerow(["Name\t", "Phone\t", "Date\t", "Time\t","Item\t","Quantity\t","Price\n","Total\n"])
        with open("all_bills.csv", "r") as obj:
            fobj = csv.reader(obj)
            print("All Bills:")
            for row in fobj:
                print("\t".join(row))
    def view_menu(self):
        self.display_menu()
        self.return_to_menu()
    def view_all_orders(self):
        if not os.path.isfile("all_bills.csv"):
            with open("all_bills.csv", "w", newline='') as obj:
                fobj = csv.writer(obj)
                fobj.writerow(["Name\t", "Phone  ", "Date\t", "Time  ","Item  ","Quantity  ","Price  " "Total"])
        with open("all_bills.csv", "r") as obj:
            fobj = csv.reader(obj)
            print("All Orders:")
            for row in fobj:
                print("\t".join(row))

class Customer(Menu):
    def __init__(self):
        #self.menu = Menu()
        self.name = ""
        self.phone = ""

    def customer_menu(self):
        print("WELCOME TO CUSTOMER MENU:")
        print("===========================")
        self.name = input("Enter Customer Name: ")
        while True:
            self.phone = input("Enter Phone Number: ")
            if len(self.phone) == 10 and self.phone.isdigit():
                break
            else:
                print("Invalid Phone Number. Please Enter A 10-digit Number.")

        while True:
            x = int(input("1. View menu\n2. Place order\n3. Exit\nChoose an option: "))
            if x == 1:
                self.display_menu()
            elif x == 2:
                self.place_order()
            elif x == 3:
                break
            else:
                print("Invalid option. Please choose again.")
    def place_order(self):
        order = []
        while True:
            item_name = input("Enter Item Name (or 'done' to finish): ")
            if item_name.lower() == "done":
                break
            if not self.item_exists(item_name):
                print("Item not found in menu. Please select a valid item.")
                continue
            quantity = int(input(f"Enter Quantity For {item_name}: "))
            if quantity <= 0:
                print("Invalid quantity. Please enter a positive number.")
                continue
            item_price = self.get_item_price(item_name)
            order.append({"item": item_name, "quantity": quantity, "price": item_price})
        total = sum(item["quantity"] * item["price"] for item in order)
        print(f"Total: Rs{total}")
        confirm = input("Confirm order (yes/no): ")
        if confirm.lower() == "yes":
            with open("bill.csv", "w", newline='') as file:
                writer = csv.writer(file)
                for item in order:
                    writer.writerow([item["item"], item["quantity"], item["price"]])
            print("Order Placed Successfully!")
            self.generate_bill(total)
        else:
            print("Order Canceled.")


    def generate_bill(self, total):
        now = datetime.datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")
        with open("bill.csv", "r", newline='') as obj:
            fobj=csv.reader(obj)
            lines=list(fobj)
        print("\n\n")
        print("                                LETTUS EAT                  ")
        print("_"*75)
        print("                               Bhubhneshwar                 ")
        print("                           phone : 0624-2234523           ")
        print()
        print("                                    BILL")
        print("_"*75, "\n")
        print()
        print("     Customer Details")
        print("_"*26)
        print("Customer Name     :  ", self.name)
        print("Customer Mobile No:  ", self.phone)
        print("Invoice Date      :  ", date)
        print("Invoice Time      :  ", time)
        print("_"*75)
        print("Item\t\tQuantity\tPrice")
        print("-"*75)
             # Skip the header row
        for line in lines:
            item, quantity, price =line
            print(f"{item}\t\t{quantity}\t\t{price}")
        print("-"*75)
        print("Total Amount      :  ", total, "rs")
        print("\n\t\t        Thank You For Ordering\n\t\t            Enjoy Your Meal")
        if not os.path.isfile("all_bills.csv"):
            with open("all_bills.csv", "w", newline='') as obj:
                fobj = csv.writer(obj)
                fobj.writerow(["Name\t", "Phone  ", "Date\t", "Time  ","Item  ","Quantity  ","Price  " "Total"])
        with open("all_bills.csv","a",newline='') as all_bills_file:
            writer=csv.writer(all_bills_file)
            for line in lines:
                item,quantity,price=line
                writer.writerow([self.name,self.phone,date,time,item,quantity,price,total])


main()
