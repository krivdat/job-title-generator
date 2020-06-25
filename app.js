// code to be added

let words = {};
const jobTitle = document.getElementById("job-title");
const generateBtn = document.querySelector(".generate-btn");

fetch("./words.json")
  .then(function (resp) {
    return resp.json();
  })
  .then(initialTitle);

function initialTitle(data) {
  words = data;
  generateBtn.addEventListener("click", genJobTitle);
  genJobTitle();
}

function genJobTitle() {
  let adj1 = Math.floor(Math.random() * words.adjective1.length);
  let adj2 = Math.floor(Math.random() * words.adjective2.length);
  let adj3 = Math.floor(Math.random() * words.adjective2.length);
  let pos = Math.floor(Math.random() * words.position.length);
  let adjective1 = words.adjective1[adj1];
  let adjective2 = words.adjective2[adj2];
  let adjective3 = words.adjective3[adj3];
  let position = words.position[pos];
  jobTitle.textContent = `${adjective1} ${adjective2} ${adjective3} ${position}`;
}
