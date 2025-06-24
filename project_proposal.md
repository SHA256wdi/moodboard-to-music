# **Pinterest PM Proposal: Enhancing Pinterest Boards with Spotify Playlists**

**Product Area:** Visual Discovery & Personalization

**Prepared by:** Shawdi

**Date:** June 23 2025

---

### **Problem Statement**

Pinterest boards are emotional, aesthetic-driven collections; Users curate them to represent moods, aspirations, or moments (e.g. *Coastal Summer*, *Dark Academia*, *Dream Apartment*). However, these experiences are purely visual. There’s currently no way for users to extend a board’s emotional tone into other sensory dimensions, like sound. This represents a missed opportunity for deeper immersion and engagement.

---

### **Opportunity**

Pairing mood-based playlists with visual boards creates a multi-sensory experience. This aligns with user behavior and market trends:

* Pinterest has over **518M monthly active users** (Q1 2024).
* Spotify has over **615M active users**, with **239M premium subscribers** (Q1 2024).
* A 2021 Spotify survey found **75% of Gen Z and Millennials** listen to music to improve their mood.
* Nielsen reports that **90% of people say music helps them focus** while working or creating.

---

### **Solution Overview**

Launch an MVP Chrome extension and companion web app that enables users to generate a Spotify playlist based on the vibe of a Pinterest board.

#### Key Steps:

1. User selects one of their public Pinterest boards
2. Images are analyzed using a pre-trained AI model (CLIP)
3. Extracted tags are mapped to Spotify parameters (genre, valence, energy)
4. A Spotify playlist is generated via the Recommendations API
5. Playlist is displayed and optionally embedded or linked within the board

---

### **Target Users & Use Cases**

* **Creators**: Add music to moodboards or content kits
* **Lifestyle planners**: Curate immersive experiences for events, homes, or outfits
* **Pinterest power users**: Extend the board experience with audio personalization

---

### **Implementation Plan**

#### **Tech Stack**

* **Frontend**: React or vanilla JS (for Chrome extension + web interface)
* **Backend**: Python Flask or Node.js
* **Image analysis**: OpenAI CLIP (via API or local model)
* **Music matching**: Hand-mapped or GPT-assisted tag → audio parameter pipeline
* **Playlist generation**: Spotify Web API

#### **Key MVP Components**

* Image uploader or Pinterest board scraper
* CLIP model for tag extraction
* Mapping layer to translate tags → Spotify inputs
* Spotify playlist builder + embed UI

#### **4-Week Build Timeline**

* Week 1: Tag extraction pipeline
* Week 2: MVP frontend + manual board selection
* Week 3: Spotify integration + playlist generation
* Week 4: UI polish, testing, and demo packaging

---

### **Future Opportunities**

* Native Pinterest feature: “Add a Vibe” to boards
* Collaborations with Spotify or licensing of ambient libraries
* AI-powered Image-to-Music Translator
* Personalized replays or daily board radio

---

### **Success Metrics**

* % of users who generate playlists
* Increase in session duration on boards with embedded music
* Playlist click-through and save rates
* Qualitative feedback on immersion and mood accuracy

---

### **Risks & Mitigations**

| Risk                            | Mitigation                                                |
| ------------------------------- | --------------------------------------------------------- |
| Limited Pinterest API access    | Start with user-uploaded images or manual board selection |
| Spotify free tier limitations   | Offer login + surface limitations clearly                 |
| Subjective tag-to-music mapping | A/B test mappings and use GPT where helpful               |

---

### **Conclusion**

This feature bridges visual and auditory storytelling to create a uniquely immersive Pinterest experience. By translating aesthetics into sound, we extend how users feel and connect with their boards. A lightweight MVP allows us to validate demand and guide future native development.

---

### **Sources**
Pinterest Q1 2024 Earnings Report: https://investor.pinterestinc.com

Spotify Q1 2024 Shareholder Letter: https://investors.spotify.com

Spotify Culture Next Global Trends Report 2021: https://ads.spotify.com/en-US/news-and-insights/culture-next-2021/

Nielsen Music 360 Report 2020 (via Billboard): https://www.billboard.com/pro/music-360-report-highlights-2020-nielsen/
