import streamlit as st

scan_medicine = st.Page(
    "features/scan_medicine.py", title="Scan Medicine", icon=":material/dashboard:", default=True
)
generate_prescription = st.Page(
    "features/generate_pres.py", title="Generate Prescription", icon=":material/dashboard:"
)
scan_prescription = st.Page("features/scan_pres.py", title="Scan Test Reports", icon=":material/bug_report:")
scan_reports = st.Page(
    "features/scan_reports.py", title="Scan Prescriptions", icon=":material/notification_important:"
)


search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")


pg = st.navigation(
    {
        
        "Features": [scan_medicine, generate_prescription, scan_prescription, scan_reports],
        "Extra": [search, history],
    }
)


pg.run()




