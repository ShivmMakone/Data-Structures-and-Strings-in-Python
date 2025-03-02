Data Structures and Strings in Python

## Task 1: Create a Dictionary of Student Marks

### Description:
- This program creates a **dictionary** where student names are the **keys** and their marks are the **values**.
- It asks the user to input a student's name.
- The program retrieves and displays the corresponding marks for the student.
- If the student’s name is not found, an appropriate message is displayed.

### Code Explanation:
- A dictionary `student_data` is defined with student names as keys and their marks as values.
- The user is prompted to enter a student's name.
- The program checks if the student's name exists in the dictionary and prints the corresponding marks.
- If the name is not found, the program displays a "Student not found" message.

### How to Run:
1. Run `student_marks.py` in any Python environment.
2. Enter a student's name when prompted.
3. The program will display the marks for the student or an error message if the student doesn't exist in the dictionary.

### Example Output:
**If the student exists:**
Enter the student's name: Alice Alice's marks: 85

**If the student does not exist:**
Enter the student's name: John Student not found.




## Task 2: Demonstrate List Slicing

### Description:
- This program demonstrates **list slicing** using a list of numbers from 1 to 10.
- It extracts the **first five elements** from the list.
- It then **reverses** the extracted elements.
- Both the **extracted list** and the **reversed list** are printed.

### Code Explanation:
- The list `ori_list` is created with numbers from 1 to 10.
- The program slices the list to extract the first five elements.
- The extracted elements are then reversed using list slicing.
- Both the extracted and reversed lists are printed.

### How to Run:
1. Run `list_slicing.py` in any Python environment.
2. The program will print the original list, the extracted elements, and the reversed list.

### Example Output:
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
Extracted first five elements: [1, 2, 3, 4, 5] 
Reversed extracted elements: [5, 4, 3, 2, 1]
