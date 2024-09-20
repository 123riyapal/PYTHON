## Python Notes

### `__pycache__` Directory

- **Purpose**: This directory is created when one Python file imports another.
- **Excludes Top-Level Files**: It's not generated for top-level files.
- **Contents**: Inside this folder, a file is created indicating the imported file's name, Python version, and standard used.
- **Functionality**: The contents of `__pycache__` act as "frozen binaries," enabling independent execution.

### Python Virtual Machine

- **Execution Engine**: Responsible for running Python bytecode.
- **Runtime Engine**: Also known as the Python interpreter.
- **Interprets Bytecode**: Bytecode isn't machine code; it's Python-specific.
- **Variants**: 
  - `cpython`: The standard implementation.
  - `jython`: Runs on the Java Virtual Machine (JVM).
  - `IronPython`: Targets the .NET framework.
  - `Stackless Python`: Focuses on concurrency.
  - `PyPy`: Emphasizes speed through a Just-In-Time (JIT) compiler.

## Data Types
- **Numbers**: `1234`, `2.123`, `3+2i`, `0b111`, `Decimal()`, `Fraction()` . Integers, floats, complex numbers, binary numbers, `Decimal`, and `Fraction`.

- **String**: `'spam'`, `"BOB's"`, `b'a\x01c'`, `u'sp\xc4m'`.
Textual data enclosed in single or double quotes, with various representations (`b` for bytes, `u` for Unicode).

- **Boolean**: `True`, `False`.
Represents true or false values.

- **List**: `[1,2,3]`, `[1,[2,3],4]`.Ordered, mutable collections of items.
- **Tuple**: `(1,2,3)`.Ordered, immutable collections of items.
- **Dictionary**: `{'food': 'khadhi', 'sweet': 'rusgulla'}`.Key-value pairs, enclosed in curly braces.
- **Set**: `{a, b, c}`.Unordered collections of unique items.
- **None**: `None`.Represents the absence of a value.

## Mutable and Immutable

- **Mutable**  objects are those whose state (content) can be changed after they are created.

- **Examples**: Lists, dictionaries, sets.

- You can modify their elements or contents after creation.
Changes made to a mutable object directly affect its memory location.
- Mutable objects can be altered in-place without creating a new object.
- They use more memory and are generally slower for some operations compared to immutable objects.


 **Immutable** objects are those whose state cannot be changed after they are created.

**Examples**: Integers, floats, strings, tuples.

- Once created, their content cannot be altered.
- Any operation that appears to modify an immutable object actually creates a new object.
- Immutable objects are hashable, making them suitable for dictionary keys or set elements.
- They are generally faster and more memory-efficient for some operations compared to mutable objects.


**Internal wotking of memory reference:**

1.In python, Initially, when `a = 4` is executed:
   - Python allocates memory for an integer object to represent the value `4`.
   - First, The value `4` is stored in this memory location.
   - Then variable `a` references this memory location.

   Memory representation:
   ```plaintext
          +----------------------+
    a --->|    Integer Object    |
          +----------------------+
                    |
                    V
                 Value: 4
           

```
2.Initially in other Languages,
  - Memory is allocated for the integer variable a.
  - The binary representation of 4 is stored directly in this       memory location.

 Memory representation:
  ```plaintext

         +------+
    a--->|  4   |
         +------+
 ```
  ## **repr() vs str()**
   - repr() :if we print a string using the repr() function then it prints with a pair of quotes and if we calculate a value we get a more precise value than the str() function.
      
    - Example : repr(‘hello’) returns “‘hello'”
                repr(‘hello’) returns “‘hello'”
                print (repr(2.0/11.0)) 0.18181818181818182






   - str() : if we print a string using the str() function then it prints simply a string and if we calculate a value we get a less precise value than the repr() function.
    
    - Example :str(123) returns ‘123’
               str(‘hello’) returns ‘hello’
               print (str(2.0/11.0)) 0.181818181818







