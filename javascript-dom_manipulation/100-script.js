document.addEventListener("DOMContentLoaded", () => {
	const ul = document.querySelector("ul.my_list");
	const add_item = document.querySelector("#add_item");
	const remove_item = document.querySelector("#remove_item");
	const clear_list = document.querySelector("#clear_list");

	add_item.addEventListener("click", () => {
		const new_li = document.createElement("li")
		ul.append(new_li);
		new_li.innerText = "Item"
	});

	remove_item.addEventListener("click", () => {
		ul.lastElementChild.remove()
	});

	clear_list.addEventListener("click", () => {
		while (ul.firstChild) {
			ul.removeChild(ul.firstChild)
		}
	});
});
