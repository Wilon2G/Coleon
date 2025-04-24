document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("add-article-form");
    const table = document.getElementById("collection_table");
    if (!table) {
        console.warn("Table not found, js issue");
        return;
    }
    if (!form) {
        console.warn("Form not found, js issue");
        return;
    }

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        console.log("Intercepted form submit");

        fetch("", {
            method: "POST",
            headers: {
                "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value,
                "Accept": "application/json"
            },
            body: new FormData(form)
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === "success" && data.new_article) {
                    table.querySelector("tbody").insertAdjacentHTML("beforeend", data.new_article);
                }
            })
            .catch(error => {
                console.error("Fetch error:", error);
            });
    })
});
