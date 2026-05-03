"""
Vitamaze Brand Performance Dashboard
=====================================
Brand management analytics for Vision Healthcare's Vitamaze brand.
Tracks product performance, competitive positioning, market trends,
and the product launch pipeline.

Author: Arqam Faiz Siddiqui
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Vitamaze Brand Dashboard", page_icon="V", layout="wide", initial_sidebar_state="expanded")

VHC_TEAL = "#009B8D"
VHC_DARK = "#1A3A3A"
VITAMAZE_ORANGE = "#E8751A"
ACCENT = "#F39C12"
LIGHT_BG = "#F7FAFA"

st.markdown(f"""<style>
.header {{ color: {VHC_DARK}; font-weight: 700; padding-bottom: 0.4rem; border-bottom: 3px solid {VHC_TEAL}; margin-bottom: 1.2rem; }}
.insight {{ background-color: {LIGHT_BG}; border-left: 4px solid {VHC_TEAL}; padding: 0.85rem 1rem; border-radius: 0.3rem; margin: 0.8rem 0; font-size: 0.95em; }}
div[data-testid="metric-container"] {{ background-color: #FAFAFA; border-radius: 0.5rem; padding: 0.7rem; border: 1px solid #E5E7EB; }}
</style>""", unsafe_allow_html=True)

DATA_DIR = Path(__file__).parent / "data"

@st.cache_data
def load_all():
    products = pd.read_csv(DATA_DIR / "product_portfolio.csv")
    sales = pd.read_csv(DATA_DIR / "monthly_sales.csv")
    sales["month"] = pd.to_datetime(sales["month"])
    competitors = pd.read_csv(DATA_DIR / "competitor_landscape.csv")
    trends = pd.read_csv(DATA_DIR / "market_trends.csv")
    launches = pd.read_csv(DATA_DIR / "product_launches.csv")
    return products, sales, competitors, trends, launches

products, sales, competitors, trends, launches = load_all()

with st.sidebar:
    st.markdown("### Navigation")
    section = st.radio("Section", ["Brand Overview", "Product Performance", "Competitor Landscape", "Market Trends", "Launch Pipeline"], label_visibility="collapsed")
    st.divider()
    st.caption("Brand performance tracker for Vitamaze, Vision Healthcare's Amazon-first VMS brand in the DACH region. Real product names and competitor brands; sales figures are illustrative.")
    st.caption("Built by Arqam Faiz Siddiqui")

st.markdown("<h1 class='header'>Vitamaze Brand Performance Dashboard</h1>", unsafe_allow_html=True)
st.markdown("Brand management analytics for **Vitamaze** (Vision Healthcare NV). Tracks product performance across Amazon.de and e-pharma channels, competitive positioning in the German VMS market, consumer trends, and the product launch pipeline.")

with st.expander("What is real / what is illustrative"):
    st.markdown("""**Real:** Product names, prices, and review counts are from the public Vitamaze Amazon.de storefront. Competitor brands (Natural Elements, Nature Love, Gloryfeel, etc.) and their positioning are based on published industry reports and public Amazon data. Market trend growth rates reference published 2024-2025 German dietary supplement market reports.\n\n**Illustrative:** Specific monthly sales volumes, revenue figures, BSR rankings, and exact competitor revenue estimates. Real internal Vision Healthcare data is confidential.""")

st.divider()

if section == "Brand Overview":
    st.subheader("Brand Overview: Vitamaze")
    total_rev = sales["revenue_eur"].sum()
    total_units = sales["units_sold"].sum()
    avg_rating = products["avg_rating"].mean()
    total_reviews = products["review_count"].sum()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Revenue (12mo)", f"\u20ac{total_rev:,.0f}")
    c2.metric("Units Sold (12mo)", f"{total_units:,}")
    c3.metric("Avg Product Rating", f"{avg_rating:.1f} / 5.0")
    c4.metric("Total Reviews", f"{total_reviews:,}")

    st.markdown("##### Monthly revenue trend")
    rev_by_month = sales.groupby("month")["revenue_eur"].sum().reset_index()
    fig = px.area(rev_by_month, x="month", y="revenue_eur", template="plotly_white", color_discrete_sequence=[VHC_TEAL], labels={"month": "Month", "revenue_eur": "Revenue (EUR)"})
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("##### Revenue by category")
        cat_rev = sales.groupby("category")["revenue_eur"].sum().reset_index().sort_values("revenue_eur", ascending=False)
        fig2 = px.bar(cat_rev, x="revenue_eur", y="category", orientation="h", color_discrete_sequence=[VHC_TEAL], template="plotly_white", labels={"revenue_eur": "Revenue (EUR)", "category": ""})
        fig2.update_layout(height=380, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig2, use_container_width=True)
    with col_r:
        st.markdown("##### Top products by revenue")
        prod_rev = sales.groupby("product_name")["revenue_eur"].sum().reset_index().sort_values("revenue_eur", ascending=False).head(6)
        fig3 = px.bar(prod_rev, x="revenue_eur", y="product_name", orientation="h", color_discrete_sequence=[VITAMAZE_ORANGE], template="plotly_white", labels={"revenue_eur": "Revenue (EUR)", "product_name": ""})
        fig3.update_layout(height=380, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown(f"""<div class='insight'><b>Key takeaway:</b> Vitamaze's top 3 SKUs (Biotin, L-Arginine, Vitamin D3+K2) account for roughly half of total revenue. The winter seasonality spike (Oct-Feb) is clearly visible in the revenue trend, driven by vitamin D and immune-support products. This seasonality should inform inventory planning and campaign timing.</div>""", unsafe_allow_html=True)

elif section == "Product Performance":
    st.subheader("Product Performance Detail")
    selected = st.selectbox("Select product", options=sales["product_name"].unique())
    prod_data = sales[sales["product_name"] == selected]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Units (12mo)", f"{prod_data['units_sold'].sum():,}")
    c2.metric("Total Revenue", f"\u20ac{prod_data['revenue_eur'].sum():,.0f}")
    c3.metric("Avg Rating", f"{prod_data['avg_rating'].mean():.1f}")
    c4.metric("Avg Return Rate", f"{prod_data['return_rate_pct'].mean():.1f}%")

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("##### Units sold over time")
        fig = px.bar(prod_data, x="month", y="units_sold", color_discrete_sequence=[VHC_TEAL], template="plotly_white", labels={"month": "Month", "units_sold": "Units"})
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    with col_r:
        st.markdown("##### Amazon BSR (Best Seller Rank)")
        fig2 = px.line(prod_data, x="month", y="amazon_bsr", color_discrete_sequence=[VITAMAZE_ORANGE], template="plotly_white", labels={"month": "Month", "amazon_bsr": "BSR (lower = better)"}, markers=True)
        fig2.update_yaxes(autorange="reversed")
        fig2.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("##### All products: rating vs return rate")
    ps = sales.groupby("product_name").agg(avg_rating=("avg_rating", "mean"), return_rate=("return_rate_pct", "mean"), total_revenue=("revenue_eur", "sum")).reset_index()
    fig3 = px.scatter(ps, x="avg_rating", y="return_rate", size="total_revenue", hover_data=["product_name"], color_discrete_sequence=[VHC_TEAL], template="plotly_white", labels={"avg_rating": "Avg Rating", "return_rate": "Return Rate (%)"})
    fig3.update_layout(height=380, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig3, use_container_width=True)

elif section == "Competitor Landscape":
    st.subheader("German VMS Amazon Competitor Landscape")
    st.caption("Top Amazon-first supplement brands in the DACH region. Revenue estimates based on published industry reports.")

    st.markdown("##### Estimated revenue by brand (EUR M)")
    comp_sorted = competitors.sort_values("est_revenue_eur_m", ascending=True)
    colors = [VITAMAZE_ORANGE if b == "Vitamaze" else VHC_TEAL for b in comp_sorted["brand"]]
    fig = go.Figure(go.Bar(x=comp_sorted["est_revenue_eur_m"], y=comp_sorted["brand"], orientation="h", marker_color=colors, text=comp_sorted["est_revenue_eur_m"].apply(lambda x: f"\u20ac{x}M"), textposition="outside"))
    fig.update_layout(template="plotly_white", height=400, margin=dict(l=20, r=60, t=20, b=20), xaxis_title="Estimated Revenue (EUR M)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("##### Rating vs portfolio breadth")
    fig2 = px.scatter(competitors, x="num_products", y="avg_rating", size="est_revenue_eur_m", color="primary_channel", hover_data=["brand", "key_strength"], template="plotly_white", labels={"num_products": "Number of Products", "avg_rating": "Avg Rating", "primary_channel": "Channel"})
    fig2.update_layout(height=400, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("##### Competitor profiles")
    st.dataframe(competitors.sort_values("est_revenue_eur_m", ascending=False), use_container_width=True, hide_index=True, column_config={"brand": "Brand", "hq": "HQ", "est_revenue_eur_m": st.column_config.NumberColumn("Revenue (EUR M)", format="\u20ac%dM"), "num_products": "Products", "avg_rating": "Rating", "primary_channel": "Primary Channel", "key_strength": "Key Strength"})

    st.markdown("""<div class='insight'><b>Vitamaze's position:</b> 5th by revenue in the DACH Amazon VMS market, but with the highest average rating (4.6) among brands with 20+ products. The "Made in Germany" positioning and VHC platform synergies (shared logistics, digital marketing hub, cross-sell with Nupure) are the main competitive advantages. Gap: portfolio breadth vs Natural Elements (23 vs 66 SKUs).</div>""", unsafe_allow_html=True)

elif section == "Market Trends":
    st.subheader("German VMS Market Trends")
    st.caption("Key consumer and channel trends shaping the health and nutrition supplements market in Germany.")

    st.markdown("##### Trend growth rates (YoY %)")
    ts = trends.sort_values("growth_yoy_pct", ascending=True)
    fig = px.bar(ts, x="growth_yoy_pct", y="trend", orientation="h", color="relevance_to_vitamaze", color_discrete_map={"High": VHC_TEAL, "Medium": ACCENT, "Low (gap)": "#E74C3C", "Already strong": "#27AE60"}, template="plotly_white", labels={"growth_yoy_pct": "YoY Growth (%)", "trend": "", "relevance_to_vitamaze": "Relevance"})
    fig.update_layout(height=420, margin=dict(l=20, r=20, t=20, b=20), legend=dict(orientation="h", yanchor="bottom", y=-0.3))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("##### Recommended actions by trend")
    st.dataframe(trends[["trend", "growth_yoy_pct", "relevance_to_vitamaze", "action"]], use_container_width=True, hide_index=True, column_config={"trend": "Trend", "growth_yoy_pct": "Growth (%)", "relevance_to_vitamaze": "Relevance", "action": "Recommended Action"})

    st.markdown("""<div class='insight'><b>Biggest opportunity:</b> Gummy vitamins are growing at 25% YoY but Vitamaze has no gummy SKUs. VitaYummy (a VHC sister brand acquired Nov 2025) already operates in this space, so cross-brand learnings and shared manufacturing could accelerate a Vitamaze gummy line without starting from scratch.</div>""", unsafe_allow_html=True)

elif section == "Launch Pipeline":
    st.subheader("Product Launch Pipeline")
    st.caption("Upcoming product launches aligned with market trends and portfolio gaps.")

    status_counts = launches["status"].value_counts()
    c1, c2, c3 = st.columns(3)
    c1.metric("In Development", status_counts.get("In Development", 0) + status_counts.get("Formulation", 0))
    c2.metric("In Planning", status_counts.get("Planning", 0))
    c3.metric("Concept Stage", status_counts.get("Concept", 0))

    st.markdown("##### Launch roadmap")
    st.dataframe(launches, use_container_width=True, hide_index=True, column_config={"product": "Product", "target_launch": "Target Launch", "status": "Status", "category": "Category", "rationale": "Market Rationale"})

    st.markdown("##### Launch timeline")
    fig = px.scatter(launches, x="target_launch", y="category", size=[40]*len(launches), color="status", hover_data=["product", "rationale"], color_discrete_map={"In Development": VHC_TEAL, "Formulation": ACCENT, "Planning": "#95A5A6", "Concept": "#BDC3C7"}, template="plotly_white", labels={"target_launch": "Target Quarter", "category": "Category"})
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), legend=dict(orientation="h", yanchor="bottom", y=-0.3))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""<div class='insight'><b>Strategic logic:</b> Each pipeline product addresses a specific market gap identified in the trends analysis. Ashwagandha and Collagen target the two fastest-growing Amazon.de supplement categories. The Vitamin D Gummy tests format extension of the bestselling D3+K2 SKU. The Prenatal line opens an entirely new consumer segment for Vitamaze.</div>""", unsafe_allow_html=True)

st.divider()
st.markdown("""<div style='text-align: center; color: #888; font-size: 0.85em; padding-top: 1em;'>Built by Arqam Faiz Siddiqui as a portfolio project for the Vision Healthcare Working Student Brand Management application.<br>Product names and competitor brands are real; sales figures are illustrative. Not affiliated with or endorsed by Vision Healthcare NV.</div>""", unsafe_allow_html=True)
