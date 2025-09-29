# Part C: Comparison Document

 1. Assembly Reflections
- In assembly we work step by step. For example you can’t just add two numbers, first you put them into registers and then use add.  
- Small tasks take many lines. It feels manual, like you are talking direct to the machine.

 2. Python Reflections
- Python is easier because you just write the idea, not all the machine details. One command can do a whole task.  
- Errors are also easier to understand in Python. In assembly if it’s wrong, the code just fails and is hard to fix.

 3. Comparison Table

| Task             | Assembly Example | Python Example        | Note |
|------------------|------------------|-----------------------|------|
| Store a value    | `MOV AX, 5`      | `x = 5`               | In assembly need register, in python just name |
| Add numbers      | `ADD AX, BX`     | `x + y`               | Python looks like normal math |
| Loop / repeat    | Jump instruction | `for i in range(5):`  | Assembly loop is harder, python is short |
| Print message    | DOS interrupt    | `print("hi")`         | Python printing is much simpler |


In summary, Assembly shows what happens inside, but Python is faster and better for real coding.
