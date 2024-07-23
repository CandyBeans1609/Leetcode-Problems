
## Determine if a Number is a Power of Two ([Leetcode - 231](https://leetcode.com/problems/power-of-two/))

Write a function that determines if a given integer is a power of two

<br>



## 🌟 How it works

The code checks if a given integer `n` is a power of two. It starts by returning `False` if `n` is less than or equal to zero, as powers of two are always positive. It then initializes a variable `x` to 1 and repeatedly doubles `x` until it is no longer less than `n`. Finally, it returns `True` if `x` equals `n` (indicating `n` is a power of two) and `False` otherwise.

The corrected code creates an instance of the `Solution` class and calls the `isPowerOfTwo` method on it with the values 1, 16, and 3, printing the results.

<br>

## ✅ Test Cases


![image](https://github.com/user-attachments/assets/b12ff8e7-e0af-4b6f-9cdc-5ad7da75ee6c)


![image](https://github.com/user-attachments/assets/3b3495dd-2427-4de9-9b60-0798bdb8d453)


![image](https://github.com/user-attachments/assets/8fbfd86a-0eda-4fac-8b5d-31de0626d2dd)

<br>

## 📜 Conclusion

The isPowerOfTwo(n) function effectively determines if a given integer is a power of two through a straightforward and iterative approach. By checking the input's validity and multiplying a base value (starting at 1) by 2 until it meets or exceeds the input, the function can accurately identify powers of two. This method ensures that the function can handle both positive and non-positive integers, providing a reliable tool for this specific mathematical check. The user interaction allows for easy testing and validation of various input values, confirming the function's correctness and utility.
<br>

## ⚙️ Prerequisites

Install Python 3 to run the code.

<br>

## 🛠️ How to Run

```python3
  python3 powertwo.py
```

<br>

## 📺 Output

![image](https://github.com/user-attachments/assets/0af0fe2c-053d-470f-bdff-3ae549d5b1cc)


<br>

## 👻 Author
[Akanksha Kanade](https://github.com/CandyBeans1609)
