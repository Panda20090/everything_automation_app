# Templates Directory

This directory contains HTML templates used for generating content reports.

## Template Files

- `google_trends_template.html`: Template for Google Trends reports.
- `twitter_template.html`: Template for Twitter reports.

## Usage

The templates in this directory are used by the application to generate HTML reports based on the data retrieved from APIs. These templates are populated with data and saved as complete HTML files in the application's output.

## Example

An example of how a template might look:

```html
<!-- Example for Google Trends -->
<html>
<head>
    <title>Google Trends Report</title>
</head>
<body>
    <h1>Google Trends Report for {{ date }}</h1>
    <img src="google_trends_visualization.png" alt="Google Trends Visualization">
    <p>The above graph shows the trend data for the selected keywords over the past month.</p>
</body>
</html>
