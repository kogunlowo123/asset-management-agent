# Asset Management Agent Architecture

IT asset management agent that tracks hardware and software assets throughout their lifecycle, manages procurement workflows, monitors license compliance, forecasts refresh cycles, and generates asset reports.

## Domain Tools

- **register_asset**: Register a new IT asset with specifications and assignment
- **track_lifecycle**: Track asset lifecycle stage (procurement, deployed, maintenance, retired)
- **check_license_compliance**: Check software license compliance across the organization
- **forecast_refresh**: Forecast assets due for refresh based on age and warranty
- **generate_asset_report**: Generate asset inventory and utilization report