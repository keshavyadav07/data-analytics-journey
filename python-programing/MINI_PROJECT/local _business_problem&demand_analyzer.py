customers = []
sales = []

customers = [
    {
        "id": 1,
        "name": "Keshav",
        "age": 21,
        "city": "Bhopal",
        "type": "New"
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 23,
        "city": "Indore",
        "type": "Returning"
    }
]
def add_customer():

    customer_id = int(input("Enter customer ID: "))
    name = input("Enter customer name: ")
    age = int(input("Enter customer age: "))
    city = input("Enter customer city: ")
    customer_type = input("Enter customer type (New/Returning): ")

customers = []


def add_customer():

    customer_id = int(input("Enter customer ID: "))
    name = input("Enter customer name: ")
    age = int(input("Enter customer age: "))
    city = input("Enter customer city: ")
    customer_type = input("Enter customer type (New/Returning): ")

    customer = {
        "id": customer_id,
        "name": name,
        "age": age,
        "city": city,
        "type": customer_type
    }

    customers.append(customer)

    print("Customer added successfully!")



def show_customers():

    if len(customers) == 0:
        print("No customers found!")
        return

    print("\n===== ALL CUSTOMERS =====")

    for customer in customers:

        print("--------------------")
        print("ID:", customer["id"])
        print("Name:", customer["name"])
        print("Age:", customer["age"])
        print("City:", customer["city"])
        print("Type:", customer["type"])

def search_customer():

    search_id = int(input("Enter customer ID: "))

    for customer in customers:

        if customer["id"] == search_id:

            print("\n===== CUSTOMER FOUND =====")
            print("ID:", customer["id"])
            print("Name:", customer["name"])
            print("Age:", customer["age"])
            print("City:", customer["city"])
            print("Type:", customer["type"])

            return

    print("Customer not found!")

def add_sale():

    customer_id = int(input("Enter customer ID: "))

    # Check customer exists or not
    for customer in customers:

        if customer["id"] == customer_id:

            product = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))

            total = quantity * price

            sale = {
                "customer_id": customer_id,
                "product": product,
                "quantity": quantity,
                "price": price,
                "total": total
            }

            sales.append(sale)

            print("\nSale added successfully!")
            print("Total Amount:", total)

            return

    print("Customer not found!")
     
def show_sales():

    if len(sales) == 0:
        print("No sales found!")
        return

    print("\n===== ALL SALES =====")

    for sale in sales:

        print("--------------------")
        print("Customer ID:", sale["customer_id"])
        print("Product:", sale["product"])
        print("Quantity:", sale["quantity"])
        print("Price:", sale["price"])
        print("Total:", sale["total"])    

def total_revenue():

    if len(sales) == 0:
        print("No sales found!")
        return

    revenue = 0

    for sale in sales:

        revenue = revenue + sale["total"]

    print("\n===== REVENUE =====")
    print("Total Revenue:", revenue)  

def highest_sale():

    if len(sales) == 0:
        print("No sales found!")
        return

    highest = sales[0]

    for sale in sales:

        if sale["total"] > highest["total"]:
            highest = sale

    print("\n===== HIGHEST SALE =====")
    print("Product:", highest["product"])
    print("Quantity:", highest["quantity"])
    print("Total:", highest["total"])    

def best_selling_product():

    if len(sales) == 0:
        print("No sales found!")
        return

    product_quantity = {}

    for sale in sales:

        product = sale["product"]
        quantity = sale["quantity"]

        if product in product_quantity:
            product_quantity[product] += quantity
        else:
            product_quantity[product] = quantity

    best_product = ""
    highest_quantity = 0

    for product in product_quantity:

        if product_quantity[product] > highest_quantity:
            highest_quantity = product_quantity[product]
            best_product = product

    print("\n===== BEST SELLING PRODUCT =====")
    print("Product:", best_product)
    print("Quantity Sold:", highest_quantity)

def worst_selling_product():

    if len(sales) == 0:
        print("No sales found!")
        return

    product_quantity = {}

    for sale in sales:

        product = sale["product"]
        quantity = sale["quantity"]

        if product in product_quantity:
            product_quantity[product] += quantity
        else:
            product_quantity[product] = quantity

    worst_product = ""
    lowest_quantity = float("inf")

    for product in product_quantity:

        if product_quantity[product] < lowest_quantity:
            lowest_quantity = product_quantity[product]
            worst_product = product

    print("\n===== WORST SELLING PRODUCT =====")
    print("Product:", worst_product)
    print("Quantity Sold:", lowest_quantity)



