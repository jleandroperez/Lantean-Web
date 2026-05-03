(function () {
  var IMG_EXT = /\.(jpe?g|png|gif|webp|svg|bmp|avif)(\?|$)/i;
  var current = null;

  function open(src, alt) {
    close();

    var box = document.createElement('div');
    box.className = 'lightbox';

    var img = document.createElement('img');
    img.src = src;
    if (alt) img.alt = alt;

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'lightbox-close';
    btn.setAttribute('aria-label', 'Close');
    btn.textContent = '×';

    box.appendChild(img);
    box.appendChild(btn);
    document.body.appendChild(box);
    document.body.classList.add('lightbox-open');

    requestAnimationFrame(function () { box.classList.add('open'); });

    box.addEventListener('click', function () { close(); });
    img.addEventListener('click', function (e) { e.stopPropagation(); });
    btn.addEventListener('click', function (e) { e.stopPropagation(); close(); });

    current = box;
  }

  function close() {
    if (!current) return;
    var box = current;
    current = null;
    box.classList.remove('open');
    document.body.classList.remove('lightbox-open');
    setTimeout(function () { if (box.parentNode) box.parentNode.removeChild(box); }, 150);
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && current) close();
  });

  document.addEventListener('click', function (e) {
    var img = e.target.closest && e.target.closest('img');
    if (!img) return;
    if (!img.closest('.entry-content')) return;

    var anchor = img.closest('a');
    var src;
    if (anchor) {
      var href = anchor.getAttribute('href') || '';
      if (!IMG_EXT.test(href)) return;
      src = anchor.href;
    } else {
      src = img.currentSrc || img.src;
    }
    if (!src) return;
    e.preventDefault();
    open(src, img.alt);
  });
})();
