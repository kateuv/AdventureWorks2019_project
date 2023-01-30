USE AdventureWorks2019;

--What are the regional sales in the best performing country?
SELECT CountryRegionCode,name AS Region, sum(SalesYTD) AS Sales
FROM Sales.SalesTerritory
GROUP BY CountryRegionCode, name;
--Query result shows US as best performing country
--Select regional sales on the US
SELECT name AS Region, SalesYTD AS Sales
FROM Sales.SalesTerritory
WHERE CountryRegionCode  IN  ('US')
ORDER BY SalesYTD;

--What is the relationship between annual leave taken and bonus?

SELECT SUM(VacationHours) AS  "Average Hours", Bonus,
CASE WHEN AVG(Bonus) = 0.00 THEN 'No bonus'
  WHEN AVG(Bonus) < 3000 THEN 'Small bonus'
  WHEN AVG(Bonus) < 5000 THEN 'Medium bonus'
  ELSE 'Large bonus'
END AS "Average bonus"
FROM HumanResources.Employee
INNER JOIN Sales.SalesPerson ON HumanResources.Employee.BusinessEntityID=Sales.SalesPerson.BusinessEntityID
GROUP BY Bonus;

--What is the relationship between country and revenue?
--To get the sum of total revenue select columuns from two tables 

SELECT SUM([TotalDue]),CountryRegionCode
FROM [Sales].[SalesOrderHeader]
JOIN [Sales].[SalesTerritory] ON [SalesOrderHeader].TerritoryID = [SalesTerritory] .TerritoryID
GROUP BY CountryRegionCode
ORDER BY SUM([TotalDue]);

--What is the relationship between sick leave and JobTitle(PersonType)?
--SELECT the datacolumns Sickleavehours, Jobtitle,PersonType

SELECT e.JobTitle, COUNT(P.PersonType) AS PersonType, AVG(e.SickLeaveHours) AS AverageSickLeaveHours
FROM HumanResources.Employee AS e
--Join Person table to get PersonType using BusinessEntityID
JOIN Person.Person AS p
ON e.BusinessEntityID = p.BusinessEntityID
GROUP BY p.PersonType, e.JobTitle
--Reduce JobTitle variables using person type
HAVING COUNT(P.PersonType) > 1
ORDER BY AverageSickLeaveHours, PersonType;

--What is the relationship between store trading duration and revenue?

SELECT [Name], AnnualRevenue, YearOpened
FROM Sales.vStoreWithDemographics;

--What is the relationsip between the size of the stores, number of employees and revenue?
--Data columns are as follow
SELECT AnnualRevenue, SquareFeet, NumberEmployees
--Table name is as follows
FROM Sales.vStoreWithDemographics;