def product_revenue():

    if len(sales) == 0:
        print("No sales found!")
        return

    product_revenue = {}

    for sale in sales:

        product = sale["product"]
        total = sale["total"]

        if product in product_revenue:
            product_revenue[product] += total
        else:
            product_revenue[product] = total

    print("\n===== PRODUCT-WISE REVENUE =====")

    for product in product_revenue:
        print(product, "-> ₹", product_revenue[product])

def highest_revenue_product():

    if len(sales) == 0:
        print("No sales found!")
        return

    product_revenue = {}

    for sale in sales:

        product = sale["product"]
        total = sale["total"]

        if product in product_revenue:
            product_revenue[product] += total
        else:
            product_revenue[product] = total

    highest_product = ""
    highest_revenue = 0

    for product in product_revenue:

        if product_revenue[product] > highest_revenue:
            highest_revenue = product_revenue[product]
            highest_product = product

    print("\n===== HIGHEST REVENUE PRODUCT =====")
    print("Product:", highest_product)
    print("Revenue: ₹", highest_revenue)


def customer_spending():

    if len(sales) == 0:
        print("No sales found!")
        return

    customer_spending = {}

    for sale in sales:

        customer_id = sale["customer_id"]
        total = sale["total"]

        if customer_id in customer_spending:
            customer_spending[customer_id] += total
        else:
            customer_spending[customer_id] = total

    print("\n===== CUSTOMER SPENDING =====")

    for customer_id in customer_spending:

        print(
            "Customer ID:",
            customer_id,
            "-> ₹",
            customer_spending[customer_id]
        )

def most_valuable_customer():

    if len(sales) == 0:
        print("No sales found!")
        return

    customer_spending = {}

    for sale in sales:

        customer_id = sale["customer_id"]
        total = sale["total"]

        if customer_id in customer_spending:
            customer_spending[customer_id] += total
        else:
            customer_spending[customer_id] = total

    best_customer = ""
    highest_spending = 0

    for customer_id in customer_spending:

        if customer_spending[customer_id] > highest_spending:

            highest_spending = customer_spending[customer_id]
            best_customer = customer_id

    print("\n===== MOST VALUABLE CUSTOMER =====")
    print("Customer ID:", best_customer)
    print("Total Spending: ₹", highest_spending)

def customer_type_analysis():

    new_customers = 0
    returning_customers = 0

    for customer in customers:

        if customer["type"].lower() == "new":
            new_customers += 1

        elif customer["type"].lower() == "returning":
            returning_customers += 1

    print("\n===== CUSTOMER TYPE ANALYSIS =====")
    print("New Customers:", new_customers)
    print("Returning Customers:", returning_customers)

    total_customers = new_customers + returning_customers

    if total_customers > 0:

        retention = (returning_customers / total_customers) * 100

        print("Returning Customer Rate:", round(retention, 2), "%")


# ================= BUSINESS PROBLEM DETECTOR =================

def business_problem_detector():

    print("\n========== BUSINESS PROBLEM DETECTOR ==========")

    problems = []

    # ---------- Revenue Check ----------

    revenue = 0

    for sale in sales:
        revenue = revenue + sale["total"]

    if revenue == 0:
        problems.append("No revenue generated yet.")

    elif revenue < 10000:
        problems.append("Revenue is very low.")

    # ---------- Customer Retention Check ----------

    new_customers = 0
    returning_customers = 0

    for customer in customers:

        if customer["type"].lower() == "new":
            new_customers += 1

        elif customer["type"].lower() == "returning":
            returning_customers += 1

    total_customers = new_customers + returning_customers

    if total_customers > 0:

        retention = (returning_customers / total_customers) * 100

        if retention < 30:
            problems.append("Customer retention is very low.")

    # ---------- Product Check ----------

    if len(sales) > 0:

        product_quantity = {}

        for sale in sales:

            product = sale["product"]
            quantity = sale["quantity"]

            if product in product_quantity:
                product_quantity[product] += quantity
            else:
                product_quantity[product] = quantity

        lowest_product = min(
            product_quantity,
            key=product_quantity.get
        )

        lowest_quantity = product_quantity[lowest_product]

        if lowest_quantity <= 2:
            problems.append(
                f"Low demand for product: {lowest_product}"
            )

    # ---------- Final Result ----------

    if len(problems) == 0:

        print(" No major problems detected!")
        print("Business is performing well.")

    else:

        print("\n PROBLEMS DETECTED:")

        for problem in problems:
            print("-", problem)

# ================= BUSINESS RECOMMENDATION =================

