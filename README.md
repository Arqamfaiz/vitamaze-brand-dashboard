# Vitamaze Brand Performance Dashboard

A brand management analytics dashboard for Vision Healthcare's **Vitamaze** brand,
tracking product performance, competitive positioning, market trends, and the
product launch pipeline in the German VMS (Vitamins, Minerals & Supplements) market.

Built as a portfolio project for the **Working Student Brand Management** role
at Vision Healthcare NV (Munich).

**Live demo:** https://vitamaze-brand-dashboard-jlkjjca4n6kmjjfxbgmu7b.streamlit.app/

---

## What this dashboard contains

Five sections navigated from the sidebar:

1. **Brand Overview** — 12-month revenue trend, category split, top products by revenue.
   Shows seasonality patterns (winter vitamin D spike) useful for campaign planning.

2. **Product Performance** — Drill into any of the 12 Vitamaze SKUs. Units sold,
   BSR (Best Seller Rank) tracking, rating vs return rate scatter across the portfolio.

3. **Competitor Landscape** — 8 brands mapped by revenue, portfolio breadth, channel
   strategy, and rating. Identifies Vitamaze's positioning gap (quality leader, but
   smaller portfolio than Natural Elements or Nature Love).

4. **Market Trends** — 8 trends in the German VMS market with YoY growth rates,
   relevance scoring, and recommended actions. Highlights gummy vitamins (+25% YoY)
   and personalised subscriptions (+22% YoY) as the biggest opportunities.

5. **Launch Pipeline** — 5 upcoming products mapped to specific market gaps, with
   timeline and strategic rationale for each.

---

## What is real / what is illustrative

**Real:**
- Vitamaze product names, prices, and review counts (from the public Amazon.de storefront)
- Competitor brands and positioning (Natural Elements, Nature Love, Gloryfeel, etc.)
- Market trend growth rates (published German dietary supplement reports)
- Vision Healthcare acquisition history and brand portfolio structure

**Illustrative:**
- Monthly sales volumes, revenue figures, BSR rankings
- Exact competitor revenue estimates
- Product launch pipeline items

---

## Why this project

The JD asks for: brand strategy support, market and competitor research, product
launch coordination, performance reports, and health & nutrition trend analysis.
This dashboard covers each of those activities with real Vitamaze and competitor data.

My background at GSK (55,000+ pharmacy outlets, distribution KPI tracking, product
launch support) gives me direct experience in the consumer healthcare data ecosystem
that Vision Healthcare operates in.

---

## Local setup

```bash
git clone https://github.com/Arqamfaiz/vitamaze-brand-dashboard.git
cd vitamaze-brand-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## About the author

Arqam Faiz Siddiqui — M.Sc. International Information Systems at FAU
Erlangen-Nurnberg, with a BBA in Business Administration and prior
experience in pharmaceutical brand analytics at GSK.

Not affiliated with or endorsed by Vision Healthcare NV or Vitamaze GmbH.
