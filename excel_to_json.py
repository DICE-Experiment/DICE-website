#!/usr/bin/env python3
"""
Convert DICE coauthors Excel file to JSON format for the website.
Run this script whenever you update the Excel file:
    python3 excel_to_json.py
"""

import pandas as pd
import json

# Country name to ISO3 code mapping
COUNTRY_TO_ISO3 = {
    'Spain': 'ESP',
    'Czechia': 'CZE',
    'Philippines': 'PHL',
    'Honduras': 'HND',
    'Ivory Coast': 'CIV',
    'Madagascar': 'MDG',
    'Italy': 'ITA',
    'Greece': 'GRC',
    'Argentina': 'ARG',
    'China': 'CHN',
    'Qatar': 'QAT',
    'Kazakhstan': 'KAZ',
    'Russia': 'RUS',
    'Singapore': 'SGP',
    'Colombia': 'COL',
    'Chile': 'CHL',
    'Hungary': 'HUN',
    'Uruguay': 'URY',
    'Germany': 'DEU',
    'France': 'FRA',
    'Portugal': 'PRT',
    'UK': 'GBR',
    'Turkey': 'TUR',
    'Poland': 'POL',
    'Austria': 'AUT',
    'Japan': 'JPN',
    'South Korea': 'KOR',
    'UAB': 'ARE',  # UAE - United Arab Emirates
    'USA': 'USA',
    'Hong Kong': 'HKG',
    'Taiwan': 'TWN',
    'Pakistan': 'PAK',
    'Egypt': 'EGY',
    'Australia': 'AUS',
}

# Country metadata
COUNTRY_METADATA = {
    'ESP': {'flag': '🇪🇸', 'name': 'Spain', 'anchor': 'spain'},
    'CZE': {'flag': '🇨🇿', 'name': 'Czech Republic', 'anchor': 'czechia'},
    'PHL': {'flag': '🇵🇭', 'name': 'Philippines', 'anchor': 'philippines'},
    'HND': {'flag': '🇭🇳', 'name': 'Honduras', 'anchor': 'honduras'},
    'CIV': {'flag': '🇨🇮', 'name': 'Côte d\'Ivoire', 'anchor': 'cotedivoire'},
    'MDG': {'flag': '🇲🇬', 'name': 'Madagascar', 'anchor': 'madagascar'},
    'ITA': {'flag': '🇮🇹', 'name': 'Italy', 'anchor': 'italy'},
    'GRC': {'flag': '🇬🇷', 'name': 'Greece', 'anchor': 'greece'},
    'ARG': {'flag': '🇦🇷', 'name': 'Argentina', 'anchor': 'argentina'},
    'CHN': {'flag': '🇨🇳', 'name': 'China', 'anchor': 'china'},
    'QAT': {'flag': '🇶🇦', 'name': 'Qatar', 'anchor': 'qatar'},
    'KAZ': {'flag': '🇰🇿', 'name': 'Kazakhstan', 'anchor': 'kazakhstan'},
    'RUS': {'flag': '🇷🇺', 'name': 'Russia', 'anchor': 'russia'},
    'SGP': {'flag': '🇸🇬', 'name': 'Singapore', 'anchor': 'singapore'},
    'COL': {'flag': '🇨🇴', 'name': 'Colombia', 'anchor': 'colombia'},
    'CHL': {'flag': '🇨🇱', 'name': 'Chile', 'anchor': 'chile'},
    'HUN': {'flag': '🇭🇺', 'name': 'Hungary', 'anchor': 'hungary'},
    'URY': {'flag': '🇺🇾', 'name': 'Uruguay', 'anchor': 'uruguay'},
    'DEU': {'flag': '🇩🇪', 'name': 'Germany', 'anchor': 'germany'},
    'FRA': {'flag': '🇫🇷', 'name': 'France', 'anchor': 'france'},
    'PRT': {'flag': '🇵🇹', 'name': 'Portugal', 'anchor': 'portugal'},
    'GBR': {'flag': '🇬🇧', 'name': 'United Kingdom', 'anchor': 'uk'},
    'TUR': {'flag': '🇹🇷', 'name': 'Turkey', 'anchor': 'turkey'},
    'POL': {'flag': '🇵🇱', 'name': 'Poland', 'anchor': 'poland'},
    'AUT': {'flag': '🇦🇹', 'name': 'Austria', 'anchor': 'austria'},
    'JPN': {'flag': '🇯🇵', 'name': 'Japan', 'anchor': 'japan'},
    'KOR': {'flag': '🇰🇷', 'name': 'South Korea', 'anchor': 'korea'},
    'ARE': {'flag': '🇦🇪', 'name': 'United Arab Emirates', 'anchor': 'uae'},
    'USA': {'flag': '🇺🇸', 'name': 'United States', 'anchor': 'usa'},
    'HKG': {'flag': '🇭🇰', 'name': 'Hong Kong', 'anchor': 'hongkong'},
    'TWN': {'flag': '🇹🇼', 'name': 'Taiwan', 'anchor': 'taiwan'},
    'PAK': {'flag': '🇵🇰', 'name': 'Pakistan', 'anchor': 'pakistan'},
    'EGY': {'flag': '🇪🇬', 'name': 'Egypt', 'anchor': 'egypt'},
    'AUS': {'flag': '🇦🇺', 'name': 'Australia', 'anchor': 'australia'},
}

