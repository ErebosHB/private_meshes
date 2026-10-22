'use strict';
const $ = (selector) => document.querySelector(selector);
const escapeHTML = (value) => String(value ?? '').replace(/[&<>"']/g, (c) => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));
const state = { data: null, category: 'all', query: '', sort: 'id', pose: 'rest', detail: null, detailPose: 'rest' };
const number = (value) => Number(value).toLocaleString('en-US', { maximumFractionDigits: 3 });
const categoryFor = (obj) => state.data.categories.find((c) => c.key === obj.category);
const plural = (count, word) => `${count} ${word}${count === 1 ? '' : 's'}`;

function renderNavigation() {
  const entries = [{ key: 'all', code: 'ALL', title: 'All objects', count: state.data.objects.length }, ...state.data.categories];
  $('#categories').innerHTML = entries.map((c) => `<a class="nav-item" href="#${escapeHTML(c.key)}" ${state.category === c.key ? 'aria-current="page"' : ''}><span class="nav-code">${escapeHTML(c.code)}</span><span>${escapeHTML(c.title)}</span><span class="nav-count">${c.count}</span></a>`).join('');
  $('#category-select').innerHTML = entries.map((c) => `<option value="${escapeHTML(c.key)}">${escapeHTML(c.title)} (${c.count})</option>`).join('');
  $('#category-select').value = state.category;
}

function renderModels() {
  if (!state.data) return;
  const category = state.data.categories.find((c) => c.key === state.category);
  $('#library-title').textContent = category?.title ?? 'All objects';
  $('#category-description').textContent = category?.blurb ?? '';
  const terms = state.query.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  const models = state.data.objects.filter((obj) => {
    if (state.category !== 'all' && obj.category !== state.category) return false;
    const haystack = [obj.id, obj.name, obj.desc, categoryFor(obj).title, ...obj.joints.flatMap((j) => [j.name, j.type]), ...obj.frames.flatMap((f) => [f.name, f.purpose])].join(' ').toLocaleLowerCase();
    return terms.every((term) => haystack.includes(term));
  }).sort((a,b) => {
    if (state.sort === 'name') return a.name.localeCompare(b.name);
    if (state.sort === 'newest') return String(b.added ?? '').localeCompare(String(a.added ?? '')) || Number(b.id) - Number(a.id);
    if (state.sort === 'joints') return b.joints.length - a.joints.length || Number(a.id) - Number(b.id);
    return Number(a.id) - Number(b.id);
  });
  $('#result-count').textContent = `${models.length} of ${state.data.objects.length} objects`;
  $('#clear-search').hidden = !state.query;
  $('#empty').hidden = models.length !== 0;
  $('#models').innerHTML = models.map((obj) => `<article class="card">
    <button type="button" class="card-preview" data-object="${obj.id}" aria-label="View ${escapeHTML(obj.name)}"><img src="${escapeHTML(obj.url)}/renders/${state.pose}.webp" alt="${escapeHTML(obj.name)} in ${state.pose === 'rest' ? 'rest' : 'inspection'} pose" loading="lazy" width="520" height="400"><span class="object-id">№ ${obj.id}</span><span class="preview-arrow" aria-hidden="true">↗</span></button>
    <div class="card-copy"><p class="card-category">${escapeHTML(categoryFor(obj).title)}</p><h3><button class="title-button" type="button" data-object="${obj.id}">${escapeHTML(obj.name)}</button></h3><p class="card-desc">${escapeHTML(obj.desc)}</p><div class="card-meta"><span>${plural(obj.joints.length, 'joint')}</span><span>${plural(obj.frames.length, 'frame')}</span><a href="${escapeHTML(obj.download)}" download aria-label="Download ${escapeHTML(obj.name)} ZIP">ZIP ↓</a></div></div>
  </article>`).join('');
  $('#models').setAttribute('aria-busy', 'false');
}

function setPose(pose) {
  state.pose = pose;
  for (const value of ['rest', 'open']) $(`#pose-${value}`).setAttribute('aria-pressed', String(pose === value));
  renderModels();
}

function table(headings, rows) {
  if (!rows.length) return '<p>No moving joints.</p>';
  return `<div class="table-wrap"><table><thead><tr>${headings.map((h) => `<th scope="col">${escapeHTML(h)}</th>`).join('')}</tr></thead><tbody>${rows.map((row) => `<tr>${row.map((cell) => `<td>${escapeHTML(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}

function openDetail(obj) {
  state.detail = obj;
  state.detailPose = state.pose;
  document.title = `${obj.name} — Objects, Individually`;
  const joints = obj.joints.map((j) => [j.name, j.type, `${number(j.lower)} → ${number(j.upper)} ${j.type === 'prismatic' ? 'm' : 'rad'}`, number(j.inspect)]);
  const frames = obj.frames.map((f) => [f.name, String(f.purpose ?? '').replaceAll('_', ' ')]);
  $('#detail-body').innerHTML = `<div class="detail-top"><div class="detail-image"><img id="detail-preview" src="${escapeHTML(obj.url)}/renders/${state.detailPose}.webp" alt="${escapeHTML(obj.name)} in ${state.detailPose === 'rest' ? 'rest' : 'inspection'} pose"><div class="segmented" role="group" aria-label="Object preview pose"><button type="button" data-detail-pose="rest" aria-pressed="${state.detailPose === 'rest'}">Rest</button><button type="button" data-detail-pose="open" aria-pressed="${state.detailPose === 'open'}">Inspection</button></div></div><div class="detail-text"><p class="eyebrow">№ ${obj.id} / ${escapeHTML(categoryFor(obj).title)}</p><h2 id="detail-title">${escapeHTML(obj.name)}</h2><p>${escapeHTML(obj.desc)}</p><dl class="detail-meta"><div><dt>Dimensions · X × Y × Z</dt><dd>${obj.size.map(number).join(' × ')} m</dd></div><div><dt>Added to collection</dt><dd>${escapeHTML(obj.added ?? '—')}</dd></div><div><dt>Moving joints</dt><dd>${obj.joints.length}</dd></div><div><dt>Interaction frames</dt><dd>${obj.frames.length}</dd></div></dl><div class="detail-links"><a class="primary" href="${escapeHTML(obj.download)}" download>Download object ZIP ↓</a><a href="${escapeHTML(obj.url)}/README.md">Read README ↗</a></div><p>Includes the Blender model, URDF, GLB meshes, previews, and original notices.</p></div></div><div class="detail-bottom"><h3>Moving parts</h3>${table(['Joint', 'Type', 'Limits', 'Inspection'], joints)}<details><summary>Interaction frames (${obj.frames.length})</summary>${table(['Frame', 'Purpose'], frames)}</details><details><summary>Model notice</summary><pre id="model-notice">Loading notice…</pre><a href="NOTICE.md">Repository licence scope ↗</a></details></div>`;
  if (!$('#details').open) $('#details').showModal();
  $('#details').scrollTop = 0;
  fetch(`${obj.url}/NOTICE.md`).then((r) => { if (!r.ok) throw Error(); return r.text(); }).then((text) => { if (state.detail === obj) $('#model-notice').textContent = text; }).catch(() => { if (state.detail === obj) $('#model-notice').textContent = 'Could not load the notice. It is included in the object ZIP.'; });
}

function route() {
  if (!state.data) return;
  const hash = location.hash.slice(1);
  if (hash.startsWith('object/')) {
    const obj = state.data.objects.find((o) => o.id === hash.slice(7));
    if (obj) { openDetail(obj); return; }
  }
  if ($('#details').open) $('#details').close();
  state.detail = null;
  document.title = 'Objects, Individually — Model library';
  state.category = state.data.categories.some((c) => c.key === hash) ? hash : 'all';
  renderNavigation();
  renderModels();
}

function closeDetails() {
  if (!$('#details').open) return;
  $('#details').close();
  state.detail = null;
  history.replaceState(null, '', `#${state.category}`);
  document.title = 'Objects, Individually — Model library';
}

$('#search').addEventListener('input', (event) => { state.query = event.target.value; renderModels(); });
$('#clear-search').addEventListener('click', () => { $('#search').value = ''; state.query = ''; renderModels(); $('#search').focus(); });
$('#sort').addEventListener('change', (event) => { state.sort = event.target.value; renderModels(); });
$('#category-select').addEventListener('change', (event) => { location.hash = event.target.value; });
$('#pose-rest').addEventListener('click', () => setPose('rest'));
$('#pose-open').addEventListener('click', () => setPose('open'));
$('#models').addEventListener('click', (event) => { const target = event.target.closest('[data-object]'); if (target) location.hash = `object/${target.dataset.object}`; });
$('#reset').addEventListener('click', () => { $('#search').value = ''; state.query = ''; location.hash = 'all'; route(); });
$('#close-details').addEventListener('click', closeDetails);
$('#details').addEventListener('cancel', (event) => { event.preventDefault(); closeDetails(); });
$('#details').addEventListener('click', (event) => {
  if (event.target === $('#details')) { const r = $('#details').getBoundingClientRect(); if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) closeDetails(); }
  const target = event.target.closest('[data-detail-pose]');
  if (!target) return;
  state.detailPose = target.dataset.detailPose;
  $('#detail-preview').src = `${state.detail.url}/renders/${state.detailPose}.webp`;
  $('#detail-preview').alt = `${state.detail.name} in ${state.detailPose === 'rest' ? 'rest' : 'inspection'} pose`;
  document.querySelectorAll('[data-detail-pose]').forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.detailPose === state.detailPose)));
});

fetch('catalogue.json').then((r) => { if (!r.ok) throw Error('Catalogue unavailable'); return r.json(); }).then((data) => {
  state.data = data;
  $('#stats').innerHTML = [['objects', 'independent models'], ['categories', 'categories'], ['joints', 'moving joints'], ['frames', 'interaction frames']].map(([key, label]) => `<div class="stat"><strong>${number(data.stats[key])}</strong><span>${label}</span></div>`).join('');
  window.addEventListener('hashchange', route);
  route();
}).catch(() => {
  $('#models').setAttribute('aria-busy', 'false');
  $('#models').innerHTML = '<p>The collection could not be loaded. Please reload, or <a href="https://github.com/sunava/private_meshes/tree/main/objects/articulated">browse it on GitHub</a>.</p>';
});
