import streamlit as st
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Diyun Lu's Portfolio",
    page_icon="🌺",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .profile-img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
    }
    .tight-line-height {
        line-height: 0.8;
        margin-bottom: 0px;
    }
    .tight-line-height li {
        margin-bottom: 0px;
    }
    .circular-image {
        width: 100%;
        border-radius: 5%;
        object-fit: cover;
    }
    </style>
    """, unsafe_allow_html=True)

# Header section


# Personal information section
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown(
        """
        <div style="display: flex; align-items: flex-end; height: 150px;">
            <h1 style="margi-left: 0px;">Welcome to Diyun Lu's Portfolio</h1>
        </div>
        <hr>
        """,
        unsafe_allow_html=True
    )

with col1:
    st.markdown(
        """
        <div style="display: flex; align-items: flex-end; height: 180px;">
            <img src="https://knovvx.github.io/ludiyun/assets/me-996b5999.jpg"
                 alt="Profile Photo"
                 style="border-radius: 30%; width: 100%; max-width: 150px; object-fit: cover;">
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("### 🍀About Me")
st.write("""
Hi! I'm Diyun Lu, a Master's student of UW. I am passionate about creating meaningful tech experiences.
With a background in computer science, I love building innovative solutions that connect people, hardware, and intelligent systems.
""")

# Skills section
st.markdown("<h3 style='margin-bottom: 0.3rem;'>💻Skills</h3>", unsafe_allow_html=True)
col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("#### Programming Languages")
    st.markdown(
        """
        <ul style='line-height:1.1; margin-bottom:0;'>
            <li>Python</li>
            <li>C/C++</li>
            <li>Java</li>
            <li>JavaScript</li>
            <li>HTML/CSS</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown("#### Frameworks & Tools")
    st.markdown(
        """
        <ul style='line-height:1.1; margin-bottom:0;'>
            <li>Pytorch</li>
            <li>React</li>
            <li>Vue.js</li>
            <li>Django</li>
            <li>Flutter</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

with col5:
    st.markdown("#### Other Skills")
    st.markdown(
        """
        <ul style='line-height:1.1; margin-bottom:0;'>
            <li>Data Analysis</li>
            <li>Circuit and PCB Design</li>
            <li>User Experience Design</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

# Projects section
st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)
st.markdown("### 📚Projects")

st.markdown("#### 1. Taxi Data Visualization and Mining Popular Areas ")
st.markdown(
    """
    <div style="display: flex; justify-content: center; gap: 36px;">
        <img src="https://knovvx.github.io/ludiyun/assets/taxi_main-1b408609.png"
             alt="Project Screenshot 1"
             style="max-width: 240px; border-radius: 10px;">
        <img src="https://knovvx.github.io/ludiyun/assets/all_traj-1ca3e0e9.png"
             alt="Project Screenshot 2"
             style="max-width: 240px; border-radius: 10px;">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
st.write("**Project Description:** Given the dataset of taxi trajectories in Shenzhen on a specific day, our goal is to design a visualization system to help the analysts to understand the taxis' behaviors and to discover the popular areas in Shenzhen or other interesting information behind the data.")
st.markdown(
        """
        <ul style='line-height:1.4; margin-bottom:0;'>
            <li>Developed a webpage to visualize taxis' routes on a map</li>
            <li>Clustered and predicted taxi behaviors to understand the patterns behind.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )
# st.markdown("[View Project](https://github.com)")



st.markdown("#### 2. Visual Analytic System for Knowledgegraphs ")
# 
st.markdown(
    """
    <div style="display: flex; justify-content: center; gap: 36px;">
        <img src="https://knovvx.github.io/ludiyun/assets/vast_main-d2f25c24.png"
             alt="Project Screenshot 1"
             style="max-width: 240px; border-radius: 10px;">
        <img src="https://knovvx.github.io/ludiyun/assets/vast_overview-42403210.png"
             alt="Project Screenshot 2"
             style="max-width: 240px; border-radius: 10px;">
    </div>
    """,
    unsafe_allow_html=True
)
st.write("**Project Description:** Vast Challenge 2023 is based on the real life scene of the IUU (Illegal, Unreported and Unregulated) fishing phenomenon in the world. Given an extracted knowledgegraph, the challenge is to design a visualization system to help the analysts to understand the entities' behaviors and to discover the potential IUU behaviours.")
# st.markdown("[View Project](https://github.com)")
st.markdown(
        """
        <ul style='line-height:1.4; margin-bottom:0;'>
            <li>Visualized statistical data for better anomaly detection.</li>
            <li>Implemented various clustering and machine learning methods to detect and observe graph structure</li>
            <li>Designed and completed part of the poster</li>
        </ul>
        """,
        unsafe_allow_html=True
    )


st.markdown("#### 3. Black Mirror: Sci-fi Theme Interactive Webpage ")
# 
st.markdown(
    '''
    <div style="display: flex; justify-content: center; gap: 36px;">
        <img src="https://knovvx.github.io/ludiyun/assets/bm_main-8981bfa2.png"
             alt="Project Screenshot 1"
             style="max-width: 260px; border-radius: 10px;">
        <iframe width="320" height="180" src="https://www.youtube.com/embed/JZXAAm4lYSs" frameborder="0" allowfullscreen></iframe>
    </div>
    ''',
    unsafe_allow_html=True
)
st.write("**Project Description:** lack Mirror is an interactive webpage revolves around an embedded story line. The story line develops around specific humanistic aspects inspired and based on the Black Mirror TV series. Players make binary choices and fall into different developments which result in different endings. Data visualization under the theme using real-life data is also embedded in the storyline for a thought-provoking purpose.")
st.markdown(
        """
        <ul style='line-height:1.4; margin-bottom:0;'>
            <li>Extract topics and design the storyline including the theoretical layout of the web</li>
            <li>Crawl data from weibo and public news websites. Analyze data and generate proper data visualization in different forms including normal charts, word cloud, danmaku and gallery.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )



# Contact information
st.markdown("### 📧Contact")
st.markdown(
    "📧 Email: ludiyun@uw.edu &nbsp;&nbsp; | &nbsp;&nbsp; "
    "🔗 LinkedIn: [Diyun Lu](https://www.linkedin.com/in/diyun-lu-7760902a1/) &nbsp;&nbsp; | &nbsp;&nbsp; "
    "🐱 Github: [knovvX](https://github.com/knovvx)",
    unsafe_allow_html=True
) 