def business_recommendation():

    print("\n========== BUSINESS RECOMMENDATION ==========")

    revenue = 0

    for sale in sales:
        revenue += sale["total"]

    # Revenue recommendation

    if revenue < 10000:

        print(" Increase promotions and focus on high-demand products.")

    else:

        print(" Revenue level is healthy.")

    # Customer recommendation

    new_customers = 0
    returning_customers = 0

    for customer in customers:

        if customer["type"].lower() == "new":
            new_customers += 1

        elif customer["type"].lower() == "returning":
            returning_customers += 1

    total_customers = new_customers + returning_customers

    if total_customers > 0:

        retention = (returning_customers / total_customers) * 100

        if retention < 30:

            print(
                " Launch loyalty offers to increase returning customers."
            )

        else:

            print(
                " Customer retention is good."
            )

    # Product recommendation

    if len(sales) > 0:

        product_quantity = {}

        for sale in sales:

            product = sale["product"]
            quantity = sale["quantity"]

            if product in product_quantity:
                product_quantity[product] += quantity
            else:
                product_quantity[product] = quantity

        lowest_product = min(
            product_quantity,
            key=product_quantity.get
        )

        print(
            f" Review the demand of '{lowest_product}' product."
        )



# ================= BUSINESS HEALTH SCORE =================

def business_health_score():

    print("\n========== BUSINESS HEALTH ==========")

    score = 0

    # ---------- Revenue Score ----------

    revenue = 0

    for sale in sales:
        revenue += sale["total"]

    if revenue >= 100000:
        revenue_score = 40

    elif revenue >= 50000:
        revenue_score = 30

    elif revenue >= 10000:
        revenue_score = 20

    elif revenue > 0:
        revenue_score = 10

    else:
        revenue_score = 0

    score += revenue_score

    # ---------- Customer Score ----------

    new_customers = 0
    returning_customers = 0

    for customer in customers:

        if customer["type"].lower() == "new":
            new_customers += 1

        elif customer["type"].lower() == "returning":
            returning_customers += 1

    total_customers = new_customers + returning_customers

    if total_customers > 0:

        retention = (
            returning_customers / total_customers
        ) * 100

    else:
        retention = 0

    if retention >= 70:
        customer_score = 30

    elif retention >= 50:
        customer_score = 25

    elif retention >= 30:
        customer_score = 15

    elif retention > 0:
        customer_score = 10

    else:
        customer_score = 0

    score += customer_score

    # ---------- Sales Score ----------

    total_sales = len(sales)

    if total_sales >= 20:
        sales_score = 30

    elif total_sales >= 10:
        sales_score = 25

    elif total_sales >= 5:
        sales_score = 20

    elif total_sales > 0:
        sales_score = 10

    else:
        sales_score = 0

    score += sales_score

    # ---------- Final Score ----------

    print("Revenue Score:", revenue_score, "/40")
    print("Customer Score:", customer_score, "/30")
    print("Sales Score:", sales_score, "/30")

    print("----------------------------")
    print("Overall Health Score:", score, "/100")

    if score >= 80:
        print("Status: EXCELLENT")

    elif score >= 60:
        print("Status: HEALTHY")

    elif score >= 40:
        print("Status: AVERAGE")

    else:
        print("Status: NEEDS IMPROVEMENT")



def main_menu():

    while True:

        print("\n========================================")
        print("   BUSINESS PROBLEM & DEMAND ANALYZER")
        print("========================================")

        print("\n----- CUSTOMER MANAGEMENT -----")
        print("1. Add Customer")
        print("2. Show Customers")
        print("3. Search Customer")

        print("\n----- SALES MANAGEMENT -----")
        print("4. Add Sale")
        print("5. Show Sales")

        print("\n----- SALES ANALYSIS -----")
        print("6. Total Revenue")
        print("7. Highest Sale")
        print("8. Best Selling Product")
        print("9. Worst Selling Product")
        print("10. Product-wise Revenue")
        print("11. Highest Revenue Product")

        print("\n----- CUSTOMER ANALYSIS -----")
        print("12. Customer Spending")
        print("13. Most Valuable Customer")
        print("14. Customer Type Analysis")

        print("\n----- BUSINESS INTELLIGENCE -----")
        print("15. Business Problem Detector")
        print("16. Business Recommendation")
        print("17. Business Health Score")

        print("\n18. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            show_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            add_sale()

        elif choice == "5":
            show_sales()

        elif choice == "6":
            total_revenue()

        elif choice == "7":
            highest_sale()

        elif choice == "8":
            best_selling_product()

        elif choice == "9":
            worst_selling_product()

        elif choice == "10":
            product_revenue()

        elif choice == "11":
            highest_revenue_product()

        elif choice == "12":
            customer_spending()

        elif choice == "13":
            most_valuable_customer()

        elif choice == "14":
            customer_type_analysis()

        elif choice == "15":
            business_problem_detector()

        elif choice == "16":
            business_recommendation()

        elif choice == "17":
            business_health_score()

        elif choice == "18":
            print("\nThank you for using Business Analyzer!")
            break

        else:
            print("\nInvalid choice! Please try again.")


main_menu()