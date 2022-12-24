import streamlit as st

st.markdown("##  Anita Bhanja")
st.markdown("### Data Analyst")

st.markdown("""
    **I am a Data Analyst Enthusiast, with experience in working through entire life cycle of data analysis projects starting with data collection, data cleaning, data modelling, data analysis and data visualization. I can map the Business Requirements as a Business Analyst and as a Data Analyst translate them into operational dashboards and draw insights. I am experienced with the latest tools and technologies for helping businesses to understand their data, build data pipelines to collect data from multiple sources, structure to answer strategic queries and build dashboards for presenting the findings to both technical and non-technical audience. I have very good knowledge on Microsoft Excel, SQL, Tableau, PowerBI, Python, Agile methodology and ETL processes; Data Extraction, Data Transformation and Data Loading falls under my expertise.**
""")


st.markdown("""This web app is created to give you a glimpse into my skills and all these are built out of my own personal interest in the data and related topics.""")

st.markdown("### Data Visualizations - Tableau")
st.markdown("""
    Data Visualization is a very powerful tool for presenting the data in a more insightful way to the target audience. 
    Here in this section I present some of the visualizations or dashboards created using real world data sets using technologies like **Tableau**.
""")

with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Airbnb Listings in NewYork City](https://public.tableau.com/app/profile/anita.bhanja/viz/NewYorkCityAirbnb_16639602543610/NewYorkCityAirbnb)")
        st.write("""
        Interactive Dashboard to view the Map of the Airbnb listings in NewYork City
        """)
        st.image("images/NewYork_City_Airbnb.png")

    with col2:
        st.markdown("[Superstore Sales Projection](https://public.tableau.com/app/profile/anita.bhanja/viz/SalesProjection_16636216323450/SalesKPIDashboard)")
        st.write("""
        Interactive Dashboard to view the sales projection of Superstore
        """)
        st.image("images/Sales_KPI_Dashboard.png")

with st.container():
    col1, col2 = st.columns((4,4))
    with col1:
        st.markdown("[Park Crime Report (NYC)](https://public.tableau.com/app/profile/anita.bhanja/viz/ParkCrimeReportNYC/StatsNYCParkCrimes)")
        st.write("""
        Interactive Dashboard to view Crime Report for New York Parks (PDF Report Analysis)
        """)
        st.image("images/Stats NYC Park Crimes.png")
         
         
         

st.markdown("### Data Analysis using SQL")
st.markdown("""
    SQL is a powerful programming language that helps data analysts interact with data stored in Relational databases. 
    Here in this section I present the "Global Deforestation" project as part of SQL Nanodegree from Udacity using **SQL** and given recommendations.
""")
#st.markdown("[Global Deforestion](https://github.com/anitabhanja/SQL_NanoDegree/blob/main/Deforestation-exploration_report.pdf)")
#st.image("images/SQL_Nanodegree.PNG",width=350)
with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Global Deforestion](https://github.com/anitabhanja/SQL_NanoDegree/blob/main/Deforestation-exploration_report.pdf)")
        st.image("images/Global_Deforestation.PNG",width=350)

    with col2:
        st.markdown("[Udiddit, a social news aggregator](https://github.com/anitabhanja/SQL_NanoDegree/blob/main/udiddit-a-social-news-aggregator.pdf)")
        st.image("images/Udiddit.PNG",width=350)
        

st.markdown("### Magic of Excel in Data Analysis")
st.markdown("""
    Microsoft Excel is one of the most popular applications for data analysis. Equipped with built-in pivot tables, they are without a doubt the most sought-after analytic tool available. It is an all-in-one data management software that allows you to easily import, explore, clean, analyze, and visualize your data.
""")
st.markdown("[Pivot Table](https://github.com/anitabhanja/Magic-of-Excel)")
st.image("images/excel_pivot.png",width=350)


st.markdown("### Python and Data (Jupyter Notebooks)")
st.markdown("""
    Jupyter Notebooks is a great tool for all the data analysis tasks from exploring, cleaning, visualizing to present the data stories to the target audience.
""")

with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Exploratory data analysis on car features](https://github.com/anitabhanja/jupyternotebook/blob/main/Car_Features_EDA.ipynb)")
        st.write("""
        Exploratory Data Analysis or (EDA) on car dataset.
        
        """)
        st.image("images/EDA_CarFeatures.PNG",width=350)

    with col2:
        st.markdown("[Who Americans Spend Their Time With?](https://github.com/anitabhanja/jupyternotebook/blob/main/EDA-time-spent-with-relationships-by-age-us-checkpoint.ipynb)")
        st.write("""
        As humans, we have heavily relied on social relationships to thrive and who we spend time with evolves throughout our lifetime.
        """)
        st.image("images/Americans_Time_Spend.PNG",width=350)
