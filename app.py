import streamlit as st # type: ignore


scan_medicines = st.Page("features/scan_medicine.py", title="Scan Medicines", icon=":material/circle:")
scan_test_reports = st.Page("features/scan_pres.py", title="Scan Prescriptions", icon=":material/add_circle:")
scan_prescriptions = st.Page("features/scan_reports.py", title="Scan test Reports", icon=":material/dashboard:")
generate_prescriptions = st.Page("features/generate_pres.py", title="Generate AI Prescriptions", icon=":material/history:")

pg = st.navigation([scan_medicines, scan_test_reports, scan_prescriptions, generate_prescriptions])


pg.run()

