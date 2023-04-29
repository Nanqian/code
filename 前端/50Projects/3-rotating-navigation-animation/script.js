const bar_header = document.querySelector('.bar-header');
const open = document.querySelector('#open');
const close = document.querySelector('#close');
const card = document.querySelector('.card');
const menu = document.querySelector('.menu');

open.addEventListener('click', () => {
  bar_header.style.transform = 'rotate(-90deg)';
  card.style.transform = 'rotate(-20deg)';
  menu.style.transform = 'translate(0)';
});
close.addEventListener('click', () => {
  bar_header.style.transform = 'rotate(0deg)';
  card.style.transform = 'rotate(0deg)';
  menu.style.transform = 'translate(-100%)';
});
