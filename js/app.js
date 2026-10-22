const $app = document.getElementById('app');
const state = { states: {}, topics: [], candidates: [], updated: '' };
const ATLAS = 'https://cdn.jsdelivr.net/npm/us-atlas@3/states-albers-10m.json';

const PARTY = { D: 'Democratic', R: 'Republican', I: 'Independent', G: 'Green' };
const partyKey = p => (['D', 'R', 'I', 'G'].includes(p) ? p : 'O');
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const initials = n => n.split(/\s+/).map(w => w[0]).slice(0, 2).join('');

/* ---------- citations ---------- */
function sup(c, key) {
  const i = c.sources.findIndex(s => s.key === key);
  if (i < 0) return '';
  const s = c.sources[i];
  return `<sup><a class="cite" href="${esc(s.url)}" target="_blank" rel="noopener" title="${esc(s.title)}" aria-label="Source ${i + 1}: ${esc(s.title)}">${i + 1}</a></sup>`;
}
function segment(c, seg) {
  const s = c.sources.find(x => x.key === seg.s);
  if (seg.q != null) {
    return `<a class="quote" href="${esc(s.url)}" target="_blank" rel="noopener">“${esc(seg.q)}”</a>${sup(c, seg.s)}`;
  }
  return esc(seg.t) + (seg.s ? sup(c, seg.s) : '');
}
const paragraphs = (c, paras) => paras.map(p => `<p>${p.map(seg => segment(c, seg)).join('')}</p>`).join('');

/* ---------- photo ---------- */
function photo(c) {
  const fb = `<div class="photo" aria-hidden="true">${esc(initials(c.name))}</div>`;
  if (!c.photo) return fb;
  return `<img class="photo" src="${esc(c.photo)}" alt="Photo of ${esc(c.name)}" loading="lazy" referrerpolicy="no-referrer"
    onerror="this.outerHTML='${fb.replace(/'/g, '&#39;').replace(/"/g, '&quot;')}'">`;
}

const hasData = code => state.candidates.some(c => c.state === code);

/* ---------- home / map ---------- */
async function homeView() {
  const links = Object.entries(state.states)
    .map(([k, v]) => `<li><a href="#/state/${k}" class="${hasData(k) ? 'has-data' : ''}">${esc(v)}${hasData(k) ? ' <span class="pill">candidates available</span>' : ''}</a></li>`).join('');
  $app.innerHTML = `
    <h1>Who's on your ballot?</h1>
    <p class="muted">Click your state on the map to see the candidates running in the 2026 U.S. midterm elections.
    Connecticut is available now; other states are being added.</p>
    <div class="map-wrap">
      <div id="map" aria-label="Map of the United States. Choose a state."></div>
      <div id="tip" class="tip" hidden></div>
    </div>
    <div class="legend"><span><i class="sw avail"></i> Red outline: candidates available</span><span><i class="sw"></i> Other states: coming soon</span></div>
    <h2 class="race">Or choose from the list</h2>
    <ul class="state-grid">${links}</ul>`;
  drawMap().catch(() => { document.getElementById('map').innerHTML = '<p class="muted">The map could not be loaded. Use the state list below.</p>'; });
}

