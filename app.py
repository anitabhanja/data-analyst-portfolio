import streamlit as st

st.markdown("# Anita Bhanja")
st.markdown("### Data Analyst")
st.markdown("""
    **I am a Data Science and Analytics Enthusiast, with experience of working through entire life cycle of data science projects starting with data collection, data cleaning, data analysis, data visualization and to some extent even in model building. I am experienced with the latest tools and technologies for helping the businesses to understand the their data, build data pipelines to collect the data from multiple sources to clean and structure the data to answer strategic queries as well as build dashboards for presenting the findings to both technical and non-technical audience**
""")


st.markdown("***This web app is created to give you a glimpse into my skills and all these are built out of my own personal interest in the data and the topics***")

st.markdown("### Data Visualizations (Tableau & R)")
st.markdown("""
    Data Visualization is a very powerful tool for presenting the data in a more insightful way to the target audience. 
    Here in this section I present some of the visualizations or dashboards created using real world data sets using technologies like **R and Tableau**.
""")

with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Covid-19 USA Cases 2020 to 2021](https://public.tableau.com/app/profile/umeshjn/viz/Covid-19CasesUSA/Covid19CaseUSA)")
        st.write("""
        Fight against Covid19 is into third year almost and the numbers are increasing against due to the new variant.
        """)
        st.image("images/Covid19 Case USA.png")

    with col2:
        st.markdown("[Covid Deaths in USA(2020 and 2021)](https://public.tableau.com/app/profile/umeshjn/viz/CovidDeathsinUSA2020and2021/CovidDeathsUSA2020and2021)")
        st.write("""
        So many deaths due to Covid and we have ended up treating them as just statictics which is very sad and painful if you really think about all the people who have lost their loved ones.
        """)
        st.image("images/750x.png")



with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("**New York State Cancer Death Rates 1976-2018**")
        st.write("""
        Humanity has been fighting a brave war with the cancer and the progress made since last 4-5 decades shows that there is lot of optimism. 
        """)
        st.image("images/nyscancerviz.PNG")

    with col2:
        st.markdown("**Drug Overdose Deaths in USA 2014-2019**")
        st.write("""
        Drug Overdose is one of the most biggest health concerns in America and this visualization gives you the view of Drug Overdose Death Rates 2014-2019. 
        """)
        st.image("images/750x.PNG")

       

with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("**Seattle Crimes Numbers Reported **")
        st.write("""
        Crimes in the cities are the biggest challenges for the law and order authorities. This dashboard view gives a glimpse of Seattle crimes numbers between 2008 and 2017. 
        """)
        st.image("images/750x.PNG")

    with col2:
        st.markdown("**Spider Species Identified in North America**")
        st.write("""
        There are over 45000 spider species in the world and 7000 out of those are in North American Countries. 
        """)
        st.image("images/750x.PNG")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Gun Violence in America](https://public.tableau.com/app/profile/umeshjn/viz/GunViolenceinAmerica_0/GunViolence)")
        st.write("""
        This dashboard gives you a view of the gun violence reported across America from 2014 to 2017.
        """)
        st.image("images/750x.png")

    with col2:
        st.markdown("[Montgomery County - 911 Calls](https://public.tableau.com/app/profile/umeshjn/viz/911-MontgomeryCounty/911-MontgomeryCounty)")
        st.write("""
        This dashboard gives you a view of 911 Emergency Calls made in Montgomery County, PA.
        """)
        st.image("images/750x.png")


with st.container():
    col1, col2 = st.columns((3,3))
    with col1:
        st.markdown("[Bicycle Sharing in Chicago](https://public.tableau.com/app/profile/umeshjn/viz/ChicagoBicycleSharing/ChicagoBiCycleSharing)")
        st.write("""
        This dashboard gives you a view of bicycle hiring in Chicago from 2014 to 2017.
        """)
        st.image("images/750x.png")

    with col2:
        st.markdown("[Airbnb Listings in NewYork City](https://public.tableau.com/app/profile/umeshjn/viz/AirbnbNewYorkCityListings_16316414938610/NyCityAirbnbLIsting)")
        st.write("""
        Interactive Dashboard to View the Map of the Airbnb listings in NewYork City
        """)
        st.image("images/750x.png")
