"""
Generate illustrative brand performance data for Vision Healthcare's Vitamaze brand.

Real facts used:
- Vitamaze is Amazon-first, Heidelberg-based, acquired by VHC in 2021
- Top products: Vitamin D3+K2, L-Arginine, Biotin, Vitamin K Complex, Milk Thistle, Omega-3
- Top 500 Amazon.de seller (ranked ~335th)
- Competitors: Natural Elements, Nature Love, Gloryfeel, Feel Natural, WeightWorld
- German VMS Amazon market: Omega-3 ~€16M, Probiotics ~€10M, Vitamin B ~€20M (2020 data)
- Products are "Made in Germany", clean label, no unnecessary additives
- Revenue ~€22M in 2021 at acquisition

Illustrative: specific monthly sales figures, exact ratings, competitor share splits.
"""
import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

# ── 1. PRODUCT PORTFOLIO with real Vitamaze products ──
products = pd.DataFrame([
    {"sku": "VMZ-D3K2", "product_name": "Vitamin D3 + K2 5000 IU (180 Tablets)", "category": "Vitamins", "launch_date": "2018-03-01", "avg_rating": 4.7, "review_count": 5054, "price_eur": 19.97, "status": "Active"},
    {"sku": "VMZ-LARG", "product_name": "L-Arginine 4500mg (360 Capsules)", "category": "Amino Acids", "launch_date": "2017-09-01", "avg_rating": 4.5, "review_count": 5442, "price_eur": 24.97, "status": "Active"},
    {"sku": "VMZ-BIOT", "product_name": "Biotin + Zinc + Selenium (365 Tablets)", "category": "Hair Skin Nails", "launch_date": "2017-06-01", "avg_rating": 4.6, "review_count": 8230, "price_eur": 17.97, "status": "Active"},
    {"sku": "VMZ-VITK", "product_name": "Vitamin K Complex K1+K2 (120 Capsules)", "category": "Vitamins", "launch_date": "2019-01-01", "avg_rating": 4.7, "review_count": 1494, "price_eur": 17.97, "status": "Active"},
    {"sku": "VMZ-MILK", "product_name": "Milk Thistle 80% Silymarin (90 Capsules)", "category": "Herbal", "launch_date": "2018-08-01", "avg_rating": 4.6, "review_count": 2870, "price_eur": 15.97, "status": "Active"},
    {"sku": "VMZ-OMG3", "product_name": "Omega-3 1000mg Fish Oil (240 Capsules)", "category": "Omega & Oils", "launch_date": "2019-05-01", "avg_rating": 4.5, "review_count": 3640, "price_eur": 21.97, "status": "Active"},
    {"sku": "VMZ-ZINC", "product_name": "Zinc 25mg High Dose (365 Tablets)", "category": "Minerals", "launch_date": "2020-02-01", "avg_rating": 4.6, "review_count": 4120, "price_eur": 14.97, "status": "Active"},
    {"sku": "VMZ-CURC", "product_name": "Curcuma + Piperine (240 Capsules)", "category": "Herbal", "launch_date": "2019-11-01", "avg_rating": 4.5, "review_count": 3890, "price_eur": 18.97, "status": "Active"},
    {"sku": "VMZ-MSM", "product_name": "MSM 2000mg + Vitamin C (360 Tablets)", "category": "Joint Health", "launch_date": "2020-06-01", "avg_rating": 4.4, "review_count": 2150, "price_eur": 19.97, "status": "Active"},
    {"sku": "VMZ-PROB", "product_name": "Probiotics Complex 20 Strains (180 Capsules)", "category": "Gut Health", "launch_date": "2021-03-01", "avg_rating": 4.3, "review_count": 1240, "price_eur": 22.97, "status": "Active"},
    {"sku": "VMZ-MAGN", "product_name": "Magnesium 400mg Tri-Complex (360 Tablets)", "category": "Minerals", "launch_date": "2022-01-01", "avg_rating": 4.5, "review_count": 1680, "price_eur": 16.97, "status": "Active"},
    {"sku": "VMZ-IRON", "product_name": "Iron 40mg + Vitamin C (120 Capsules)", "category": "Minerals", "launch_date": "2023-06-01", "avg_rating": 4.4, "review_count": 620, "price_eur": 13.97, "status": "New Launch"},
])

