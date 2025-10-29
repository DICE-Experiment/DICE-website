# DICE Project - Data Folder Structure

This folder contains all downloadable materials for the DICE experiment.

## Structure

```
data/
├── countries/                    # Country-specific materials
│   ├── argentina/
│   │   ├── questionnaire.pdf
│   │   └── argentina-results.csv
│   ├── austria/
│   │   ├── questionnaire.pdf
│   │   └── austria-results.csv
│   ├── ... (32 more countries)
│   └── usa/
│       ├── questionnaire.pdf
│       └── usa-results.csv
├── projects/                     # 14 linked projects
│   ├── project-01/
│   │   └── preregistration.pdf
│   ├── project-02/
│   │   └── preregistration.pdf
│   ├── ... (12 more projects)
│   └── project-14/
│       └── preregistration.pdf
└── general/                      # General project materials
    ├── sample-full-data.csv
    ├── ethics-documentation.pdf
    └── replication-package-README.txt
```

## Files

### Country-specific folders (34 countries)
Each country folder contains:

1. **questionnaire.pdf** - Survey questionnaire used in that country
2. **[country]-results.csv** - Raw data from that country's participants (e.g., spain-results.csv)

**Countries included**: Argentina, Austria, Chile, China, Côte d'Ivoire, D.R. Congo, Colombia, Czech Republic, Germany, Egypt, Spain, France, United Kingdom, Greece, Hong Kong, Hungary, Italy, Japan, Kazakhstan, South Korea, Madagascar, Pakistan, Peru, Philippines, Poland, Portugal, Qatar, Russia, Saudi Arabia, Singapore, Turkey, Taiwan, Uruguay, USA

### Projects folders (14 linked projects)
Each project folder contains:

1. **preregistration.pdf** - Preregistration document for the specific research question

**Projects included**:
- Project 01: Cross-Cultural Honesty Norms
- Project 02: Civic Capital and Honesty
- Project 03: Institutional Trust and Honesty
- Project 04: Social Preferences and Dishonesty
- Project 05: Rule Compliance Norms
- Project 06: Gender Differences in Honesty
- Project 07: Economic Development and Honesty
- Project 08: Religious Beliefs and Honesty
- Project 09: Age Effects on Honesty
- Project 10: Educational Context and Honesty
- Project 11: Corruption Perception and Honesty
- Project 12: Cultural Tightness and Honesty
- Project 13: Collectivism and Honesty
- Project 14: Methodological Validation Study

### General folder
Contains project-wide materials:

1. **sample-full-data.csv** - Combined dataset containing data from all 34 participating countries
   - **Columns**: country, participant_id, dice_roll, reported_value, session_date, age, gender, trust_score
   - **Rows**: Sample data (15 entries as placeholder)
2. **ethics-documentation.pdf** - Ethics approvals and documentation for the multi-country study
3. **replication-package-README.txt** - Information about the full replication package

## Usage

All files are accessible via:
- **Web interface**: Click download buttons on the website
- **Direct access**: Navigate to `/data/[folder]/[file]` URLs

## Notes

- **Placeholder files**: Current files are placeholders for demonstration. Replace with actual study materials.
- **File formats**: PDF files are currently text-based placeholders. Replace with actual PDF documents.
- **Data privacy**: Ensure all shared data is anonymized and complies with ethics approvals.

## Updating Files

To update materials:
1. Replace files in the appropriate folder
2. Ensure naming conventions remain consistent
3. Update website links if needed
4. Update this README if structure changes

## License

[Add appropriate license information for data sharing]
