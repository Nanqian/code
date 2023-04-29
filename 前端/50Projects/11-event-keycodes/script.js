window.addEventListener('keyup', (e) => {
  document.body.innerHTML = `
  <div class="wrapper">
    <small>event.key</small>
    ${e.key}
  </div>
  <div class="wrapper">
    <small>event.keyCode</small>
    ${e.keyCode}
  </div>
  <div class="wrapper">
    <small>event.code</small>
    ${e.code}
  </div>
  `;
});
