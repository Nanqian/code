window.onload = () => {
  const btns = document.querySelectorAll('.faq button');

  btns.forEach(btn => {
    btn.addEventListener('click', function () {
      btn.classList.toggle('icon-xiala');
      btn.classList.toggle('icon-close-circle-fill');
      btn.parentElement.classList.toggle('show');
    })
  })
}