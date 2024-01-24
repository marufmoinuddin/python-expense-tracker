# Expense Tracker

Expense Tracker is a simple Python script that allows users to track and manage their expenses. It uses SQLite for data storage and provides functionality to add expenses, display a list of expenses, and save expenses to a CSV file.

## Usage

1. **Install Dependencies:**

   Make sure you have Python installed on your system. The script uses the `sqlite3` and `csv` modules, which are included in the Python standard library.

2. **Run the Script:**

   Open a terminal or command prompt, navigate to the script's directory, and run the script:

   ```bash
   python Expense_Tracker.py
   ```

3. **Menu Options:**

   - **Add Expense (Option 1):**
     - Enter the amount, category, and an optional description.
     - The expense will be added to the database.

   - **Display Expenses (Option 2):**
     - View a list of all expenses with details like date, amount, category, and description.

   - **Save Expenses to CSV (Option 3):**
     - Enter a filename to save the expenses in CSV format.

   - **Exit (Option 4):**
     - Exit the Expense Tracker.

4. **Database:**

   The script uses an SQLite database (`ET.db`) to store expense data. The database is created automatically if it doesn't exist.

5. **Note:**
   - Ensure that you have proper permissions to read and write files in the script's directory.
   - Make sure to enter valid input when prompted.

Feel free to use and modify the script according to your needs. If you encounter any issues or have suggestions for improvements, please let me know.

Enjoy tracking your expenses!
