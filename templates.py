html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>EcomIntel — E-Commerce Intelligence Platform</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: #060d1a; color: #e2e8f0; min-height: 100vh; display: flex; }

        /* Sidebar */
        .sidebar { width: 220px; background: #0d1829; border-right: 1px solid #1e3a5f; display: flex; flex-direction: column; position: fixed; height: 100vh; left: 0; top: 0; z-index: 100; }
        .sidebar-logo { padding: 20px; font-size: 1.1em; font-weight: 700; color: #60a5fa; border-bottom: 1px solid #1e3a5f; display: flex; align-items: center; gap: 8px; }
        .sidebar-logo span { font-size: 0.65em; background: #1e3a5f; color: #60a5fa; padding: 2px 8px; border-radius: 20px; font-weight: 600; }
        .nav-section { padding: 16px 16px 6px; font-size: 0.7em; color: #475569; text-transform: uppercase; letter-spacing: 1px; font-weight: 600; }
        .nav-item { display: flex; align-items: center; gap: 10px; padding: 9px 16px; margin: 1px 8px; border-radius: 8px; cursor: pointer; font-size: 0.88em; color: #64748b; transition: all 0.15s; }
        .nav-item:hover { background: #1e293b; color: #94a3b8; }
        .nav-item.active { background: #1e3a5f; color: #60a5fa; font-weight: 600; }
        .nav-icon { font-size: 0.85em; width: 16px; text-align: center; }
        .nav-badge { margin-left: auto; background: #ef4444; color: white; font-size: 0.7em; padding: 1px 6px; border-radius: 20px; }

        /* Main content */
        .main { margin-left: 220px; flex: 1; display: flex; flex-direction: column; min-height: 100vh; }
        .topbar { padding: 14px 28px; background: #0d1829; border-bottom: 1px solid #1e3a5f; display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 50; }
        .topbar-left h1 { font-size: 1em; font-weight: 600; color: #e2e8f0; }
        .topbar-left p { font-size: 0.78em; color: #475569; margin-top: 1px; }
        .topbar-right { display: flex; align-items: center; gap: 12px; }
        .live-badge { display: flex; align-items: center; gap: 5px; font-size: 0.78em; color: #4ade80; }
        .live-dot { width: 6px; height: 6px; border-radius: 50%; background: #4ade80; animation: pulse 2s infinite; }
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }

        /* Pages */
        .page { display: none; padding: 24px 28px; }
        .page.active { display: block; }

        /* Metric cards */
        .metrics-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }
        .metric-card { background: #0d1829; border: 1px solid #1e3a5f; border-radius: 12px; padding: 18px; }
        .metric-label { font-size: 0.75em; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
        .metric-value { font-size: 1.8em; font-weight: 700; color: #e2e8f0; }
        .metric-sub { font-size: 0.75em; margin-top: 4px; }
        .metric-up { color: #4ade80; }
        .metric-down { color: #f87171; }
        .metric-neutral { color: #475569; }

        /* Cards */
        .card { background: #0d1829; border: 1px solid #1e3a5f; border-radius: 12px; padding: 20px; margin-bottom: 20px; }
        .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
        .card-title { font-size: 0.9em; font-weight: 600; color: #94a3b8; }
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
        .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 20px; }

        /* Forms */
        .form-group { margin-bottom: 14px; }
        .form-label { display: block; font-size: 0.75em; color: #475569; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 5px; }
        input, textarea, select { width: 100%; padding: 9px 12px; background: #060d1a; border: 1px solid #1e3a5f; border-radius: 8px; color: #e2e8f0; font-size: 0.88em; outline: none; transition: border-color 0.15s; }
        input:focus, textarea:focus, select:focus { border-color: #3b82f6; }
        textarea { resize: vertical; min-height: 80px; }

        /* Buttons */
        .btn { padding: 9px 18px; border: none; border-radius: 8px; cursor: pointer; font-size: 0.88em; font-weight: 600; transition: all 0.15s; display: inline-flex; align-items: center; gap: 6px; }
        .btn-primary { background: #2563eb; color: white; }
        .btn-primary:hover { background: #1d4ed8; transform: translateY(-1px); }
        .btn-success { background: #059669; color: white; }
        .btn-success:hover { background: #047857; }
        .btn-full { width: 100%; justify-content: center; margin-top: 8px; }
        .btn-sm { padding: 5px 12px; font-size: 0.8em; }

        /* Badges */
        .badge { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 0.75em; font-weight: 600; }
        .badge-positive { background: #052e16; color: #4ade80; border: 1px solid #166534; }
        .badge-negative { background: #450a0a; color: #f87171; border: 1px solid #7f1d1d; }
        .badge-neutral { background: #431407; color: #fb923c; border: 1px solid #78350f; }
        .badge-info { background: #0c2340; color: #60a5fa; border: 1px solid #1e3a5f; }

        /* Result box */
        .result-box { background: #060d1a; border: 1px solid #1e3a5f; border-radius: 10px; padding: 16px; margin-top: 14px; display: none; }
        .score-display { text-align: center; padding: 14px 0 12px; border-bottom: 1px solid #1e3a5f; margin-bottom: 12px; }
        .score-num { font-size: 3em; font-weight: 800; line-height: 1; }
        .score-lbl { font-size: 0.82em; font-weight: 600; margin-top: 3px; }
        .score-sub { font-size: 0.72em; color: #475569; margin-top: 2px; }
        .stat-row { display: flex; justify-content: space-between; align-items: flex-start; padding: 8px 0; border-bottom: 1px solid #0f172a; font-size: 0.84em; gap: 12px; }
        .stat-row:last-child { border-bottom: none; }
        .stat-lbl { color: #475569; white-space: nowrap; }
        .stat-val { color: #e2e8f0; font-weight: 500; text-align: right; }

        /* Competitor selector */
        .comp-selector { display: none; background: #060d1a; border: 1px solid #1e3a5f; border-radius: 8px; padding: 12px; margin-top: 8px; }
        .comp-selector p { font-size: 0.78em; color: #475569; margin-bottom: 8px; }
        .comp-btn { display: inline-block; padding: 4px 10px; background: #0d1829; border: 1px solid #1e3a5f; border-radius: 6px; cursor: pointer; font-size: 0.78em; margin: 3px; color: #94a3b8; transition: all 0.15s; }
        .comp-btn:hover, .comp-btn.selected { background: #1e3a5f; color: #60a5fa; border-color: #3b82f6; }
        .fetch-status { font-size: 0.78em; margin-top: 5px; min-height: 16px; }

        /* Rank items */
        .rank-item { display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; border-radius: 6px; margin: 4px 0; background: #060d1a; font-size: 0.84em; }
        .rank-you { border-left: 3px solid #3b82f6; }
        .rank-num { color: #475569; margin-right: 8px; font-size: 0.85em; }

        /* Table */
        .data-table { width: 100%; border-collapse: collapse; font-size: 0.84em; }
        .data-table th { padding: 10px 12px; text-align: left; color: #475569; font-size: 0.78em; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #1e3a5f; font-weight: 600; }
        .data-table td { padding: 10px 12px; border-bottom: 1px solid #0f172a; color: #cbd5e1; vertical-align: middle; }
        .data-table tr:hover td { background: #060d1a; }
        .data-table tr:last-child td { border-bottom: none; }

        /* Score bar */
        .score-bar { height: 4px; background: #1e293b; border-radius: 2px; overflow: hidden; margin-top: 3px; }
        .score-fill { height: 100%; border-radius: 2px; }

        /* Alert items */
        .alert-item { display: flex; align-items: flex-start; gap: 12px; padding: 12px; border-radius: 8px; margin-bottom: 8px; }
        .alert-urgent { background: #1a0606; border: 1px solid #7f1d1d; }
        .alert-warning { background: #1a0e00; border: 1px solid #78350f; }
        .alert-success { background: #021a0a; border: 1px solid #166534; }
        .alert-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; margin-top: 4px; }
        .alert-title { font-size: 0.85em; font-weight: 600; margin-bottom: 2px; }
        .alert-sub { font-size: 0.78em; color: #475569; }

        /* Trend input */
        .trend-row { display: flex; gap: 10px; margin-bottom: 16px; }
        .trend-row input { flex: 1; }

        /* Empty state */
        .empty-state { text-align: center; padding: 40px; color: #334155; font-size: 0.88em; }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: #0d1829; }
        ::-webkit-scrollbar-thumb { background: #1e3a5f; border-radius: 2px; }
    </style>
</head>
<body>

<!-- Sidebar -->
<div class="sidebar">
    <div class="sidebar-logo">⚡ EcomIntel <span>AI</span></div>

    <div class="nav-section">Intelligence</div>
    <div class="nav-item active" onclick="showPage('dashboard')">
        <span class="nav-icon">◈</span> Dashboard
    </div>
    <div class="nav-item" onclick="showPage('analyze')">
        <span class="nav-icon">◎</span> Product Analysis
    </div>
    <div class="nav-item" onclick="showPage('compare')">
        <span class="nav-icon">◐</span> Price Monitor
    </div>
    <div class="nav-item" onclick="showPage('trends')">
        <span class="nav-icon">↗</span> Trend Analysis
    </div>

    <div class="nav-section">Analytics</div>
    <div class="nav-item" onclick="showPage('segmentation')">
        <span class="nav-icon">◉</span> Segmentation
    </div>
    <div class="nav-item" onclick="showPage('forecasting')">
        <span class="nav-icon">∿</span> Forecasting
    </div>
    <div class="nav-item" onclick="showPage('recommendations')">
        <span class="nav-icon">✦</span> Recommendations
    </div>

    <div class="nav-section">System</div>
    <div class="nav-item" onclick="showPage('history')">
        <span class="nav-icon">≡</span> History
    </div>
    <div class="nav-item" onclick="showPage('alerts')">
        <span class="nav-icon">◬</span> Alerts
        <span class="nav-badge" id="alert-count">0</span>
    </div>
</div>

<!-- Main -->
<div class="main">
    <div class="topbar">
        <div class="topbar-left">
            <h1 id="page-title">Intelligence Dashboard</h1>
            <p id="page-sub">Overview of your e-commerce intelligence signals</p>
        </div>
        <div class="topbar-right">
            <div class="live-badge"><div class="live-dot"></div> Live</div>
        </div>
    </div>

    <!-- DASHBOARD PAGE -->
    <div class="page active" id="page-dashboard">
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-label">Products tracked</div>
                <div class="metric-value" id="m-products">0</div>
                <div class="metric-sub metric-neutral">All time</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Avg sentiment</div>
                <div class="metric-value" id="m-sentiment">—</div>
                <div class="metric-sub metric-neutral">Across all products</div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Positive products</div>
                <div class="metric-value" id="m-positive">0</div>
                <div class="metric-sub metric-up" id="m-positive-pct"></div>
            </div>
            <div class="metric-card">
                <div class="metric-label">At risk products</div>
                <div class="metric-value" id="m-atrisk">0</div>
                <div class="metric-sub metric-down" id="m-atrisk-pct"></div>
            </div>
        </div>

        <div class="grid-2">
            <div class="card">
                <div class="card-header">
                    <div class="card-title">Recent analyses</div>
                    <button class="btn btn-sm" onclick="showPage('analyze')" style="background:#1e3a5f;color:#60a5fa;border:none;cursor:pointer;border-radius:6px;padding:5px 12px;font-size:0.78em">+ New analysis</button>
                </div>
                <div id="dashboard-recent">
                    <div class="empty-state">No analyses yet. Start from Product Analysis.</div>
                </div>
            </div>
            <div class="card">
                <div class="card-header">
                    <div class="card-title">Pricing alerts</div>
                    <span id="alert-summary" style="font-size:0.78em;color:#475569"></span>
                </div>
                <div id="dashboard-alerts">
                    <div class="empty-state">No alerts yet.</div>
                </div>
            </div>
        </div>
    </div>

    <!-- ANALYZE PAGE -->
    <div class="page" id="page-analyze">
        <div class="grid-2">
            <div class="card">
                <div class="card-header">
                    <div class="card-title">Product Intelligence</div>
                </div>
                <div class="form-group">
                    <label class="form-label">Product Name</label>
                    <input type="text" id="product_name" placeholder="e.g. Sony Headphones" />
                </div>
                <div class="form-group">
                    <label class="form-label">Your Price ($)</label>
                    <input type="number" id="your_price" placeholder="0.00" step="0.01" />
                </div>
                <div class="form-group">
                    <label class="form-label">Competitor Price ($)</label>
                    <input type="number" id="comp_price" placeholder="0.00" step="0.01" />
                    <button class="btn btn-success btn-sm" onclick="autoFetchPrice()" style="margin-top:6px">🔍 Auto Fetch from Database</button>
                    <div class="fetch-status" id="fetch_status"></div>
                    <div class="comp-selector" id="comp_selector">
                        <p>Select competitor to compare against:</p>
                        <div id="comp_buttons"></div>
                    </div>
                </div>
                <div class="form-group">
                    <label class="form-label">Customer Review</label>
                    <textarea id="review" placeholder="Paste a customer review here..."></textarea>
                </div>
                <button class="btn btn-primary btn-full" onclick="analyzeProduct()">Run Intelligence Analysis →</button>
                <div class="result-box" id="analyze_result"></div>
            </div>

            <div class="card">
                <div class="card-header">
                    <div class="card-title">How it works</div>
                </div>
                <div style="space-y:12px">
                    <div style="display:flex;gap:12px;margin-bottom:16px;padding:12px;background:#060d1a;border-radius:8px;border:1px solid #1e293b">
                        <div style="width:28px;height:28px;border-radius:50%;background:#1e3a5f;color:#60a5fa;display:flex;align-items:center;justify-content:center;font-size:0.8em;font-weight:700;flex-shrink:0">1</div>
                        <div><div style="font-size:0.84em;font-weight:600;color:#94a3b8;margin-bottom:2px">NLP Sentiment Analysis</div><div style="font-size:0.78em;color:#475569">TextBlob scores the review from -1 (negative) to +1 (positive)</div></div>
                    </div>
                    <div style="display:flex;gap:12px;margin-bottom:16px;padding:12px;background:#060d1a;border-radius:8px;border:1px solid #1e293b">
                        <div style="width:28px;height:28px;border-radius:50%;background:#1e3a5f;color:#60a5fa;display:flex;align-items:center;justify-content:center;font-size:0.8em;font-weight:700;flex-shrink:0">2</div>
                        <div><div style="font-size:0.84em;font-weight:600;color:#94a3b8;margin-bottom:2px">Pricing Intelligence</div><div style="font-size:0.78em;color:#475569">Compares your price against competitor and calculates market position</div></div>
                    </div>
                    <div style="display:flex;gap:12px;margin-bottom:16px;padding:12px;background:#060d1a;border-radius:8px;border:1px solid #1e293b">
                        <div style="width:28px;height:28px;border-radius:50%;background:#1e3a5f;color:#60a5fa;display:flex;align-items:center;justify-content:center;font-size:0.8em;font-weight:700;flex-shrink:0">3</div>
                        <div><div style="font-size:0.84em;font-weight:600;color:#94a3b8;margin-bottom:2px">AI Scoring</div><div style="font-size:0.78em;color:#475569">Combines sentiment + pricing into an overall product intelligence score out of 10</div></div>
                    </div>
                    <div style="display:flex;gap:12px;padding:12px;background:#060d1a;border-radius:8px;border:1px solid #1e293b">
                        <div style="width:28px;height:28px;border-radius:50%;background:#1e3a5f;color:#60a5fa;display:flex;align-items:center;justify-content:center;font-size:0.8em;font-weight:700;flex-shrink:0">4</div>
                        <div><div style="font-size:0.84em;font-weight:600;color:#94a3b8;margin-bottom:2px">Actionable Recommendation</div><div style="font-size:0.78em;color:#475569">Platform generates a business recommendation based on combined signals</div></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- COMPARE PAGE -->
    <div class="page" id="page-compare">
        <div class="grid-2">
            <div class="card">
                <div class="card-header"><div class="card-title">Market Comparison</div></div>
                <div class="form-group">
                    <label class="form-label">Product Name</label>
                    <input type="text" id="comp_product" placeholder="e.g. Samsung Phone" />
                </div>
                <div class="form-group">
                    <label class="form-label">Your Price ($)</label>
                    <input type="number" id="comp_your_price" placeholder="0.00" step="0.01" />
                </div>
                <div class="form-group">
                    <label class="form-label">Competitor 1</label>
                    <input type="text" id="comp1_name" placeholder="Name" style="margin-bottom:6px" />
                    <input type="number" id="comp1_price" placeholder="Price ($)" step="0.01" />
                </div>
                <div class="form-group">
                    <label class="form-label">Competitor 2</label>
                    <input type="text" id="comp2_name" placeholder="Name" style="margin-bottom:6px" />
                    <input type="number" id="comp2_price" placeholder="Price ($)" step="0.01" />
                </div>
                <div class="form-group">
                    <label class="form-label">Competitor 3 (optional)</label>
                    <input type="text" id="comp3_name" placeholder="Name" style="margin-bottom:6px" />
                    <input type="number" id="comp3_price" placeholder="Price ($)" step="0.01" />
                </div>
                <button class="btn btn-primary btn-full" onclick="compareCompetitors()">Compare Market →</button>
                <div class="result-box" id="compare_result"></div>
            </div>
            <div class="card">
                <div class="card-header"><div class="card-title">Market positioning guide</div></div>
                <div style="font-size:0.84em;color:#64748b;line-height:1.8">
                    <div style="margin-bottom:12px;padding:10px;background:#060d1a;border-radius:8px;border-left:3px solid #4ade80">
                        <strong style="color:#4ade80">#1 — Market Leader</strong><br>You are the cheapest. Strong competitive position. Consider maintaining price or slight increase.
                    </div>
                    <div style="margin-bottom:12px;padding:10px;background:#060d1a;border-radius:8px;border-left:3px solid #60a5fa">
                        <strong style="color:#60a5fa">Top 50% — Competitive</strong><br>You are in a good position. Monitor competitors for price changes.
                    </div>
                    <div style="margin-bottom:12px;padding:10px;background:#060d1a;border-radius:8px;border-left:3px solid #fb923c">
                        <strong style="color:#fb923c">Bottom 50% — At Risk</strong><br>Consider reducing price or improving product value proposition.
                    </div>
                    <div style="padding:10px;background:#060d1a;border-radius:8px;border-left:3px solid #f87171">
                        <strong style="color:#f87171">Last — Critical</strong><br>Immediate action needed. Significant price reduction or product differentiation required.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- TRENDS PAGE -->
    <div class="page" id="page-trends">
        <div class="card">
            <div class="card-header"><div class="card-title">Price Trend Analysis</div></div>
            <div class="trend-row">
                <input type="text" id="trend_product" placeholder="Enter product name to see price trend over time..." />
                <button class="btn btn-primary" onclick="loadTrend()">Show Trend →</button>
            </div>
            <canvas id="trendChart" style="max-height:320px"></canvas>
            <p id="trend_message" style="color:#334155;text-align:center;font-size:0.84em;margin-top:12px"></p>
        </div>
        <div class="card">
            <div class="card-header"><div class="card-title">How to build trend data</div></div>
            <p style="font-size:0.84em;color:#475569;line-height:1.7">Analyze the same product multiple times over different days with updated prices. Each analysis automatically saves a price history record. The trend chart shows how both your price and competitor prices change over time — helping you spot pricing patterns and opportunities.</p>
        </div>
    </div>

    <!-- SEGMENTATION PAGE -->
    <div class="page" id="page-segmentation">
        <div class="card">
            <div class="card-header"><div class="card-title">Customer Segmentation</div><span class="badge badge-info">Coming in Week 2</span></div>
            <div style="text-align:center;padding:48px 20px">
                <div style="font-size:2em;margin-bottom:12px">◉</div>
                <div style="font-size:0.95em;font-weight:600;color:#94a3b8;margin-bottom:8px">K-Means Clustering Engine</div>
                <div style="font-size:0.84em;color:#475569;max-width:400px;margin:0 auto;line-height:1.7">This module will segment your customers into behavior clusters using K-Means machine learning — identifying high-value, price-sensitive, and at-risk customer groups automatically.</div>
                <div style="margin-top:20px;display:inline-flex;gap:8px;flex-wrap:wrap;justify-content:center">
                    <span class="badge badge-info">K-Means ML</span>
                    <span class="badge badge-info">Behavioral clustering</span>
                    <span class="badge badge-info">Segment profiles</span>
                    <span class="badge badge-info">Python scikit-learn</span>
                </div>
            </div>
        </div>
    </div>

    <!-- FORECASTING PAGE -->
    <div class="page" id="page-forecasting">
        <div class="card">
            <div class="card-header"><div class="card-title">Sales Forecasting</div><span class="badge badge-info">Coming in Week 3</span></div>
            <div style="text-align:center;padding:48px 20px">
                <div style="font-size:2em;margin-bottom:12px">∿</div>
                <div style="font-size:0.95em;font-weight:600;color:#94a3b8;margin-bottom:8px">Time-Series Regression Engine</div>
                <div style="font-size:0.84em;color:#475569;max-width:400px;margin:0 auto;line-height:1.7">This module will forecast future sales trends using time-series regression — helping you predict demand, optimize inventory, and plan pricing strategy weeks ahead.</div>
                <div style="margin-top:20px;display:inline-flex;gap:8px;flex-wrap:wrap;justify-content:center">
                    <span class="badge badge-info">Time-series regression</span>
                    <span class="badge badge-info">Demand forecasting</span>
                    <span class="badge badge-info">Trend prediction</span>
                    <span class="badge badge-info">30/60/90 day outlook</span>
                </div>
            </div>
        </div>
    </div>

    <!-- RECOMMENDATIONS PAGE -->
    <div class="page" id="page-recommendations">
        <div class="card">
            <div class="card-header"><div class="card-title">Recommendation Engine</div><span class="badge badge-info">Coming in Week 3</span></div>
            <div style="text-align:center;padding:48px 20px">
                <div style="font-size:2em;margin-bottom:12px">✦</div>
                <div style="font-size:0.95em;font-weight:600;color:#94a3b8;margin-bottom:8px">Collaborative Filtering Engine</div>
                <div style="font-size:0.84em;color:#475569;max-width:400px;margin:0 auto;line-height:1.7">This module will generate personalized product recommendations using collaborative filtering — the same technique used by Amazon and Netflix to suggest products customers are most likely to buy.</div>
                <div style="margin-top:20px;display:inline-flex;gap:8px;flex-wrap:wrap;justify-content:center">
                    <span class="badge badge-info">Collaborative filtering</span>
                    <span class="badge badge-info">SVD algorithm</span>
                    <span class="badge badge-info">Personalization</span>
                    <span class="badge badge-info">Surprise library</span>
                </div>
            </div>
        </div>
    </div>

    <!-- HISTORY PAGE -->
    <div class="page" id="page-history">
        <div class="card">
            <div class="card-header">
                <div class="card-title">Analysis History</div>
                <button onclick="loadHistory()" style="background:#1e3a5f;color:#60a5fa;border:none;cursor:pointer;border-radius:6px;padding:5px 12px;font-size:0.78em">↻ Refresh</button>
            </div>
            <div id="history_table"><div class="empty-state">Loading...</div></div>
        </div>
    </div>

    <!-- ALERTS PAGE -->
    <div class="page" id="page-alerts">
        <div class="card">
            <div class="card-header"><div class="card-title">Pricing & Sentiment Alerts</div></div>
            <div id="alerts_content"><div class="empty-state">Loading alerts...</div></div>
        </div>
    </div>

</div>

<script>
    const pageTitles = {
        dashboard: ['Intelligence Dashboard', 'Overview of your e-commerce intelligence signals'],
        analyze: ['Product Analysis', 'Run AI-powered sentiment and pricing intelligence'],
        compare: ['Price Monitor', 'Compare your pricing against competitors in the market'],
        trends: ['Trend Analysis', 'Track how prices change over time for any product'],
        segmentation: ['Customer Segmentation', 'K-Means clustering — coming in Week 2'],
        forecasting: ['Sales Forecasting', 'Time-series regression — coming in Week 3'],
        recommendations: ['Recommendation Engine', 'Collaborative filtering — coming in Week 3'],
        history: ['Analysis History', 'All product analyses saved to your database'],
        alerts: ['Alerts', 'Pricing opportunities and sentiment warnings']
    };

    function showPage(name) {
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        document.getElementById('page-' + name).classList.add('active');
        document.querySelector(`[onclick="showPage('${name}')"]`).classList.add('active');
        const [title, sub] = pageTitles[name];
        document.getElementById('page-title').textContent = title;
        document.getElementById('page-sub').textContent = sub;
        if (name === 'history') loadHistory();
        if (name === 'alerts') loadAlerts();
        if (name === 'dashboard') loadDashboard();
    }

    async function loadDashboard() {
        try {
            const res = await fetch('/history');
            const records = await res.json();
            document.getElementById('m-products').textContent = records.length;
            if (records.length > 0) {
                const avg = records.reduce((s, r) => s + r.sentiment_score, 0) / records.length;
                document.getElementById('m-sentiment').textContent = avg.toFixed(2);
                const pos = records.filter(r => r.sentiment === 'Positive').length;
                const neg = records.filter(r => r.sentiment === 'Negative').length;
                document.getElementById('m-positive').textContent = pos;
                document.getElementById('m-positive-pct').textContent = Math.round(pos/records.length*100) + '% of products';
                document.getElementById('m-atrisk').textContent = neg;
                document.getElementById('m-atrisk-pct').textContent = Math.round(neg/records.length*100) + '% of products';

                // Recent analyses
                const recent = records.slice(0, 4);
                document.getElementById('dashboard-recent').innerHTML = `
                    <table class="data-table">
                        <thead><tr><th>Product</th><th>Sentiment</th><th>Score</th><th>Date</th></tr></thead>
                        <tbody>${recent.map(r => `
                            <tr>
                                <td style="font-weight:500;color:#e2e8f0">${r.product_name}</td>
                                <td><span class="badge ${r.sentiment==='Positive'?'badge-positive':r.sentiment==='Negative'?'badge-negative':'badge-neutral'}">${r.sentiment}</span></td>
                                <td style="color:#60a5fa">${r.sentiment_score}</td>
                                <td style="color:#475569">${new Date(r.created_at).toLocaleDateString()}</td>
                            </tr>`).join('')}
                        </tbody>
                    </table>`;

                // Alerts
                const alerts = [];
                records.forEach(r => {
                    if (r.sentiment === 'Negative' && r.your_price > r.competitor_price) {
                        alerts.push({type:'urgent', title: r.product_name + ' — At risk', sub: 'Negative reviews and overpriced vs competitor'});
                    } else if (r.sentiment === 'Positive' && r.your_price < r.competitor_price) {
                        alerts.push({type:'success', title: r.product_name + ' — Opportunity', sub: 'Strong reviews and competitive price — consider raising slightly'});
                    } else if (r.sentiment === 'Negative') {
                        alerts.push({type:'warning', title: r.product_name + ' — Review alert', sub: 'Negative sentiment detected — review product quality'});
                    }
                });
                document.getElementById('alert-count').textContent = alerts.length;
                document.getElementById('alert-summary').textContent = alerts.length + ' active alerts';
                if (alerts.length > 0) {
                    document.getElementById('dashboard-alerts').innerHTML = alerts.slice(0,3).map(a => `
                        <div class="alert-item alert-${a.type}">
                            <div class="alert-dot" style="background:${a.type==='urgent'?'#f87171':a.type==='success'?'#4ade80':'#fb923c'}"></div>
                            <div><div class="alert-title" style="color:${a.type==='urgent'?'#f87171':a.type==='success'?'#4ade80':'#fb923c'}">${a.title}</div><div class="alert-sub">${a.sub}</div></div>
                        </div>`).join('');
                } else {
                    document.getElementById('dashboard-alerts').innerHTML = '<div class="empty-state">No alerts — all products healthy!</div>';
                }
            }
        } catch(e) { console.log(e); }
    }

    async function autoFetchPrice() {
        const productName = document.getElementById('product_name').value;
        if (!productName) {
            document.getElementById('fetch_status').textContent = 'Enter a product name first.';
            document.getElementById('fetch_status').style.color = '#fb923c';
            return;
        }
        document.getElementById('fetch_status').textContent = 'Searching price database...';
        document.getElementById('fetch_status').style.color = '#94a3b8';
        document.getElementById('comp_selector').style.display = 'none';
        try {
            const res = await fetch(`/fetch-price/${encodeURIComponent(productName)}`);
            const data = await res.json();
            if (data.status === 'found' && data.suggested_price) {
                document.getElementById('comp_price').value = data.suggested_price;
                document.getElementById('fetch_status').textContent = `✓ ${data.competitor_name}: $${data.suggested_price} — select another competitor below`;
                document.getElementById('fetch_status').style.color = '#4ade80';
                if (data.all_competitors) {
                    const buttonsDiv = document.getElementById('comp_buttons');
                    buttonsDiv.innerHTML = '';
                    Object.entries(data.all_competitors).forEach(([name, price]) => {
                        const btn = document.createElement('span');
                        btn.className = 'comp-btn' + (name === data.competitor_name ? ' selected' : '');
                        btn.textContent = `${name}  $${price}`;
                        btn.onclick = () => {
                            document.getElementById('comp_price').value = price;
                            document.getElementById('fetch_status').textContent = `✓ Comparing against ${name}: $${price}`;
                            document.querySelectorAll('.comp-btn').forEach(b => b.classList.remove('selected'));
                            btn.classList.add('selected');
                        };
                        buttonsDiv.appendChild(btn);
                    });
                    document.getElementById('comp_selector').style.display = 'block';
                }
            } else {
                document.getElementById('fetch_status').textContent = 'Not in database. Enter price manually.';
                document.getElementById('fetch_status').style.color = '#fb923c';
            }
        } catch(e) {
            document.getElementById('fetch_status').textContent = 'Error. Enter price manually.';
            document.getElementById('fetch_status').style.color = '#f87171';
        }
    }

    async function analyzeProduct() {
        const productName = document.getElementById('product_name').value;
        const price = parseFloat(document.getElementById('your_price').value);
        const compPrice = parseFloat(document.getElementById('comp_price').value);
        const review = document.getElementById('review').value;
        if (!productName || !price || !compPrice || !review) { alert('Please fill in all fields.'); return; }

        const res = await fetch('/analyze', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ product_name: productName, price, competitor_price: compPrice, review })
        });
        const result = await res.json();
        const badgeClass = result.sentiment==='Positive'?'badge-positive':result.sentiment==='Negative'?'badge-negative':'badge-neutral';

        let scoreHtml = '';
        try {
            const scoreRes = await fetch(`/score/${encodeURIComponent(productName)}`);
            const sd = await scoreRes.json();
            if (sd.score !== undefined) {
                scoreHtml = `<div class="score-display">
                    <div class="score-num" style="color:${sd.color}">${sd.score}</div>
                    <div class="score-lbl" style="color:${sd.color}">${sd.label}</div>
                    <div class="score-sub">Intelligence Score / 10</div>
                </div>`;
            }
        } catch(e) {}

        const div = document.getElementById('analyze_result');
        div.style.display = 'block';
        div.innerHTML = `
            <span class="badge ${badgeClass}">${result.sentiment}</span>
            ${scoreHtml}
            <div class="stat-row"><span class="stat-lbl">Sentiment Score</span><span class="stat-val">${result.sentiment_score}</span></div>
            <div class="stat-row"><span class="stat-lbl">Pricing</span><span class="stat-val">${result.pricing_insight}</span></div>
            <div class="stat-row"><span class="stat-lbl">Recommendation</span><span class="stat-val">${result.recommendation}</span></div>`;

        loadDashboard();
    }

    async function compareCompetitors() {
        const competitors = {};
        ['1','2','3'].forEach(n => {
            const name = document.getElementById('comp'+n+'_name').value;
            const price = document.getElementById('comp'+n+'_price').value;
            if (name && price) competitors[name] = parseFloat(price);
        });
        const data = {
            product_name: document.getElementById('comp_product').value,
            your_price: parseFloat(document.getElementById('comp_your_price').value),
            competitors
        };
        const res = await fetch('/compare', { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(data) });
        const result = await res.json();
        const div = document.getElementById('compare_result');
        div.style.display = 'block';
        div.innerHTML = `
            <div class="stat-row"><span class="stat-lbl">Market Ranking</span><span class="stat-val">${result.market_ranking}</span></div>
            <div class="stat-row" style="margin-bottom:10px"><span class="stat-lbl">Insight</span><span class="stat-val">${result.insight}</span></div>
            ${result.full_ranking.map(item => `
                <div class="rank-item ${item.name==='Your Product'?'rank-you':''}">
                    <span><span class="rank-num">#${item.rank}</span>${item.name}</span>
                    <span style="font-weight:600">$${item.price}</span>
                </div>`).join('')}`;
    }

    let trendChartInstance = null;
    async function loadTrend() {
        const productName = document.getElementById('trend_product').value;
        if (!productName) return;
        const res = await fetch(`/trend/${encodeURIComponent(productName)}`);
        const records = await res.json();
        if (records.length === 0) {
            document.getElementById('trend_message').textContent = 'No trend data yet. Analyze this product multiple times to build trend history.';
            return;
        }
        document.getElementById('trend_message').textContent = '';
        if (trendChartInstance) trendChartInstance.destroy();
        const ctx = document.getElementById('trendChart').getContext('2d');
        trendChartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: records.map(r => new Date(r.date).toLocaleDateString()),
                datasets: [
                    { label: 'Your Price', data: records.map(r => r.your_price), borderColor: '#3b82f6', backgroundColor: 'rgba(59,130,246,0.06)', tension: 0.4, fill: true, pointBackgroundColor: '#3b82f6', pointRadius: 4 },
                    { label: 'Competitor Price', data: records.map(r => r.competitor_price), borderColor: '#f87171', backgroundColor: 'rgba(248,113,113,0.06)', tension: 0.4, fill: true, pointBackgroundColor: '#f87171', pointRadius: 4 }
                ]
            },
            options: {
                responsive: true,
                plugins: { legend: { labels: { color: '#64748b', usePointStyle: true } } },
                scales: {
                    x: { ticks: { color: '#475569' }, grid: { color: '#0f172a' } },
                    y: { ticks: { color: '#475569' }, grid: { color: '#0f172a' } }
                }
            }
        });
    }

    async function loadHistory() {
        const res = await fetch('/history');
        const records = await res.json();
        if (records.length === 0) {
            document.getElementById('history_table').innerHTML = '<div class="empty-state">No analyses yet.</div>';
            return;
        }
        document.getElementById('history_table').innerHTML = `
            <table class="data-table" style="table-layout:fixed">
                <thead><tr>
                    <th style="width:16%">Product</th>
                    <th style="width:9%">Your Price</th>
                    <th style="width:9%">Comp Price</th>
                    <th style="width:10%">Sentiment</th>
                    <th style="width:7%">Score</th>
                    <th style="width:22%">Pricing Insight</th>
                    <th style="width:19%">Recommendation</th>
                    <th style="width:8%">Date</th>
                </tr></thead>
                <tbody>${records.map(r => `<tr>
                    <td style="font-weight:500;color:#e2e8f0;word-wrap:break-word">${r.product_name}</td>
                    <td>$${r.your_price}</td>
                    <td>$${r.competitor_price}</td>
                    <td><span class="badge ${r.sentiment==='Positive'?'badge-positive':r.sentiment==='Negative'?'badge-negative':'badge-neutral'}">${r.sentiment}</span></td>
                    <td style="color:#60a5fa">${r.sentiment_score}</td>
                    <td style="word-wrap:break-word">${r.pricing_insight}</td>
                    <td style="word-wrap:break-word">${r.recommendation}</td>
                    <td style="color:#475569">${new Date(r.created_at).toLocaleDateString()}</td>
                </tr>`).join('')}</tbody>
            </table>`;
    }

    async function loadAlerts() {
        const res = await fetch('/history');
        const records = await res.json();
        const alerts = [];
        records.forEach(r => {
            if (r.sentiment === 'Negative' && r.your_price > r.competitor_price) {
                alerts.push({type:'urgent', title: r.product_name + ' — Critical: At risk', sub: 'Negative reviews AND overpriced vs competitor. Immediate action needed.'});
            } else if (r.sentiment === 'Positive' && r.your_price < r.competitor_price) {
                alerts.push({type:'success', title: r.product_name + ' — Opportunity detected', sub: 'Strong reviews and competitive price. Consider a slight price increase.'});
            } else if (r.sentiment === 'Negative') {
                alerts.push({type:'warning', title: r.product_name + ' — Sentiment warning', sub: 'Negative customer sentiment detected. Review product quality and marketing.'});
            }
        });
        document.getElementById('alert-count').textContent = alerts.length;
        document.getElementById('alerts_content').innerHTML = alerts.length === 0
            ? '<div class="empty-state">No alerts — all products are healthy!</div>'
            : alerts.map(a => `
                <div class="alert-item alert-${a.type}">
                    <div class="alert-dot" style="background:${a.type==='urgent'?'#f87171':a.type==='success'?'#4ade80':'#fb923c'}"></div>
                    <div><div class="alert-title" style="color:${a.type==='urgent'?'#f87171':a.type==='success'?'#4ade80':'#fb923c'}">${a.title}</div><div class="alert-sub">${a.sub}</div></div>
                </div>`).join('');
    }

    window.onload = loadDashboard;
</script>
</body>
</html>
"""