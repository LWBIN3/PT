document
  .getElementById("elementForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const symbolInput = document
      .getElementById("elementSymbol")
      .value.trim()
      .toLowerCase();
    const numberInput = document.getElementById("elementNumber").value.trim();
    const nameInput = document
      .getElementById("elementName")
      .value.trim()
      .toLowerCase();

    const elements = document.querySelectorAll(".mat.simple");
    elements.forEach((element) => {
      const symbol = element.dataset.element.toLowerCase();
      const number = element.dataset.number;
      const name = element.dataset.name.toLowerCase();

      if (
        symbol === symbolInput ||
        number === numberInput ||
        name === nameInput
      ) {
        element.style.display = "flex";
        element.scrollIntoView({ behavior: "smooth", block: "center" });
      } else {
        element.style.display = "none";
      }
    });

    // 清空输入框
    document.getElementById("elementSymbol").value = "";
    document.getElementById("elementNumber").value = "";
    document.getElementById("elementName").value = "";
  });

const elementInputs = document.querySelectorAll(
  "#elementSymbol, #elementNumber, #elementName"
);
elementInputs.forEach((input) => {
  input.addEventListener("input", function () {
    const symbolInput = document
      .getElementById("elementSymbol")
      .value.trim()
      .toLowerCase();
    const numberInput = document.getElementById("elementNumber").value.trim();
    const nameInput = document
      .getElementById("elementName")
      .value.trim()
      .toLowerCase();

    const elements = document.querySelectorAll(".mat.simple");
    elements.forEach((element) => {
      const symbol = element.dataset.element.toLowerCase();
      const number = element.dataset.number;
      const name = element.dataset.name.toLowerCase();

      if (
        symbol === symbolInput ||
        number === numberInput ||
        name === nameInput
      ) {
        if (input.id !== "elementSymbol") {
          document.getElementById("elementSymbol").value =
            element.dataset.element;
        }
        if (input.id !== "elementNumber") {
          document.getElementById("elementNumber").value =
            element.dataset.number;
        }
        if (input.id !== "elementName") {
          document.getElementById("elementName").value = element.dataset.name;
        }
      }
    });
  });
});
