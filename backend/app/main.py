from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.routes import router

app = FastAPI(
    title="TruthLens API",
    description="AI Content Authenticity Detector powered by Telegraph Protocol",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

HTML_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TruthLens — AI Content Authenticity Detector</title>
<style>
:root{--bg:#0a0a0a;--bg2:#111;--card:#161616;--border:#222;--green:#00ff88;--green20:#00ff8820;--red:#ff4444;--yellow:#ffaa00;--text:#f0f0f0;--muted:#888;--dim:#555;--mono:'SF Mono','Fira Code',monospace}
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--green);text-decoration:none}
.container{max-width:1200px;margin:0 auto;padding:0 24px}
header{border-bottom:1px solid var(--border);padding:16px 0;position:sticky;top:0;z-index:100;background:rgba(10,10,10,.85);backdrop-filter:blur(12px)}
header .inner{display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:12px}
.logo-icon{font-size:28px;font-family:var(--mono);color:var(--green)}
.logo h1{font-size:18px;font-weight:700;letter-spacing:-.5px}
.logo p{font-size:11px;color:var(--dim);font-family:var(--mono)}
.nav-btns{display:flex;gap:8px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:8px;font-weight:600;font-size:14px;cursor:pointer;transition:all .2s;border:none;outline:none}
.btn-primary{background:var(--green);color:#000}
.btn-primary:hover{filter:brightness(.85);transform:translateY(-1px)}
.btn-primary:disabled{opacity:.5;cursor:not-allowed;transform:none}
.btn-ghost{background:transparent;color:var(--text);border:1px solid var(--border);font-size:12px;padding:8px 16px}
.btn-ghost:hover{border-color:var(--green);color:var(--green)}
section.hero{text-align:center;padding:40px 0 32px}
.hero h1{font-size:clamp(28px,5vw,52px);font-weight:800;letter-spacing:-2px;line-height:1.1;margin-bottom:16px}
.hero .accent{color:var(--green)}
.hero p{font-size:17px;color:var(--muted);max-width:600px;margin:0 auto}
.card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:24px;transition:border-color .2s}
.card:hover{border-color:var(--green20)}
.card h2{font-size:16px;font-weight:600;margin-bottom:16px}
.tabs{display:flex;gap:4px;background:var(--bg);border-radius:8px;padding:4px;border:1px solid var(--border);margin-bottom:16px}
.tab{padding:8px 16px;border-radius:6px;font-size:14px;font-weight:500;cursor:pointer;color:var(--muted);background:transparent;border:none}
.tab:hover{color:var(--text)}
.tab.active{background:var(--card);color:var(--green);box-shadow:0 1px 3px rgba(0,0,0,.3)}
textarea,.url-input{width:100%;min-height:120px;padding:16px;background:var(--bg);border:1px solid var(--border);border-radius:8px;color:var(--text);font-family:inherit;font-size:15px;resize:vertical;outline:none;transition:border-color .2s}
textarea:focus,.url-input:focus{border-color:var(--green)}
.url-input{min-height:auto}
textarea::placeholder,.url-input::placeholder{color:var(--dim)}
.detect-row{margin-top:16px;display:flex;align-items:center;gap:12px}
.char-count{font-size:12px;color:var(--dim)}
.badge{display:inline-flex;align-items:center;padding:4px 12px;border-radius:9999px;font-size:12px;font-weight:600;letter-spacing:.5px}
.badge-auth{background:#00ff8820;color:#00ff88;border:1px solid #00ff8840}
.badge-susp{background:#ffaa0020;color:#ffaa00;border:1px solid #ffaa0040}
.badge-fake{background:#ff444420;color:#ff4444;border:1px solid #ff444440}
.badge-verified{background:#00ff8820;color:#00ff88;border:1px solid #00ff8840;font-family:var(--mono)}
.result-box{margin-top:24px;padding:24px;background:var(--bg);border-radius:8px;border:1px solid var(--border);animation:fadeIn .4s ease}
.result-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;flex-wrap:wrap;gap:8px}
.score-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}
.score-label{font-size:13px;color:var(--muted)}
.score-value{font-size:24px;font-weight:700;font-family:var(--mono)}
.score-bar{width:100%;height:8px;background:var(--border);border-radius:4px;overflow:hidden;margin-bottom:16px}
.score-bar-fill{height:100%;border-radius:4px;transition:width .8s ease}
.details-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.detail-label{font-size:12px;color:var(--dim)}
.detail-value{font-size:14px;font-weight:600;margin-top:2px}
.raw-box{margin-top:16px;padding:12px;background:var(--card);border-radius:8px;font-size:13px;font-family:var(--mono)}
.raw-row{display:flex;justify-content:space-between;padding:4px 0}
.raw-key{color:var(--dim)}
.raw-val{color:var(--text)}
.error-box{margin-top:16px;padding:12px 16px;background:#ff444410;border:1px solid #ff444430;border-radius:8px;color:var(--red);font-size:14px}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.signal-item{padding:12px 16px;background:var(--bg);border-radius:8px;border:1px solid var(--border);display:flex;align-items:flex-start;justify-content:space-between;gap:12px}
.signal-text{font-size:13px;font-weight:500;margin-bottom:4px}
.signal-meta{display:flex;gap:8px;align-items:center}
.signal-cat{font-size:11px;font-family:var(--mono);font-weight:600}
.signal-src{font-size:11px;color:var(--dim)}
.signal-score{font-size:16px;font-weight:700;font-family:var(--mono);color:var(--green);white-space:nowrap}
.miner-item{padding:12px 16px;background:var(--bg);border-radius:8px;border:1px solid var(--border);display:flex;align-items:center;justify-content:space-between}
.miner-id{font-size:14px;font-weight:600;font-family:var(--mono)}
.miner-cap{font-size:14px;margin-left:8px}
.miner-price{font-size:13px;font-family:var(--mono);color:var(--green)}
.loading{text-align:center;padding:40px;color:var(--dim);animation:pulse 1.5s infinite}
.live-badge{margin-left:auto}
footer{margin-top:64px;text-align:center;color:var(--dim);font-size:13px;border-top:1px solid var(--border);padding-top:24px;margin-bottom:32px}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
@media(max-width:768px){.grid-2{grid-template-columns:1fr}.hero h1{font-size:28px}}
</style>
</head>
<body>
<header>
<div class="container inner">
<div class="logo">
<span class="logo-icon">&#x23AC;</span>
<div>
<h1>TruthLens</h1>
<p>POWERED BY TELEGRAPH PROTOCOL</p>
</div>
</div>
<div class="nav-btns">
<a href="https://hackathon.telegraphprotocol.com" target="_blank" class="btn btn-ghost">Telegraph Hackathon</a>
<a href="https://github.com/telegraph-protocol" target="_blank" class="btn btn-ghost">GitHub</a>
</div>
</div>
</header>

<main class="container" style="padding:32px 24px 64px">

<section class="hero">
<h1>Can you trust what you<br><span class="accent">see and read?</span></h1>
<p>TruthLens uses Telegraph Protocol's verified miners to detect AI-generated text, deepfakes, and misinformation. Every result is cryptographically verifiable.</p>
</section>

<div style="max-width:800px;margin:0 auto 48px">
<div class="card">
<h2>Content Detection</h2>
<div class="tabs">
<button class="tab active" onclick="switchTab('text',this)">&#x1F4DD; Text</button>
<button class="tab" onclick="switchTab('image_url',this)">&#x1F5BC;&#xFE0F; Image URL</button>
</div>
<div id="text-input">
<textarea id="content-input" placeholder="Paste text here to check for AI-generated content, spam, or misinformation..." oninput="updateCount()"></textarea>
</div>
<div id="url-input" style="display:none">
<input class="url-input" id="url-content" type="url" placeholder="Enter image URL to check for deepfakes or manipulation...">
</div>
<div class="detect-row">
<button class="btn btn-primary" id="detect-btn" onclick="detect()">&#x1F50D; Detect Authenticity</button>
<span class="char-count" id="char-count"></span>
</div>
<div id="error-box" class="error-box" style="display:none"></div>
<div id="result-box" class="result-box" style="display:none"></div>
</div>
</div>

<div class="grid-2">
<div class="card" id="signals-card">
<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px">
<div>
<h2>Live Signal Feed</h2>
<p style="font-size:12px;color:var(--dim)">Verified intelligence from Telegraph Daemon</p>
</div>
<span class="badge badge-verified live-badge">LIVE</span>
</div>
<div id="signals-list"><div class="loading">Loading signals...</div></div>
</div>

<div class="card">
<h2>Active Miners</h2>
<p style="font-size:12px;color:var(--dim);margin-bottom:16px">Detection capabilities powered by Telegraph miners</p>
<div id="miners-list"><div class="loading">Loading...</div></div>
</div>
</div>

<footer>
<p>TruthLens &mdash; Built for Telegraph Protocol Hackathon 2026</p>
<p style="margin-top:4px">Powered by <a href="https://telegraphprotocol.com" target="_blank">Telegraph Protocol</a> on Base</p>
</footer>
</main>

<script>
const API = window.location.origin + '/api/v1';
let currentTab = 'text';

function switchTab(tab, el) {
  currentTab = tab;
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  document.getElementById('text-input').style.display = tab === 'text' ? '' : 'none';
  document.getElementById('url-input').style.display = tab === 'image_url' ? '' : 'none';
  document.getElementById('error-box').style.display = 'none';
  document.getElementById('result-box').style.display = 'none';
}

function updateCount() {
  const v = document.getElementById('content-input').value;
  document.getElementById('char-count').textContent = v.length ? v.length + ' characters' : '';
}

function scoreColor(s) { return s >= .75 ? '#00ff88' : s >= .45 ? '#ffaa00' : '#ff4444'; }
function verdictBadge(v) {
  if (v === 'authentic') return '<span class="badge badge-auth">AUTHENTIC</span>';
  if (v === 'suspicious') return '<span class="badge badge-susp">SUSPICIOUS</span>';
  return '<span class="badge badge-fake">LIKELY FAKE</span>';
}

async function detect() {
  const content = currentTab === 'text' ? document.getElementById('content-input').value : document.getElementById('url-content').value;
  if (!content.trim()) return;
  const btn = document.getElementById('detect-btn');
  const errBox = document.getElementById('error-box');
  const resBox = document.getElementById('result-box');
  btn.disabled = true;
  btn.innerHTML = '<span style="animation:pulse 1.5s infinite">&#x23F3;</span> Analyzing via Telegraph...';
  errBox.style.display = 'none';
  resBox.style.display = 'none';
  try {
    const r = await fetch(API + '/detect', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({content_type: currentTab, content})
    });
    if (!r.ok) throw new Error('Detection failed');
    const d = await r.json();
    const raw = d.raw_response || {};
    resBox.innerHTML = `
      <div class="result-header">
        <div style="display:flex;align-items:center;gap:12px">
          ${verdictBadge(d.verdict)}
          ${d.telegraph_verified ? '<span class="badge badge-verified">TELEGRAPH VERIFIED</span>' : ''}
        </div>
        <span style="font-size:12px;color:var(--dim)">${new Date(d.timestamp).toLocaleTimeString()}</span>
      </div>
      <div class="score-row">
        <span class="score-label">Confidence Score</span>
        <span class="score-value" style="color:${scoreColor(d.confidence_score)}">${(d.confidence_score*100).toFixed(1)}%</span>
      </div>
      <div class="score-bar"><div class="score-bar-fill" style="width:${d.confidence_score*100}%;background:${scoreColor(d.confidence_score)}"></div></div>
      <div class="details-grid">
        <div><div class="detail-label">Miner</div><div class="detail-value">${d.miner_name} <span style="color:var(--dim)">#${d.miner_id}</span></div></div>
        <div><div class="detail-label">Content Type</div><div class="detail-value">${d.content_type}</div></div>
      </div>
      ${Object.keys(raw).length ? '<div class="raw-box">' + Object.entries(raw).map(([k,v]) => '<div class="raw-row"><span class="raw-key">'+k+':</span><span class="raw-val">'+v+'</span></div>').join('') + '</div>' : ''}
    `;
    resBox.style.display = '';
  } catch(e) {
    errBox.textContent = 'Detection failed. Is the backend connected to Telegraph?';
    errBox.style.display = '';
  }
  btn.disabled = false;
  btn.innerHTML = '&#x1F50D; Detect Authenticity';
}

const catColors = {CLIMATE:'#4488ff',FINANCE:'#00ff88',CRYPTO:'#ff8844',TECHNOLOGY:'#aa44ff',POLITICS:'#ff4444',SOCIAL:'#ff44ff'};

async function loadSignals() {
  try {
    const r = await fetch(API + '/signals/top?since_hours=6&limit=8');
    const d = await r.json();
    const list = document.getElementById('signals-list');
    const items = d.results || [];
    if (!items.length) { list.innerHTML = '<p style="color:var(--dim);text-align:center;padding:20px">No signals yet</p>'; return; }
    list.innerHTML = items.map(s => `
      <div class="signal-item" style="margin-bottom:8px">
        <div style="flex:1">
          <p class="signal-text">${(s.question?.text || '').substring(0,80)}${(s.question?.text||'').length>80?'...':''}</p>
          <div class="signal-meta">
            <span class="signal-cat" style="color:${catColors[s.question?.category]||'var(--muted)'}">${s.question?.category||''}</span>
            <span class="signal-src">via ${(s.routing?.subnet_name||'').split('-').pop()}</span>
          </div>
        </div>
        <span class="signal-score" style="color:${(s.question?.interest_score||0)>=7?'var(--green)':'var(--muted)'}">${(s.question?.interest_score||0).toFixed(1)}</span>
      </div>
    `).join('');
  } catch(e) {
    document.getElementById('signals-list').innerHTML = '<p style="color:var(--red);text-align:center;padding:20px">Failed to load signals</p>';
  }
}

async function loadMiners() {
  try {
    const r = await fetch(API + '/miners');
    const d = await r.json();
    const list = document.getElementById('miners-list');
    const miners = d.miners || [];
    if (!miners.length) { list.innerHTML = '<p style="color:var(--dim);text-align:center;padding:20px">No miners found</p>'; return; }
    list.innerHTML = miners.map(m => `
      <div class="miner-item" style="margin-bottom:8px">
        <div><span class="miner-id">#${m.id}</span><span class="miner-cap">${m.capability||''}</span></div>
        ${m.min_price != null ? '<span class="miner-price">$'+m.min_price.toFixed(2)+'/call</span>' : ''}
      </div>
    `).join('');
  } catch(e) {
    document.getElementById('miners-list').innerHTML = '<p style="color:var(--red);text-align:center;padding:20px">Failed to load miners</p>';
  }
}

loadSignals();
loadMiners();
setInterval(loadSignals, 30000);
</script>
</body>
</html>"""

HTML_RESPONSE = HTMLResponse(content=HTML_PAGE)

app.add_route("/", lambda r: HTML_RESPONSE, methods=["GET"])