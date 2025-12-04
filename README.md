# Data Pipeline for Tengrinews.kz

## Website Description:
[Tengrinews](https://tengrinews.kz/) is a Kazakhstani online news portal and media site, one of the largest information resources in the country
Tengrinews.kz publishes content such as:
- News about Kazakhstan and the world (politics, economy, society, incidents)
- Topics such as business, science and technology, health, and education
- Culture, entertainment, sports, and travel
- Author’s articles, opinions, blogs, analytical reviews
- Multimedia content: photos, videos, interviews, special projects

This script scrapes news from various sections (e.g., Kazakhstan, World, Crime, Science, and others).
Tengrinews.kz is considered a dynamic website because it continuously updates with fresh content. New articles appear as you scroll down, thanks to JavaScript that loads content in real-time. This means the site is constantly evolving, making it essential to use tools like Selenium or Playwright to capture the latest news and keep the data up-to-date


## How to Run Scraping

To scrape the latest news data from Tengrinews.kz, you can run the scraper manually or automate it using Apache Airflow.

### 1. Install Dependencies

Before running the scraper, make sure you have installed all necessary dependencies. You can do this by running:

```bash
pip install -r requirements.txt
