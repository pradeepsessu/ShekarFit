ShekarFit — 90-Day Aesthetic Transformation (Landing Page)

A fast, single-page marketing site for ShekarFit coaching. It showcases real transformations, pricing plans, coach story, FAQs, and drives users to a 60-second Typeform quiz and WhatsApp chat. The page is designed to be lightweight, mobile-first, and conversion-oriented.

✨ Features

Hero video with controls, safe mobile autoplay, and auto-pause on scroll

Typeform CTA wired to all “Start 60-sec Fit Quiz” buttons

WhatsApp deep links with prefilled message

Proof carousel (before/after pairs) with snap scrolling & nav buttons

Results gallery with a built-in lightbox viewer

Pricing section (3/6/12 months) ready to hook into a payment flow

FAQ accordion using <details>

Sticky bottom bar with persistent CTAs

Simple i18n toggle (EN / TE) via localStorage

Subtle reveal-on-scroll animations and count-up metrics

🧱 Tech Stack

Pure HTML/CSS/JS (no build tools required)

Fonts: Inter, Space Grotesk, Caveat (Google Fonts)

No external JS frameworks

Optional backend for payments (e.g., Node/Express for Razorpay Orders)

📁 Project Structure
/ (web root)
├─ index.html               # The landing page (all sections + scripts)
├─ /assets                  # Images, video files (you create this)
│  ├─ hero.mp4
│  ├─ G1.webp, G2.webp, ...
│  └─ ...
└─ /server  (optional)      # Only if you integrate Razorpay or any backend
   ├─ server.js
   └─ .env                  # Your secrets (never commit)


You can keep everything in a single index.html for hosting on Netlify, Vercel (static), GitHub Pages, or your cPanel server. Add /server only if you implement payments.

🚀 Getting Started (Static Site)

Download index.html and your assets (images/video).

Put them on any static hosting:

Netlify / Vercel (static project)

GitHub Pages

cPanel / Apache / Nginx (just upload files)

Update these values inside <script> in index.html:

TYPEFORM_URL – your form link

WHATSAPP_NUMBER – full international format (e.g., 91XXXXXXXXXX)

Replace image/video file paths with your actual files
