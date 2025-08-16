const dialog = document.getElementById("addPostDialog");
const addPostBtn = document.getElementById("addPostBtn");
const cancel = document.getElementById("cancel");
const formPost = document.getElementById("form-post");

// Ouvre la boîte en mode modal
addPostBtn.addEventListener("click", () => dialog.showModal());

// Ferme après soumission
formPost.addEventListener("submit", () => dialog.close());

// Ferme au clic sur "Annuler"
cancel.addEventListener("click", () => dialog.close());