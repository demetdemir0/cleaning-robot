# Cleaning Simulation Program  

This Python program simulates a basic cleaning robot that checks the cleanliness of two rooms (A and B) and performs cleaning actions accordingly. The program logs the cleaning actions, tracks the history of room states, and provides a report at the end.  

---

## Features  

- **Room States:**  
  Each room can either be clean (0) or dirty (1), randomly determined in each cycle.  

- **Cleaning Actions:**  
  - If a room is dirty, the robot cleans it (`Suck` action).  
  - If a room is clean, the robot takes no action (`No Op`).  

- **Logging:**  
  - The program logs the actions taken and the history of room states for each cycle.  

- **Cleaning Report:**  
  - At the end of the simulation, a report is generated showing the total cleaning time (based on actions taken).  

---

## How It Works  

1. **Initial State:**  
   The program starts with both rooms initialized to clean (`0`).  

2. **Random Room States:**  
   In each cycle, the states of the rooms are randomly assigned as clean (`0`) or dirty (`1`).  

3. **Cleaning Process:**  
   - The program cleans the rooms based on their current state.  
   - Actions are logged as either `Suck` (cleaning) or `No Op` (no action required).  

4. **User Interaction:**  
   - The user is prompted to continue the simulation or stop it.  
   - Once the user decides to stop, the program generates a cleaning report and ends.  

---

## Program Structure  

- **Functions:**  
  - `clean()`: Performs cleaning actions and logs them.  
  - `report()`: Calculates and displays the cleaning time based on the number of actions.  

- **Data Structures:**  
  - `rooms`: Dictionary holding the states of rooms A and B.  
  - `actions`: List storing the sequence of cleaning actions.  
  - `history`: List tracking the history of room states.  
