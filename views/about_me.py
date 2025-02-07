
import streamlit as st


st.title(" 🎊 🎊 🎊 Welcome to Computer Science in NWU Mahikeng Campus, First Years 🎊 🎊 🎊")
st.divider()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("images/profilePic.jpeg", caption="Me at Paris", width=330)

with col2:
    st.title("_Zoe Idemudia_", anchor=False)
    st.subheader("_Quick Facts About Me_")
    st.markdown(
        """
        - I'm a Bsc Honour student in Comp Sci. 
        - I'm passionate about technology and innovation. I like to keep up with the latest trends in tech.
        - I am a huge fan of reading books from novels to manga. 
        - I **love** to travel! I've been to 10 countries so far.
        I had :blue-background[ZERO KNOWLEDGE] about coding before I started my computer science & math undergraduate degree.
        """
        )
    
st.write("\n")


st.balloons()