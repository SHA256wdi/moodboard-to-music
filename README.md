# moodboard-to-music 🎵

This is a personal project that generates a Spotify playlist based on the aesthetic or "vibe" of a Pinterest board. It analyzes images from a Pinterest board using computer vision models and maps the results to mood-based audio features or genres on Spotify.

## Goal

To explore how moodboards—especially those curated on Pinterest—can translate into sound. This is part of an ongoing interest in creativity, discovery, and building bridges between platforms that evoke emotion in different media (visual vs. auditory).

## Features

- Pulls Pinterest board content (image URLs, titles, etc.)
- Uses image analysis (via CLIP or Google Vision) to identify mood tags
- Maps tags to Spotify genres and audio features
- Generates a mood-matching Spotify playlist

## Stack

- Pinterest API (for board and pin data)
- Spotify API (for playlist creation and track recommendations)
- Python (Flask or Streamlit for basic interface)
- OpenAI CLIP / Google Vision API (for tag extraction from images)

## Status

In development — currently building out the MVP and experimenting with tag-to-music mappings.

## About Me

Hi, I'm Shawdi — a creative technologist with a background in software engineering, digital media, community organizing, and a love for using and building products. This project is part of a personal exploration into product management and cross-platform creativity.

## 🔒 Privacy Policy

See [privacy.md](./privacy.md) for details.
