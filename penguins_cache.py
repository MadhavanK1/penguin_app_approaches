# Caching in Streamlit

# Import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Main title of the app
st.title("Palmer's Penguins")

# Our subtitle
st.subheader("Use this Streamlit app to make your own scatterplot about penguins!")

# Import CSV file provided by user (if not, use default)
penguin_file = st.file_uploader("Select Your Local Penguins CSV (default provided)")

# We create a function called load_file()
# It waits 3 seconds and then loads the file that we need
@st.cache_data # 👈 Add the caching decorator
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('penguins.csv')
    return(df)
    
penguins_df = load_file(penguin_file)

# Select box for x_var
selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)

# Select box for y_var
selected_y_var = st.selectbox(
    "What about the y?",
    ["bill_depth_mm", "bill_length_mm", "flipper_length_mm", "body_mass_g"],
)

# Filter to select gender
selected_gender = st.selectbox(
    "What geneder do you want to filter for?",
    ["all penguins", "male penguins", "female penguins"],
)

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass


# Create scatterplot
fig, ax = plt.subplots()
ax = sns.scatterplot(data = penguins_df, x = selected_x_var, y = selected_y_var,
                     hue = 'species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins: " + selected_gender)
st.pyplot(fig)