async function drawMap() {
  const topo = await fetch(ATLAS).then(r => r.json());
  const feats = topojson.feature(topo, topo.objects.states).features;
  const nameToCode = Object.fromEntries(Object.entries(state.states).map(([k, v]) => [v, k]));
  // us-atlas "albers" files are already projected to a 975x610 plane, so paths are plain polylines.
  const ring = r => 'M' + r.map(p => p[0].toFixed(1) + ',' + p[1].toFixed(1)).join('L') + 'Z';
  const geom = g => g.type === 'Polygon' ? g.coordinates.map(ring).join('') : g.type === 'MultiPolygon' ? g.coordinates.map(pl => pl.map(ring).join('')).join('')
    : g.type === 'LineString' ? 'M' + g.coordinates.map(p => p.join(',')).join('L') : g.type === 'MultiLineString' ? g.coordinates.map(l => 'M' + l.map(p => p.join(',')).join('L')).join('') : '';
  const path = geom;
  const tip = document.getElementById('tip');
  const wrap = document.querySelector('.map-wrap');
  const paths = feats.map(f => {
    const code = nameToCode[f.properties.name];
    if (!code) return '';
    const cls = hasData(code) ? 'st avail' : 'st soon';
    return `<a href="#/state/${code}" aria-label="${esc(f.properties.name)}"><path class="${cls}" data-code="${code}" d="${path(f.geometry)}"/></a>`;
  }).join('');
  const mesh = `<path class="borders" d="${path(topojson.mesh(topo, topo.objects.states, (a, b) => a !== b))}"/>`;
  document.getElementById('map').innerHTML = `<svg viewBox="0 0 975 610" role="group" aria-label="United States map">${paths}${mesh}</svg>`;
  const show = (e, code) => {
    const r = wrap.getBoundingClientRect();
    tip.hidden = false;
    tip.textContent = state.states[code] + (hasData(code) ? '' : ' (coming soon)');
    tip.style.left = (e.clientX - r.left + 12) + 'px';
    tip.style.top = (e.clientY - r.top + 12) + 'px';
  };
  wrap.querySelectorAll('path.st').forEach(p => {
    p.addEventListener('mousemove', e => show(e, p.dataset.code));
    p.addEventListener('mouseleave', () => { tip.hidden = true; });
  });
  wrap.querySelectorAll('svg a').forEach(a => {
    a.addEventListener('focus', () => {
      const p = a.querySelector('path');
      const r = p.getBoundingClientRect(), w = wrap.getBoundingClientRect();
      tip.hidden = false; tip.textContent = state.states[p.dataset.code];
      tip.style.left = (r.left - w.left + r.width / 2) + 'px'; tip.style.top = (r.top - w.top) + 'px';
    });
    a.addEventListener('blur', () => { tip.hidden = true; });
  });
}

/* ---------- state ---------- */
const OFFICE_RANK = { 'Governor': 0, 'Lieutenant Governor': 1, 'Secretary of the State': 2, 'Treasurer': 3, 'Comptroller': 4, 'Attorney General': 5, 'U.S. House': 6, 'State Senate': 7 };
const raceLabel = c => c.district ? `${c.office} — District ${c.district}` : c.office;
const raceOrder = c => OFFICE_RANK[c.office] * 100 + Number(c.district || 0);

const GROUPS = [
  ['statewide', 'Statewide offices', c => OFFICE_RANK[c.office] <= 5],
  ['house', 'U.S. House', c => c.office === 'U.S. House'],
  ['senate', 'State Senate', c => c.office === 'State Senate'],
];

function card(c) {
  return `
    <a class="card" href="#/candidate/${esc(c.id)}">
      ${photo(c)}
      <div class="body"><div class="name">${esc(c.name)}</div>
      <span class="party ${partyKey(c.party)}">${esc(PARTY[c.party] || c.party)}</span>${c.incumbent ? ' <span class="inc">Incumbent</span>' : ''}</div>
    </a>`;
}

function stateView(code) {
  const name = state.states[code];
  if (!name) return notFound();
  const list = state.candidates.filter(c => c.state === code).sort((a, b) => raceOrder(a) - raceOrder(b));
  if (!list.length) {
    $app.innerHTML = `<p><a href="#/">← Back to the map</a></p><h1>${esc(name)}</h1><div class="empty">Candidate information for ${esc(name)} hasn't been added yet. Connecticut is available now.</div>`;
    return;
  }
  const sections = GROUPS.map(([id, label, pred]) => {
    const cs = list.filter(pred);
    if (!cs.length) return null;
    const races = {};
    cs.forEach(c => (races[raceLabel(c)] ||= []).push(c));
    const body = Object.entries(races).map(([r, rc]) => `
      <h3 class="race" id="${id}-${esc(r.replace(/\D+/g, '') || r)}">${esc(r)}</h3>
      <div class="cards">${rc.map(card).join('')}</div>`).join('');
    return { id, label, body, races: Object.keys(races) };
  }).filter(Boolean);
  const senate = sections.find(s => s.id === 'senate');
  const districtPicker = senate ? `
    <label class="picker-l" for="dist">Find your State Senate district</label>
    <select id="dist"><option value="">Choose a district…</option>${senate.races.map(r => `<option value="${esc(r.replace(/\D+/g, ''))}">${esc(r.replace('State Senate — ', ''))}</option>`).join('')}</select>` : '';
  $app.innerHTML = `
    <p><a href="#/">← Back to the map</a></p>
    <h1>${esc(name)}</h1>
    <nav class="jump" aria-label="Jump to">${sections.map(s => `<a href="#" data-j="${s.id}">${esc(s.label)}</a>`).join('')}</nav>
    ${districtPicker}
    ${sections.map(s => `<section id="sec-${s.id}"><h2 class="sec">${esc(s.label)}</h2>${s.body}</section>`).join('')}
    <p class="muted small">Candidates are those listed for the November 3, 2026 general election as of ${esc(state.updated)}, per ${[...new Set(list.map(c => c.sources[0]))].map(s => `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a>`).join(' and ')}. Write-in candidates are not included.</p>`;
  $app.querySelectorAll('[data-j]').forEach(a => a.onclick = e => { e.preventDefault(); document.getElementById('sec-' + a.dataset.j).scrollIntoView({ behavior: 'smooth' }); });
  const dist = document.getElementById('dist');
  if (dist) dist.onchange = () => { const el = document.getElementById('senate-' + dist.value); if (el) el.scrollIntoView({ behavior: 'smooth' }); };
}

