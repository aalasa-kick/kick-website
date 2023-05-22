var player = document.getElementById("logoLottie");

player.addEventListener("ready", () => {
    LottieInteractivity.create({
        player: "#logoLottie",
        mode: "cursor",
        actions: [{ type: "hover", forceFlag: false }]
    });
});