# ── 2. MONTHLY SALES PERFORMANCE (illustrative, 12 months) ──
months = pd.date_range("2025-06-01", "2026-05-01", freq="MS")
sales_rows = []
for _, prod in products.iterrows():
    base_units = random.randint(800, 4000)
    for m in months:
        # Seasonal patterns: vitamins spike in winter
        season_mult = 1.0
        if m.month in [10, 11, 12, 1, 2]:
            season_mult = random.uniform(1.15, 1.35)
        elif m.month in [6, 7, 8]:
            season_mult = random.uniform(0.80, 0.95)

        units = int(base_units * season_mult * random.uniform(0.9, 1.1))
        revenue = round(units * prod["price_eur"] * random.uniform(0.92, 1.0), 2)  # account for discounts
        sales_rows.append({
            "month": m.strftime("%Y-%m-%d"),
            "sku": prod["sku"],
            "product_name": prod["product_name"],
            "category": prod["category"],
            "units_sold": units,
            "revenue_eur": revenue,
            "avg_rating": round(prod["avg_rating"] + random.uniform(-0.1, 0.1), 1),
            "new_reviews": random.randint(20, 120),
            "return_rate_pct": round(random.uniform(1.5, 4.5), 1),
            "amazon_bsr": random.randint(200, 8000),
        })

df_sales = pd.DataFrame(sales_rows)

# ── 3. COMPETITOR LANDSCAPE ──
competitors = pd.DataFrame([
    {"brand": "Natural Elements", "hq": "Monheim am Rhein, DE", "est_revenue_eur_m": 59, "num_products": 66, "avg_rating": 4.5, "primary_channel": "Amazon Exclusive", "key_strength": "Broadest Amazon portfolio in DACH"},
    {"brand": "Nature Love", "hq": "Bochum, DE", "est_revenue_eur_m": 42, "num_products": 50, "avg_rating": 4.6, "primary_channel": "Amazon + Retail", "key_strength": "Strong organic/vegan positioning"},
    {"brand": "Gloryfeel", "hq": "Hamburg, DE", "est_revenue_eur_m": 35, "num_products": 45, "avg_rating": 4.4, "primary_channel": "Amazon Exclusive", "key_strength": "Aggressive pricing strategy"},
    {"brand": "Feel Natural", "hq": "Buxtehude, DE", "est_revenue_eur_m": 28, "num_products": 38, "avg_rating": 4.5, "primary_channel": "Amazon + e-Pharma", "key_strength": "Clean label, family-owned trust"},
    {"brand": "Vitamaze", "hq": "Heidelberg, DE", "est_revenue_eur_m": 25, "num_products": 23, "avg_rating": 4.6, "primary_channel": "Amazon + e-Pharma", "key_strength": "Made in Germany quality, VHC platform synergies"},
    {"brand": "WeightWorld", "hq": "Manchester, UK", "est_revenue_eur_m": 20, "num_products": 55, "avg_rating": 4.3, "primary_channel": "Amazon + D2C", "key_strength": "Weight management niche leader"},
    {"brand": "Nutravita", "hq": "Hampshire, UK", "est_revenue_eur_m": 18, "num_products": 40, "avg_rating": 4.5, "primary_channel": "Amazon Exclusive", "key_strength": "Price-value leader UK/DACH"},
    {"brand": "Nupure (VHC)", "hq": "Netherlands", "est_revenue_eur_m": 22, "num_products": 12, "avg_rating": 4.7, "primary_channel": "e-Pharma + Amazon", "key_strength": "Probiotic specialist, same VHC group"},
])

