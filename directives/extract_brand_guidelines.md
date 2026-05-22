# Extract Brand Guidelines Directive

## Goal
Extract brand colors, typography, logos, hero images, and styling effects from a target website using the Firecrawl API.

## Inputs
- `url`: The target website to scrape.

## Tools/Scripts to Use
- `execution/scrape_brand.py`: A Python script that uses the Firecrawl API to extract branding, images, and structured styling information.

## Execution Steps
1. Verify `FIRECRAWL_API_KEY` is present in the `.env` file. If not, prompt the user for it.
2. Run the script: `python execution/scrape_brand.py <url>`
3. The script will output a JSON payload to `tmp/brand_data.json`.
4. Read the generated JSON file and present the extracted brand guidelines, colors, typography, and styling effects to the user or update relevant `SKILL.md` files as requested.

## Outputs
- A JSON file in `tmp/brand_data.json` containing:
  - `branding`: Firecrawl's native extraction of colors, typography, and spacing.
  - `json`: LLM extraction containing `hero_images` and `styling_effects`.
