window.onload = () => {
  const wd = document.querySelector('input[name="wd"]');
  const submit = document.querySelector('.btn');

  submit.addEventListener('click', () => {
    if (wd.value != '') {
      searchBox.style.width = '200px';
      document.querySelector('form').submit();
    }
  });
};
