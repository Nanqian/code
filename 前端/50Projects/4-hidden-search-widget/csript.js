const searchBox = document.querySelector('.searchBox');
const text = searchBox.querySelector('input');
const btn = document.querySelector('.btn');
let flag = 0;

btn.addEventListener('click', () => {
  if (flag === 0) {
    flag = 1;
    searchBox.style.width = '200px';
    text.focus();
  } else if (flag === 1) {
    flag = 0;
    searchBox.style.width = '0';
  }
});
