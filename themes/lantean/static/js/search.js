(function () {
  var input = document.getElementById('search-input');
  var results = document.getElementById('search-results');
  if (!input || !results) return;
  var fuse = null;
  fetch('/index.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      fuse = new Fuse(data, { keys: ['title', 'content'], threshold: 0.35, minMatchCharLength: 2, ignoreLocation: true });
    });
  input.addEventListener('input', function () {
    var q = input.value.trim();
    results.innerHTML = '';
    if (q.length < 2 || !fuse) return;
    fuse.search(q).slice(0, 8).forEach(function (hit) {
      var a = document.createElement('a');
      a.href = hit.item.url;
      a.textContent = hit.item.title;
      results.appendChild(a);
    });
  });
  document.addEventListener('click', function (e) {
    if (!input.contains(e.target) && !results.contains(e.target)) results.innerHTML = '';
  });
}());
