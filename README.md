# ⚡ Solar Load Calculator - Energybae

Automate electricity bill analysis and generate solar system recommendations instantly.

## What It Does

1. **Upload** an electricity bill (PDF or image)
2. **AI reads** and extracts key data automatically (consumer details, monthly consumption, load, etc.)
3. **Excel filled** with all extracted data - calculations auto-generate solar system size
4. **Download** the filled Excel template ready for client use

## Features

- ✅ Supports PDF and image uploads (PNG, JPG, JPEG)
- ✅ AI-powered OCR to read electricity bills
- ✅ Automatic data extraction (consumer name, load, monthly units, bill amounts)
- ✅ Excel template auto-filled with calculations intact
- ✅ Web interface for easy use
- ✅ No manual data entry needed

## Installation

```bash
pip install -r requirements.txt
```

**System Requirements:**
- Tesseract OCR: [Download here](https://github.com/UB-Mannheim/tesseract/wiki)
- Python 3.8+

## Running the App

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## How It Works

1. User uploads electricity bill
2. **extractor.py** → Reads bill with OCR, extracts data using regex patterns
3. **excel_writer.py** → Fills template with extracted data
4. User downloads filled Excel file

## Extracted Fields

- Consumer Name & Number
- Sanctioned Load (kW)
- Fixed Charges
- Connection Type
- Monthly consumption data (units & amounts)

## Excel Template

The template includes:
- Input fields for customer details
- Monthly consumption tracking
- Automatic formulas for:
  - Average consumption calculation
  - Recommended solar capacity
  - Number of solar panels needed
  - ROI calculations

**Important:** Only fills input cells, preserves all formulas.

## File Structure

```
EnergyBae/
├── app.py               # Streamlit web interface
├── extractor.py        # OCR + data extraction logic
├── excel_writer.py     # Excel template filling
├── template.xlsx       # Solar calculation template
├── requirements.txt    # Python dependencies
└── uploads/            # Temporary bill storage
```

## Notes

- OCR accuracy depends on bill quality
- Supports MSEDCL bills (Maharashtra electricity board)
- Easily extensible for other bill formats
- All customer data is processed locally (no cloud upload)

---

**Built for Energybae** | Renewable Energy Solutions
