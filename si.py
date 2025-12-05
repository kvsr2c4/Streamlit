import streamlit as st

# --- Calculation Functions ---

def calculate_simple_interest(P, R, T):
    """Calculates Simple Interest (SI) and Total Amount."""
    # Formula: SI = (P * R * T) / 100
    si = (P * R * T) / 100
    total_amount = P + si
    return si, total_amount

def calculate_compound_interest(P, R, T, n):
    """Calculates Compound Interest (CI) and Total Amount."""
    # Convert annual rate (R%) to decimal (r)
    r = R / 100
    
    # Formula for Total Amount (A): A = P(1 + r/n)^(nt)
    total_amount = P * (1 + r / n)**(n * T)
    
    # Compound Interest (CI): CI = A - P
    ci = total_amount - P
    return ci, total_amount

# --- Streamlit App Layout ---

st.title("💰 Simple and Compound Interest Calculator")

# --- Input Widgets ---

st.header("1. Input Parameters")

# Sidebar for the compounding frequency, which only affects CI
st.sidebar.header("Compound Interest Settings")
compounding_frequency = st.sidebar.selectbox(
    "Compounding Frequency (n)",
    options=[
        ("Annually (n=1)", 1),
        ("Semi-Annually (n=2)", 2),
        ("Quarterly (n=4)", 4),
        ("Monthly (n=12)", 12)
    ],
    format_func=lambda x: x[0],
    help="How often interest is calculated and added to the principal."
)
n = compounding_frequency[1] # Extract the numerical value for 'n'

# Main input fields
col1, col2, col3 = st.columns(3)

with col1:
    principal = st.number_input(
        "Principal Amount (P)",
        min_value=0.0,
        value=10000.0,
        step=100.0,
    )

with col2:
    rate = st.number_input(
        "Annual Interest Rate (R) (%)",
        min_value=0.0,
        value=5.0,
        step=0.1,
    )

with col3:
    time = st.number_input(
        "Time Period (T) in Years",
        min_value=0.0,
        value=5.0,
        step=0.5,
    )

# --- Calculation and Output ---

if principal > 0 and rate >= 0 and time >= 0:
    st.header("2. Calculation Results")
    
    # --- Simple Interest Calculation ---
    si, si_total = calculate_simple_interest(principal, rate, time)
    
    with st.expander("Simple Interest (SI)"):
        st.info("Interest is only calculated on the original Principal amount.")
        st.metric(
            label="Simple Interest Earned (SI)",
            value=f"₹ {si:,.2f}"
        )
        st.metric(
            label="Total Amount (Principal + SI)",
            value=f"₹ {si_total:,.2f}"
        )
        
    # --- Compound Interest Calculation ---
    ci, ci_total = calculate_compound_interest(principal, rate, time, n)
    
    with st.expander("Compound Interest (CI)", expanded=True):
        st.info(f"Interest is calculated on the principal PLUS accumulated interest, compounded {compounding_frequency[0].split()[0].lower()}.")
        st.metric(
            label="Compound Interest Earned (CI)",
            value=f"₹ {ci:,.2f}"
        )
        st.metric(
            label="Total Amount (Principal + CI)",
            value=f"₹ {ci_total:,.2f}"
        )
        
    st.markdown("---")
    st.subheader("Comparison")
    
    # Highlight the better option
    difference = ci - si
    st.success(f"Compound Interest earned ₹ {difference:,.2f} more than Simple Interest.")

else:
    st.warning("Please enter valid, non-negative values for Principal, Rate, and Time.")

# --- End of App ---
