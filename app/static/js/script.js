async function sendMessage()
    {
      const questionInput = document.getElementById("questionInput").value;
      
      const chatContainer = document.getElementById("chatContainer");

      chatContainer.innerHTML +=  `
        <div class="user-message">
            ${questionInput}
        </div>
      `;

      const response = await fetch("/chat",{
      method: "POST",
      headers:{
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        question:questionInput
        })
      });

      console.log("send secussefuly");

      data = await response.json()

      chatContainer.innerHTML +=  `
        <div class="bot-message">
            ${data.answer}
        </div>
      `;
      document.getElementById("questionInput").value = "";

}