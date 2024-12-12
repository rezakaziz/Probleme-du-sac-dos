# Knapsack Problem Solution Implementation

## Description

This project provides a solution to the **Knapsack Problem** using **Dynamic Programming**. The goal is to select items with specific weights and gains such that the total gain is maximized without exceeding the capacity of the knapsack.

## Features

1. **Graphical Interface**: An interactive application built with **PyQt5**.
2. **Manual Item Addition**: Users can add items by inputting their weight and gain.
3. **Random Item Generation**: Generate random items within a specified range of weights and gains.
4. **Optimal Solution**: Uses a dynamic programming algorithm to find the optimal solution and display results.
5. **Deletion and Reset**: Remove selected items and reset the entire workspace.

## Project Structure

- `main.py`: The main entry point, initializes the interface and connects the functionalities.
- `functions.py`: Contains the solving algorithms, including dynamic programming.
- `Objet.py`: Defines the **Objet** class representing an item with weight and gain.
- `fenetre.py`: Auto-generated PyQt5 user interface code from `MainWin.ui`.

## Prerequisites

- **Python 3.x**
- **PyQt5** (for the graphical user interface)

### Install Dependencies

```bash
pip install PyQt5
```

## Run the Application

To launch the application, run:

```bash
python main.py
```

## How to Use

1. **Set Capacity**: Enter the maximum capacity of the knapsack.
2. **Add Items**:
   - Input the **weight** and **gain** in the respective fields.
   - Click on **"Add"**.
3. **Generate Random Items**:
   - Specify the weight and gain range and the number of items.
   - Click on **"Random"**.
4. **Compute the Solution**:
   - Click on **"Generate Solution"** to display the selected items, maximum gain, and total weight.
5. **Delete/Reset**:
   - Remove items with **"Delete"**.
   - Click **"Clear All"** to reset everything.
