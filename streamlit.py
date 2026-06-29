# !python -m streamlit run file.py
import streamlit as st

# Sidebar
st.sidebar.title("Sidebar title")
choice = st.sidebar.radio("Select a view:", ["Home", "About", "Contact"])

# Headings
st.title("Page")      # main title
st.header("This is a Header")   # section header
st.write("---")

# Body Texts
st.text("- **Some text**")     # to display plain text
st.write("- **Some text**")    # more versatile than text, can handle (dataframes, markdowns, etc.)
st.write("---")

# Special Messages, Colorful texts
st.header("Colored messages")
st.success("Success msgs are in Green")
st.error("Error msgs are in Red")
st.warning("Warning msgs are in Yellow")
st.info("Info msgs are in Blue")
st.write("---")

# Text input
st.header("Text input")
name = st.text_input("Enter your name", key="name_top")

# Number input
st.header("Number input")
age = st.number_input("Enter your age", min_value=0, max_value=100, value=50, key="age_top")

# Button, on click events
st.header("Button")
if st.button("Show Details"):
    st.write(f"Your name is {name} and your age is {age}")
st.write("---")

# Slider
st.header("Slider")
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write(f"Slider value: {value}")
st.write("---")

# Checkbox
st.header("Checkbox")
value = st.checkbox("Show Text")
st.write(f"Checkbox value: {value}")
st.write("---")

# Radio
st.header("Radio")
value = st.radio("Pick one:", ["A", "B", "C"])
st.write(f"Radio value: {value}")
st.write("---")

# Selectbox
st.header("Selectbox")
value = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selectbox value: {value}")
st.write("---")

# Multiselect
st.header("Multiselect")
value = st.multiselect("Choose multiple options", ["Option 1", "Option 2", "Option 3"])
st.write(f"Multiselect value: {value}")
st.write("---")

# Table
import pandas as pd
st.header("Dataframe Tables")
df = pd.DataFrame({"A": [1, 2, 3], "B": [5, 6, 4], "C": [9, 7, 8]})
st.write(df)
st.write("---")


# Load images from URL
st.header("Image from URL")
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/250px-Python-logo-notext.svg.png"
st.image(img_url, caption="Image from URL")
st.write("---")

# Load audio from URL
st.header("Audio from URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)
st.write("---")

# Load video from URL
st.header("Video from URL")
video_url = "https://youtu.be/dQw4w9WgXcQ?si=twGniNRaP866vwoA"
st.video(video_url)
st.write("---")




# In Streamlit, every time the user interacts with a widget (button, slider, text input, etc.),
# the entire script reruns from top to bottom. Because of this behavior,
# normal Python variables do not remember their values between interactions.

# st.session_state is a special dictionary-like object in Streamlit
# that stores data for a particular user session.

# It helps your app:
# - Remember values
# - Maintain app state
# - Store user progress
# - Preserve variables between reruns
# - Without session state, variables reset after every interaction.

def incr():
    global temp_counter
    temp_counter += 1
    st.session_state.perm_counter += 1

st.button("Increment", on_click=incr)

temp_counter = 0
st.write(f"TEMP = {temp_counter}")

if "perm_counter" not in st.session_state:
    st.session_state.perm_counter = 0
st.write(f"PERM = {st.session_state.perm_counter}")


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

web_url = "https://pokemondb.net/pokedex/all"
raw_content = requests.get(web_url)

parsed_content = bs(raw_content.text, "html.parser")

table = parsed_content.find("table", id="pokedex")

table_body = table.tbody

list_of_rows = table_body.find_all("tr")

pokedex = list()
for row in list_of_rows:
    stats = dict()
    name_row = row.find("td", class_="cell-name")
    stats['name'] = name_row.a.text
    num_rows = row.find_all("td", class_="cell-num")
    stats['total'] = num_rows[1].text
    stats['HP'] = num_rows[2].text
    stats['phAtk'] = num_rows[3].text
    stats['phDef'] = num_rows[4].text
    stats['spAtk'] = num_rows[5].text
    stats['spDef'] = num_rows[6].text
    stats['speed'] = num_rows[7].text
    pokedex.append(stats)
pokedex_df = pd.DataFrame(pokedex)

st.sidebar.title("Search for a pokemon")
filter = st.sidebar.selectbox("Pokemon", ["All"] + list(pokedex_df["name"].unique()) )

st.title("PokedexApp")
if(filter == "All"):
    filtered_df = pokedex_df
else:
    filtered_df = pokedex_df[pokedex_df["name"] == filter]
st.write(filtered_df)

st.write("button with snow, baloon, and spinner")

#Text input
st.header("Text input")
name = st.text_input("Enter your name", key="name_bottom")
st.write(name)
#Number input
st.header("Number input")
age = st.number_input("Enter your age", min_value=0, max_value=100, value=50, key="age_bottom")
st.write(age)
if st.button('press me'):
    st.balloons()