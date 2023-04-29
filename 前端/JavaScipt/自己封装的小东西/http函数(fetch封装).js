async function http(obj) {
  let { method, url, params, data } = obj;
  let res;

  // get 和 delete 请求 有参数,处理参数
  if (params) {
    let str = new URLSearchParams(params).toString();
    url += '?' + str;
  }

  // post, put, patch 请求 有参数
  if (data) {
    res = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
    })
  } else {//其他情况
    res = await fetch(url);
  }

  return res.json();
}