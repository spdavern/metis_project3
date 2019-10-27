

# Challenge Set 9

## Part I: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?

`SELECT * FROM Customers WHERE Country='UK';`

Gives the result:

| **CustomerID** | **CustomerName**      | **ContactName**   | **Address**                  | **City** | **PostalCode** | **Country** |
| -------------- | --------------------- | ----------------- | ---------------------------- | -------- | -------------- | ----------- |
| 4              | Around the Horn       | Thomas Hardy      | 120 Hanover Sq.              | London   | WA1 1DP        | UK          |
| 11             | B's Beverages         | Victoria Ashworth | Fauntleroy Circus            | London   | EC2 5NT        | UK          |
| 16             | Consolidated Holdings | Elizabeth Brown   | Berkeley Gardens 12 Brewery  | London   | WX1 6LT        | UK          |
| 19             | Eastern Connection    | Ann Devon         | 35 King George               | London   | WX3 6FW        | UK          |
| 38             | Island Trading        | Helen Bennett     | Garden House Crowther Way    | Cowes    | PO31 7PJ       | UK          |
| 53             | North/South           | Simon Crowther    | South House 300 Queensbridge | London   | SW7 1RZ        | UK          |
| 72             | Seven Seas Imports    | Hari Kumar        | 90 Wadhurst Rd.              | London   | OX15 4NB       | UK          |

2. What is the name of the customer who has the most orders?

```sql
SELECT Max(CountOfOrders), CustomerName FROM
(SELECT count(OrderID) as CountOfOrders, CustomerName FROM
(SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID)
GROUP BY CustomerName ORDER BY CountOfOrders DESC);
```

Gives the results:

| MAX(CountOfOrders) | CustomerName |
| ------------------ | ------------ |
| 10                 | Ernst Handel |

3. Which supplier has the highest average product price?

```sql
SELECT SupplierName, MAX(AvgProdPrice) FROM
(SELECT SupplierName, AVG(Price) As AvgProdPrice FROM
(SELECT Products.ProductID, Products.SupplierID, Suppliers.SupplierName, Products.Price FROM Products
INNER JOIN Suppliers ON Products.SupplierID=Suppliers.SupplierID)
GROUP BY SupplierName);
```

Gives the result:

| **SupplierName**           | **MAX(AvgProdPrice)** |
| -------------------------- | --------------------- |
| Aux joyeux ecclésiastiques | 140.75                |

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

`SELECT Count(DISTINCT Country) FROM Customers;`

Gives the results:

| Count(DISTINCT Country) |
| :---------------------- |
| 21                      |

5. What category appears in the most orders?

```sql
SELECT CategoryName, MAX(NumOfOrdersContainingCategory) FROM
(SELECT CategoryName, Count(*) As NumOfOrdersContainingCategory FROM
(Select OrderDetails.OrderID, OrderDetails.ProductID, TBL1.CategoryName FROM OrderDetails
INNER JOIN 
(Select Products.ProductID, Categories.CategoryName FROM Products
INNER JOIN Categories ON Products.CategoryID=Categories.CategoryID) As TBL1
ON OrderDetails.ProductID=TBL1.ProductID)
GROUP BY CategoryName);
```

Gives the result:

| CategoryName   | MAX(NumOfOrdersContainingCategory) |
| :------------- | :--------------------------------- |
| Dairy Products | 100                                |

6. What was the total cost for each order?

```sql
SELECT OrderID, Round(SUM(Quantity*Price),2) As TotalCost FROM
(SELECT OrderID, Quantity, Price FROM OrderDetails LEFT JOIN Products ON OrderDetails.ProductID=Products.ProductID)
GROUP BY OrderID;
```

Gives the result:

| **OrderID** | **TotalCost** |
| ----------- | ------------- |
| 10248       | 566           |
| 10249       | 2329.25       |
| 10250       | 2267.25       |
| 10251       | 839.5         |
| 10252       | 4662.5        |
| 10253       | 1806          |
| 10254       | 781.5         |
| 10255       | 3115.75       |
| 10256       | 648           |
| 10257       | 1400.5        |
| 10258       | 2529.75       |
| 10259       | 126           |
| 10260       | 2183.9        |
| 10261       | 560           |
| etc...      |               |

7. Which employee made the most sales (by total price)?

```sql
SELECT MAX(TBL2.TotalSales) As MaxTotalSales, Employees.FirstName, Employees.LastName From
(SELECT EmployeeID, Round(SUM(TotalPrice),2) As TotalSales FROM
(SELECT TBL1.OrderID, TBL1.TotalPrice, Orders.EmployeeID FROM
(SELECT OrderID, Round(SUM(Quantity*Price),2) AS TotalPrice FROM
(SELECT OrderID, Quantity, Price FROM OrderDetails LEFT JOIN Products ON OrderDetails.ProductID=Products.ProductID)
GROUP BY OrderID) AS TBL1
LEFT JOIN Orders ON TBL1.OrderID=Orders.OrderID)
GROUP BY EmployeeID) AS TBL2
Inner Join Employees ON TBL2.EmployeeID=Employees.EmployeeID;
```

Gives the result:

| MaxTotalSales | FirstName | LastName |
| ------------- | --------- | -------- |
| 105696.5      | Margaret  | Peacock  |

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

`SELECT FirstName, LastName, Notes FROM Employees WHERE Notes LIKE '%BS%'`

Gives the result:

| FirstName | LastName  | Notes                                                        |
| --------- | --------- | ------------------------------------------------------------ |
| Janet     | Leverling | Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative. |
| Steven    | Buchanan  | Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London, where he was promoted to sales manager. Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management'. He is fluent in French. |

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

```sql
SELECT SupplierName, MAX(AvgProdPrice) FROM
(SELECT SupplierName, AVG(Price) As AvgProdPrice FROM
(SELECT Products.ProductID, Suppliers.SupplierName, Products.Price FROM Products
INNER JOIN Suppliers ON Products.SupplierID=Suppliers.SupplierID)
GROUP BY SupplierName
HAVING COUNT(ProductID)>2)
```

Gives the result:

| SupplierName  | MAX(AvgProdPrice) |
| :------------ | :---------------- |
| Tokyo Traders | 46                |

