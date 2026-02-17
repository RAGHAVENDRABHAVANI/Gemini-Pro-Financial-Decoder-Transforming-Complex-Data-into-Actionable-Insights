import streamlit as st
import pandas as pd

# App Title
st.title("💰 Financial Decoder (Offline Version)")

st.write("Enter your company financial details below:")

# Inputs
income = st.number_input("Enter Total Income (in Lakhs)", min_value=0.0)
expense = st.number_input("Enter Total Expenses (in Lakhs)", min_value=0.0)
investment = st.number_input("Enter Total Investment (in Lakhs)", min_value=0.0)

# Button
if st.button("Analyze"):

    # Calculate profit
    profit = income - expense

    # Show results
    st.subheader("📊 Financial Analysis")

    st.write(f"✅ Income: {income} Lakhs")
    st.write(f"✅ Expenses: {expense} Lakhs")
    st.write(f"✅ Investment: {investment} Lakhs")
    st.write(f"💰 Profit: {profit} Lakhs")

    # Status
    if profit > 0:
        st.success("Company is in Profit ✅")
    elif profit == 0:
        st.warning("Company is in Break-even ⚠️")
    else:
        st.error("Company is in Loss ❌")

    # Suggestions
    st.subheader("📌 Suggestions")

    if profit > 20:
        st.write("✔️ Excellent performance. Consider expanding business.")
    elif profit > 5:
        st.write("✔️ Good profit. Maintain expense control.")
    elif profit > 0:
        st.write("✔️ Low profit. Reduce unnecessary costs.")
    else:
        st.write("❌ Loss detected. Review expenses and improve revenue.")

    if investment > profit:
        st.info("⚠️ Investment is high compared to profit. Review strategy.")
