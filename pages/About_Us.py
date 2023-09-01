import streamlit as st
import streamlit.components.v1 as components


# Set page title
st.set_page_config(
    page_title="Dementia AI | About Us",
    page_icon=":brain:",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
img{border-radius: 10px;}
</style> """, unsafe_allow_html=True)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)



# Define page layout
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            left: 0px;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#20D2FE, #5292FE);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">About Us</p>
    """,
    height=69,
)
st.image("https://pphr.princeton.edu/wp-content/uploads/sites/61/2019/12/demencia-1024x683.jpg")


# Add Dementia description
st.markdown("## Dementia")
st.write("Dementia AI is an app that uses AI and machine learning to detect diseases from images uploaded by users. Our goal is to make healthcare more accessible and affordable by providing a fast, accurate, and reliable diagnosis tool. We believe that technology can revolutionize the way we approach healthcare, and we're excited to be at the forefront of this innovation.")


