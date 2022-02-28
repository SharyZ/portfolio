(function () {
  const menuBtn = document.getElementById('menu-btn');
  const menu = document.getElementById('menu');
  const loader = document.getElementById('loader');

  const preloadImages = (selector = 'img') => new Promise((resolve) => {
    imagesLoaded(document.querySelectorAll(selector), {
      background: true,
    }, resolve);
  });

  Promise.all([preloadImages()]).then(() => {
    setTimeout(() => {
      loader.style.display = 'none';
    }, 1000);
  });

  menuBtn.addEventListener('click', function (e) {
    menu.classList.toggle('hidden');
  });
})();
