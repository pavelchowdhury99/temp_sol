-- 1. Write the DDL statement that create a table named employees with the following columns:
-- ○ id (integer, primary key, auto-increment)
-- ○ name (string)
-- ○ department (string)
-- ○ salary (decimal)
-- ○ hire_date (date)

-- ANS:
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    department VARCHAR(255),
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- 2. Write SQL queries to perform the following operations:
-- ○ Insert several records into the employees table.

-- ANS
INSERT INTO employees (name, department, salary, hire_date) VALUES 
('Test Name 1', 'Department_1', 30000.00, '2021-01-01'),
('Test Name 2', 'Department_2', 10000.00, '2021-02-29'),
('Test Name 3', 'Department_2', 10000.00, '2021-03-11'),
('Test Name 4', 'Department_3', 30000.00, '2022-04-10'),
('Test Name 5', 'Department_4', 35000.00, '2024-06-06');

-- ○ Retrieve all employees in a specific department.
-- ANS
SELECT * FROM employees
WHERE department = 'Department_1';


-- ○ Update the salary of a specific employee.
-- ANS
UPDATE employees
SET salary = 15000.00
WHERE name = 'Test Name 3';

-- ○ Delete an employee record by ID.
-- ANS
DELETE FROM employees
WHERE id = 2;


-- ○ Retrieve the average salary of employees in each department.
-- ANS
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department;

-- ○ Given two tables, employees and departments, where the departments table contains information about department names and their IDs, write a query to retrieve a list of all employees along with their department names. If an employee does not belong to a department, their department name should show as NULL.
-- ANS
SELECT e.id, e.name, e.salary, e.hire_date, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department = d.id;

--------------- END ------------------------