/* ---------- candidate ---------- */
const fmtDate = iso => iso.length === 4 ? iso
  : new Date(iso + (iso.length === 7 ? '-01' : '') + 'T00:00:00Z').toLocaleDateString('en-US', iso.length === 7 ? { year: 'numeric', month: 'long', timeZone: 'UTC' } : { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });

function photoCaption(c) {
  if (!c.photo) return '<p class="muted small credit">No photo was available on the candidate’s website or public social pages.</p>';
  const from = `<a href="${esc(c.photoSource)}" target="_blank" rel="noopener">${esc(c.photoKind || 'the candidate’s website')}</a>`;
  let when;
  if (c.photoYear) when = c.photoBasis === 'taken' ? `Taken in ${esc(c.photoYear)}.` : `Posted ${esc(c.photoYear)}; date taken not published.`;
  else when = 'Year taken not published.';
  return `<p class="muted small credit">Photo from ${from}. ${when}${c.photoLowRes ? ' Low-resolution profile image.' : ''}</p>`;
}

function saidBlock(c, items, heading) {
  if (!items.length) return '';
  return `<h4 class="said-h">${esc(heading)}</h4>` + items.map(it => `
    <div class="said">
      <span class="when">${esc(fmtDate(it.when))}</span>
      <p>${it.seg.map(g => segment(c, g)).join('')}</p>
      <span class="ctx"><b>Context:</b> ${esc(it.context)}</span>
    </div>`).join('');
}

function topicPanel(c, topic) {
  const t = c.topics[topic.id];
  const rev = c.reviewed;
  let html = `<div class="topic-panel"><h3>${esc(topic.label)}</h3>`;
  if (c.unreviewed && !(t.paras && t.paras.length) && !t.said.length && !(t.plan && t.plan.length)) {
    return html + `<p class="nosite">Not yet reviewed: this candidate’s positions on ${esc(topic.label.toLowerCase())} have not been researched for this site yet.${c.website ? ` Their own website is the best source: <a href="${esc(c.website)}" target="_blank" rel="noopener">${esc(c.website)}</a>.` : ' No campaign website was listed on their Ballotpedia profile.'}</p></div>`;
  }

  html += '<h4 class="sec-h">Their position</h4>';
  if (t.paras && t.paras.length) html += paragraphs(c, t.paras);
  else html += c.noWebsite
    ? '<p class="nosite">No campaign website was found for this candidate, so there is no information on this topic from a candidate website.</p>'
    : `<p class="nosite">No information on this topic was found on this candidate’s website.${rev ? sup(c, rev) : ''}</p>`;

  html += `<div class="plan"><h4 class="sec-h plan-h">Plan of action</h4>`;
  html += t.plan && t.plan.length
    ? paragraphs(c, t.plan)
    : `<p class="muted">No specific plan on this topic was found in the sources reviewed.${rev ? sup(c, rev) : ''}</p>`;
  html += '</div>';

  const heading = t.paras && t.paras.length ? 'Other statements from the past five years' : 'What they have said elsewhere (past five years)';
  if (t.said.length) html += saidBlock(c, t.said, heading);
  else if (!(t.paras && t.paras.length)) html += '<p class="muted small">No direct statements on this topic from the past five years were found in the sources reviewed.</p>';
  return html + '</div>';
}

