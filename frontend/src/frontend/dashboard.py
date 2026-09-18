import streamlit as st
import httpx
import os 

BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
# https://docs.streamlit.io/develop/concepts/connections/connecting-to-data

def main():
    st.markdown("# Crops Data")

    st.write(BASE_URL)

    stats = httpx.get(f"{BASE_URL}/crops").json()

    st.dataframe(stats)

if __name__ == "__main__":
    main()