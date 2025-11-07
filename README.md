# 🐍 AI/ML Python Learning Journey

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Included-green.svg)](https://numpy.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)

A comprehensive collection of Python fundamentals, data structures, and NumPy for AI/ML learning. This repository documents my learning journey from basic Python concepts to advanced NumPy operations essential for machine learning and data science.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Module Details](#module-details)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Learning Path](#learning-path)
- [Contributing](#contributing)

---

## 🎯 Overview

This repository contains hands-on Python code examples, exercises, and Jupyter notebooks covering:
- **Python Fundamentals**: Variables, data types, operators, control flow
- **Data Structures**: Lists, tuples, sets, dictionaries
- **Functions**: Arguments, lambda functions, map/filter/reduce
- **Object-Oriented Programming**: Classes, inheritance, polymorphism, encapsulation
- **File Handling**: Reading, writing, and manipulating files
- **NumPy**: Arrays, operations, linear algebra, statistics
- **Pandas**: DataFrames, data loading, cleaning, preprocessing, and analysis

---

## 📁 Repository Structure

```
AI_ML_Python/
│
├── Python/                          # Beginner Python scripts
│   ├── first.py                    # Hello World
│   ├── variable.py                 # Variable basics
│   └── input_take.py               # User input handling
│
├── Module_1/                        # Python Fundamentals
│   ├── python_basic_fundamentals.py    # Core types, literals
│   ├── comprehension.py                # List/Dict comprehensions
│   ├── basic_slice.py                  # Slicing operations
│   ├── loop_practise.py                # Loop exercises
│   ├── nested_data_structure.py        # Nested lists/dicts
│   └── exercise_comprehension.py       # Comprehension problems
│
├── Module_2/                        # Operators and Input (Notebooks)
│   ├── variable.ipynb              # Variables in depth
│   ├── arithmatic-operator.ipynb   # Arithmetic operations
│   ├── comparison_operator.ipynb   # Comparison operators
│   ├── logical_operator.ipynb      # Logical operators
│   ├── iput.ipynb                  # Input handling
│   └── digit_summation_problem_solve.ipynb
│
├── Module_3/                        # Control Flow (Notebooks)
│   ├── if_else_statement.ipynb     # Conditional statements
│   ├── loop.ipynb                  # For & While loops
│   ├── continue_break.ipynb        # Loop control
│   ├── positive_negative_even_odd.ipynb
│   ├── max-min-problem.ipynb       # Min/Max problems
│   └── digit_problem.ipynb         # Digit manipulation
│
├── Module_3_list.ipynb             # Lists in Detail
├── Module_3_string.ipynb           # String Operations
├── Module_5_tuple_dict_set.ipynb   # Tuples, Dicts, Sets
├── Module_6_Function.ipynb         # Functions & Functional Programming
├── Module7.ipynb                   # File Handling
├── Module_8.ipynb                  # Object-Oriented Programming
├── Module_10.ipynb                 # NumPy Basics & Arrays
├── Module_11.ipynb                 # NumPy Advanced & Linear Algebra
├── Module_12_Related_File/         # Pandas - Data Analysis & Manipulation
│   ├── Module_12.ipynb             # Pandas complete tutorial
│   ├── student_data (1).csv        # Sample CSV dataset
│   ├── phitron_student_marks.xlsx  # Sample Excel dataset
│   ├── students.parquet            # Sample Parquet dataset
│   └── data.json                   # Sample JSON dataset
└── start.ipynb                     # Quick Start
```

---

## 📖 Module Details

### 🟢 Python Folder - Getting Started
**Beginner-friendly Python scripts**
- `first.py`: Your first "Hello World" program
- `variable.py`: Understanding variables and data types
- `input_take.py`: Taking user input in Python

---

### 🔵 Module 1 - Python Fundamentals
**Core Python concepts and data structures**

#### Key Topics:
- ✅ **Data Types**: int, float, str, bool, list, tuple, dict, set
- ✅ **List Comprehensions**: Efficient list creation
- ✅ **Dictionary Comprehensions**: Key-value pair generation
- ✅ **Slicing**: Array/list slicing operations
- ✅ **Nested Data Structures**: Working with nested lists and dicts
- ✅ **Loops**: For and while loop practice

#### Files:
- `python_basic_fundamentals.py`: Core types, literals, and basic operations
- `comprehension.py`: List/dict/set comprehensions
- `basic_slice.py`: Slicing techniques
- `loop_practise.py`: Loop exercises
- `nested_data_structure.py`: Nested structures handling
- `nested_comprehension_practise2.py`: Advanced comprehensions

---

### 🟡 Module 2 - Operators and Input (Jupyter Notebooks)
**Understanding operators and user interaction**

#### Topics Covered:
- ➕ **Arithmetic Operators**: +, -, *, /, %, //, **
- 🔍 **Comparison Operators**: ==, !=, <, >, <=, >=
- 🔗 **Logical Operators**: and, or, not
- 📥 **Input Handling**: Taking and processing user input
- 🧮 **Problem Solving**: Digit summation problems

---

### 🟣 Module 3 - Control Flow (Jupyter Notebooks)
**Decision making and loops**

#### Topics Covered:
- 🔀 **If-Else Statements**: Conditional logic
- 🔁 **Loops**: For loops, while loops, nested loops
- ⏭️ **Loop Control**: break, continue statements
- 🎲 **Problem Solving**:
  - Positive/Negative/Even/Odd detection
  - Max/Min finding algorithms
  - Digit manipulation problems

---

### 🟠 Module 3 Extended - Data Structures

#### **Module_3_list.ipynb** - Lists Deep Dive
- ✅ List declaration and initialization
- ✅ Accessing and modifying elements
- ✅ List methods: append(), insert(), pop(), remove()
- ✅ Sorting and reversing: sort(), reverse()
- ✅ **Stack Implementation**: LIFO (Last In First Out)
- ✅ **Queue Implementation**: FIFO (First In First Out)
- ✅ **List Comprehensions**: Creating lists efficiently

#### **Module_3_string.ipynb** - String Manipulation
- ✅ String declaration and types
- ✅ Multi-line strings
- ✅ Indexing and slicing
- ✅ **String Methods**:
  - lower(), capitalize(), len()
  - find(), count(), replace()
- ✅ **String Operations**:
  - Splitting and joining
  - String formatting (f-strings)
  - Percentage formatting

---

### 🔴 Module 5 - Tuples, Dictionaries & Sets
**Advanced data structures**

#### **Module_5_tuple_dict_set.ipynb** Topics:

#### 📦 Tuples
- Immutable sequences
- Accessing and slicing
- count() and index() methods
- Use cases for immutability

#### 📖 Dictionaries
- Key-value pairs
- Accessing: dict["key"], get()
- Adding/updating: dict["key"] = value, update()
- Methods: keys(), values(), items()
- Dictionary comprehensions
- Iteration over dictionaries

#### 🎲 Sets
- Unique elements collection
- Adding and removing: add(), pop(), remove()
- **Mathematical Operations**:
  - Union, Intersection
  - isdisjoint(), issubset()

#### 💡 Problem Solving:
- Finding unique values in lists
- Word frequency counter

---

### 🟢 Module 6 - Functions & Functional Programming
**Mastering functions in Python**

#### **Module_6_Function.ipynb** Topics:

#### 🔧 Function Basics
- Defining functions with `def`
- Parameters and arguments
- Return values and multiple returns
- Unpacking return values

#### 📝 Function Arguments
- **Positional arguments**: Order matters
- **Keyword arguments**: Named parameters
- **\*args**: Variable positional arguments
- **\*\*kwargs**: Variable keyword arguments

#### 🎯 Advanced Concepts
- **Iterators**: iter(), next()
- **Generators**: yield keyword for lazy evaluation
- **Lambda Functions**: Anonymous functions
- **Map**: Apply function to iterables
- **Filter**: Filter elements based on condition
- **Reduce**: Aggregate operations (from functools)

#### 💻 Practical Examples:
- Square addition functions
- Data loader with chunking
- String manipulation with map/filter
- Finding max with reduce

---

### 🟣 Module 7 - File Handling
**Reading and writing files**

#### **Module7.ipynb** Topics:
- 📖 **Reading Files**:
  - read(), readlines()
  - Line-by-line iteration
- ✍️ **Writing Files**:
  - Creating new files
  - Overwriting with 'w' mode
  - Appending with 'a' mode
- 🔒 **Context Managers**: Using `with` statement
- 📝 Writing lists: writelines()

---

### 🔵 Module 8 - Object-Oriented Programming
**Classes and OOP principles**

#### **Module_8.ipynb** Topics:

#### 🏗️ Classes and Objects
- Class definition
- `__init__()` constructor
- Instance variables and methods
- Class variables

#### 🧬 Inheritance
- **Single Inheritance**: Parent → Child
- **Multiple Inheritance**: Multiple parents
- `super()` function for parent class access

#### 🔄 Polymorphism
- Method overriding
- Same method, different behaviors

#### 🔐 Encapsulation
- Private variables: `__variable`
- Getter methods: `get_variable()`
- Setter methods: `set_variable()`

#### 🎨 Abstraction
- Abstract Base Classes (ABC)
- @abstractmethod decorator
- Enforcing method implementation

#### 📱 Real-World Examples:
- Phone class hierarchy
- SmartPhone with cooling system
- Camera types (Smart, DSLR, Drone)

---

### 🟡 Module 10 - NumPy Fundamentals
**Introduction to NumPy for ML/AI**

#### **Module_10.ipynb** Topics:

#### 📊 NumPy Arrays (ndarray)
- **1D, 2D, 3D arrays**: Multi-dimensional arrays
- **Array Attributes**:
  - ndim, shape, dtype, size

#### 🎯 Array Creation
- **From existing data**: lists, tuples, sets, dicts
- **From scratch**:
  - zeros(), ones(), empty(), full()
  - zeros_like(), ones_like(), empty_like()
- **Random arrays**:
  - random.rand(), random.randint(), random.uniform()
- **Range functions**:
  - arange(), linspace(), logspace()
- **Matrix creation**:
  - diag(), eye() (identity matrix)

#### 🔍 Indexing and Slicing
- **1D slicing**: arr[start:end:step]
- **2D slicing**: arr[rows, columns]
- **Advanced indexing**: Boolean and fancy indexing
- **Copy vs View**: Understanding memory

#### 🔄 Array Manipulation
- reshape(), flatten(), ravel()
- Iteration with nditer()

---

### 🔴 Module 11 - NumPy Advanced Operations
**Advanced NumPy for Data Science**

#### **Module_11.ipynb** Topics:

#### 🔗 Array Operations
- **Concatenation**: Row-wise and column-wise
- **Transpose**: .T attribute
- **Splitting**: array_split()

#### ➗ Mathematical Operations
- **Arithmetic**: add(), subtract(), multiply(), divide()
- **Trigonometry**: sin(), cos(), tan(), rad2deg()
- **Logarithms**: log10(), log2()
- **Roots**: sqrt()
- **Aggregation**: sum(), cumsum()

#### 📡 Broadcasting
- Scalar operations on arrays
- Vector operations on matrices
- Broadcasting rules

#### 🔎 Logical & Comparison
- Comparison operators: >, <, ==, !=
- all(), any() functions
- Element-wise comparisons

#### 📈 Sorting & Searching
- sort(), np.sort()
- Sorting 2D arrays (axis=0, axis=1)
- where() function
- argmax(), argmin()

#### 📊 Statistical Functions
- max(), min(), mean(), median()
- std() (standard deviation)
- unique(), count_nonzero()
- corrcoef() (correlation)

#### 🧮 Linear Algebra
- **Matrix operations**:
  - dot() (dot product)
  - trace() (diagonal sum)
- **Matrix properties**:
  - det() (determinant)
  - matrix_rank()
  - linalg.inv() (inverse)

#### 📁 Data Loading
- genfromtxt() for CSV files
- Loading student scores dataset

---

### 🟢 Module 12 - Pandas for Data Analysis
**Complete guide to Pandas library**

#### **Module_12.ipynb** Topics:

#### 📊 Introduction to Pandas
- What is Pandas?
- Data cleaning and preprocessing
- Data analysis capabilities
- **DataFrame**: Core tabular data structure
- **Series**: Single column data structure

#### 📂 Loading Different File Formats
- **CSV files**: read_csv()
- **Excel files**: read_excel() (.xlsx)
- **Parquet files**: read_parquet()
- **JSON files**: read_json()

#### 🔍 Basic DataFrame Operations
- **Viewing data**:
  - head(), tail() - First/last rows
  - sample() - Random samples
  - info() - DataFrame information
  - describe() - Statistical summary
- **DataFrame attributes**:
  - columns - Column names
  - index - Row indices
  - shape, size, dtypes

#### 🏗️ Creating DataFrames
- From **lists**: pd.DataFrame(list)
- From **tuples**: pd.DataFrame(tuple)
- From **dictionaries**: pd.DataFrame(dict)
- From **list of dictionaries**
- Custom index and column names

#### 🎯 Accessing Data
- **Column selection**: df['column_name']
- **loc[]**: Label-based indexing
  - Single row: df.loc[0]
  - Multiple rows: df.loc[[2,5,17]]
  - Row ranges: df.loc[4:18]
  - Single column: df.loc[:, 'ColumnName']
  - Multiple columns: df.loc[:, ['Col1', 'Col2']]
  - Rows with columns: df.loc[3:7, 'Column']
- **iloc[]**: Integer position-based indexing

#### ✏️ Modifying DataFrames
- **Index operations**:
  - set_index() - Set custom index
  - reset_index() - Reset to default
- **Renaming**:
  - rename() - Rename columns/rows
- **Changing values**:
  - Single cell: df.loc[row, col] = value
  - Multiple cells: df.loc[3:6, 'Col'] += 2
- **Deletion**:
  - drop() - Remove rows/columns
  - inplace parameter for permanent changes

#### 🔄 Iteration
- **iterrows()**: Iterate as (index, Series) pairs
- **itertuples()**: Iterate as named tuples

#### 📈 Sorting Data
- **sort_values()**: Sort by column values
  - Single column sorting
  - Multiple column sorting
  - ascending/descending order
  - Custom sorting: ascending=[0,1]

#### 🔎 Filtering Data
- **Conditional filtering**:
  - Single condition: df.loc[df['Col'] == value]
  - Multiple conditions with & (and)
  - Multiple conditions with | (or)
- **Boolean indexing**
- **Comparison operators**: ==, !=, >, <, >=, <=

#### 📚 Sample Datasets Included
- **student_data.csv**: Student information
- **phitron_student_marks.xlsx**: Course marks data
- **students.parquet**: Compressed student data
- **data.json**: JSON format data

#### 💡 Real-World Applications
- Student performance analysis
- Completion status tracking
- Marks filtering and sorting
- Data quality assessment

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

```bash
Python 3.x
NumPy
Pandas
Jupyter Notebook (optional, for .ipynb files)
```

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Jami40/AI_ML_Python.git
cd AI_ML_Python
```

2. **Install required packages**:
```bash
pip install numpy pandas jupyter openpyxl pyarrow
```

3. **Run Python scripts**:
```bash
python Python/first.py
python Module_1/comprehension.py
```

4. **Run Jupyter Notebooks**:
```bash
jupyter notebook
# Then navigate to any .ipynb file
```

---

## 📝 Usage

### For Beginners:
1. Start with **Python/** folder for basic syntax
2. Move to **Module_1/** for fundamental concepts
3. Practice with **Module_2/** and **Module_3/** notebooks

### For Intermediate Learners:
1. Deep dive into data structures: **Module_3_list.ipynb**, **Module_5_tuple_dict_set.ipynb**
2. Master functions: **Module_6_Function.ipynb**
3. Learn OOP: **Module_8.ipynb**

### For AI/ML Enthusiasts:
1. Start with **Module_10.ipynb** for NumPy basics
2. Advance to **Module_11.ipynb** for statistical operations
3. Master **Module_12_Related_File/Module_12.ipynb** for Pandas and data analysis
4. Practice with real datasets (CSV, Excel, JSON, Parquet)

---

## 🎓 Learning Path

```
Week 1-2: Python Basics
├── Python syntax and variables
├── Data types and operators
└── Control flow (if-else, loops)

Week 3-4: Data Structures
├── Lists, tuples, sets
├── Dictionaries
└── Comprehensions

Week 5-6: Functions & OOP
├── Function definitions
├── Lambda, map, filter, reduce
└── Classes and inheritance

Week 7-8: NumPy Mastery
├── Array creation and manipulation
├── Mathematical operations
└── Linear algebra for ML

Week 9-10: Pandas for Data Science
├── DataFrames and Series
├── Data loading (CSV, Excel, JSON, Parquet)
├── Data manipulation and cleaning
└── Filtering and sorting data
```

---

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **NumPy**: Numerical computing library
- **Pandas**: Data analysis and manipulation library
- **Jupyter Notebooks**: Interactive coding environment

---

## 📊 Key Highlights

✅ **60+ Python scripts and notebooks**  
✅ **Comprehensive coverage** from basics to advanced  
✅ **Hands-on exercises** and problem-solving  
✅ **Real-world examples** (Phone classes, student scores)  
✅ **NumPy for ML/AI** preparation  
✅ **Pandas for data analysis** with real datasets  
✅ **Multiple file formats** (CSV, Excel, JSON, Parquet)  
✅ **Well-documented code** with comments  

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions or find issues:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📧 Contact

**Repository Owner**: Jami40  
**Repository**: [AI_ML_Python](https://github.com/Jami40/AI_ML_Python)  

---

## 📜 License

This project is open-source and available for educational purposes.

---

## 🌟 Acknowledgments

Special thanks to **Phitron** for the structured AI/ML curriculum and learning materials.

---

<div align="center">

### ⭐ If you find this repository helpful, please give it a star! ⭐

**Happy Learning! 🚀**

</div>
