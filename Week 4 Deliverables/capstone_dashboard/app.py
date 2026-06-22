import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="InGen Market Dashboard",
    layout="wide"
)

# -----------------------------------
# DATABASE CONNECTION
# -----------------------------------

conn = sqlite3.connect(
    "ingen_market_warehouse.sqlite"
)

# -----------------------------------
# SIDEBAR
# -----------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "US Market",
        "Fari Eldercare",
        "Sentinel Security",
        "Competitor Explorer"
    ]
)

# ===================================
# GLOBAL MARKET
# ===================================

if page == "US Market":

    st.title("US Market Overview")

    query = """
    SELECT
        c.countryName,
        c.region,
        m.vertical,
        m.marketType,
        m.marketSize,
        m.unit
    FROM market_estimates m
    JOIN countries c
    ON m.countryId = c.countryId
    """

    df = pd.read_sql(query, conn)

    # -----------------------------
    # ELDERCARE
    # -----------------------------

    eldercare_df = df[
        df["vertical"] == "Eldercare"
    ]

    eldercare_tam = eldercare_df[
        eldercare_df["marketType"] == "TAM"
    ]["marketSize"].iloc[0]

    eldercare_sam = eldercare_df[
        eldercare_df["marketType"] == "SAM"
    ]["marketSize"].iloc[0]

    st.header("Eldercare Market")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "TAM",
            f"{eldercare_tam:,.0f} Users"
        )

    with col2:
        st.metric(
            "SAM",
            f"{eldercare_sam:,.0f} Users"
        )

    fig1 = px.bar(
        eldercare_df,
        x="marketSize",
        y="marketType",
        orientation="h",
        text="marketSize",
        title="Eldercare TAM vs SAM"
    )

    fig1.update_traces(
        texttemplate="%{x:,.0f}",
        textposition="outside"
    )

    fig1.update_layout(
        showlegend=False,
        yaxis_title="",
        xaxis_title="Users"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # PHYSICAL SECURITY
    # -----------------------------

    security_df = df[
        df["vertical"] == "Physical Security"
    ]

    security_tam = security_df[
        security_df["marketType"] == "TAM"
    ]["marketSize"].iloc[0]

    security_sam = security_df[
        security_df["marketType"] == "SAM"
    ]["marketSize"].iloc[0]

    st.header("Physical Security Market")

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "TAM",
            f"${security_tam:,.0f}"
        )

    with col4:
        st.metric(
            "SAM",
            f"${security_sam:,.0f}"
        )

    fig2 = px.bar(
        security_df,
        x="marketSize",
        y="marketType",
        orientation="h",
        text="marketSize",
        title="Physical Security TAM vs SAM"
    )

    fig2.update_traces(
        texttemplate="$%{x:,.0f}",
        textposition="outside"
    )

    fig2.update_layout(
        showlegend=False,
        yaxis_title="",
        xaxis_title="USD"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


# ===================================
# FARI
# ===================================

elif page == "Fari Eldercare":

    st.title("Fari Eldercare")

    tam_query = """
    SELECT *
    FROM market_estimates
    WHERE vertical='Eldercare'
    """

    indicators_query = """
    SELECT *
    FROM demographic_indicators
    WHERE vertical='Eldercare'
    """

    tam_df = pd.read_sql(
        tam_query,
        conn
    )

    indicator_df = pd.read_sql(
        indicators_query,
        conn
    )

    col1, col2 = st.columns(2)

    with col1:

        tam = tam_df[
            tam_df["marketType"]=="TAM"
        ]["marketSize"].iloc[0]

        st.metric(
            "TAM",
            f"{tam:,.0f} Users"
        )

    with col2:

        sam = tam_df[
            tam_df["marketType"]=="SAM"
        ]["marketSize"].iloc[0]

        st.metric(
            "SAM",
            f"{sam:,.0f} Users"
        )

    st.subheader(
        "Eldercare Indicators"
    )

    st.dataframe(
        indicator_df[
            [
                "variable",
                "value",
                "unit"
            ]
        ]
    )



# ===================================
# SENTINEL
# ===================================

elif page == "Sentinel Security":

    st.title(
        "Sentinel Prime AI"
    )

    market_query = """
    SELECT *
    FROM market_estimates
    WHERE vertical='Physical Security'
    """

    indicator_query = """
    SELECT *
    FROM demographic_indicators
    WHERE vertical='Physical Security'
    """

    market_df = pd.read_sql(
        market_query,
        conn
    )

    indicator_df = pd.read_sql(
        indicator_query,
        conn
    )

    col1, col2 = st.columns(2)

    with col1:

        tam = market_df[
            market_df["marketType"]=="TAM"
        ]["marketSize"].iloc[0]

        st.metric(
            "TAM",
            f"${tam:,.0f}"
        )

    with col2:

        sam = market_df[
            market_df["marketType"]=="SAM"
        ]["marketSize"].iloc[0]

        st.metric(
            "SAM",
            f"${sam:,.0f}"
        )

    st.subheader(
        "Security Indicators"
    )

    st.dataframe(
        indicator_df[
            [
                "variable",
                "value",
                "unit"
            ]
        ]
    )

# ===================================
# COMPETITORS
# ===================================

elif page == "Competitor Explorer":

    st.title(
        "Competitor Explorer"
    )

    query = """
    SELECT
        competitorName,
        countryName,
        vertical,
        distributionChannel
    FROM competitors
    JOIN countries
    ON competitors.countryId =
       countries.countryId
    """

    df = pd.read_sql(
        query,
        conn
    )

    verticals = [
        "All"
    ] + sorted(
        df["vertical"]
        .unique()
        .tolist()
    )

    selected = st.selectbox(
        "Vertical",
        verticals
    )

    if selected != "All":

        df = df[
            df["vertical"] == selected
        ]

    st.dataframe(df)

    fig = px.histogram(
        df,
        x="countryName",
        title="Competitors by Country"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -----------------------------------
# CLOSE CONNECTION
# -----------------------------------

conn.close()
