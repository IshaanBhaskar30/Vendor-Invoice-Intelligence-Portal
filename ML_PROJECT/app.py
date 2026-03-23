import streamlit as st
from inference.predict_freight import predict_freight
from inference.predict_invoice_flag import predict_invoice_flag

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="🚚📄",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🚚📄 Vendor Invoice Intelligence Portal")

st.markdown("""
This AI-powered tool helps finance teams:

- 🚚 Predict **Freight Cost**
- 🧾 Detect **Risky Vendor Invoices**
- 📉 Reduce financial leakage
""")

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
option = st.sidebar.radio(
    "Select Module",
    ["Freight Cost Prediction", "Invoice Risk Detection"]
)

# =========================================================
# 🚚 FREIGHT PREDICTION
# =========================================================

if option == "Freight Cost Prediction":

    st.subheader("🚚 Freight Cost Prediction")

    st.markdown("""
    Predict freight cost based on invoice details.
    """)

    with st.form("freight_form"):
        col1, col2 = st.columns(2)

        with col1:
            dollars = st.number_input("Invoice Dollars", min_value=1.0, value=1000.0)

        with col2:
            quantity = st.number_input("Quantity", min_value=1, value=10)

        submit = st.form_submit_button("Predict Freight")

    if submit:
        data = {
            "Dollars": [dollars],
            "Quantity": [quantity]
        }

        result = predict_freight(data)

        predicted_value = result["Predicted_Freight"][0]

        st.success("Prediction Completed")

        st.metric(
            label="Estimated Freight Cost",
            value=f"${predicted_value:,.2f}"
        )

# =========================================================
# 🧾 INVOICE RISK DETECTION
# =========================================================

else:

    st.subheader("🧾 Invoice Risk Detection")

    st.markdown("""
    Detect whether an invoice should be flagged for manual review.
    """)

    with st.form("invoice_form"):

        col1, col2, col3 = st.columns(3)

        with col1:
            quantity = st.number_input("Invoice Quantity", min_value=1, value=50)
            freight = st.number_input("Freight", min_value=0.0, value=100.0)

        with col2:
            dollars = st.number_input("Invoice Dollars", min_value=1.0, value=2000.0)
            total_item_quantity = st.number_input("Total Item Quantity", min_value=1, value=48)

        with col3:
            total_item_dollars = st.number_input("Total Item Dollars", min_value=1.0, value=1980.0)
            avg_receiving_delay = st.number_input("Receiving Delay (days)", min_value=0.0, value=5.0)

        submit_flag = st.form_submit_button("Evaluate Risk")

    if submit_flag:

        data = {
            "Quantity": [quantity],
            "Dollars": [dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars],
            "avg_receiving_delay": [avg_receiving_delay]
        }

        result = predict_invoice_flag(data)

        flag = result["Predicted_Flag"][0]

        st.success("Evaluation Completed")

        if flag == 1:
            st.error("⚠️ High Risk Invoice — Manual Review Required")
        else:
            st.success("✅ Invoice is Safe for Auto Approval")