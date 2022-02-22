let words = {};
const jobTitle = document.getElementById('job-title');

initWords().catch((error) => {
  console.error(error);
});

async function initWords() {
  const resp = await fetch('./words.json');
  words = await resp.json();
  const generateBtn = document.querySelector('.generate-btn');
  generateBtn.addEventListener('click', genJobTitle);
  genJobTitle();
  console.log('all done');
}

function genJobTitle() {
  const adj1 = Math.floor(Math.random() * words.adjective1.length);
  const adj2 = Math.floor(Math.random() * words.adjective2.length);
  const adj3 = Math.floor(Math.random() * words.adjective2.length);
  const pos = Math.floor(Math.random() * words.position.length);
  const adjective1 = words.adjective1[adj1];
  const adjective2 = words.adjective2[adj2];
  const adjective3 = words.adjective3[adj3];
  const position = words.position[pos];
  jobTitle.textContent = `${adjective1} ${adjective2} ${adjective3} ${position}`;
}
