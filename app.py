import streamlit as st
import os
from extractor import read_image, read_pdf, extract_data
from excel_writer import fill_excel

st.set_page_config(page_title="⚡ Solar Load Calculator", layout="wide")
st.title("⚡ Solar Load Calculator")
st.caption("Automate electricity bill analysis → Generate solar recommendations")

os.makedirs("uploads", exist_ok=True)

uploaded_file = st.file_uploader(
    "📄 Upload Electricity Bill (PDF or Image)",
    type=["png", "jpg", "jpeg", "pdf"]
)

if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.success("✅ File uploaded successfully!")
    
    # OCR
    with st.spinner("🔍 Reading bill..."):
        if uploaded_file.name.lower().endswith(".pdf"):
            text = read_pdf(file_path)
        else:
            text = read_image(file_path)
    
    # Extract data
    with st.spinner("🤖 Extracting data..."):
        data = extract_data(text)
    
    # Show extracted data
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Extracted Information")
        st.write(f"**Consumer Name:** {data.get('consumer_name', 'Not found')}")
        st.write(f"**Consumer No:** {data.get('consumer_no', 'Not found')}")
        st.write(f"**Sanctioned Load:** {data.get('load', 'Not found')} kW")
        st.write(f"**Fixed Charges:** Rs. {data.get('fixed_charges', 'Not found')}")
        st.write(f"**Connection Type:** {data.get('connection_type', 'Not found')}")
    
    with col2:
        st.subheader("📈 Monthly Consumption Data")
        if data.get("monthly_data"):
            st.write(f"**Months Found:** {len(data['monthly_data'])}")
            st.write(f"**Units:** {', '.join(map(str, data['monthly_data']))}")
        st.write(f"**Current Bill Amount:** Rs. {data.get('current_amount', 'Not found')}")
    
    # Generate Excel
    template_path = "template.xlsx"
    
    if not os.path.exists(template_path):
        st.error("❌ template.xlsx missing!")
        st.stop()
    
    excel_file = "output.xlsx"
    fill_excel(data, template_path, excel_file)
    
    st.success("✅ Excel file generated!")
    
    # Download button
    with open(excel_file, "rb") as f:
        st.download_button(
            label="📥 Download Solar Recommendation Excel",
            data=f.read(),
            file_name="Solar_Load_Calculation.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    # Show debug OCR text if needed
    with st.expander("🔧 Debug: OCR Text"):
        st.text(text[:2000])