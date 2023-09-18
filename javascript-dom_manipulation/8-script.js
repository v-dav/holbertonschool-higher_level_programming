document.addEventListener("DOMContentLoaded", () => {
	const hello = document.querySelector("#hello");
	
	fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
		.then(result => {
			return result.json();
		})
		.then(data => {
			hello.innerText = data.hello;
		});
});