function online(c) {
  const chips = [];
  if (c.website) chips.push(`<a class="chip web" href="${esc(c.website)}" target="_blank" rel="noopener">Website</a>`);
  (c.links || []).forEach(l => chips.push(`<a class="chip" href="${esc(l.url)}" target="_blank" rel="noopener" aria-label="${esc(c.name)} on ${esc(l.platform)}">${esc(l.platform)}</a>`));
  if (!chips.length) return '<p class="muted small">No campaign website or social media accounts were listed on their Ballotpedia profile.</p>';
  return `<div class="online" aria-label="Find ${esc(c.name)} online"><span class="online-l">Find them online:</span>${chips.join('')}</div>
    <p class="muted small">Links come from the candidate’s own website and their Ballotpedia profile; they open external sites.</p>`;
}

function candidateView(id, topicId) {
  const c = state.candidates.find(x => x.id === id);
  if (!c) return notFound();
  const topics = state.topics.filter(t => c.topics[t.id]);
  const topic = topics.find(t => t.id === topicId);
  const panel = topic ? topicPanel(c, topic) : '<p class="muted">Select a topic to see what this candidate has said.</p>';
  const noInfo = c.noInfo
    ? '<div class="empty">No campaign website or published policy statements were found for this candidate as of ' + esc(c.accessed) + '. This page will be updated if they become available.</div>' : '';
  const siteNote = c.siteNote ? `<p class="muted small">${esc(c.siteNote)}</p>` : '';
  $app.innerHTML = `
    <p><a href="#/state/${esc(c.state)}">← ${esc(state.states[c.state])} candidates</a></p>
    <div class="profile">
      <div>${photo(c)}${photoCaption(c)}</div>
      <div>
        <h1>${esc(c.name)}</h1>
        <span class="party ${partyKey(c.party)}">${esc(c.ticket)}</span>${sup(c, 'ballot')}
        <p class="muted">${esc(raceLabel(c))}</p>
        ${paragraphs(c, c.overview)}
        ${online(c)}
        ${siteNote}
      </div>
    </div>
    ${noInfo}
    ${c.unreviewed ? `<div class="unrev"><b>Profile in progress.</b> This page confirms who is running and links to their website; their positions and plans have not been reviewed yet.</div>` : ''}
    <h2>Where they stand</h2>
    <div class="topics" role="group" aria-label="Topics">
      ${topics.map(x => `<button class="${c.topics[x.id].gap && !c.unreviewed ? 'noweb' : ''}" aria-pressed="${x.id === topicId}" data-t="${x.id}">${esc(x.label)}</button>`).join('')}
    </div>
    ${c.unreviewed ? '' : '<p class="muted small">Dashed buttons: nothing on this topic on the candidate’s own website; the page shows other sourced statements instead.</p>'}
    ${panel}
    <h2 class="sources-h">Sources</h2>
    <ol class="sources">${c.sources.map(s => `<li><a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.title)}</a> <span class="muted">(accessed ${esc(c.accessed)})</span></li>`).join('')}</ol>`;
  $app.querySelectorAll('[data-t]').forEach(b => b.onclick = () => { location.hash = `#/candidate/${id}/${b.dataset.t}`; });
}

function notFound() {
  $app.innerHTML = '<div class="empty">Page not found. <a href="#/">Back to the map</a></div>';
}

function route() {
  const [, page, a, b] = location.hash.split('/');
  if (page === 'state') stateView(a);
  else if (page === 'candidate') candidateView(a, b);
  else homeView();
  if (!b) window.scrollTo(0, 0);
}

async function init() {
  const [s, t, c] = await Promise.all(['states', 'topics', 'candidates'].map(f => fetch(`data/${f}.json`).then(r => r.json())));
  Object.assign(state, { states: s, topics: t, candidates: c.candidates, updated: c.updated });
  window.addEventListener('hashchange', route);
  route();
}
init().catch(() => { $app.innerHTML = '<div class="empty">Could not load data. Serve this folder over HTTP (e.g. <code>python3 -m http.server</code>).</div>'; });
