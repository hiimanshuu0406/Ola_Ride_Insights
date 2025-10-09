import streamlit as st
import pandas as pd
import os
import base64

# --- Page Config ---
st.set_page_config(page_title="OLA Analytics Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\Lenovo\Desktop\Cleaned_OLA_DataSet.csv")

df = load_data()

# ✅ Sidebar Styling
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #000000;
        }
        .sidebar-logo {
            text-align: center;
            margin-bottom: 20   px;
        }
        .sidebar-header {
            font-size: 18px;
            font-weight: bold;
            color: white;
            padding-left: 10px;
            margin-bottom: 15px;
        }
        .menu-item {
            padding: 10px 15px;
            margin-bottom: 8px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 500;
            color: white;
        }
        .menu-item:hover {
            background-color: #333333;
        }
        .menu-item.selected {
            background-color: #00FF00;
            color: black !important;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Logo Image ---
image_path = r"C:\Users\Lenovo\Desktop"

logo_path = os.path.join(image_path, "ola_logo.png")
with open(logo_path, "rb") as img_file:
    logo_base64 = base64.b64encode(img_file.read()).decode()

st.sidebar.markdown(f"""
    <div class="sidebar-logo">
        <img src="data:image/png;base64,{logo_base64}" width="180">
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-header"></div>', unsafe_allow_html=True)

# --- Sidebar Menu Items (Text Only, No Images) ---
menu_items = ["Overall", "Cancellation", "Rating", "Revenue"]

if "selected_section" not in st.session_state:
    st.session_state.selected_section = "Overall"

for section in menu_items:
    if st.sidebar.button(section, key=section):
        st.session_state.selected_section = section

selected_section = st.session_state.selected_section

# --- Main Title ---
st.title("🚖 OLA Analytics Dashboard")
st.subheader(f"📊 {selected_section} Summary")

# ✅ Vehicle Types 
image_path = r"C:\Users\Lenovo\Desktop"

vehicle_types = [
    ("Prime Sedan", "Prime Sedan.png"),
    ("Prime SUV", "Prime SUV.png"),
    ("Prime Plus", "Prime Plus.png"),
    ("Mini", "Mini.png"),
    ("Auto", "Auto.png"),
    ("Bike", "Bike.png"),
    ("eBike", "eBike.png"),
]

cols = st.columns(4)
cols2 = st.columns(3)

def vehicle_card(col, vehicle, img_file, section):
    with col:
        st.image(os.path.join(image_path, img_file), width=100)
        df_vehicle = df[df["Vehicle_Type"] == vehicle]

        if section == "Revenue":
            total_value = df_vehicle["Booking_Value"].sum()
            avg_distance = df_vehicle["Ride_Distance"].mean()
            st.metric(label=vehicle, value=f"₹{total_value:,.0f}", delta=f"Avg Dist: {avg_distance:.1f} km")

        elif section == "Overall":
            total_rides = df_vehicle.shape[0]
            st.metric(label=vehicle, value=f"{total_rides:,} Trips")

        elif section == "Rating":
            avg_rating = df_vehicle["Customer_Rating"].mean()
            st.metric(label=vehicle, value=f"{avg_rating:.2f} ⭐")

        elif section == "Cancellation":
            cancel_count = df_vehicle[df_vehicle["Booking_Status"].isin(["Canceled by Driver", "Canceled by Customer"])].shape[0]
            st.metric(label=vehicle, value=f"{cancel_count:,}❌")

# --- Render Vehicle Cards ---
vehicle_card(cols[0], "Prime Sedan", "Prime Sedan.png", selected_section)
vehicle_card(cols[1], "Prime SUV", "Prime SUV.png", selected_section)
vehicle_card(cols[2], "Prime Plus", "Prime Plus.png", selected_section)
vehicle_card(cols[3], "Mini", "Mini.png", selected_section)
vehicle_card(cols2[0], "Auto", "Auto.png", selected_section)
vehicle_card(cols2[1], "Bike", "Bike.png", selected_section)
vehicle_card(cols2[2], "eBike", "eBike.png", selected_section)
