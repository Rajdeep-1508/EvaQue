console.clear();

const navBar = document.querySelector("nav");
const sections = [...document.querySelectorAll("section")];
const options = {
	root: null,
	threshold: 0,
	rootMargin: "-150px 0px 0px 0px",
};
const callback = function(entries) {
	entries.forEach(entry => {
		if (!entry.isIntersecting) {
			navBar.classList.add("nav-change");
		} else {
			navBar.classList.remove("nav-change");
		}
	});
}
const observer = new IntersectionObserver(callback, options);
observer.observe(sections[0])
