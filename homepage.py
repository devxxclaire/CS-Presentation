import streamlit as st



about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="👧🏾",
    default=True,

)

page_1 = st.Page(
    page="views/advice_school.py",
    title="Advice for School",
    icon="📝",
)

page_2 = st.Page(
    page="views/advice_life.py",
    title="Advice for Life",
    icon="👔",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, page_1, page_2])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "INFO": [about_page],
        "ADVICE": [page_1, page_2],
    }
)


# --- SHARED ON ALL PAGES ---
st.sidebar.text("Made with ❤️ by Zoe")
st.logo(
    image="images/coding.jpg", 
    size="large",
    )



# --- RUN NAVIGATION ---
pg.run()