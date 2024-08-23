import streamlit as st

ask_medicine = st.Page(
    "features/ask_medicine.py", title="Ask Medicine", icon=":material/dashboard:", default=True
)

scan_reports = st.Page(
    "features/scan_reports.py", title="Scan Test Reports", icon=":material/notification_important:"
)

scan_medicine = st.Page(
    "features/scan_medicines.py", title="Scan Medicines", icon=":material/dashboard:"
)

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/upload_data.py", title="Upload Data")


pg = st.navigation(
    {
        
        "Features": [ask_medicine, scan_reports, scan_medicine],
        "Extra": [search, history],
    }
)


pg.run()




