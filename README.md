
# **Minesweeper: Learning 2D Lists in Python**

## **Overview**  
This project is my exploration of **Data Structures**, focusing on **2D Lists** through a Python-based **Minesweeper game**. It showcases grid manipulation, nested loops, and game logic, built from scratch to deepen my programming skills.

🔗 **[View Code](https://github.com/GowerCampbell/minesweeper.git)**  

---

## **Learning Goals**  
- **2D Lists**: Access and modify grid elements.  
- **Nested Loops**: Iterate over rows and columns.  
- **Randomization**: Place mines with `random`.  
- **Boundary Checks**: Prevent index errors.  
- **Modularity**: Break logic into reusable functions.  

---

## **Project Structure**  
```
minesweeper/
├── main.py          # Game loop and entry point
├── grid_utils.py    # Grid creation and logic
├── display.py       # Grid printing
├── tests/           # Unit tests
│   └── test_grid.py
└── README.md        # Project overview
```

---

## **Key Features**  
### **Grid Creation**  
Randomly generates a minefield:  
```python
def create_random_grid(rows, cols, mine_prob=0.2):
    return [["#" if random.random() < mine_prob else "-" 
             for _ in range(cols)] for _ in range(rows)]
```

### **Mine Counting**  
Counts adjacent mines with boundary checks:  
```python
def count_adjacent_mines(grid, row, col):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    return sum(1 for dr, dc in directions 
               if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) 
               and grid[row + dr][col + dc] == "#")
```

### **Gameplay**  
- Reveal cells or flag mines.  
- 3 lives system; win by clearing all safe cells.  

---

## **Lessons Learned**  
- Mastered 2D list traversal and modification.  
- Gained confidence with nested loops and recursion.  
- Learned to handle edge cases and debug via grid printing.  
- Improved code organization with modular functions.  

---

## **Future Plans**  
- Add a GUI with `pygame`.  
- Implement adjustable difficulty.  
- Track scores with file I/O.  

---

## **Running the Game**  
1. Clone the repo:  
   ```bash
   git clone https://github.com/yourusername/minesweeper.git
   ```
2. Run:  
   ```bash
   python main.py
   ```

---

## **Resources**  
- [Python Docs – Lists](https://docs.python.org/3/tutorial/datastructures.html)  
- [Real Python – Minesweeper](https://realpython.com/python-minesweeper/)  
- [GeeksforGeeks – 2D Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)  

---

## **Contributing**  
Fork, tweak, or report issues!  
📧 [Gower.Campbell@gmail.com]  
