window.addEventListener('load', () => {
  let executed = false; // Variable pour suivre si la fonction a déjà été exécutée

  setInterval(() => {
    // Vérifier si l'URL contient "product.template" et "kanban"
    if (window.location.href.includes("product.template") && window.location.href.includes("kanban")) {
      // Vérifier si la balise <span> contient le texte "Livre"
      const spanElement = document.querySelector('span.text-900');
      if (spanElement && spanElement.textContent === "Livre") {
        // Si les conditions sont remplies et que la fonction n'a pas encore été exécutée, exécuter la fonction et marquer comme exécutée
        if (!executed) {
          bootFlipster();
          executed = true;
        }
      }
    }
  }, 1000); // Répéter toutes les secondes

  function bootFlipster() {
    console.log("Chargement du flipster!");
    // Récupérer toutes les divs avec la classe "oe_kanban_global_click"
    const divs = document.querySelectorAll('.oe_kanban_global_click');

    // Stocker chaque div et son contenu dans un tableau
    const divContents = [];
    for (let i = 0; i < divs.length; i++) {
      divContents.push(divs[i].innerHTML);
    }

    // Vider le contenu de la div avec la classe "o_content"
    const contentDiv = document.querySelector('.o_content');
    contentDiv.innerHTML = '';

    // Créer une div avec la classe "flipster" et une liste non ordonnée à l'intérieur
    const flipsterDiv = document.createElement('div');
    flipsterDiv.classList.add('flipster');
    const ul = document.createElement('ul');

    // Ajouter chaque div stockée à l'intérieur des divs "flipster" sous forme d'éléments de liste
    for (let j = 0; j < divContents.length; j++) {
      const newDiv = document.createElement('div');
      //liste des class oe_kanban_card oe_kanban_global_click o_kanban_record
      newDiv.classList.add("oe_kanban_global_click");
      //newDiv.classList.add("oe_kanban_card");
      newDiv.classList.add("o_kanban_record");
      newDiv.classList.add("oe_kanban_global_click");
      newDiv.setAttribute("modifiers", "{}");
      newDiv.setAttribute("tabindex", "0");
      newDiv.setAttribute("role", "article");
      newDiv.innerHTML = divContents[j];
      const li = document.createElement('li');
      li.appendChild(newDiv);
      ul.appendChild(li);
    }

    // Ajouter la liste à la div "flipster" et la div "flipster" à la div "o_content"
    flipsterDiv.appendChild(ul);
    contentDiv.appendChild(flipsterDiv);

    // Initialisation du flipster
    $('.flipster').flipster();

  }
});
