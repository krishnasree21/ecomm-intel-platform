landing_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>PriceIQ — AI-Powered E-Commerce Intelligence</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #0e0e10; color: #ededed; overflow-x: hidden; }

        /* NAV */
        nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; padding: 16px 60px; display: flex; align-items: center; justify-content: space-between; background: rgba(14,14,16,0.85); backdrop-filter: blur(12px); border-bottom: 1px solid #1f1f23; }
        .nav-logo { font-size: 1.2em; font-weight: 800; color: #ededed; display: flex; align-items: center; gap: 8px; cursor: pointer; }
        .nav-logo span { background: #2d1f52; color: #a78bfa; font-size: 0.6em; padding: 2px 8px; border-radius: 20px; font-weight: 600; }
        .nav-links { display: flex; align-items: center; gap: 28px; }
        .nav-links a { color: #52525b; font-size: 0.88em; text-decoration: none; transition: color 0.2s; cursor: pointer; }
        .nav-links a:hover { color: #ededed; }
        .nav-actions { display: flex; align-items: center; gap: 12px; }
        .btn-nav { padding: 7px 18px; border-radius: 7px; font-size: 0.85em; font-weight: 600; cursor: pointer; transition: all 0.15s; border: none; }
        .btn-ghost { background: transparent; color: #71717a; border: 1px solid #27272a; }
        .btn-ghost:hover { background: #18181b; color: #ededed; }
        .btn-purple { background: #7c3aed; color: white; }
        .btn-purple:hover { background: #6d28d9; transform: translateY(-1px); }

        /* HERO */
        .hero { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 120px 40px 80px; position: relative; overflow: hidden; }
        .hero-glow { position: absolute; top: 20%; left: 50%; transform: translateX(-50%); width: 600px; height: 600px; background: radial-gradient(circle, rgba(124,58,237,0.08) 0%, transparent 70%); pointer-events: none; }
        .hero-badge { display: inline-flex; align-items: center; gap: 6px; background: #1c1528; color: #a78bfa; border: 1px solid #2d1f52; padding: 5px 14px; border-radius: 20px; font-size: 0.78em; font-weight: 600; margin-bottom: 24px; }
        .hero-badge-dot { width: 6px; height: 6px; border-radius: 50%; background: #a78bfa; animation: pulse 2s infinite; }
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }
        .hero h1 { font-size: 3.8em; font-weight: 800; line-height: 1.1; margin-bottom: 20px; max-width: 800px; }
        .hero h1 em { font-style: normal; background: linear-gradient(135deg, #a78bfa, #6ee7b7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .hero p { font-size: 1.1em; color: #52525b; max-width: 560px; line-height: 1.7; margin-bottom: 36px; }
        .hero-actions { display: flex; gap: 14px; justify-content: center; margin-bottom: 60px; }
        .btn-hero-primary { padding: 13px 28px; background: #7c3aed; color: white; border: none; border-radius: 8px; font-size: 0.95em; font-weight: 700; cursor: pointer; transition: all 0.2s; }
        .btn-hero-primary:hover { background: #6d28d9; transform: translateY(-2px); }
        .btn-hero-secondary { padding: 13px 28px; background: transparent; color: #a1a1aa; border: 1px solid #27272a; border-radius: 8px; font-size: 0.95em; font-weight: 600; cursor: pointer; transition: all 0.2s; }
        .btn-hero-secondary:hover { background: #18181b; color: #ededed; }
        .hero-stats { display: flex; gap: 48px; justify-content: center; }
        .hero-stat { text-align: center; }
        .hero-stat-num { font-size: 1.6em; font-weight: 800; color: #ededed; }
        .hero-stat-lbl { font-size: 0.78em; color: #3f3f46; margin-top: 2px; }

        /* DEMO STRIP */
        .demo-strip { background: #111113; border-top: 1px solid #1f1f23; border-bottom: 1px solid #1f1f23; padding: 20px 60px; display: flex; align-items: center; gap: 32px; overflow: hidden; }
        .demo-strip-label { font-size: 0.75em; color: #3f3f46; text-transform: uppercase; letter-spacing: 1px; white-space: nowrap; }
        .demo-strip-items { display: flex; gap: 32px; align-items: center; }
        .demo-strip-item { font-size: 0.82em; color: #52525b; white-space: nowrap; display: flex; align-items: center; gap: 6px; }
        .demo-strip-item::before { content: ''; width: 5px; height: 5px; border-radius: 50%; background: #3f3f46; display: inline-block; }

        /* LIGHT SECTION */
        .light-section { background: #fafafa; color: #111; padding: 80px 60px; }
        .light-section h2 { font-size: 2em; font-weight: 800; text-align: center; margin-bottom: 12px; color: #111; }
        .light-section .section-sub { text-align: center; color: #71717a; font-size: 0.95em; max-width: 500px; margin: 0 auto 48px; line-height: 1.6; }
        .features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1100px; margin: 0 auto; }
        .feature-card { background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 24px; transition: all 0.2s; }
        .feature-card:hover { border-color: #a78bfa; transform: translateY(-3px); box-shadow: 0 8px 24px rgba(124,58,237,0.08); }
        .feature-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.1em; margin-bottom: 14px; }
        .feature-icon-purple { background: #f3f0ff; }
        .feature-icon-green { background: #f0fdf4; }
        .feature-icon-amber { background: #fffbeb; }
        .feature-icon-blue { background: #eff6ff; }
        .feature-icon-red { background: #fef2f2; }
        .feature-icon-teal { background: #f0fdfa; }
        .feature-title { font-size: 0.95em; font-weight: 700; color: #111; margin-bottom: 6px; }
        .feature-desc { font-size: 0.83em; color: #71717a; line-height: 1.6; }
        .coming-soon { display: inline-block; font-size: 0.7em; background: #f3f0ff; color: #7c3aed; padding: 2px 8px; border-radius: 20px; margin-left: 6px; font-weight: 600; vertical-align: middle; }

        /* HOW IT WORKS */
        .how-section { padding: 80px 60px; background: #0e0e10; }
        .how-section h2 { font-size: 2em; font-weight: 800; text-align: center; margin-bottom: 12px; }
        .how-section .section-sub { text-align: center; color: #3f3f46; font-size: 0.93em; max-width: 480px; margin: 0 auto 48px; line-height: 1.6; }
        .steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; max-width: 1100px; margin: 0 auto; }
        .step { text-align: center; padding: 28px 20px; background: #111113; border: 1px solid #1f1f23; border-radius: 12px; position: relative; }
        .step-num { width: 36px; height: 36px; border-radius: 50%; background: #1c1528; color: #a78bfa; font-weight: 700; font-size: 0.88em; display: flex; align-items: center; justify-content: center; margin: 0 auto 14px; border: 1px solid #2d1f52; }
        .step-title { font-size: 0.9em; font-weight: 600; color: #ededed; margin-bottom: 8px; }
        .step-desc { font-size: 0.8em; color: #3f3f46; line-height: 1.6; }

        /* LIGHT SECTION 2 — WHY US */
        .why-section { background: #f8f7ff; padding: 80px 60px; }
        .why-section h2 { font-size: 2em; font-weight: 800; text-align: center; margin-bottom: 12px; color: #111; }
        .why-section .section-sub { text-align: center; color: #71717a; font-size: 0.93em; max-width: 500px; margin: 0 auto 48px; line-height: 1.6; }
        .compare-table { max-width: 800px; margin: 0 auto; background: white; border-radius: 14px; border: 1px solid #e5e7eb; overflow: hidden; }
        .compare-header { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; background: #111; color: white; padding: 12px 20px; font-size: 0.8em; font-weight: 600; }
        .compare-row { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; padding: 12px 20px; border-bottom: 1px solid #f3f4f6; font-size: 0.83em; align-items: center; }
        .compare-row:last-child { border-bottom: none; }
        .compare-row:hover { background: #fafafa; }
        .compare-feature { color: #374151; font-weight: 500; }
        .compare-val { text-align: center; color: #9ca3af; }
        .compare-val.yes { color: #059669; font-weight: 700; }
        .compare-val.no { color: #ef4444; }
        .compare-val.us { color: #7c3aed; font-weight: 700; }
        .compare-us-col { background: #faf5ff; }

        /* ABOUT / DATA */
        .about-section { padding: 80px 60px; background: #0e0e10; }
        .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; max-width: 1000px; margin: 0 auto; align-items: center; }
        .about-left h2 { font-size: 1.9em; font-weight: 800; line-height: 1.2; margin-bottom: 16px; }
        .about-left h2 em { font-style: normal; color: #a78bfa; }
        .about-left p { font-size: 0.88em; color: #52525b; line-height: 1.8; margin-bottom: 20px; }
        .data-points { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
        .data-point { background: #111113; border: 1px solid #1f1f23; border-radius: 9px; padding: 14px; }
        .data-point-num { font-size: 1.4em; font-weight: 800; color: #a78bfa; }
        .data-point-lbl { font-size: 0.75em; color: #3f3f46; margin-top: 2px; }

        /* CTA */
        .cta-section { background: linear-gradient(135deg, #1c1528, #111113); padding: 80px 60px; text-align: center; border-top: 1px solid #2d1f52; border-bottom: 1px solid #2d1f52; }
        .cta-section h2 { font-size: 2.2em; font-weight: 800; margin-bottom: 14px; }
        .cta-section p { font-size: 0.93em; color: #52525b; max-width: 460px; margin: 0 auto 32px; line-height: 1.7; }
        .cta-actions { display: flex; gap: 14px; justify-content: center; }

        /* FOOTER */
        footer { background: #0a0a0c; border-top: 1px solid #1f1f23; padding: 40px 60px; display: flex; justify-content: space-between; align-items: center; }
        .footer-logo { font-size: 1em; font-weight: 700; color: #52525b; }
        .footer-links { display: flex; gap: 24px; }
        .footer-links a { font-size: 0.82em; color: #3f3f46; text-decoration: none; }
        .footer-links a:hover { color: #71717a; }
        .footer-right { font-size: 0.78em; color: #27272a; }

        /* LOGIN MODAL */
        .modal-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 1000; align-items: center; justify-content: center; backdrop-filter: blur(4px); }
        .modal-overlay.open { display: flex; }
        .modal { background: #111113; border: 1px solid #27272a; border-radius: 14px; padding: 36px; width: 380px; max-width: 90vw; }
        .modal h3 { font-size: 1.1em; font-weight: 700; margin-bottom: 6px; }
        .modal p { font-size: 0.82em; color: #52525b; margin-bottom: 24px; }
        .modal-close { float: right; background: none; border: none; color: #52525b; cursor: pointer; font-size: 1.2em; margin-top: -4px; }
        .oauth-btn { width: 100%; padding: 11px; border-radius: 8px; font-size: 0.88em; font-weight: 600; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 10px; transition: all 0.15s; }
        .btn-google { background: #18181b; border: 1px solid #27272a; color: #ededed; }
        .btn-google:hover { background: #1f1f23; }
        .btn-github { background: #ededed; border: 1px solid #d1d5db; color: #111; }
        .btn-github:hover { background: #d1d5db; }
        .modal-divider { display: flex; align-items: center; gap: 12px; margin: 16px 0; }
        .modal-divider span { font-size: 0.75em; color: #3f3f46; }
        .modal-divider::before, .modal-divider::after { content: ''; flex: 1; height: 1px; background: #27272a; }
        .modal-note { font-size: 0.75em; color: #27272a; text-align: center; margin-top: 16px; line-height: 1.5; }

        /* CHATBOT */
        .chat-bubble { position: fixed; bottom: 24px; left: 24px; z-index: 999; }
        .chat-toggle { width: 52px; height: 52px; border-radius: 50%; background: #7c3aed; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1.3em; box-shadow: 0 4px 20px rgba(124,58,237,0.4); transition: all 0.2s; }
        .chat-toggle:hover { background: #6d28d9; transform: scale(1.05); }
        .chat-window { display: none; position: absolute; bottom: 64px; left: 0; width: 320px; background: #111113; border: 1px solid #27272a; border-radius: 14px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
        .chat-window.open { display: flex; flex-direction: column; }
        .chat-header { padding: 14px 16px; background: #7c3aed; display: flex; align-items: center; justify-content: space-between; }
        .chat-header-left { display: flex; align-items: center; gap: 8px; }
        .chat-avatar { width: 28px; height: 28px; border-radius: 50%; background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 0.8em; }
        .chat-header-info { }
        .chat-header-name { font-size: 0.85em; font-weight: 600; color: white; }
        .chat-header-status { font-size: 0.72em; color: rgba(255,255,255,0.7); }
        .chat-close { background: none; border: none; color: white; cursor: pointer; font-size: 1em; opacity: 0.7; }
        .chat-close:hover { opacity: 1; }
        .chat-messages { height: 280px; overflow-y: auto; padding: 14px; display: flex; flex-direction: column; gap: 10px; }
        .chat-msg { max-width: 85%; padding: 9px 12px; border-radius: 10px; font-size: 0.82em; line-height: 1.5; }
        .chat-msg-bot { background: #1c1c1e; color: #a1a1aa; align-self: flex-start; border-bottom-left-radius: 3px; }
        .chat-msg-user { background: #7c3aed; color: white; align-self: flex-end; border-bottom-right-radius: 3px; }
        .chat-typing { display: none; align-self: flex-start; }
        .chat-typing span { display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #52525b; margin: 0 2px; animation: typing 1.2s infinite; }
        .chat-typing span:nth-child(2) { animation-delay: 0.2s; }
        .chat-typing span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes typing { 0%,60%,100%{transform:translateY(0)} 30%{transform:translateY(-6px)} }
        .chat-suggestions { padding: 8px 14px; display: flex; flex-wrap: wrap; gap: 6px; border-top: 1px solid #1f1f23; }
        .chat-suggest-btn { padding: 4px 10px; background: #1c1528; border: 1px solid #2d1f52; border-radius: 20px; color: #a78bfa; font-size: 0.75em; cursor: pointer; transition: all 0.15s; white-space: nowrap; }
        .chat-suggest-btn:hover { background: #2d1f52; }
        .chat-input-row { display: flex; gap: 0; border-top: 1px solid #1f1f23; }
        .chat-input-row input { flex: 1; background: #0e0e10; border: none; padding: 12px 14px; color: #ededed; font-size: 0.84em; outline: none; }
        .chat-input-row input::placeholder { color: #3f3f46; }
        .chat-send { background: #7c3aed; border: none; padding: 12px 14px; color: white; cursor: pointer; font-size: 0.88em; transition: background 0.15s; }
        .chat-send:hover { background: #6d28d9; }

        /* FAQ */
        .faq-item { border: 1px solid #1f1f23; border-radius: 10px; margin-bottom: 10px; overflow: hidden; cursor: pointer; transition: border-color 0.2s; }
        .faq-item:hover { border-color: #2d1f52; }
        .faq-item.open { border-color: #7c3aed; }
        .faq-question { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; font-size: 0.92em; font-weight: 600; color: #ededed; background: #111113; }
        .faq-icon { color: #7c3aed; font-size: 1.2em; font-weight: 300; transition: transform 0.2s; }
        .faq-item.open .faq-icon { transform: rotate(45deg); }
        .faq-answer { display: none; padding: 0 20px 16px; font-size: 0.84em; color: #52525b; line-height: 1.7; background: #111113; }
        .faq-item.open .faq-answer { display: block; }
    </style>
</head>
<body>

<!-- NAV -->
<nav>
    <div class="nav-logo" onclick="goToDashboard()">⚡ PriceIQ <span>AI</span></div>
    <div class="nav-links">
        <a onclick="scrollTo('features')">Features</a>
        <a onclick="scrollTo('how-it-works')">How it works</a>
        <a onclick="scrollTo('why-priceiq')">Why PriceIQ</a>
        <a onclick="scrollTo('our-data')">Our Data</a>
    </div>
    <div class="nav-actions">
        <button class="btn-nav btn-ghost" onclick="openLogin()">Sign in</button>
        <button class="btn-nav btn-purple" onclick="goToDashboard()">Get Intelligence Access →</button>
    </div>
</nav>

<!-- HERO -->
<section class="hero">
    <div class="hero-glow"></div>
    <div class="hero-badge"><div class="hero-badge-dot"></div> AI-powered competitor intelligence</div>
    <h1>Your competitors are watching.<br><em>Now you can too.</em></h1>
    <p>PriceIQ uses AI to automatically track competitor prices, analyze customer sentiment, and tell you exactly where your product stands in the market — in real time.</p>
    <div class="hero-actions">
        <button class="btn-hero-primary" onclick="goToDashboard()">Try Live Intelligence Demo →</button>
        <button class="btn-hero-secondary" onclick="scrollTo('how-it-works')">See how it works</button>
    </div>
    <div class="hero-stats">
        <div class="hero-stat"><div class="hero-stat-num">80+</div><div class="hero-stat-lbl">Product categories</div></div>
        <div class="hero-stat"><div class="hero-stat-num">Real-time</div><div class="hero-stat-lbl">Price intelligence</div></div>
        <div class="hero-stat"><div class="hero-stat-num">Free</div><div class="hero-stat-lbl">No credit card needed</div></div>
        <div class="hero-stat"><div class="hero-stat-num">AI</div><div class="hero-stat-lbl">Powered decisions</div></div>
    </div>
</section>

<!-- DEMO STRIP -->
<div class="demo-strip">
    <div class="demo-strip-label">Tracks</div>
    <div class="demo-strip-items">
        <div class="demo-strip-item">Sony vs Bose vs JBL</div>
        <div class="demo-strip-item">Samsung vs Apple vs OnePlus</div>
        <div class="demo-strip-item">Nike vs Adidas vs Puma</div>
        <div class="demo-strip-item">Dell vs HP vs Lenovo</div>
        <div class="demo-strip-item">Samsung TV vs LG vs Sony</div>
        <div class="demo-strip-item">Philips vs Ninja vs Cosori</div>
    </div>
</div>

<!-- FEATURES — LIGHT -->
<section class="light-section" id="features"> 
    <h2>Everything your pricing team needs</h2>
    <p class="section-sub">Six AI-powered modules that work together to give you an unfair competitive advantage.</p>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon feature-icon-purple">📊</div>
            <div class="feature-title">Sentiment Intelligence</div>
            <div class="feature-desc">NLP-powered review analysis scores customer sentiment from -1 to +1. Know what customers really think before it hurts your sales.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon feature-icon-green">💰</div>
            <div class="feature-title">Competitor Price Tracking</div>
            <div class="feature-desc">Automatically fetch and compare competitor prices across 80+ product categories. Know your exact market position at any time.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon feature-icon-amber">📈</div>
            <div class="feature-title">Price Trend Analysis</div>
            <div class="feature-desc">Track how your prices and competitor prices change over time. Spot pricing opportunities and patterns before your competitors do.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon feature-icon-blue">◉</div>
            <div class="feature-title">Customer Segmentation <span class="coming-soon">Soon</span></div>
            <div class="feature-desc">K-Means ML clustering automatically groups your customers by behavior — identifying high-value, price-sensitive, and at-risk segments.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon feature-icon-teal">∿</div>
            <div class="feature-title">Sales Forecasting <span class="coming-soon">Soon</span></div>
            <div class="feature-desc">Time-series regression predicts future demand so you can optimize inventory, pricing, and marketing strategy weeks ahead.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon feature-icon-red">✦</div>
            <div class="feature-title">Recommendation Engine <span class="coming-soon">Soon</span></div>
            <div class="feature-desc">Collaborative filtering suggests the right products to the right customers — the same technology powering Amazon recommendations.</div>
        </div>
    </div>
</section>

<!-- HOW IT WORKS -->
<section class="how-section" id="how-it-works">
    <h2>How PriceIQ works</h2>
    <p class="section-sub">Four steps from raw data to actionable business intelligence — all automated.</p>
    <div class="steps">
        <div class="step">
            <div class="step-num">1</div>
            <div class="step-title">Input your product</div>
            <div class="step-desc">Enter your product name, price, and a customer review. PriceIQ auto-fetches competitor prices from our market database.</div>
        </div>
        <div class="step">
            <div class="step-num">2</div>
            <div class="step-title">AI analysis runs</div>
            <div class="step-desc">NLP sentiment engine scores the review. Pricing engine calculates your market position against all known competitors.</div>
        </div>
        <div class="step">
            <div class="step-num">3</div>
            <div class="step-title">Intelligence score</div>
            <div class="step-desc">Sentiment and pricing signals combine into a single Product Intelligence Score out of 10 — your competitive health rating.</div>
        </div>
        <div class="step">
            <div class="step-num">4</div>
            <div class="step-title">Act on insights</div>
            <div class="step-desc">Receive a precise business recommendation. Pricing alerts notify you automatically when opportunities or risks are detected.</div>
        </div>
    </div>
</section>

<!-- WHY US — LIGHT -->
<section class="why-section" id="why-priceiq">
    <h2>Why PriceIQ over others</h2>
    <p class="section-sub">Jungle Scout tracks Amazon. Keepa shows price history. We give you the full intelligence picture — and we're building towards it fast.</p>
    <div class="compare-table">
        <div class="compare-header">
            <span>Feature</span>
            <span style="text-align:center">Jungle Scout</span>
            <span style="text-align:center">Keepa</span>
            <span style="text-align:center;color:#a78bfa">PriceIQ</span>
        </div>
        <div class="compare-row">
            <span class="compare-feature">Sentiment analysis</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val us">✓ AI-powered</span>
        </div>
        <div class="compare-row">
            <span class="compare-feature">Competitor price comparison</span>
            <span class="compare-val yes">✓</span>
            <span class="compare-val yes">✓</span>
            <span class="compare-val us">✓ Multi-brand</span>
        </div>
        <div class="compare-row">
            <span class="compare-feature">Product intelligence score</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val us">✓ Unique to us</span>
        </div>
        <div class="compare-row">
            <span class="compare-feature">Price trend tracking</span>
            <span class="compare-val yes">✓</span>
            <span class="compare-val yes">✓</span>
            <span class="compare-val us">✓ Real-time</span>
        </div>
        <div class="compare-row">
            <span class="compare-feature">Customer segmentation ML</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val us">Coming soon</span>
        </div>
        <div class="compare-row">
            <span class="compare-feature">Sales forecasting</span>
            <span class="compare-val yes">✓ Amazon only</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val us">Coming soon</span>
        </div>
        <div class="compare-row">
            <span class="compare-feature">Recommendation engine</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val no">✗</span>
            <span class="compare-val us">Coming soon</span>
        </div>
        <div class="compare-row">
            <span class="compare-feature">Free to try</span>
            <span class="compare-val no">✗ Paid only</span>
            <span class="compare-val yes">✓ Limited</span>
            <span class="compare-val us">✓ Full demo</span>
        </div>
    </div>
</section>

<!-- ABOUT / OUR DATA -->
<section class="about-section" id="our-data">
    <div class="about-grid">
        <div class="about-left">
            <h2>Built on <em>real market data</em>, not guesswork.</h2>
            <p>PriceIQ's intelligence layer is powered by a continuously growing market price database spanning electronics, appliances, fashion, food, fitness, and more — with competitor pricing sourced from verified market data.</p>
            <p>Our NLP sentiment engine is built on TextBlob and is being upgraded to transformer-based models (DistilBERT) for context-aware sentiment understanding that catches sarcasm, mixed opinions, and nuanced feedback.</p>
        </div>
        <div class="data-points">
            <div class="data-point"><div class="data-point-num">80+</div><div class="data-point-lbl">Product categories tracked</div></div>
            <div class="data-point"><div class="data-point-num">6</div><div class="data-point-lbl">AI microservices architecture</div></div>
            <div class="data-point"><div class="data-point-num">NLP</div><div class="data-point-lbl">Review sentiment engine</div></div>
            <div class="data-point"><div class="data-point-num">Real-time</div><div class="data-point-lbl">Pricing intelligence alerts</div></div>
        </div>
    </div>
</section>

<!-- CTA -->
<section class="cta-section">
    <h2>Ready to outsmart your competition?</h2>
    <p>Start for free. No credit card. No setup. Just intelligence.</p>
    <div class="cta-actions">
        <button class="btn-hero-primary" onclick="goToDashboard()">Launch Intelligence Dashboard →</button>
        <button class="btn-hero-secondary" onclick="openLogin()">Create free account</button>
    </div>
</section>

<!-- FAQ -->
<section style="background:#0e0e10; padding:80px 60px;" id="faq">
    <h2 style="font-size:2em; font-weight:800; text-align:center; margin-bottom:12px;">Frequently asked questions</h2>
    <p style="text-align:center; color:#3f3f46; font-size:0.93em; max-width:480px; margin:0 auto 48px; line-height:1.6;">Everything you need to know about PriceIQ.</p>
    <div style="max-width:700px; margin:0 auto;">

        <div class="faq-item" onclick="toggleFaq(this)">
            <div class="faq-question">What exactly does PriceIQ do? <span class="faq-icon">+</span></div>
            <div class="faq-answer">PriceIQ is an AI-powered e-commerce intelligence platform. You enter your product, your price, a competitor price, and a customer review. PriceIQ instantly analyzes the sentiment of the review, compares your pricing against competitors, gives you an overall intelligence score out of 10, and recommends exactly what action to take.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
            <div class="faq-question">Is PriceIQ really free? <span class="faq-icon">+</span></div>
            <div class="faq-answer">Yes — completely free to use in demo mode. No credit card, no signup required. Just click the demo button and start analyzing your products immediately. Premium features like customer segmentation and sales forecasting are coming soon.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
            <div class="faq-question">How does the sentiment analysis work? <span class="faq-icon">+</span></div>
            <div class="faq-answer">PriceIQ uses Natural Language Processing to read and score customer reviews. It analyzes the emotional tone of the text and gives a score from -1 (very negative) to +1 (very positive). This score is combined with your pricing position to create an overall product intelligence score.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
            <div class="faq-question">What products and categories can I track? <span class="faq-icon">+</span></div>
            <div class="faq-answer">PriceIQ covers 80+ product categories including electronics, phones, laptops, headphones, TVs, home appliances, fashion, food and grocery, fitness equipment, gaming, beauty products, and furniture. We are continuously expanding the database.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
            <div class="faq-question">How is PriceIQ different from Jungle Scout or Keepa? <span class="faq-icon">+</span></div>
            <div class="faq-answer">Jungle Scout is focused on Amazon sellers only. Keepa tracks Amazon price history only. PriceIQ works across all product categories, adds AI sentiment analysis on top of pricing data, and gives you a combined intelligence score — something neither platform offers.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
            <div class="faq-question">What is the Product Intelligence Score? <span class="faq-icon">+</span></div>
            <div class="faq-answer">It is a unique PriceIQ score out of 10 that combines two signals — how customers feel about your product (sentiment) and how competitively you are priced (pricing position). A score of 8+ means excellent, 6-8 is good, 4-6 is average, below 4 needs immediate action.</div>
        </div>

        <div class="faq-item" onclick="toggleFaq(this)">
            <div class="faq-question">When are customer segmentation and forecasting coming? <span class="faq-icon">+</span></div>
            <div class="faq-answer">Customer segmentation using K-Means ML and sales forecasting using time-series regression are actively being built as separate microservices. They will be available in the next major update. Create an account to get notified when they launch.</div>
        </div>

    </div>
</section>

<!-- FOOTER -->
<footer>
    <div class="footer-logo">⚡ PriceIQ</div>
    <div class="footer-links">
        <a onclick="scrollTo('features')">Features</a>
        <a onclick="scrollTo('how-it-works')">How it works</a>
        <a onclick="scrollTo('why-us')">Why PriceIQ</a>
        <a onclick="scrollTo('about')">Our Data</a>
    </div>
    <div class="footer-right">Built with Python FastAPI · AI-powered · © 2026 PriceIQ</div>
</footer>

<!-- LOGIN MODAL -->
<div class="modal-overlay" id="login-modal" onclick="closeLoginOnOverlay(event)">
    <div class="modal">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px">
            <h3>Sign in to PriceIQ</h3>
            <button class="modal-close" onclick="closeLogin()">✕</button>
        </div>
        <p>Access your intelligence dashboard and saved analyses.</p>
        <button class="oauth-btn btn-google" onclick="loginWithGoogle()">
            <svg width="16" height="16" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
            Continue with Google
        </button>
        <button class="oauth-btn btn-github" onclick="loginWithGitHub()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
            Continue with GitHub
        </button>
        <div class="modal-divider"><span>or</span></div>
        <button class="oauth-btn btn-google" onclick="goToDashboard()" style="background:#1c1528;border-color:#2d1f52;color:#a78bfa">
            Try demo without account →
        </button>
        <div class="modal-note">By signing in you agree to our terms. Login functionality coming soon — use the demo in the meantime.</div>
    </div>
</div>

<!-- CHATBOT -->
<div class="chat-bubble">
    <div class="chat-window" id="chat-window">
        <div class="chat-header">
            <div class="chat-header-left">
                <div class="chat-avatar">⚡</div>
                <div class="chat-header-info">
                    <div class="chat-header-name">Maya — PriceIQ Assistant</div>
                <div class="chat-header-status">AI-powered · Always online</div>
                </div>
            </div>
            <button class="chat-close" onclick="toggleChat()">✕</button>
        </div>
        <div class="chat-messages" id="chat-messages">
            <div class="chat-msg chat-msg-bot">Hey! I'm the PriceIQ assistant. I can answer questions about the platform, help you understand features, or connect you with the team. What can I help you with?</div>
        </div>
        <div class="chat-suggestions" id="chat-suggestions">
            <span class="chat-suggest-btn" onclick="askQuestion('What does PriceIQ do?')">What is PriceIQ?</span>
            <span class="chat-suggest-btn" onclick="askQuestion('Is PriceIQ free?')">Is it free?</span>
            <span class="chat-suggest-btn" onclick="askQuestion('How does sentiment analysis work?')">Sentiment analysis?</span>
            <span class="chat-suggest-btn" onclick="askQuestion('What products can I track?')">What can I track?</span>
            <span class="chat-suggest-btn" onclick="askQuestion('How is PriceIQ different from Jungle Scout?')">vs Jungle Scout?</span>
            <span class="chat-suggest-btn" onclick="askQuestion('What is the intelligence score?')">Intelligence score?</span>
            <span class="chat-suggest-btn" onclick="askQuestion('How do I get started?')">How to start?</span>
        </div>
        <div class="chat-input-row">
            <input type="text" id="chat-input" placeholder="Ask anything..." onkeydown="if(event.key==='Enter')sendChat()" />
            <button class="chat-send" onclick="sendChat()">→</button>
        </div>
    </div>
    <button class="chat-toggle" onclick="toggleChat()" id="chat-toggle-btn">💬</button>
</div>

<script>
    function scrollTo(id) {
        document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
    }

    function goToDashboard() {
        window.location.href = '/dashboard';
    }

    function openLogin() {
        document.getElementById('login-modal').classList.add('open');
    }

    function closeLogin() {
        document.getElementById('login-modal').classList.remove('open');
    }

    function closeLoginOnOverlay(e) {
        if (e.target === document.getElementById('login-modal')) closeLogin();
    }

    function loginWithGoogle() {
        alert('Google OAuth integration coming soon! Use the demo for now.');
    }

    function loginWithGitHub() {
        alert('GitHub OAuth integration coming soon! Use the demo for now.');
    }

    function toggleChat() {
        const win = document.getElementById('chat-window');
        const btn = document.getElementById('chat-toggle-btn');
        win.classList.toggle('open');
        btn.textContent = win.classList.contains('open') ? '✕' : '💬';
    }

    const faqAnswers = {
        'what does priceiq do': 'PriceIQ is an AI-powered e-commerce intelligence platform. It automatically compares your product prices against competitors, analyzes customer review sentiment, gives you an intelligence score out of 10, and recommends exactly what action to take. Try the live demo — no signup needed!',
        'how does sentiment analysis work': 'PriceIQ reads customer reviews using Natural Language Processing and scores the emotional tone from -1 (very negative) to +1 (very positive). This sentiment score is combined with your pricing position to create your overall Product Intelligence Score.',
        'is priceiq free': 'Yes — completely free! No credit card, no signup required. Click the demo button and start analyzing immediately. Premium features like customer segmentation and forecasting are coming soon.',
        'what products can i track': 'PriceIQ covers 80+ categories — electronics, phones, laptops, headphones, TVs, appliances, fashion, food, fitness, gaming, beauty, and furniture. We are always adding more.',
        'how is priceiq different from jungle scout': 'Jungle Scout only works for Amazon sellers. Keepa only tracks Amazon price history. PriceIQ works across all categories, adds AI sentiment analysis, and gives a combined intelligence score — something neither platform offers.',
        'what is the intelligence score': 'The Product Intelligence Score out of 10 combines sentiment (how customers feel) and pricing position (how competitive you are). 8+ is excellent, 6-8 is good, 4-6 is average, below 4 needs urgent action.',
        'how do i get started': 'Just click the "Try Live Intelligence Demo" button — no account needed! Enter your product name, your price, a competitor price, and a customer review. PriceIQ does the rest instantly.',
        'how to start': 'Click "Try Live Intelligence Demo" at the top of the page. No signup, no credit card. Just enter your product details and get instant AI intelligence.',
        'when is segmentation coming': 'Customer segmentation and sales forecasting are actively being built. Create an account to get notified when they launch!',
        'price trend': 'Price Trend Analysis tracks how your price and competitor prices change over time. Every time you analyze a product, the price is saved to history so you can spot patterns.',
    };

    function findAnswer(question) {
        const q = question.toLowerCase();
        for (const [key, answer] of Object.entries(faqAnswers)) {
            const keywords = key.split(' ').filter(w => w.length > 3);
            if (keywords.filter(k => q.includes(k)).length >= 2) return answer;
        }
        for (const [key, answer] of Object.entries(faqAnswers)) {
            const keywords = key.split(' ').filter(w => w.length > 3);
            if (keywords.some(k => q.includes(k))) return answer;
        }
        return null;
    }

    async function askQuestion(question) {
        document.getElementById('chat-suggestions').style.display = 'none';
        addMessage(question, 'user');
        showTyping();

        const faqAnswer = findAnswer(question);
        if (faqAnswer) {
            setTimeout(() => {
                hideTyping();
                addMessage(faqAnswer, 'bot');
                showFollowups();
            }, 800);
        } else {
            try {
                const response = await fetch('https://api.anthropic.com/v1/messages', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        model: 'claude-sonnet-4-20250514',
                        max_tokens: 1000,
                        system: 'You are the PriceIQ assistant. PriceIQ is an AI-powered e-commerce intelligence platform that uses NLP sentiment analysis, competitor price tracking, product intelligence scoring, and price trend analysis. Answer questions concisely and helpfully about the platform. Keep answers under 3 sentences.',
                        messages: [{ role: 'user', content: question }]
                    })
                });
                const data = await response.json();
                hideTyping();
                const text = data.content?.[0]?.text || 'I can help with questions about PriceIQ features, pricing intelligence, and sentiment analysis. What would you like to know?';
                addMessage(text, 'bot');
                showFollowups();
            } catch(e) {
                hideTyping();
                addMessage("I'm not sure about that one! For detailed answers, create a free account and explore the full platform. Or try asking me about features, pricing, or how to get started 😊", 'bot');
                showFollowups();
            }
        }
    }

    function sendChat() {
        const input = document.getElementById('chat-input');
        const question = input.value.trim();
        if (!question) return;
        input.value = '';
        askQuestion(question);
    }

    function addMessage(text, type) {
        const msgs = document.getElementById('chat-messages');
        const div = document.createElement('div');
        div.className = 'chat-msg chat-msg-' + type;
        div.textContent = text;
        msgs.appendChild(div);
        msgs.scrollTop = msgs.scrollHeight;
    }

    function showTyping() {
        const msgs = document.getElementById('chat-messages');
        const div = document.createElement('div');
        div.className = 'chat-msg chat-msg-bot chat-typing';
        div.id = 'typing-indicator';
        div.style.display = 'flex';
        div.innerHTML = '<span></span><span></span><span></span>';
        msgs.appendChild(div);
        msgs.scrollTop = msgs.scrollHeight;
    }

    function hideTyping() {
        const el = document.getElementById('typing-indicator');
        if (el) el.remove();
    }

    function showFollowups() {
        document.getElementById('chat-suggestions').style.display = 'flex';
    }
</script>
</body>
</html>
"""