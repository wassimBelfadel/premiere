function popUpUn(){
  window.alert('un événement clic sur UN a déclenché cette fenêtre')
}
function popUpDeux(){
  window.alert('un événement clic sur DEUX a déclenché cette fenêtre')
}


var un = document.querySelector("li:first-child")
un.addEventListener('click', popUpUn)

var deux = document.querySelector("li+li")
deux.addEventListener('click', popUpDeux)
