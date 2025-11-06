🔐 Hex to WIF Converter

A simple and secure Streamlit web app to convert a hex private key into WIF.
The app automatically generates both Uncompressed and Compressed WIF versions.

🚀 Features

Converts any valid hex private key (w or w/o 0x)

Displays both WIF formats instantly

Validates input and warns if key length is incorrect

100% local execution – your private key is never stored or sent anywhere

Clean, minimal Streamlit interface

🧩 Requirements

Make sure you have Python 3.9+ installed, then run:

pip install streamlit base58

▶️ Run the app

streamlit run app.py

Then open the local URL shown in your terminal

⚙️ How it works

Prefix 0x80 is added to the private key (Bitcoin mainnet format).

If the compressed option is enabled, 01 is appended.

The checksum is computed using double SHA-256, and the final key is Base58Check-encoded.

🔒 Security note

This app runs entirely on your machine.
Your private key never leaves your browser — it’s processed locally and not transmitted anywhere.
Use test keys when experimenting.

🧠 Author

Developed with ❤️ by dnapog.base.eth



