# Default sample sizes
DEFAULT_SAMPLES = {
    'ESP': 465, 'CZE': 390, 'PHL': 385, 'HND': 350, 'CIV': 340,
    'MDG': 290, 'ITA': 475, 'GRC': 360, 'ARG': 450, 'CHN': 520,
    'QAT': 320, 'KAZ': 330, 'RUS': 460, 'SGP': 430, 'COL': 480,
    'CHL': 425, 'HUN': 375, 'URY': 335, 'DEU': 510, 'FRA': 440,
    'PRT': 365, 'GBR': 490, 'TUR': 445, 'POL': 420, 'AUT': 380,
    'JPN': 500, 'KOR': 485, 'ARE': 340, 'USA': 505, 'HKG': 405,
    'TWN': 455, 'PAK': 410, 'EGY': 370, 'AUS': 450
}


def convert_excel_to_json():
    """Convert Excel file to JSON format."""
    print("Reading Excel file...")
    df = pd.read_excel('DICE - coauthors.xlsx')

    # Filter out supervision rows
    df_filtered = df[~df['Unnamed: 0'].str.contains('Supervision', na=False)]

    country_data = {}

    for idx, row in df_filtered.iterrows():
        country_name = row['Unnamed: 0']

        # Skip if country mapping not found
        if country_name not in COUNTRY_TO_ISO3:
            print(f"Warning: No ISO3 mapping for '{country_name}' - skipping")
            continue

        iso3 = COUNTRY_TO_ISO3[country_name]

        # Skip if we already have this country (handles duplicates in Excel)
        if iso3 in country_data:
            print(f"Warning: Duplicate entry for '{country_name}' ({iso3}) - using first occurrence")
            continue

        # Build team string
        team_parts = []

        # First coauthor
        first_name = row['First Coauthor Name']
        first_surname = row['First Coauthor Surname']
        if pd.notna(first_name) and pd.notna(first_surname):
            team_parts.append(f"{first_name} {first_surname}")

        # Second coauthor
        second_name = row['Second Coauthor Name']
        second_surname = row['Second Coauthor Surname']
        if pd.notna(second_name) and pd.notna(second_surname):
            team_parts.append(f"{second_name} {second_surname}")

        team = ', '.join(team_parts) if team_parts else 'TBA'

        # Get institution (use first coauthor's university)
        institution = row['First Coauthor University']
        if pd.isna(institution):
            institution = 'TBA'

        # Get metadata for this country
        metadata = COUNTRY_METADATA.get(iso3, {
            'flag': '🏳️',
            'name': country_name,
            'anchor': country_name.lower().replace(' ', '')
        })

        # Build country data entry
        country_data[iso3] = {
            'anchor': metadata['anchor'],
            'flag': metadata['flag'],
            'name': metadata['name'],
            'team': team,
            'institution': str(institution),
            'sample': f"N = {DEFAULT_SAMPLES.get(iso3, 400)}"
        }

    # Create output structure (derive codes from country_data keys to ensure no duplicates)
    output = {
        'participatingCountryCodes': sorted(list(country_data.keys())),
        'countryData': country_data
    }

    # Write to JSON file
    print("Writing to country-data.json...")
    with open('country-data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✓ Successfully converted {len(country_data)} countries to JSON")
    print(f"✓ Output saved to: country-data.json")
    return output


if __name__ == '__main__':
    convert_excel_to_json()
