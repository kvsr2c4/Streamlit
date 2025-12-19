import streamlit as st
import pywhatkit
import time
import pyautogui
from datetime import datetime

#Follow me on  Linkdin :https://www.linkedin.com/in/venkata-suchendra-reddy-k-bba190162
# this Program can help to send msg through what up automatically no need human intervention
# Page Configuration
st.set_page_config(page_title="WhatsApp Love Spreader", page_icon="😍")

st.title(" WhatsApp Message Automator")
st.markdown("Spread some love by sending multiple automated messages!")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Settings")
    phone_no = st.text_input("Recipient Phone Number", value="+911234567890", help="Include country code (e.g., +91)")
    msg = st.text_area("Your Message", value='HI! ❤️')
    
    st.divider()
    
    count = st.number_input("How many times?", min_value=1, max_value=50, value=5)
    initial_wait = st.slider("Initial Browser Load Time (sec)", 10, 30, 15)
    wait_sec = st.slider("Delay between messages (sec)", 1, 10, 2)

# Main UI Area
col1, col2 = st.columns(2)
with col1:
    st.info(f"**Target:** {phone_no}")
with col2:

    st.info(f"**Total Messages:** {count}")

st.warning("⚠️ **Note by Suchi :** Dont touch anything Everything automatically taken care based on your input. Ensure you are logged into WhatsApp Web in your default browser.")

if st.button("🚀 Start Sending Messages", use_container_width=True):
    try:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Step 1: Open Browser and send first message
        status_text.text("🔗 Opening WhatsApp Web and sending the first message...")
        pywhatkit.sendwhatmsg_instantly(phone_no, msg, wait_time=initial_wait, tab_close=False)
        progress_bar.progress(1 / count)
        
        # Step 2: Loop for remaining messages
        for i in range(count - 1):
            time.sleep(wait_sec)
            pyautogui.typewrite(msg)
            pyautogui.press('enter')
            
            # Update UI
            current_idx = i + 2
            percent = current_idx / count
            progress_bar.progress(percent)
            status_text.text(f"✅ Sent {current_idx} of {count} messages...")

        st.success(f" Succes sent {count} messages to {phone_no}!")
        st.balloons()

    except Exception as e:
        st.error(f"An error occurred: {e}")
