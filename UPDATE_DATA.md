# How to Update Data

Your website data is now dynamically loaded from Excel files. Follow these steps to update the data:

## Updating Country Data

1. **Edit the Excel file**: Make your changes to `DICE - coauthors.xlsx`
   - Add new countries
   - Update researcher names
   - Update institutions
   - Change any other information

2. **Run the conversion script**:
   ```bash
   python3 excel_to_json.py
   ```
   This will generate a new `country-data.json` file with your updated data.

3. **Refresh your website**: Simply reload the page in your browser
   - The website will automatically load the new data from `country-data.json`
   - No need to edit HTML files!

## Updating Projects Data

1. **Edit the Excel file**: Make your changes to `DICE extra projects.xlsx`
   - Add new projects
   - Update project titles
   - Update author names
   - Change project status (ACTIVE/CLOSED)

2. **Run the conversion script**:
   ```bash
   python3 projects_excel_to_json.py
   ```
   This will generate a new `projects-data.json` file with your updated data.

3. **Refresh your website**: Simply reload the page in your browser
   - The website will automatically load the new projects from `projects-data.json`

## What Changed

- **Before**: All data was hardcoded in `index.html`
- **After**: Data is loaded from JSON files (which are generated from Excel files)

## Important Files

### Country Data
- `DICE - coauthors.xlsx` - Your source data (edit this)
- `excel_to_json.py` - Conversion script (run this after editing Excel)
- `country-data.json` - Generated JSON file (don't edit directly)

### Projects Data
- `DICE extra projects.xlsx` - Your source data (edit this)
- `projects_excel_to_json.py` - Conversion script (run this after editing Excel)
- `projects-data.json` - Generated JSON file (don't edit directly)

### Website
- `index.html` - Website (no manual editing needed for data updates)

## Benefits

✅ Easy updates: Just edit Excel and run one command
✅ Clean separation: Data and code are separate
✅ Performance: Small JSON files load quickly
✅ Maintainable: Non-technical users can update Excel
✅ Version control: Track changes to Excel files

## Troubleshooting

If data doesn't load:
1. Make sure you're running a local web server (e.g., `python3 -m http.server 3000`)
2. Check the browser console (F12) for errors
3. Ensure both `country-data.json` and `projects-data.json` exist in the same directory as `index.html`
4. Verify your Excel files are in the correct format
5. Re-run the conversion scripts if you made changes to the Excel files
