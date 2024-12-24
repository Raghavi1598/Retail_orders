import streamlit as st
import mysql.connector
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Raghavi@1598"
)

mycursor = mydb.cursor()
mycursor.execute("USE retail_orders")

st.title('Retail Order Analysis')

# Create two tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

# Content for Tab 1
with tab1:
    st.subheader("Query Selection")
    option = st.selectbox(
        "Choose Your Query:",
        options=[
            "Find top 10 highest revenue generating products",
            "Find the top 5 cities with the highest profit margins",
            "Calculate the total discount given for each category",
            "Find the average sale price per product category",
            "Find the region with the highest average sale price",
            "Find the total profit per category",
            "Identify the top 3 segments with the highest quantity of orders",
            "Determine the average discount percentage given per region",
            "Find the product category with the highest total profit",
            "Calculate the total revenue generated per year"
        ]
    )

    # Query execution
    try:
        query = None

        # Define queries
        if option == "Find top 10 highest revenue generating products":
            query = """
                SELECT product_id, SUM(sale_price) AS sales
                FROM df_orders
                GROUP BY product_id
                ORDER BY sales DESC
                LIMIT 10;
            """
            st.subheader("Top 10 Highest Revenue Generating Products")

        elif option == "Find the top 5 cities with the highest profit margins":
            query = """
                SELECT city, SUM(profit) AS total_profit
                FROM df_order
                JOIN df_orders ON df_order.order_id = df_orders.order_id
                GROUP BY city
                ORDER BY total_profit DESC
                LIMIT 5;
            """
            st.subheader("Top 5 Cities with the Highest Profit Margins")

        elif option == "Calculate the total discount given for each category":
            query = """
                SELECT category, SUM(discount) AS total_discount 
            FROM df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id   
            GROUP BY category 
            LIMIT 0, 1000;
            """
            st.subheader("Total Discount Given for Each Category")

        elif option == "Find the average sale price per product category":
            query = """
                SELECT category, avg(sale_price) AS avg_sale_price 
            FROM df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id   
            GROUP BY category 
            LIMIT 0, 1000;
            """
            st.subheader("Average Sale Price per Product Category")

        elif option == "Find the region with the highest average sale price":
            query = """
                SELECT region, AVG(sale_price) AS avg_sale_price
            FROM  df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id
            GROUP BY region
            ORDER BY avg_sale_price DESC
            LIMIT 1;
            """
            st.subheader("Region with the Highest Average Sale Price")

        elif option == "Find the total profit per category":
            query = """
                SELECT category, SUM(profit) AS total_profit 
            FROM df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id   
            GROUP BY category 
            LIMIT 0, 1000; 
            """
            st.subheader("Total Profit per Category")

        elif option == "Identify the top 3 segments with the highest quantity of orders":
            query = """
                SELECT segment, SUM(quantity) AS total_quantity
            FROM df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id    
            GROUP BY segment
            ORDER BY total_quantity DESC
            LIMIT 3;
            """
            st.subheader("Top 3 Segments with the Highest Quantity of Orders")

        elif option == "Determine the average discount percentage given per region":
            query = """
                SELECT region, AVG(discount) AS average_discount_percentage
            FROM df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id
            GROUP BY region;
            """
            st.subheader("Average Discount Percentage Given per Region")

        elif option == "Find the product category with the highest total profit":
            query = """
                SELECT Category, SUM(Profit) AS TotalProfit
            FROM df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id  
            GROUP BY Category
            ORDER BY TotalProfit DESC
            LIMIT 1;
            """
            st.subheader("Product Category with the Highest Total Profit")

        elif option == "Calculate the total revenue generated per year":
            query = """
                SELECT YEAR(order_date) AS year, SUM(quantity) AS total_quantity
            FROM df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id 
            GROUP BY YEAR(order_date)
            ORDER BY year;
            """
            st.subheader("Total Revenue Generated per Year")

        # Execute and display results
        if query:
            mycursor.execute(query)
            results = mycursor.fetchall()
            if results:
                st.table(results)
            else:
                st.info("No results found for the selected query.")
        else:
            st.warning("Please select a valid query.")

    except mysql.connector.Error as e:
        st.error(f"Error executing query: {e}")

