const questionInput = document.getElementById("questionInput");

async function sendMessage() {

    const chatContainer =
        document.getElementById("chatContainer");

    const input =
        questionInput.value.trim();

    if (!input) {
        return;
    }
    chatContainer.innerHTML += `
        <div class="user-message">
            ${input}
        </div>
    `;

    // Clear textbox
    questionInput.value = "";

    chatContainer.scrollTop =
        chatContainer.scrollHeight;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: input
        })
    });

    console.log("send successfully");

    const data = await response.json();

    // Show AI response
    chatContainer.innerHTML += `
        <div class="bot-message">
            ${marked.parse(data.answer)}
        </div>
    `;

    chatContainer.scrollTop =
        chatContainer.scrollHeight;
}

questionInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});


async function uploadFile()
{
    const file_input = document.getElementById("pdfUpload");

    const file = file_input.files[0];

    if (!file) {
        alert("Please select a PDF");
        return;
    }

    const formdata = new FormData();

    formdata.append("pdf",file);

    const response = await fetch('/upload',{
        method : "POST",
        body: formdata

    });

    const data = await response.json();

    document.getElementById("uploadedFile").innerHTML = `
        📄 ${data.filename}
    `;


}