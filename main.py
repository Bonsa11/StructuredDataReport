import streamlit as st
from ydata_profiling import ProfileReport, report
import pandas as pd
import json
import requests
import os


if __name__ == '__main__':
    with st.sidebar:
        st.image(
            "https://learn.g2.com/hubfs/Imported%20sitepage%20images"
            "/1ZB5giUShe0gw9a6L69qAgsd7wKTQ60ZRoJC5Xq3BIXS517sL6i6mnkAN9khqnaIGzE6FASAusRr7w=w1439-h786.png")

        st.title("INSIGHT Data Report Generator")

        pages = ["Report", "Docs"]
        choice = st.radio("Navigation", pages)

        st.warning("This tool is still in development, contact me @ samuel.bodza2@uhb.nhs.uk for feature requests, "
                   "bugs or issues!")
    df = None
    if choice == 'Docs':
        st.warning("I'll defo do this at some point")
    elif choice == 'Report':
        file = st.file_uploader("Upload your dataset here!")
        if file:
            try:
                df = pd.read_csv(file, index_col=None)
            except Exception as e:
                pass
                try:
                    df = pd.read_csv(file, index_col=None, engine='python', encoding='cp1252')
                except Exception as e:
                    st.warning('not able to open csv')
            st.dataframe(df)
            if st.button('generate report'):
                profile_df = df.profile_report()
                profile_df.to_file("report.html")
                if os.path.exists("report.html"):
                    with open("report.html", 'rb') as f:
                        st.download_button('Download Report', f, file_name="report.html")





