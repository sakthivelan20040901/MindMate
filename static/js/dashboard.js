const button = document.getElementById("generateBtn");

button.addEventListener("click", async () => {

    const body = {

        name: document.getElementById("name").value,

        mood: document.getElementById("mood").value,

        goal: document.getElementById("goal").value,

        interest: document.getElementById("interest").value

    };

    try {

        // ===========================
        // Generate AI Newsletter
        // ===========================

        const newsletterResponse = await fetch("/newsletter", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(body)

        });

        const newsletter = await newsletterResponse.json();

        document.getElementById("greeting").innerText =
            newsletter.greeting || "-";

        document.getElementById("motivation").innerText =
            newsletter.motivation || "-";

        document.getElementById("productivity_tip").innerText =
            newsletter.productivity_tip || "-";

        document.getElementById("wellness_tip").innerText =
            newsletter.wellness_tip || "-";

        document.getElementById("quote").innerText =
            newsletter.quote || "-";

        document.getElementById("closing").innerText =
            newsletter.closing || "-";


        // ===========================
        // Get AI Recommended Videos
        // ===========================

        const youtubeResponse = await fetch("/youtube", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(body)

        });

        const videos = await youtubeResponse.json();

        let html = "";

        videos.forEach(video => {

            html += `

            <div class="video-card">

                <img src="${video.thumbnail}" alt="${video.title}">

                <div class="video-info">

                    <h3>${video.title}</h3>

                    <p>${video.channel}</p>

                    <a href="${video.url}"
                       target="_blank">

                        ▶ Watch Video

                    </a>

                </div>

            </div>

            `;

        });

        document.getElementById("videos").innerHTML = html;

    }

    catch (error) {

        console.error(error);

        alert("Something went wrong.");

    }

});

