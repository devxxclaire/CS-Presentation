import streamlit as st
import plotly.express as px



def get_numeric_value(percentage_str):
    return int(percentage_str.replace('%', ''))

st.title("Advice for School")

st.header("📚 Study Tips")
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1: 
    st.subheader("What Classes Can Do for You")
    st.write(
        """
        1. Be present in class, take notes, and engage with lecturers for better understanding.
        2. :orange-background[Consult! Consult! Consult!] Don't be afraid to ask questions with your lecturers/Tutors/SI's.
        3. Have a comfort module to help you enjoy school.
        """
    )
    if st.button("Click for a HACK!", type="secondary"):
        st.success("Did you know? To graduate in record time in NWU, you need to love your MATH! You can't escape it. 😭 :blue-background[**MATH IS YOUR BREAD & BUTTER!!**]")
        st.image("images/mathisfun.jpg", width = 500)
        



with col2:
    st.subheader("What You Can Do for Yourself")
    st.write(
        """
        1. Master self-studying by setting small, clear goals and knowing how you learn best.      
        2. Practice coding daily to build problem-solving skills and improve logical thinking
        3. :red[**STOP CPF!!**]: you DON'T want to forget! 
        4. Learn beyond the degree knowledege. 
        5. :green-background[Know how your computer works]
        6. :bulb: **TIP**: Use online resources like YouTube, W3Schools, and Udemy to supplement your learning.
        """
    )
st.divider()  # Add a divider line

st.header("📅 Time Management")

st.write(
    """
    ### You have a slider below to select the percentage of time you can spend on different activities.
    #### The total of the three should not exceed 100%.
    """
    )
st.write("\n")

study_num = st.select_slider("Select a percentage of your time spent on **Study**", options=[f"{i}%" for i in range(0, 105, 5)])

st.write("You are spending ", study_num, " of your time on **Study**")
st.write("\n")
st.write("\n")


sleep_num = st.select_slider(
    "Select a percentage of your time spent on **Sleep/Rest**", options=[f"{i}%" for i in range(0, 105, 5)])
st.write("You are spending ", sleep_num, " of your time on **Sleep/Rest**")
st.write("\n")
st.write("\n")

enjoy_num = st.select_slider(
    "Select a percentage of your time spent on **Party**",
    options=[f"{i}%" for i in range(0, 105, 5)])

st.write("You are spending ", enjoy_num, " of your time on **Party**")
st.write("\n")
st.write("\n")



st.markdown("""
            1. Use planners and Pomodoro techniques to manage time effectively.
            2. Priotiize the modules you struggle with the most.
            3. MAKE IT REALISTIC, YOU CAN'T STUDY 100% OF THE TIME.
            """)

