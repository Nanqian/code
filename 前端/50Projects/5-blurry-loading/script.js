const loading_text = document.querySelector('.loading-text');
const bg = document.querySelector('.bg');
let n = 0;

let timer = setInterval(function () {
  if (n < 100) {
    n++;
    loading_text.innerHTML = `${n}%`;
    bg.style.filter = `blur(${(100 - n) / 5}px)`;
  } else {
    document.body.removeChild(loading_text);
    clearInterval(timer);
  }
}, 20);
