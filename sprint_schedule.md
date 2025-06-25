# Moodboard Playlist MVP – Detailed 1-Week Development Schedule

This sprint plan outlines each day’s technical and product milestones to deliver a functional prototype that transforms Pinterest board aesthetics into Spotify playlists via CLIP, GPT, Last.fm, and Spotify APIs.

---

## Day 1 – Image Input & Tag Extraction

- Set up project repo and virtual environment (e.g. with Poetry or pipenv)
- Implement local image upload functionality via Streamlit
- Load and test OpenAI’s CLIP model on sample images
- Output top tags for each image with associated cosine similarity scores
- Save and display CLIP tags in UI for debugging
- Research CLIP vs. Google Vision output comparison for fallback strategies

Deliverables:
- Working tag extractor from uploaded images
- Basic Streamlit UI with file input and tag display

---

## Day 2 – Tag Normalization & Semantic Mapping (GPT)

- Create dataset of CLIP tags + aesthetic descriptors
- Prompt GPT-4 to translate tags into musical moods, genres, and energy/valence scores
- Test different prompt templates: single tag, multiple tags, weighted tags
- Save mappings to local dictionary or .json for faster reuse
- Implement GPT fallback: if tag not in static map, call GPT live

Deliverables:
- Working tag-to-genre GPT mapping layer
- Static fallback dictionary of 30–50 common tag mappings

---

## Day 3 – Music Discovery Layer (Last.fm + Spotify)

- Use GPT/CLIP output genre tags to query `tag.getTopTracks` from Last.fm
- Collect track metadata: title, artist, tags, popularity
- Filter Last.fm results for top 5–10 tracks per tag
- Use Spotify API to cross-reference and validate track availability
- Create function to compile final Spotify tracklist from cleaned results

Deliverables:
- Pipeline from aesthetic tags → validated Spotify track URIs

---

## Day 4 – Playlist Generation & Authentication

- Set up Spotify developer app and get OAuth working for playlist creation
- Build backend route to create and populate Spotify playlists
- Add option for user to name their playlist and make it public/private
- Add error handling for duplicates, auth errors, and bad tracks
- Log and store playlist links with original board or tag data

Deliverables:
- End-to-end playlist creation based on image upload
- Playlist link and preview embedded in frontend

---

## Day 5 – UI & Usability Polish

- Add loading states, error messages, and UI feedback to Streamlit app
- Display extracted tags, selected genres, and final playlist in clean format
- Add simple customization: remove/edit tags before playlist is built
- Include toggle to use static tag map vs. GPT output
- Conduct quick user test and log feedback

Deliverables:
- Fully functional UI with smooth upload → playlist generation flow

---

## Day 6 – Final QA, Documentation, and Demo

- Write a clean README with setup instructions, dependencies, and demo flow
- Record a 1–2 min demo video (screen share) showing user journey
- Push project to GitHub with clear structure: `/app`, `/data`, `/scripts`, `/assets`
- Add sample board images + expected outputs to repo for reproducibility
- Log known issues and potential improvements

Deliverables:
- Public GitHub repo with all code, documentation, and test assets

---

## Day 7 – Marketing & PM Materials

- Refactor proposal.md and sprint_schedule.md with final architecture and learnings
- Write short case-study style writeup of build process and decisions
- Optionally: design landing page or publish to Streamlit Cloud for sharing
- Reach out to Pinterest contact or mentors with personalized project summary
- Add project to portfolio website with screenshots, demo, and short summary

Deliverables:
- Portfolio-ready assets and documentation
- Outreach material for PM case or job apps

