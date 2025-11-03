# app.py
import streamlit as st
import base58
import hashlib

# --- Streamlit setup ---
st.set_page_config(page_title="Hex → WIF Converter", layout="centered")
st.title("🔐 Convert Private Key Hex → WIF")

st.markdown(
    "Enter your **private key in hexadecimal** (with or without `0x`).\n\n"
)

# --- User input ---
hex_input = st.text_input("Private key (hex)", placeholder="e.g. 0x0123... or 0123...")
convert_button = st.button("🔁 Convert to WIF")

# --- Conversion function ---
def hex_to_wif(hex_key: str, compressed: bool = False) -> str:
    """
    Convert a 32-byte hexadecimal private key into WIF (Wallet Import Format).
    If compressed=True, append '01' before computing checksum.
    """
    # Clean and normalize key
    hex_key = hex_key.lower().strip()
    if hex_key.startswith("0x"):
        hex_key = hex_key[2:]
    
    # Add mainnet prefix (0x80)
    extended_hex = "80" + hex_key
    if compressed:
        extended_hex += "01"

    # Double SHA256 checksum
    extended_bytes = bytes.fromhex(extended_hex)
    checksum = hashlib.sha256(hashlib.sha256(extended_bytes).digest()).digest()[:4]

    # Append checksum and encode to Base58
    final_bytes = extended_bytes + checksum
    wif = base58.b58encode(final_bytes).decode("utf-8")
    return wif

# --- Conversion logic ---
if convert_button:
    if not hex_input:
        st.error("❌ Please enter a hexadecimal private key.")
    else:
        hex_clean = hex_input.lower().strip()
        if hex_clean.startswith("0x"):
            hex_clean = hex_clean[2:]

        try:
            key_bytes = bytes.fromhex(hex_clean)
        except ValueError:
            st.error("❌ Invalid hex string. Please make sure it only contains 0–9 and a–f characters.")
        else:
            if len(key_bytes) != 32:
                st.warning(
                    f"⚠️ Your key is {len(key_bytes)} bytes long. A standard private key should be 32 bytes (64 hex chars)."
                )
            try:
                # Generate both WIFs
                wif_uncompressed = hex_to_wif(hex_clean, compressed=False)
                wif_compressed = hex_to_wif(hex_clean, compressed=True)

                st.success("✅ WIF keys generated successfully!")
                st.markdown("### 🔓 Uncompressed WIF")
                st.code(wif_uncompressed, language="")

                st.markdown("### 🔒 Compressed WIF")
                st.code(wif_compressed, language="")

                st.caption("Note: This app does not store or transmit your private key. Always keep it secure.")
            except Exception as e:
                st.error(f"⚠️ Error during conversion: {e}")

