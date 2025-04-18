document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("add-article-form");

    if (!form) {
        console.warn("Form not found, js issue");
        return;
    }

    console.log("Form found, attaching event listener");

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
        .then(response => {
            if (response.ok) {
                console.log("Article added via AJAX");
                window.location.reload(); // Later we'll swap this for table re-render
            } else {
                alert("Something went wrong.");
            }
        })
        .catch(error => {
            console.error("Fetch error:", error);
        });
    });
});
