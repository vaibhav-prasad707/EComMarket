# Signal & Shelf — India E-commerce Research

**Signal & Shelf** is a static research dashboard created for the **Greentern Data Analyst Intern assignment**. It presents a source-first comparison of **30 e-commerce platforms operating in India**, divided into horizontal marketplaces and vertical or specialty platforms.

The dashboard is designed to make the research easier to inspect, compare, and share without presenting unsupported precision. It includes interactive charts, platform filters, category filtering, searchable rows, source links, and CSV download functionality.

---

## Research Scope

The dataset contains two comparison buckets:

| Bucket | Count | Coverage |
|---|---:|---|
| **Horizontal marketplaces** | 13 | General, value, B2B, open-commerce, social-commerce, government, and super-app marketplaces |
| **Vertical / specialty platforms** | 17 | Fashion, beauty, eyewear, grocery, quick commerce, electronics, furniture, baby and kids, and D2C-led categories |

The platform list includes:

- Amazon India
- Flipkart
- Meesho
- JioMart
- Snapdeal
- Tata CLiQ
- Tata Neu
- Myntra
- AJIO
- Nykaa
- Purplle
- Lenskart
- Blinkit
- Zepto
- Swiggy Instamart
- BigBasket
- Croma
- Pepperfry
- Mamaearth
- boAt
- FirstCry
- Urban Ladder
- Vijay Sales Online
- And other relevant Indian platforms

---

## Fixed Research Attributes

The research uses a fixed **ten-attribute schema**. This prevents the dataset from being backfilled inconsistently after research has started.

| Attribute | Description |
|---|---|
| **Parent / ownership** | Current controlling company or ownership structure |
| **Primary category** | Standardized category used for grouping and charting |
| **Scale metric** | Publicly disclosed MAU, GMV, revenue, orders, or people-served figure where comparable evidence was available |
| **Year founded** | Platform or operating-company launch year |
| **Funding / stage** | Public, private, corporate-backed, or late-stage context |
| **Profitability status** | Standardized profitability classification |
| **Private-label presence** | Whether an owned or private-label assortment is publicly visible, with examples where available |
| **Quick / same-day capability** | Whether quick commerce, same-day delivery, or equivalent rapid fulfilment is publicly indicated |
| **Customer base** | Urban, national, Tier 2–3, value, premium, or other strategic customer orientation |
| **Most recent notable move** | Recent acquisition, funding, listing, expansion, category, or delivery-related move |

### Derived Fields

The dataset also includes two derived fields:

| Derived Field | Purpose |
|---|---|
| **Type** | Horizontal or Vertical comparison bucket |
| **Category** | Standardized category label for pivoting and visual analysis |

---

## Evidence & Data-Quality Rules

The research prioritizes:

- Company investor-relations pages
- Annual reports
- Official company pages
- Reputable market research
- Established business reporting

Each row retains a **source note** and **source URL**.

> **NPD** means "not publicly disclosed" in the reviewed source set. It is not zero, missing data to be guessed, or an estimate.

The initial research pass found that platform-level scale metrics are not consistently disclosed across all companies. Only **four of the thirty rows** contain an explicit comparable scale figure in the current working dataset.

This uneven disclosure is preserved as a methodological finding rather than hidden through synthetic ranking.

The dashboard does **not** fabricate:

- Customer reviews
- Ratings
- MAU
- GMV
- Revenue
- Order volume
- Profitability figures

Before submitting the assignment, the researcher should re-check the latest annual reports and filings because company disclosures can change after the research date.

---

## Key Findings

The dashboard highlights several patterns from the compiled sample:

### 1. Vertical e-commerce is broad rather than narrow

The specialty bucket includes both high-frequency businesses such as quick commerce and high-consideration categories such as:

- Eyewear
- Furniture
- Electronics
- Baby products
- Fashion
- Beauty
- Grocery

### 2. Owned assortment is a shared strategic playbook

**Twenty-two of the thirty rows** explicitly identify an owned or private-label assortment across marketplaces, fashion, beauty, grocery, electronics, and D2C businesses.

### 3. Rapid fulfilment is concentrated but expanding

**Nineteen rows** identify quick or same-day capability, although delivery speed varies by:

- City
- Category
- Fulfilment model
- Partner network

### 4. Comparability remains limited

MAU, GMV, revenue, order volume, and people-served metrics are reported using different definitions and dates.

The dashboard therefore shows **evidence status instead of forcing a universal ranking**.

### 5. India's broader market context supports the category split

Bain & Company's *How India Shops Online 2025* reports approximately **$60 billion of Indian e-retail GMV**, significant Tier 2–3 shopper expansion, and the growing importance of quick commerce.

See the reference link in `Greentern_Research_Memo.md`.

---

## Dashboard Features

The static dashboard provides the following interactions:

- Filter platforms by **All**, **Horizontal**, or **Vertical**
- Filter by standardized category
- Search platform names
- Click table headers to sort rows
- Open source links for each platform
- Download the currently filtered rows as CSV
- Inspect horizontal-versus-vertical composition in a donut chart
- Compare category density in a horizontal bar chart
- Review methodology notes and evidence dates alongside headline figures

---

## Project Structure

```text
.
├── README.md
├── Greentern_DataAnalystIntern_Assignment.xlsx
├── Greentern_Research_Memo.md
├── ideas.md
├── research_notes.md
├── scripts/
│   ├── analyze_dataset.py
│   └── build_dataset.py
├── client/
│   └── src/
│       ├── data/
│       │   ├── platforms.json
│       │   └── summary.json
│       ├── pages/
│       │   └── Home.tsx
│       └── index.css
└── server/
    └── index.ts