# Content for Tab 2
with tab2:
    st.subheader("Advanced Query Selection")
    option = st.selectbox(
        "Choose Your Query:",
        options=[
            "Increase the list price by 100 rupees for the first order ID",
            "Determine the minimum profit in each subcategory",
            "Identify the minimum, maximum, and average values in each category",
            "Identify up to 10 subcategories within each category",
            "Combine two tables using a left join based on state and subcategory",
            "Combine two tables using a right join based on state and subcategory",
            "Identify the category where the subcategory is 'Art'",
            "Retrieve the top 10 regions and convert their names to uppercase",
            "Identify the top 50 ranks within the category",
            "Determine the total count of subcategories within each category"
        ]
    )

    try:
        query = None

        # Define queries for Tab 2
        if option == "Increase the list price by 100 rupees for the first order ID":
            query = """
                SELECT order_id, list_price + 100 AS new_price
                FROM df_orders
                WHERE order_id = 1;
            """
            st.subheader("List Price Increased by 100 Rupees")

        elif option == "Determine the minimum profit in each subcategory":
            query = """
                SELECT sub_category, MIN(profit) AS min_profit
                FROM df_orders
                GROUP BY sub_category;
            """
            st.subheader("Minimum Profit in Each Subcategory")

        elif option == "Identify the minimum, maximum, and average values in each category":
            query = """
                select category,min(profit),max(profit),avg(profit) from df_order 
                JOIN df_orders ON df_order.order_id = df_orders.order_id group by category;
            """
            st.subheader("The minimum, maximum, and average values in each category")

        elif option == "Identify up to 10 subcategories within each category":
            query = """
                select category,sub_category 
                from df_order JOIN df_orders ON df_order.order_id = df_orders.order_id
                limit 10;
            """
            st.subheader("10 subcategories within each category")

        elif option == "Combine two tables using a left join based on state and subcategory":
            query = """
                SELECT 
                df_order.order_id AS order_id, 
                df_order.state AS state,
                df_orders.sub_category AS sub_category
                FROM 
                df_order LEFT JOIN  df_orders ON 
                df_order.order_id = df_orders.order_id
                LIMIT 10;
            """
            st.subheader("left join based on state and subcategory")

        elif option == "Combine two tables using a right join based on state and subcategory":
            query = """
                SELECT 
                df_order.order_id AS order_id, 
                df_orders.sub_category AS sub_category,
                df_order.state AS state
                FROM  df_order RIGHT JOIN  df_orders ON  df_order.order_id = df_orders.order_id
                LIMIT 10; 
            """
            st.subheader("Right join based on state and subcategory")

        elif option == "Identify the category where the subcategory is 'Art'":
            query = """
                SELECT DISTINCT category 
                FROM df_order 
                WHERE order_id IN (
                 SELECT order_id 
                FROM df_orders 
                 WHERE sub_category = 'Art')
                LIMIT 3;
                """
            st.subheader("Categories where the subcategory is 'Art'")

        elif option == "Retrieve the top 10 regions and convert their names to uppercase":
            query = """
                select upper(region) from df_order limit 10;
            """
            st.subheader("The top 10 regions and convert their names to uppercase")

        elif option == "Identify the top 50 ranks within the category":
            query = """
                select sub_category, dense_rank() 
                over (order by quantity desc) 
                from df_orders
                limit 50;
            """
            st.subheader("Top 50 ranks within the category")

        elif option == "Determine the total count of subcategories within each category":
            query = """
                SELECT YEAR(order_date) AS year, SUM(quantity) AS total_quantity
            FROM df_order 
            JOIN df_orders ON df_order.order_id = df_orders.order_id 
            GROUP BY YEAR(order_date)
            ORDER BY year;
            """
            st.subheader("Total count of subcategories within each category")

        # Execute and display results
        if query:
            mycursor.execute(query)
            results = mycursor.fetchall()
            if results:
                st.table(results)
            else:
                st.info("No results found for the selected query.")
        else:
            st.warning("Please select a valid query.")

    except mysql.connector.Error as e:
        st.error(f"Error executing query: {e}")