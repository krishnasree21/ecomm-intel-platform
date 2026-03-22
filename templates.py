html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>E-Commerce Intelligence Platform</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: white;
            margin: 0;
            padding: 20px;
        }
        .header {
            text-align: center;
            padding: 40px;
            background: linear-gradient(135deg, #1e3a5f, #2e6da4);
            border-radius: 12px;
            margin-bottom: 30px;
        }
        h1 { font-size: 2.5em; margin: 0; }
        .subtitle { color: #94a3b8; margin-top: 10px; }
        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            background: #1e293b;
            border-radius: 12px;
            padding: 25px;
            border: 1px solid #334155;
        }
        .card h2 { color: #3b82f6; margin-top: 0; }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 6px;
            color: white;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #2e6da4;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1em;
            margin-top: 10px;
        }
        button:hover { background: #1e3a5f; }
        .result {
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 6px;
            padding: 15px;
            margin-top: 15px;
            display: none;
        }
        .badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .badge-positive { background: #166534; color: #22c55e; }
        .badge-negative { background: #7f1d1d; color: #ef4444; }
        .badge-neutral { background: #78350f; color: #f59e0b; }
        .stat { margin: 8px 0; font-size: 0.95em; color: #94a3b8; }
        .stat span { color: white; font-weight: bold; }
        .rank-item {
            display: flex;
            justify-content: space-between;
            padding: 8px;
            border-radius: 4px;
            margin: 4px 0;
            background: #1e293b;
        }
        .rank-you { border-left: 3px solid #3b82f6; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🛒 E-Commerce Intelligence Platform</h1>
        <p class="subtitle">AI-powered pricing & sentiment analysis for smarter business decisions</p>
    </div>

    <div class="cards">
        <div class="card">
            <h2>📊 Product Intelligence</h2>
            <input type="text" id="product_name" placeholder="Product Name" />
            <input type="number" id="your_price" placeholder="Your Price ($)" step="0.01" />
            <input type="number" id="comp_price" placeholder="Competitor Price ($)" step="0.01" />
            <button onclick="autoFetchPrice()" style="background:#166534; margin-top:5px">
                🔍 Auto Fetch Competitor Price
            </button>
            <p id="fetch_status" style="color:#94a3b8; font-size:0.85em; margin:5px 0"></p>
            <textarea id="review" rows="3" placeholder="Paste a customer review here..."></textarea>
            <button onclick="analyzeProduct()">Analyze Product</button>
            <div class="result" id="analyze_result"></div>
        </div>

        <div class="card">
            <h2>🏆 Competitor Comparison</h2>
            <input type="text" id="comp_product" placeholder="Product Name" />
            <input type="number" id="comp_your_price" placeholder="Your Price ($)" step="0.01" />
            <input type="text" id="comp1_name" placeholder="Competitor 1 Name" />
            <input type="number" id="comp1_price" placeholder="Competitor 1 Price ($)" step="0.01" />
            <input type="text" id="comp2_name" placeholder="Competitor 2 Name" />
            <input type="number" id="comp2_price" placeholder="Competitor 2 Price ($)" step="0.01" />
            <input type="text" id="comp3_name" placeholder="Competitor 3 Name (optional)" />
            <input type="number" id="comp3_price" placeholder="Competitor 3 Price ($) (optional)" step="0.01" />
            <button onclick="compareCompetitors()">Compare Market</button>
            <div class="result" id="compare_result"></div>
        </div>
    </div>

    <script>
        async function analyzeProduct() {
            const data = {
                product_name: document.getElementById('product_name').value,
                price: parseFloat(document.getElementById('your_price').value),
                competitor_price: parseFloat(document.getElementById('comp_price').value),
                review: document.getElementById('review').value
            };
            const res = await fetch('/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            const result = await res.json();
            const badgeClass = result.sentiment === 'Positive' ? 'badge-positive' :
                               result.sentiment === 'Negative' ? 'badge-negative' : 'badge-neutral';

            // Get product score safely
            let scoreHtml = '';
            try {
                const scoreRes = await fetch(`/score/${encodeURIComponent(data.product_name)}`);
                const scoreData = await scoreRes.json();
                if (scoreData.score !== undefined) {
                    scoreHtml = `
                        <div style="text-align:center; margin:15px 0">
                            <div style="font-size:3em; font-weight:bold; color:${scoreData.color}">${scoreData.score}</div>
                            <div style="color:${scoreData.color}; font-weight:bold">${scoreData.label}</div>
                            <div style="color:#94a3b8; font-size:0.85em">Overall Product Score / 10</div>
                        </div>`;
                }
            } catch(e) { console.log('Score fetch failed:', e); }

            const div = document.getElementById('analyze_result');
            div.style.display = 'block';
            div.innerHTML = `
                <span class="badge ${badgeClass}">${result.sentiment}</span>
                ${scoreHtml}
                <div class="stat">Sentiment Score: <span>${result.sentiment_score}</span></div>
                <div class="stat">Pricing: <span>${result.pricing_insight}</span></div>
                <div class="stat">Recommendation: <span>${result.recommendation}</span></div>
            `;
        }

        async function autoFetchPrice() {
            const productName = document.getElementById('product_name').value;
            if (!productName) {
                document.getElementById('fetch_status').textContent = 'Please enter a product name first.';
                return;
            }
            
            document.getElementById('fetch_status').textContent = '🔍 Searching for price...';
            
            try {
                const res = await fetch(`/fetch-price/${encodeURIComponent(productName)}`);
                const data = await res.json();
                
                if (data.status === 'found' && data.suggested_price) {
                    document.getElementById('comp_price').value = data.suggested_price;
                    document.getElementById('fetch_status').textContent = 
                        `✅ Price found: $${data.suggested_price} (from ${data.source})`;
                    document.getElementById('fetch_status').style.color = '#22c55e';
                } else {
                    document.getElementById('fetch_status').textContent = 
                        '⚠️ Could not find price automatically. Please enter manually.';
                    document.getElementById('fetch_status').style.color = '#f59e0b';
                }
            } catch(e) {
                document.getElementById('fetch_status').textContent = 
                    '❌ Search failed. Please enter price manually.';
                document.getElementById('fetch_status').style.color = '#ef4444';
            }
        }


        async function compareCompetitors() {
            const competitors = {};
            if (document.getElementById('comp1_name').value)
                competitors[document.getElementById('comp1_name').value] = parseFloat(document.getElementById('comp1_price').value);
            if (document.getElementById('comp2_name').value)
                competitors[document.getElementById('comp2_name').value] = parseFloat(document.getElementById('comp2_price').value);
            if (document.getElementById('comp3_name').value && document.getElementById('comp3_price').value)
                competitors[document.getElementById('comp3_name').value] = parseFloat(document.getElementById('comp3_price').value);

            const data = {
                product_name: document.getElementById('comp_product').value,
                your_price: parseFloat(document.getElementById('comp_your_price').value),
                competitors: competitors
            };
            const res = await fetch('/compare', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            const result = await res.json();
            const rankingHtml = result.full_ranking.map(item => `
                <div class="rank-item ${item.name === 'Your Product' ? 'rank-you' : ''}">
                    <span>#${item.rank} ${item.name}</span>
                    <span>$${item.price}</span>
                </div>
            `).join('');
            const div = document.getElementById('compare_result');
            div.style.display = 'block';
            div.innerHTML = `
                <div class="stat">Market Ranking: <span>${result.market_ranking}</span></div>
                <div class="stat">Insight: <span>${result.insight}</span></div>
                <div style="margin-top:10px">${rankingHtml}</div>
            `;
        }

        let trendChartInstance = null;

        async function loadTrend() {
            const productName = document.getElementById('trend_product').value;
            if (!productName) return;

            const res = await fetch(`/trend/${encodeURIComponent(productName)}`);
            const records = await res.json();

            if (records.length === 0) {
                document.getElementById('trend_message').textContent =
                    'No trend data found. Analyze this product multiple times to see trends.';
                return;
            }

            document.getElementById('trend_message').textContent = '';
            const labels = records.map(r => new Date(r.date).toLocaleDateString());
            const yourPrices = records.map(r => r.your_price);
            const compPrices = records.map(r => r.competitor_price);

            if (trendChartInstance) trendChartInstance.destroy();

            const ctx = document.getElementById('trendChart').getContext('2d');
            trendChartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Your Price',
                            data: yourPrices,
                            borderColor: '#3b82f6',
                            backgroundColor: 'rgba(59,130,246,0.1)',
                            tension: 0.4,
                            fill: true
                        },
                        {
                            label: 'Competitor Price',
                            data: compPrices,
                            borderColor: '#ef4444',
                            backgroundColor: 'rgba(239,68,68,0.1)',
                            tension: 0.4,
                            fill: true
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { labels: { color: '#94a3b8' } }
                    },
                    scales: {
                        x: { ticks: { color: '#94a3b8' }, grid: { color: '#334155' } },
                        y: { ticks: { color: '#94a3b8' }, grid: { color: '#334155' } }
                    }
                }
            });
        }

        async function loadHistory() {
            const res = await fetch('/history');
            const records = await res.json();

            if (records.length === 0) {
                document.getElementById('history_table').innerHTML =
                    '<p style="color:#94a3b8; text-align:center">No analyses saved yet.</p>';
                return;
            }

            const rows = records.map(r => `
                <tr style="border-bottom:1px solid #334155">
                    <td style="padding:10px; word-wrap:break-word">${r.product_name}</td>
                    <td style="padding:10px">$${r.your_price}</td>
                    <td style="padding:10px">$${r.competitor_price}</td>
                    <td style="padding:10px"><span class="badge ${r.sentiment === 'Positive' ? 'badge-positive' : r.sentiment === 'Negative' ? 'badge-negative' : 'badge-neutral'}">${r.sentiment}</span></td>
                    <td style="padding:10px">${r.sentiment_score}</td>
                    <td style="padding:10px; word-wrap:break-word">${r.pricing_insight}</td>
                    <td style="padding:10px; word-wrap:break-word">${r.recommendation}</td>
                    <td style="padding:10px">${new Date(r.created_at).toLocaleDateString()}</td>
                </tr>
            `).join('');

            document.getElementById('history_table').innerHTML = `
                <table style="width:100%; border-collapse:collapse; font-size:0.85em; table-layout:fixed">
                    <thead>
                        <tr style="background:#1e3a5f; color:white">
                            <th style="padding:10px; text-align:left; width:15%">Product</th>
                            <th style="padding:10px; text-align:left; width:10%">Your Price</th>
                            <th style="padding:10px; text-align:left; width:10%">Comp Price</th>
                            <th style="padding:10px; text-align:left; width:10%">Sentiment</th>
                            <th style="padding:10px; text-align:left; width:8%">Score</th>
                            <th style="padding:10px; text-align:left; width:22%">Pricing Insight</th>
                            <th style="padding:10px; text-align:left; width:17%">Recommendation</th>
                            <th style="padding:10px; text-align:left; width:8%">Date</th>
                        </tr>
                    </thead>
                    <tbody style="color:#cbd5e1; word-wrap:break-word">${rows}</tbody>
                </table>
            `;
        }

        window.onload = loadHistory;
    </script>

    <!-- Price Trend Chart -->
    <div style="margin-top:30px; background:#1e293b; border-radius:12px; padding:25px; border:1px solid #334155">
        <h2 style="color:#3b82f6; margin-top:0">📈 Price Trend Analysis</h2>
        <p style="color:#94a3b8; font-size:0.9em">Track how prices change over time for any product</p>
        <div style="display:flex; gap:10px; margin-bottom:20px">
            <input type="text" id="trend_product" placeholder="Enter product name to see trend"
                style="flex:1; padding:10px; background:#0f172a; border:1px solid #334155; border-radius:6px; color:white"/>
            <button onclick="loadTrend()"
                style="width:auto; padding:10px 20px; background:#2e6da4; color:white; border:none; border-radius:6px; cursor:pointer">
                Show Trend
            </button>
        </div>
        <canvas id="trendChart" style="max-height:300px"></canvas>
        <p id="trend_message" style="color:#94a3b8; text-align:center"></p>
    </div>

    <!-- History Section -->
    <div style="margin-top:30px; background:#1e293b; border-radius:12px; padding:25px; border:1px solid #334155">
        <h2 style="color:#3b82f6; margin-top:0">📋 Analysis History</h2>
        <p style="color:#94a3b8; font-size:0.9em">Every product you analyze gets saved here automatically</p>
        <div id="history_table">Loading...</div>
        <button onclick="loadHistory()" style="width:auto; padding:8px 20px; margin-top:15px; background:#1e3a5f">🔄 Refresh</button>
    </div>

</body>
</html>
"""