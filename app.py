import streamlit as st

st.set_page_config(page_title=“Hindi AI Shorts Generator”, page_icon=“🎬”)

st.title(“🎬 Hindi AI Shorts Generator”)
st.write(“अपनी हिंदी कहानी से YouTube Shorts बनाने की शुरुआत करें।”)

story = st.text_area(“अपनी हिंदी कहानी लिखें:”, height=200)

if st.button(“🎥 वीडियो बनाने की तैयारी करें”):
if story.strip():
st.success(“आपकी कहानी तैयार है!”)
st.write(“आपकी कहानी:”)
st.write(story)
st.info(“अगले चरण में AI आवाज़, सबटाइटल और वीडियो बनाने की सुविधा जोड़ेंगे।”)
else:
st.warning(“पहले अपनी कहानी लिखें।”)
