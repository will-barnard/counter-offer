# Counter Offer Calculator - ZIP Code Edition

## Overview
This tool helps calculate counter offers with sales tax based on ZIP codes. It automatically looks up the county and corresponding sales tax rate for any US ZIP code.

## Features
- **Comprehensive ZIP Code Database**: Includes 42,741+ ZIP codes covering all US states and territories
- **Automatic County Lookup**: Enter a ZIP code and the county and tax rate are automatically determined
- **Accurate Sales Tax Rates**: Includes state and average local sales tax rates for all counties
- **Real-time Calculations**: Instantly calculates total costs, taxes, and customer savings

## Files
- `index.html` - Main application file with Vue.js interface
- `zip-data.js` - Comprehensive ZIP code to county mapping (3.8MB)
- `us-zip-data.json` - Raw ZIP code data source
- `process-zip-data.py` - Python script to generate zip-data.js from source data

## Usage
1. Open `index.html` in a web browser (or serve via local web server)
2. Enter customer information and ZIP code
3. The county and tax rate will automatically populate
4. Enter your counter offer details
5. Copy the generated message to clipboard

## ZIP Code Data
The ZIP code database includes:
- All 50 US states
- Washington DC
- US territories (Puerto Rico, Guam, US Virgin Islands, etc.)
- County names and state abbreviations
- Combined state + local average sales tax rates

## Tax Rate Sources
Sales tax rates are approximate combined rates including:
- State sales tax
- Average local/county sales tax
- Special district taxes for major metropolitan areas

**Note**: Tax rates are representative averages. Always verify with official sources for critical transactions.

## How to Update ZIP Code Data
If you need to update the ZIP code database:
1. Update `us-zip-data.json` with new data
2. Modify tax rates in `process-zip-data.py` if needed
3. Run: `python3 process-zip-data.py`
4. This will regenerate `zip-data.js`

## Technical Details
- Built with Vue.js 3
- Pure client-side application (no server required)
- ZIP lookup is instantaneous (no API calls)
- Works offline once loaded

## Browser Compatibility
Works in all modern browsers supporting:
- ES6+ JavaScript
- Clipboard API
- Vue.js 3

## License
The ZIP code data is derived from public domain sources.
