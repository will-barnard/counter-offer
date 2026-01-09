import json

# Load the zip code data
with open('us-zip-data.json', 'r') as f:
    zip_data = json.load(f)

# State sales tax rates (approximate combined state + average local rates)
# These are representative rates - actual rates may vary by locality
state_tax_rates = {
    'AL': 0.0910, 'AK': 0.0176, 'AZ': 0.0827, 'AR': 0.0947, 'CA': 0.0850,
    'CO': 0.0746, 'CT': 0.0635, 'DE': 0.0000, 'FL': 0.0705, 'GA': 0.0729,
    'HI': 0.0444, 'ID': 0.0603, 'IL': 0.0873, 'IN': 0.0700, 'IA': 0.0694,
    'KS': 0.0865, 'KY': 0.0600, 'LA': 0.0952, 'ME': 0.0550, 'MD': 0.0600,
    'MA': 0.0625, 'MI': 0.0600, 'MN': 0.0743, 'MS': 0.0707, 'MO': 0.0821,
    'MT': 0.0000, 'NE': 0.0694, 'NV': 0.0823, 'NH': 0.0000, 'NJ': 0.0663,
    'NM': 0.0783, 'NY': 0.0852, 'NC': 0.0698, 'ND': 0.0696, 'OH': 0.0723,
    'OK': 0.0897, 'OR': 0.0000, 'PA': 0.0634, 'RI': 0.0700, 'SC': 0.0744,
    'SD': 0.0645, 'TN': 0.0955, 'TX': 0.0820, 'UT': 0.0719, 'VT': 0.0624,
    'VA': 0.0575, 'WA': 0.0920, 'WV': 0.0643, 'WI': 0.0543, 'WY': 0.0536,
    'DC': 0.0600, 'PR': 0.1150, 'GU': 0.0400, 'VI': 0.0000, 'AS': 0.0000,
    'MP': 0.0000
}

# County-specific adjustments for major counties
county_adjustments = {
    'Cook': {'IL': 0.0152},  # Chicago area higher rate
    'Los Angeles': {'CA': 0.0100},
    'King': {'WA': 0.0090},
    'Harris': {'TX': 0.0005},
    'Maricopa': {'AZ': 0.0030},
    'Miami-Dade': {'FL': 0.0000},
    'Dallas': {'TX': 0.0005},
    'Queens': {'NY': 0.0023},
    'San Diego': {'CA': -0.0075},
    'Orange': {'CA': -0.0075},
}

# Create zip to county mapping with tax rates
zip_mapping = {}
for entry in zip_data:
    zip_code = str(entry['zip_code']).zfill(5)
    county = entry['county']
    state = entry['state']
    
    # Get base state tax rate
    base_rate = state_tax_rates.get(state, 0.0700)  # Default to 7% if state not found
    
    # Check for county-specific adjustments
    adjustment = 0
    if county in county_adjustments and state in county_adjustments[county]:
        adjustment = county_adjustments[county][state]
    
    final_rate = base_rate + adjustment
    
    # Format county name to include "County" if not already present
    if not county.endswith('County') and not county.endswith('Parish') and not county.endswith('Borough'):
        county_name = f"{county} County"
    else:
        county_name = county
    
    zip_mapping[zip_code] = {
        'name': county_name,
        'state': state,
        'taxRate': round(final_rate, 4)
    }

# Write to JavaScript file
with open('zip-data.js', 'w') as f:
    f.write('// Comprehensive US ZIP Code to County mapping with sales tax rates\n')
    f.write('// Auto-generated from USCities.json\n')
    f.write('const zipToCountyData = ')
    json.dump(zip_mapping, f, indent=2)
    f.write(';\n')

print(f"Processed {len(zip_mapping)} zip codes")
print("Sample entries:")
for i, (zip_code, data) in enumerate(list(zip_mapping.items())[:5]):
    print(f"  {zip_code}: {data}")
