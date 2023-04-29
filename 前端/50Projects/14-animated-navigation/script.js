const box = document.querySelector('#box');
const closeBtn = document.querySelector('#close')

closeBtn.onclick = () => {
  box.classList.toggle('active');
}