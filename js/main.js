// Javascript for menu on mobile screen
const menuButton = document.querySelector(".hamburger-menu");
const menuItems = document.querySelector(".mobile-menu-items");

menuButton.addEventListener("click", () => {
    menuItems.classList.toggle("hidden");
});
