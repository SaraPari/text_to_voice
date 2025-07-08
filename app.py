import streamlit as st
import asyncio
import edge_tts
import tempfile
import os
import qrcode
from io import BytesIO

# --------------------
# CONFIGURATION
# --------------------
buy_me_a_coffee_link = "https://www.buymeacoffee.com/YOUR_USERNAME"  # ← CHANGE THIS
usdt_address = "0x58025464862fbc23a0c759f0565e10641618cb42"  # ← CHANGE THIS

# --------------------
# TEXT-TO-SPEECH
# --------------------
def generate_speech(text: str, voice: str = "en-US-JennyNeural"):
    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    output_path = output_file.name
    output_file.close()

    async def synthesize():
        communicate = edge_tts.Communicate(text=text, voice=voice)
        await communicate.save(output_path)

    asyncio.run(synthesize())
    return output_path

# --------------------
# STREAMLIT APP UI
# --------------------
st.set_page_config(page_title="🗣️ AI Text Reader with Support", layout="centered")
st.title("🗣️ AI Text Reader")
st.markdown("Paste text, click play, and listen with natural AI voices. Built with 💙 using free tools.")

# TEXT INPUT
text = st.text_area("✏️ Enter your text here:", height=300)

# VOICE CHOICE
voice = st.selectbox("🎤 Choose a voice:", [
    "en-US-JennyNeural",
    "en-US-GuyNeural",
    "en-GB-LibbyNeural",
    "en-GB-RyanNeural",
    "en-AU-NatashaNeural",
    "en-AU-WilliamNeural"
])

if st.button("🔊 Read Aloud"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("⏳ Generating audio..."):
            audio_path = generate_speech(text, voice)
        st.audio(audio_path, format="audio/mp3")
        st.success("✅ Done! Enjoy your audio.")

# --------------------
# SUPPORT SECTION
# --------------------
st.markdown("---")
st.header("💸 Support For Unlimited Use")

st.markdown("If you like this tool and want unlimited use, you can support me 👇")

col1, col2 = st.columns(2)

# Buy Me a Coffee
with col1:
    st.subheader("☕ If You'd Like You Can Buy Me a Coffee With USDT")
    st.write("Send USDT to this address (BEP20):")
    st.code(usdt_address, language="text")
    st.image("usdt_qr.png", caption="Scan to pay with USDT", width=180)


# Footer
st.markdown("---")
st.caption("Built with Streamlit + Edge-TTS | Free forever 🩵 | By Sara ✨")
