import streamlit as st
import pandas as pd
import math
from pathlib import Path
import streamlit.components.v1 as components

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='End Times Timeline',
    page_icon=':earth_americas:',
    layout='wide' # This is an emoji shortcode. Could be a URL too.
)



# Header
st.header('End Times Timeline - This is a prototype under development', divider='gray')
st.text("Use the buttons at the lower left of the timeline or click and drag to navigate to specific events. Use the navigation buttons overlayed to view events in chronological order.")
st.text("This should be viewed from a desktop or tablet screen.")
''

''
''
# Using cdn to pull timeline - may migrate to more customizable version later
components.iframe(src="https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=v2%3A2PACX-1vRd2YZLsZ0HODKikNXVtQjvGtq7DNcFY4vkRKOm_f2tMKRIx5hm49gdxD_NeyYPq_xJVW0zTieKqaaB&font=Default&lang=en&initial_zoom=2&scale_factor=2&width=100%25&height=900",
                  height=1200)

