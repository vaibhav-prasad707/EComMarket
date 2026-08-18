from pathlib import Path
import json
from collections import Counter

base = Path('/home/ubuntu/greentern-ecommerce-research')
rows = json.loads((base/'client/src/data/platforms.json').read_text())

def count(field, value=None):
    vals = [r[field] for r in rows if value is None or r[field] == value]
    return len(vals)

summary = {
    'total': len(rows),
    'horizontal': count('type','Horizontal'),
    'vertical': count('type','Vertical'),
    'category_counts': dict(Counter(r['category'] for r in rows)),
    'profitability_counts': dict(Counter(r['profitability'] for r in rows)),
    'private_label_yes': sum(1 for r in rows if r['private_label'].startswith('Yes')),
    'quick_or_same_day': sum(1 for r in rows if r['quick_delivery'].startswith('Yes') or r['quick_delivery'].startswith('Same-day')),
    'public_or_listed_parent': sum(1 for r in rows if 'Public' in r['funding_stage'] or 'listed' in r['funding_stage']),
    'explicit_scale_disclosures': sum(1 for r in rows if not r['scale_metric'].startswith('NPD')),
    'source_count': len(set(r['source_url'] for r in rows)),
}
(base/'client/src/data/summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2))

category_lines = '\n'.join(f'| {k} | {v} |' for k,v in sorted(summary['category_counts'].items(), key=lambda kv:(-kv[1], kv[0])))
profit_lines = '\n'.join(f'| {k} | {v} |' for k,v in sorted(summary['profitability_counts'].items(), key=lambda kv:(-kv[1], kv[0])))

memo = f'''# India E-commerce Platform Research — Working Memo

## Scope and method
This research compiles {summary['total']} platforms operating in India, split into {summary['horizontal']} horizontal marketplaces and {summary['vertical']} vertical/specialty platforms. Each row uses a fixed ten-attribute schema plus derived Type and Category fields. The source note and URL are retained for every row. “NPD” means not publicly disclosed in the reviewed source set; it is not a zero and is not an estimate.

## Dataset signals
The specialty bucket is intentionally broad: fashion, beauty, eyewear, grocery/quick commerce, electronics, furniture/home, baby/kids, and D2C-led categories appear alongside general marketplaces. {summary['private_label_yes']} of 30 rows explicitly identify an owned or private-label assortment, while {summary['quick_or_same_day']} rows identify some quick or same-day capability. Only {summary['explicit_scale_disclosures']} rows carry an explicit scale figure in this first pass; that unevenness is a finding about disclosure quality, not a reason to fill gaps with guesses.

## Category mix
| Category | Platforms |
|---|---:|
{category_lines}

## Profitability coding
| Status | Platforms |
|---|---:|
{profit_lines}

## Insights to test in the dashboard
1. **Breadth is not the same as comparability.** Horizontal marketplaces are easier to recognize as scale businesses, but platform-level MAU and GMV disclosure is inconsistent. The dashboard therefore separates explicit figures from NPD rather than ranking every player on a synthetic metric.
2. **Verticalization is a growth strategy, not a niche footnote.** The specialty set spans high-frequency quick commerce and high-consideration categories such as furniture and eyewear; this makes category-specific fulfilment and owned assortment visible as strategic levers.
3. **Private labels are widespread across both buckets.** Owned assortments appear in marketplaces, grocery, fashion, beauty, electronics, and D2C brands. The pattern suggests margin/control and differentiation are common strategic responses, though this dataset does not claim causality.
4. **Quick commerce is concentrated in urban use cases but broadening in scope.** Bain reports that more than two-thirds of e-grocery orders and one-tenth of e-retail spend were on quick-commerce platforms in 2024, with more than 40% annual growth forecast to 2030. [1]
5. **Tier-2 and Tier-3 expansion is a structural tailwind.** Bain reports three in five new shoppers since 2020 came from Tier-3 or smaller cities and 60% of new sellers since 2021 came from Tier-2 or smaller cities. [1]

## References
[1]: https://www.bain.com/insights/how-india-shops-online-2025/ "Bain & Company — How India Shops Online 2025"
[2]: https://investor.meesho.com/results "Meesho Investor Relations — Results"
[3]: https://www.lenskart.com/corporate/investorrelations "Lenskart Investor Relations"
[4]: https://www.nykaa.com/investor-relations "Nykaa Investor Relations"
[5]: https://www.ril.com/ar2024-25 "Reliance Industries Annual Report FY2024–25"
[6]: https://www.swiggy.com/corporate/investor-relations/ "Swiggy Investor Relations"
[7]: https://www.eternal.com/investor-relations/ "Eternal Investor Relations"
'''
(base/'Greentern_Research_Memo.md').write_text(memo)
print(json.dumps(summary, indent=2))