# ── 4. MARKET TRENDS (German VMS market) ──
trends = pd.DataFrame([
    {"trend": "Gut health & probiotics", "growth_yoy_pct": 18, "relevance_to_vitamaze": "High", "action": "Expand probiotic line; leverage Nupure cross-sell within VHC group"},
    {"trend": "Plant-based & vegan supplements", "growth_yoy_pct": 15, "relevance_to_vitamaze": "Medium", "action": "Add vegan certification badges; develop plant-protein SKUs"},
    {"trend": "Personalised vitamin subscriptions", "growth_yoy_pct": 22, "relevance_to_vitamaze": "High", "action": "Pilot subscription model on vitamaze.shop; leverage VHC D2C expertise"},
    {"trend": "Amazon Subscribe & Save adoption", "growth_yoy_pct": 12, "relevance_to_vitamaze": "High", "action": "Optimise Subscribe & Save listings; improve repeat purchase rate"},
    {"trend": "e-Pharma channel growth (DocMorris, Shop Apotheke)", "growth_yoy_pct": 14, "relevance_to_vitamaze": "High", "action": "Increase e-pharma listings; bundle with complementary products"},
    {"trend": "Clean label & transparency", "growth_yoy_pct": 10, "relevance_to_vitamaze": "Already strong", "action": "Double down on 'Made in Germany' messaging and ingredient transparency"},
    {"trend": "Gummy vitamin format", "growth_yoy_pct": 25, "relevance_to_vitamaze": "Low (gap)", "action": "Evaluate gummy format entry; VitaYummy (VHC sister brand) as benchmark"},
    {"trend": "Sports nutrition crossover", "growth_yoy_pct": 11, "relevance_to_vitamaze": "Medium", "action": "Position L-Arginine and protein SKUs for fitness-conscious segment"},
])

# ── 5. PRODUCT LAUNCH TRACKER ──
launches = pd.DataFrame([
    {"product": "Ashwagandha KSM-66 (90 Capsules)", "target_launch": "Q3 2026", "status": "In Development", "category": "Adaptogens", "rationale": "Adaptogens trending +20% YoY; gap in current portfolio"},
    {"product": "Collagen Peptides (300g Powder)", "target_launch": "Q3 2026", "status": "Formulation", "category": "Beauty from Within", "rationale": "Beauty supplements growing 16% YoY; collagen is #1 search term"},
    {"product": "Vitamin D3 1000 IU Gummies (60ct)", "target_launch": "Q4 2026", "status": "Planning", "category": "Vitamins (Gummy)", "rationale": "Gummy format +25% YoY; test format extension of bestseller D3+K2"},
    {"product": "Magnesium Glycinate Sleep (120 Capsules)", "target_launch": "Q4 2026", "status": "Planning", "category": "Sleep & Relaxation", "rationale": "Sleep supplements +18% YoY; glycinate form preferred for bioavailability"},
    {"product": "Iron + Folate Prenatal (90 Capsules)", "target_launch": "Q1 2027", "status": "Concept", "category": "Prenatal", "rationale": "Prenatal market growing 15.7% CAGR; underserved on Amazon.de"},
])

# ── SAVE ──
products.to_csv("/home/claude/vhc_brand/data/product_portfolio.csv", index=False)
df_sales.to_csv("/home/claude/vhc_brand/data/monthly_sales.csv", index=False)
competitors.to_csv("/home/claude/vhc_brand/data/competitor_landscape.csv", index=False)
trends.to_csv("/home/claude/vhc_brand/data/market_trends.csv", index=False)
launches.to_csv("/home/claude/vhc_brand/data/product_launches.csv", index=False)

print(f"Products: {len(products)} SKUs")
print(f"Sales: {len(df_sales)} rows ({len(products)} products x {len(months)} months)")
print(f"Competitors: {len(competitors)} brands")
print(f"Trends: {len(trends)} trends")
print(f"Launches: {len(launches)} pipeline items")
