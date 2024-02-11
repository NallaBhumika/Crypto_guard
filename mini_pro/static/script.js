const downloadButton = document.getElementById("download-button");
downloadButton.addEventListener("click", () => {
    // Get the shift value from the input field
    const shiftValue = document.getElementById("shift-input").value;
    // Show alert notification
    alert("File download initiated!");
    // Send POST request to /encrypt endpoint
    fetch("/encrypt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ shift: shiftValue })
    })
    .then(response => {
        if (response.ok) {
            return response.blob(); // Convert response to blob
        }
        throw new Error("Network response was not ok.");
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "encrypted_file.txt";
        document.body.appendChild(a);
        a.click(); // Trigger click event on the link
        window.URL.revokeObjectURL(url);
    })
    .catch(error => console.error(error));
});
