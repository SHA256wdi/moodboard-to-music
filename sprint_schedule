# Project Proposal: Visual Moodboard to Spotify Playlist Generator

**Sprint Duration:** 7 Days  
**Product Manager and Engineer:** Shawdi  
**Product Area:** Creative Tools, Mood Personalization, Cross-Platform Discovery

---

## Sprint Goal

Deliver a functional MVP that allows a user to upload visual assets (inspired by Pinterest boards), automatically extract emotional tags using CLIP, map these to audio characteristics, and generate a curated Spotify playlist reflecting the board’s aesthetic.

---

## Sprint Schedule and Deliverables

### Day 1 – Kickoff and Input Pipeline

**Objective:** Establish the image ingestion flow and frontend interface.

**Tasks:**
- Finalize user journey (Upload → Tag → Playlist → Listen)
- Set up development environment (Python, Streamlit, Spotipy)
- Implement image uploader and board title input
- Preview uploaded images in UI

**Deliverables:**
- Basic Streamlit app with upload capability
- Working input form for board name
- Draft of user interaction flow

---

### Day 2 – Tagging Engine (CLIP Integration)

**Objective:** Integrate CLIP model to extract visual tags from user-uploaded images.

**Tasks:**
- Load and run CLIP model via OpenAI or Hugging Face
- Extract top N semantic tags from each image
- Store and de-duplicate tag set per board
- Output visual tags in frontend

**Deliverables:**
- Operational tagging function
- Sample outputs for 3–5 test images
- Display of tags in user interface

---

### Day 3 – Tag-to-Music Mapping System

**Objective:** Translate visual tags into Spotify-compatible audio features.

**Tasks:**
- Build `tag_to_spotify` dictionary mapping tags to genre, valence, and energy
- Aggregate mood values across all tags for a board
- Generate a normalized audio profile (genre list + mood vector)

**Deliverables:**
- Tag mapping module
- Function to convert tag list to music parameters
- Debugged sample mappings for 20+ tags

---

### Day 4 – Spotify Integration

**Objective:** Authenticate user and generate playlists using Spotify API.

**Tasks:**
- Authenticate with Spotify using Spotipy and OAuth2
- Generate playlist with Spotify Recommendations API
- Name and save playlist to user’s Spotify account
- Display playlist link or embed in UI

**Deliverables:**
- End-to-end playlist creation flow
- Working Spotify playlist URL per test case
- Playlist customization field (optional)

---

### Day 5 – User Experience and Error Handling

**Objective:** Refine the UI and improve resilience of application.

**Tasks:**
- Add mood summary display
- Refactor layout for clarity and visual appeal
- Add loading indicators and exception handling
- Ensure fallback for unmapped tags

**Deliverables:**
- Finalized frontend design
- Error-handling for all major operations
- Responsive UX across test flows

---

### Day 6 – Deployment and QA

**Objective:** Deploy working prototype and conduct testing.

**Tasks:**
- Deploy application to hosting platform (e.g., Streamlit Cloud)
- Conduct QA with multiple image boards and tag varieties
- Validate Spotify playlist performance and response time
- Collect qualitative user feedback (minimum 2 testers)

**Deliverables:**
- Live MVP deployment
- QA checklist completed
- Adjusted configurations for deployment stability

---

### Day 7 – Documentation and Demo Packaging

**Objective:** Finalize project materials for portfolio and case study.

**Tasks:**
- Write technical README for GitHub
- Draft case study overview (problem, solution, result)
- Record 2–3 minute walkthrough demo
- Add to personal website and PM project portfolio

**Deliverables:**
- GitHub repository with documentation
- Loom or screen-recorded demo
- Optional PM case study deck

---

## Success Metrics for MVP

- Deployment and Spotify API integration fully functional
- Playlist generation time under 15 seconds
- Image-to-tag and tag-to-music mapping match user expectation
- At least 2 user testers provide positive qualitative feedback
- Playlist engagement (save or listen rate) ≥ 50% across tests

