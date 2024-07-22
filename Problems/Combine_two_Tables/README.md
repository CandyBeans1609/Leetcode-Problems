
## Combine Two Tables ([Leetcode #175](https://leetcode.com/problems/combine-two-tables/description/))

<br>

## 📚 Description:
Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.
Return the result table in any order.
<br>


##  Example
The result format is in the following example.

### Person table:

|  personId  | lastName  | firstName |
| :----------| :-------  | :-------- |
| 1          |   Wang    | Allen     |
| 2          |   Alice   | Bob       |

### Address table:

| addressId   | personId  | city           | state      |
| :---------- | :-------  | :------------- | :--------- |
| 1           |    2      | New York City  | New York   |
| 2           |    3      | Leetcode       | California |

### Output:

|  firstName  | lastName | city          | state  |
| :-----------| :------  | :----------   |:-------|
| Allen       |   Wang   | NULL          |NULL    |
| Bob         |   Alice  | New York City |New York|

<br>

## 🌟Explanation: 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.

<br>

## ⚙️ Prerequisites

Basic SQL Knowledge: Understanding of basic SQL queries, especially JOIN operations and handling NULL values.

<br>

## ✅ Test Cases

![image](https://github.com/user-attachments/assets/821e5fa8-6328-45ee-94fa-2ea545a91b46)

<br>

## 📺 Output

![image](https://github.com/user-attachments/assets/b31f1552-609a-4e77-a78e-fa360ee60db5)

<br>

## 📜 Conclusion
This solution demonstrates how to use a `LEFT JOIN` to combine data from the `Person` and `Address` tables, 
ensuring all persons are listed even if they don't have a corresponding address. 
By returning `NULL` for missing address information, it provides a comprehensive report of each person's name and address details where available.

<br>

## 👻 Author
[Akanksha Kanade](https://github.com/CandyBeans1609)
