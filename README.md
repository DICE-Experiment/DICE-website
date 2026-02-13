# DICE Website - Beginner's Guide

Welcome! This guide will help you understand how to update and customize the DICE website, even if you're not a developer.

## 🌐 Website URL
The site is hosted at: **https://dice-experiment.github.io/DICE-website/**

## 📁 File Structure Overview

### Main Files You'll Edit

| File | What It Controls |
|------|-----------------|
| `index.html` | **The main website** - contains all content, styling, and functionality |
| `projects-data.json` | **Project listings** - all research projects and their details |
| `country-data.json` | **Country information** - participating countries, teams, and institutions |
| `Classroom fotos/` | **Photos** - classroom session images displayed on the site |

---

## 📝 How to Update Different Parts of the Site

### 1. **Updating Text Content**

All text is in `index.html`. The file uses a bilingual system (English/Spanish):

#### Main Sections to Find:
- **Hero Section** (lines ~259-266): The main headline and description
- **Implementation Summary** (lines ~300-305): Protocol details
- **Collaborators** (lines ~320-346): Team and coordination info
- **Projects Section** (lines ~347-358): Project grid container
- **Data Section** (lines ~361-406): Dataset information
- **Footer** (lines ~484-501): Contact info and tagline

#### Translation System:
Text appears in **three places**:
1. **HTML** (Spanish default): `<p>texto en español</p>`
2. **English translation** (lines ~520-668): Under `translations.en = { ... }`
3. **Spanish translation** (lines ~692-853): Under `translations.es = { ... }`

**Example:** To change the main subtitle:
```html
<!-- 1. HTML (line ~261) -->
<p>Un experimento coordinado...</p>

<!-- 2. English translation (line ~528) -->
subtitle: 'A coordinated and harmonized experiment...'

<!-- 3. Spanish translation (line ~700) -->
subtitle: 'Un experimento coordinado...'
```

### 2. **Updating Projects**

Edit `projects-data.json`:

```json
{
  "projectCount": 14,
  "projects": [
    {
      "id": 0,
      "title": "Your Project Title",
      "status": "ACTIVE",  // or "CLOSED"
      "firstAuthor": "First Author Name",
      "coauthors": ["Author 2", "Author 3"],
      "allAuthors": ["First Author", "Author 2", "Author 3"],
      "authorCount": 3
    }
  ]
}
```

**To add a new project:**
1. Copy an existing project block
2. Change the `id` to the next number
3. Update all fields
4. Increase `projectCount` by 1

### 3. **Updating Country Data**

Edit `country-data.json`:

```json
{
  "participatingCountryCodes": ["ARG", "AUT", "CHL", ...],
  "countryData": {
    "ARG": {
      "anchor": "argentina",
      "flag": "🇦🇷",
      "name": "Argentina",
      "team": "Researcher Names",
      "institution": "University Name",
      "sample": "N = 450"
    }
  }
}
```

**To add a country:**
1. Add the 3-letter country code to `participatingCountryCodes` array
2. Add a new entry under `countryData` with the country details
3. Update the count in `index.html` (search for "33 countries")

### 4. **Updating Images**

#### Classroom Photos:
1. Add images to `Classroom fotos/` folder
2. In `index.html`, find the gallery section (lines ~465-477)
3. Update image paths:
```html
<img src="Classroom fotos/YourPhoto.jpg" alt="Description" loading="lazy" />
```

#### Logo:
- Replace `Dice_Logo.png` with your new logo (keep the same filename)
- Or update line 232: `<img src="Dice_Logo.png" alt="DICE Logo">`

### 5. **Updating Numbers**

Common numbers you might want to change:

| What | Where to Find | Search Term |
|------|--------------|-------------|
| Country count | `index.html` | Search: "33 countries" or "33 países" |
| Project count | `index.html` line 1470 | Hard-coded to `14` |
| Participant count | `index.html` | Search: "10,000 participants" |
| Continent count | `index.html` | Search: "4 continents" |

### 6. **Key Contact Information**

Update in `index.html` (footer section, line ~492):
```html
<a href="mailto:ph.exadaktylos@gmail.com" class="small">ph.exadaktylos@gmail.com</a>
```

### 7. **Coordination Team**

Update in `index.html` (Coordination card, lines ~326-327):
```html
<p>Principal investigator: Filippos Exadaktylos (University of Barcelona)
<br><br>Co-PIs: Names and institutions here</p>
```

Update translations at:
- English: line ~574
- Spanish: line ~746

---

## 🖥️ How to Run the Website Locally

You need a local server to view the site properly (for loading JSON files).

### Option 1: Python (Easiest)
```bash
# Navigate to the project folder
cd /path/to/DICE-website-1

# Start server
python3 -m http.server 8000

# Open in browser:
# http://localhost:8000
```

### Option 2: Node.js
```bash
npx http-server -p 8000
```

### Option 3: VS Code
Install the "Live Server" extension and click "Go Live"

---

## 🎨 Styling and Colors

Colors are defined in CSS variables (lines ~42-50):

```css
--bg: #0a0f1e;           /* Background */
--text: #e2e8f0;         /* Text color */
--brand: #D49D39;        /* Brand gold */
--accent: #4A90E2;       /* Accent blue */
```

To change the color scheme, update these values.

---

## 📋 Common Tasks Checklist

### Adding a New Country
- [ ] Add country code to `country-data.json` → `participatingCountryCodes`
- [ ] Add country details to `country-data.json` → `countryData`
- [ ] Update country count in `index.html` (search "33")
- [ ] Test on localhost

### Adding a New Project
- [ ] Add project to `projects-data.json`
- [ ] Increment `projectCount`
- [ ] Add cache-busting: `?v=YYYYMMDD` to fetch if needed
- [ ] Test on localhost

### Updating Main Text
- [ ] Update Spanish HTML (default display)
- [ ] Update English translation (`.en` section)
- [ ] Update Spanish translation (`.es` section)
- [ ] Test language switcher

### Changing Photos
- [ ] Add photos to `Classroom fotos/` folder
- [ ] Update `<img src="...">` paths in gallery
- [ ] Check that photos load correctly

---

## 🐛 Troubleshooting

### Changes don't appear
1. **Hard refresh**: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
2. Clear browser cache
3. Check browser console (F12) for errors

### JSON file not loading
- Make sure you're using a local server (not just opening index.html)
- Check JSON syntax with a validator: https://jsonlint.com

### Images not showing
- Check file paths are correct (case-sensitive!)
- Verify images are in the right folder
- Check browser console for 404 errors

### Text in wrong language
- The language switcher toggles between English/Spanish
- Default is Spanish (the HTML content)
- Check that translations are updated in all three places

---

## 📞 Need Help?

- Check browser console (F12) for error messages
- Validate JSON files: https://jsonlint.com
- HTML validator: https://validator.w3.org

## 🚀 Publishing Changes

After making changes:
1. Test locally first
2. Commit changes to Git
3. Push to GitHub
4. GitHub Pages will auto-update (may take 1-2 minutes)

---

## 📄 File Reference Quick Guide

```
DICE-website-1/
├── index.html              # Main website file
├── projects-data.json      # All project information
├── country-data.json       # All country/team data
├── Dice_Logo.png          # Site logo
├── Classroom fotos/       # Photo gallery images
├── data/                  # Additional data files
│   ├── countries/         # Country-specific files
│   ├── projects/          # Project-specific files
│   └── general/           # General datasets
└── README.md             # This guide!
```

---

**Remember:** Always test changes locally before publishing, and keep backups of your files!

Good luck! 🎉
