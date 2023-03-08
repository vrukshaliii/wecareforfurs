// Javascript for menu on mobile screen
const menuButton = document.querySelector(".hamburger-menu");
const menuItems = document.querySelector(".mobile-menu-items");

menuButton.addEventListener("click", () => {
	menuItems.classList.toggle("hidden");
});

$("form").on("change", ".file-upload-field", function () {
	$(this)
		.parent(".file-upload-wrapper")
		.attr(
			"data-text",
			$(this)
				.val()
				.replace(/.*(\/|\\)/, "")
		);
});
