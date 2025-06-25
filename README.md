# Moodboard-to-Music 

This is a personal project that generates a Spotify playlist based on the aesthetic or "vibe" of a Pinterest board or image collection. It analyzes images using computer vision and language models, translates visual mood into music genres, and builds a matching playlist.

## Goal

To explore how moodboards—especially those curated on Pinterest—can translate into sound. This project bridges platforms that evoke emotion in different media (visual vs. auditory), and is part of my broader interest in creativity, AI, and cross-sensory product design.

## Features

- Accepts image uploads from Pinterest boards or local files  
- Uses CLIP (or Google Vision) to extract aesthetic tags from visuals  
- Maps tags to genres and moods using GPT-4 + Last.fm’s genre taxonomy  
- Queries Spotify to generate and preview a matching playlist  

## Stack

- CLIP (OpenAI) or Google Vision — image-to-tag extraction  
- GPT-4 / Claude — tag-to-genre translation  
- Last.fm API — genre-based music lookup  
- Spotify API — playlist creation and playback  
- Streamlit — lightweight interactive UI  
- Python — end-to-end logic and API orchestration  

## Status

Currently in development. The MVP accepts image uploads, extracts aesthetic tags, and generates Spotify playlists based on emotional tone. Refining tag mappings, playlist quality, and UI polish.

## About Me

Hi, I'm Shawdi — a creative technologist with a background in software engineering, digital media, and community organizing. I enjoy building emotionally resonant tools and products that live between media, accessibility, and technology. This project is part of my exploration into product management and cross-platform creativity.

## Privacy Policy

This app does not store or share any uploaded images, Spotify account data, or personal information. All processing is local or API-based, and user data is discarded after session use.

If the app is deployed publicly, OAuth tokens are used only to authorize playlist creation via Spotify and are not logged or stored.

For questions, feel free to reach out.
