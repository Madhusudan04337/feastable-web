---
name: firecrawl-brand-extracted
description: Scrape any website to extract its brand identity, design system, colors, typography, hero images, and styling effects using the Firecrawl API. Use this skill whenever a user wants to analyze a competitor's brand, extract styling from a URL to use as inspiration for a new website, or build a brand guideline document from an existing site.
---

# Brand Scraper Skill

This skill uses the Firecrawl API to extract structured brand data from any target URL.

## When to use this skill
- To extract the exact colors (primary, secondary, background, text) used on a website.
- To discover the typography and font families used for headings and body text.
- To pull a list of hero images, logos, and their URLs for inspiration.
- To identify key styling effects, component styles (e.g. button border radiuses, shadows), and interactive elements.
- When generating a brand guideline document (like `SKILL_brandguidelines.md`) based on an existing website.

## How to use this skill

1. Check if the user has provided a URL to scrape.
2. If `FIRECRAWL_API_KEY` is not present in the workspace `.env` file, kindly ask the user to provide it.
3. Run the Python scraping script located in the `scripts/` directory:
   ```bash
   python firecrawl-brand-extracted/scripts/scrape.py <url>
   ```
4. Capture the JSON output from stdout. The output will contain:
   - `branding`: Firecrawl's native extraction of logos, colors, fonts, spacing, and component styles.
   - `json`: Structured LLM extraction containing `hero_images` and `styling_effects`.
5. Use the extracted data to answer the user's questions or generate a comprehensive brand guideline artifact for them. Do NOT dump the raw JSON back to the user—synthesize it into a clean, readable Markdown format.
