#!/usr/bin/env python3
"""
Convert DICE extra projects Excel file to JSON format for the website.
Run this script whenever you update the Excel file:
    python3 projects_excel_to_json.py
"""

import pandas as pd
import json

def convert_projects_to_json():
    """Convert projects Excel file to JSON format."""
    print("Reading Excel file...")
    df = pd.read_excel('DICE extra projects.xlsx')

    projects = []

    for idx, row in df.iterrows():
        project_title = row['Project author']
        if pd.isna(project_title):
            continue

        # Get status (CLOSED or ACTIVE)
        status = row['Unnamed: 1'] if pd.notna(row['Unnamed: 1']) else 'ACTIVE'

        # Get first author
        first_author = row['First author'] if pd.notna(row['First author']) else ''

        # Get co-authors
        coauthors = []
        for i in range(2, 11):  # cauthor 2 through cauthor 10
            col_name = f'cauthor {i}'
            if col_name in row and pd.notna(row[col_name]):
                coauthors.append(row[col_name])

        # Build authors list
        all_authors = []
        if first_author:
            all_authors.append(first_author)
        all_authors.extend(coauthors)

        # Create project entry
        project = {
            'id': idx + 1,
            'title': project_title,
            'status': status,
            'firstAuthor': first_author,
            'coauthors': coauthors,
            'allAuthors': all_authors,
            'authorCount': len(all_authors)
        }

        projects.append(project)

    # Create output structure
    output = {
        'projectCount': len(projects),
        'projects': projects
    }

    # Write to JSON file
    print("Writing to projects-data.json...")
    with open('projects-data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✓ Successfully converted {len(projects)} projects to JSON")
    print(f"✓ Output saved to: projects-data.json")

    # Print summary
    print("\nProjects summary:")
    for p in projects:
        status_indicator = "🔴 CLOSED" if p['status'] == 'CLOSED' else "🟢 ACTIVE"
        print(f"  {p['id']}. {status_indicator} - {p['title'][:60]}...")
        print(f"     Authors: {', '.join(p['allAuthors'][:3])}{'...' if len(p['allAuthors']) > 3 else ''}")

    return output


if __name__ == '__main__':
    convert_projects_to_json()
