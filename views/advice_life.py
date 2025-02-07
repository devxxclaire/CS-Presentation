import streamlit as st


st.title("Advice for Life 🌟")

st.subheader("1. Make the Best Out of Your 3-Year Degree")
st.write("Get involved in university activities, take on leadership roles, and maximize learning opportunities.")

st.write("\n")
st.subheader("2. Create New Memories")
st.write("University is a once-in-a-lifetime experience. Travel (if you can), make friends (**:blue[YOU LITERALLY ARE UNABLE TO DO THIS DEGREE SOLO]**), and enjoy new experiences.")

st.write("\n")
st.subheader("3. Attend Conferences and Hackathons")
st.image("images/hackathon.jpg", caption="Participate in Hackathons!", width = 500)
st.write("Expand your knowledge and gain exposure by attending tech events, coding camps and hackathons.")

st.write("\n")
st.subheader("4. Increase Your Network")
st.write("Connect with industry professionals, alumni, and peers to build a strong network.")

st.write("\n")
st.subheader("5. Mjolo is a No-Go Zone")
st.image(image="images/mathcry.jpg", width=500)
option = st.selectbox(
    " ### Are you interested in dating or currently dating?",
    ("Yes & I'm happy 💝", "No, but i'll like to 🤔", "NO and I'm not interested ❌"),
    index=None,
    placeholder="Select your thoughts...",
)
if option == "Yes & I'm happy 💝":
    st.subheader("Great! Keep it up!")
elif option == "No, but i'll like to 🤔":
    st.subheader("Find someone who is in CS or at least understands your workload.")
elif option == "NO and I'm not interested ❌":
    st.subheader("Great! Focus on your studies and personal growth.")

st.write("\n")

st.subheader("6. Books come first, but Partying is a close second")
st.write("Never neglect to have some fun and let loose once in a while.")


st.write("\n")
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1: 
    st.image("images/makeitin.jpg", caption="You can do it", use_container_width=330)


with col2:
    st.image("images/graduation.jpg", caption="Graduation Day", use_container_width=330)