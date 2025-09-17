import streamlit as st
import pandas as pd
import math
from pathlib import Path
import streamlit.components.v1 as components

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:',
    layout='wide' # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.


# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.


# Add some spacing



st.header('End Times Timeline', divider='gray')

''

''
''

components.iframe(src="https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=v2%3A2PACX-1vRd2YZLsZ0HODKikNXVtQjvGtq7DNcFY4vkRKOm_f2tMKRIx5hm49gdxD_NeyYPq_xJVW0zTieKqaaB&font=Default&lang=en&initial_zoom=1&scale_factor=1&width=100%25&height=900",
                  height=1200)
