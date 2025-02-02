# AutoPowerOff
A program to shut down the operating system at a certain time

![Python](https://www.python.org/static/img/python-logo.png)
![..](AutoPowerOff.jpeg)
```python
from datetime import datetime
from colorama import Fore
import time
import os
```
- **`from datetime import datetime`**: Imports the `datetime` function from the `datetime` module, which allows handling dates and times.
- **`from colorama import Fore`**: Imports the `Fore` object from the `colorama` library, which is used to change text color in the terminal.
- **`import time`**: Imports the `time` module, which provides time-related functions like `sleep`.
- **`import os`**: Imports the `os` module, which allows interaction with the operating system, such as executing system commands.

```python
while True:
```
- **`while True:`**: Starts an infinite loop, meaning the code inside this loop will continue running until it is manually stopped or a `break` statement is executed.

```python
    try:
```
- **`try:`**: Begins a `try` block, which attempts to execute the code inside it. If an error occurs, the program will jump to the `except` block.

```python
        os.system('clear')
```
- **`os.system('clear')`**: Executes the system command `clear`, which clears the terminal screen (works on Unix/Linux/Mac systems). On Windows, you can replace it with `'cls'`.

```python
        datatime = datetime.now()
```
- **`datatime = datetime.now()`**: Retrieves the current date and time and stores it in the variable `datatime`.

```python
        strftime = datatime.strftime('%p')
```
- **`strftime = datatime.strftime('%p')`**: Uses the `strftime` function to convert the current time into `AM` or `PM` format and stores it in the variable `strftime`.

```python
        enter_hour = int(input(Fore.MAGENTA + 'Enter hour: '))
```
- **`enter_hour = int(input(Fore.MAGENTA + 'Enter hour: '))`**: Prompts the user to enter the hour and stores it in the variable `enter_hour`. The displayed text is in magenta color (`Fore.MAGENTA`).

```python
        enter_minute = int(input(Fore.MAGENTA + 'Enter minute: '))
```
- **`enter_minute = int(input(Fore.MAGENTA + 'Enter minute: '))`**: Prompts the user to enter the minutes and stores it in the variable `enter_minute`. The displayed text is in magenta color.

```python
        while True:
```
- **`while True:`**: Starts another infinite loop.

```python
            enter_strftime = str(input(Fore.MAGENTA + 'Enter strftime AM / PM: ').upper() or strftime)
```
- **`enter_strftime = str(input(Fore.MAGENTA + 'Enter strftime AM / PM: ').upper() or strftime)`**: Prompts the user to enter `AM` or `PM`. If the user doesn't enter anything, the default value `strftime` (obtained earlier) is used. The displayed text is in magenta color.

```python
            if enter_strftime != 'AM' and enter_strftime != 'PM':
```
- **`if enter_strftime != 'AM' and enter_strftime != 'PM':`**: Checks if the user entered a valid value (`AM` or `PM`). If the value is invalid, the code inside the `if` block is executed.

```python
                print(Fore.RED + '----------------------------------------------')
                print(Fore.RED + 'Looks like you entered the timing incorrectly.')
                continue
```
- **`print(Fore.RED + '----------------------------------------------')`**: Prints a red line to separate messages.
- **`print(Fore.RED + 'Looks like you entered the timing incorrectly.')`**: Prints an error message in red indicating that the user entered an incorrect time format.
- **`continue`**: Restarts the loop, prompting the user to re-enter `AM` or `PM`.

```python
            else:
                break
```
- **`else:`**: If the entered value is valid (`AM` or `PM`), the `break` statement is executed to exit the inner loop.

```python
        enter_time = f'{enter_hour}:{enter_minute} {enter_strftime}'
```
- **`enter_time = f'{enter_hour}:{enter_minute} {enter_strftime}'`**: Creates a string containing the user-entered time in the format `hour:minute AM/PM` and stores it in the variable `enter_time`.

```python
        while True:
```
- **`while True:`**: Starts another infinite loop.

```python
            datatime = datetime.now()
```
- **`datatime = datetime.now()`**: Retrieves the current time again.

```python
            strftime = datetime.now().strftime('%p')
```
- **`strftime = datetime.now().strftime('%p')`**: Retrieves the current `AM` or `PM` value.

```python
            hour = datatime.hour
            minute = datatime.minute
```
- **`hour = datatime.hour`**: Retrieves the current hour.
- **`minute = datatime.minute`**: Retrieves the current minute.

```python
            now = f'{hour}:{minute} {strftime}'
```
- **`now = f'{hour}:{minute} {strftime}'`**: Creates a string containing the current time in the format `hour:minute AM/PM`.

```python
            os.system('clear')
```
- **`os.system('clear')`**: Clears the terminal screen again.

```python
            print(Fore.RED + 'Waiting for the time.')
```
- **`print(Fore.RED + 'Waiting for the time.')`**: Prints a message in red indicating that the program is waiting for the specified time.

```python
            if enter_time == now:
                os.system('poweroff')
                break
```
- **`if enter_time == now:`**: Checks if the user-entered time (`enter_time`) matches the current time (`now`).
- **`os.system('poweroff')`**: If the times match, the system shutdown command (`poweroff`) is executed.
- **`break`**: Exits the inner loop.

```python
            else:
                time.sleep(1)
                continue
```
- **`else:`**: If the times do not match, the code inside the `else` block is executed.
- **`time.sleep(1)`**: Pauses the program for 1 second before repeating the loop.
- **`continue`**: Restarts the loop.

```python
    except:
```
- **`except:`**: If any error occurs in the `try` block, the code inside the `except` block is executed.

```python
        print(Fore.RED + 'Looks like you entered the timing incorrectly.')
        print(Fore.RED + '----------------------------------------------')
        time.sleep(1)
        os.system('clear')
        continue
```
- **`print(Fore.RED + 'Looks like you entered the timing incorrectly.')`**: Prints an error message in red indicating that the user entered an incorrect time format.
- **`print(Fore.RED + '----------------------------------------------')`**: Prints a red line to separate messages.
- **`time.sleep(1)`**: Pauses the program for 1 second.
- **`os.system('clear')`**: Clears the terminal screen.
- **`continue`**: Restarts the loop.

### Summary:
This code prompts the user to enter a specific time (hour, minute, and `AM`/`PM`), then waits until that time arrives. When the specified time is reached, the program shuts down the system. If the user enters invalid data, they are notified and prompted to re-enter the information.
