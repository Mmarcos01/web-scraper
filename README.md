# Project: Web Scraping
---
## Feature Tasks:

Scrape a Wikipedia page and record which passages need citations.

Source: [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico) 

Your web scraper should report the number of citations needed.
Your web scraper should identify those cases AND include the relevant passage.

## Implementation Notes:

Count function must be named get_citations_needed_count
get_citations_needed takes in a url and returns an integer

Report function must be named get_citations_needed_report
get_citations_needed_report takes in a url and returns a string
the string should be formatted with each citation needed on own line, in order found.
