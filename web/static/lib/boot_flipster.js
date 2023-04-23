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

    // Filtrage des éléments récupérés pour ne garder que les images (nouvelle version)
    for (let k=0; k<divContents.length; k++) {
      let chaine = divContents[k];
      let deb = chaine.indexOf("<img");
      let fin = chaine.indexOf(">", deb);
      let portion = chaine.substring(deb, fin);
      // Redimensionnement des images
      portion = portion + 'style = "max-height:175px;width:auto;">'
      divContents[k] = portion;
    }

    // Créer une div avec la classe "flipster" et une liste non ordonnée à l'intérieur
    const flipsterDiv = document.createElement('div');
    flipsterDiv.classList.add('flipster');
    flipsterDiv.style.maxHeight = "205px";
    flipsterDiv.style.marginTop = "10px";
    flipsterDiv.style.overflowY = 'hidden';
    const ul = document.createElement('ul');

    // Ajouter chaque div stockée à l'intérieur des divs "flipster" sous forme d'éléments de liste
    for (let j = 0; j < divContents.length; j++) {
      const newDiv = document.createElement('div');
      newDiv.innerHTML = divContents[j];
      const li = document.createElement('li');
      li.appendChild(newDiv);
      ul.appendChild(li);
    }

    // Ajouter la liste à la div "flipster" et la div "flipster" à la div "o_content"
    flipsterDiv.appendChild(ul);

    // Ajout de la div flipster avant la div class="o_kanban_view"
    divKanbanView = document.querySelector(".o_kanban_view");
    divOContent = document.querySelector(".o_content");

    divOContent.insertBefore(flipsterDiv, divKanbanView);

    // Initialisation du flipster
    $('.flipster').flipster({
      autoplay: 3000,
      loop: true,
      spacing: -0.6
    });

  }
});
