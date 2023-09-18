document.addEventListener("DOMContentLoaded", () => {
	const btn_translate = document.querySelector("#btn_translate");
	const select = document.querySelector("select");
	const hello = document.querySelector("#hello");
	let url = "";

	base_url = "https://hellosalut.stefanbohacek.dev/";
	
	select.addEventListener("change", () => {
		selectedOption = select.options[select.selectedIndex];
		url = base_url + "?lang=" + selectedOption.value;
	});

	btn_translate.addEventListener("click", () => {
		fetch(url)
			.then(response => {
				return response.json();
			})
			.then(data => {
				hello.innerText = data.hello;
			});
	});
});
