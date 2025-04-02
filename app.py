import streamlit as st

# Page Title
st.set_page_config(page_title="My Streamlit Website", page_icon="🌐")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio Website! 🌍")
    st.write("Hello! I'm **Hiba**, a passionate **Full-Stack Web Developer** skilled in **Next.js, TypeScript, Python, and UI/UX Design**. "
        "I love creating innovative web applications that solve real-world problems. 🚀\n\n"
        "Currently, I am studying at **Agentic AI**, continuously learning and improving my skills. "
        "This website showcases my projects, skills, and journey in the world of web development. "
        "Feel free to explore and connect with me!.")

# About Page
elif page == "About":
    st.title("About Me")
    st.write ("Hi, I'm Hiba! 👋 A passionate **Full-Stack Web Developer** with expertise in **Next.js, TypeScript, Python, and UI/UX**. "
        "I love solving problems and building creative web applications. Currently, I am studying at **Agentic AI**, "
        "where I am enhancing my development skills. I also have **2 years of teaching experience**. "
        "Apart from coding, I enjoy reading novels and exploring new technologies. 🚀"
    )

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("📧 Email: hibameo55@gmail.com")
    st.write("contact: +92 319 2967703")
