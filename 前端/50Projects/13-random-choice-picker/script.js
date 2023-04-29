const tagBox = document.getElementById('tagBox');
const textarea = document.getElementById('textarea');

textarea.focus();

textarea.addEventListener('keyup', (e) => {
  if (e.key === 'Enter') {
    textarea.value = '';
    randomSelect();
    return;
  }

  let txt = textarea.value;
  let tagList = txt.split(',').filter(tag => tag.trim() != '');
  tagBox.innerHTML = '';
  tagList.forEach(function (tag) {
    let newTag = document.createElement('span');
    newTag.className = 'tag';
    newTag.innerHTML = tag;

    tagBox.appendChild(newTag);
  })
})

function randomSelect() {
  const items = document.querySelectorAll('.tag');
  let times = 30;
  let timer = setInterval(() => {
    if (times == 0) clearInterval(timer);
    document.querySelector('.bingo').classList.remove('bingo');
    items[Math.floor(Math.random() * items.length)].classList.add('bingo');
    times--;
  }, 100)
  items[Math.floor(Math.random() * items.length)].classList.add('bingo');
}
