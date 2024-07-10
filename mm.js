const inputElement = document.getElementById("input");
const searchButton = document.getElementById("search-button");
const form = document.getElementById("input-wrapper");

function searchItem(e) {
  // 防止表單提交和頁面刷新
  e.preventDefault();
  const text = inputElement.value.trim().toLowerCase(); // 使用 trim() 去除首尾空白

  if (text === "") {
    alert("請輸入內容");
    return;
  }
}

// 監聽輸入框的輸入事件
inputElement.addEventListener("input", searchItem);

// 監聽表單的提交事件
form.addEventListener("submit", searchItem);
