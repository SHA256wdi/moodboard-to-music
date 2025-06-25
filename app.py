import streamlit as st
from clip_tagger import get_clip_tags

st.title("Moodboard → Music")
st.write("Upload an image and we’ll tell you the vibe.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    st.image("temp.jpg", caption="Uploaded Image", use_container_width=True)

    candidate_tags = [
        "sunset", "vintage", "moody", "bright", "cozy", "grunge",
        "romantic", "dark", "dreamy", "aesthetic", "quiet", "gloomy"
    ]

    tag_scores = get_clip_tags("temp.jpg", candidate_tags)

    st.subheader("Top Tags:")
    for tag, score in tag_scores[:5]:
        st.write(f"{tag} — {round(score, 3)}")

