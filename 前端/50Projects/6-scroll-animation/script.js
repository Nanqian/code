const boxes = document.querySelectorAll('.box');

window.addEventListener('scroll', showBox);

showBox();

function showBox() {
  const triggerBottom = (document.documentElement.clientHeight / 5) * 4;

  boxes.forEach((box) => {
    let boxTop = box.getBoundingClientRect().top;
    if (boxTop < triggerBottom) box.classList.add('show');
    else box.classList.remove('show');
  });
}
