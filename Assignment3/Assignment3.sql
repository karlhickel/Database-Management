/*
1
 */
SELECT ProductName, QuantityPerUnit
FROM Product;

/*
2
 */
SELECT Id,ProductName
FROM Product
WHERE Discontinued = 0;

/*
3
 */
SELECT Id,ProductName
FROM Product
WHERE Discontinued = 1;

/*
4
 */

SELECT ProductName, MAX(UnitPrice)
FROM Product;

SELECT ProductName, MIN(UnitPrice)
FROM Product;

/*
5
 */

SELECT Id,ProductName,UnitPrice
FROM Product
WHERE UnitPrice < 20;

/*
6
 */

SELECT Id,ProductName,UnitPrice
FROM Product
WHERE UnitPrice < 25 AND UnitPrice > 15;

/*
7
 */
SELECT ProductName,UnitPrice
FROM Product
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Product);

/*
8
 */

SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;

/*
9
 */
SELECT COUNT(Discontinued)
FROM Product
WHERE Discontinued = 1;

SELECT COUNT(Discontinued)
FROM Product
WHERE Discontinued = 0;

/*
10
 */

SELECT ProductName,UnitsOnOrder, UnitsInStock
FROM Product
WHERE UnitsInStock < UnitsOnOrder