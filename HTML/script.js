function startCountdown() {
    // TARGET DATE: Feb 18, 2026 at 6:14 PM (18:14:00)
    const targetDate = new Date("February 18, 2026 18:14:00").getTime();

    const interval = setInterval(() => {
        const now = new Date().getTime();
        const distance = targetDate - now;

        // 1. If countdown is finished
        if (distance < 0) {
            clearInterval(interval);
            document.getElementById("countdown-ui").style.display = "none";
            document.getElementById("end-msg").style.display = "block";
            return;
        }

        // 2. Math Calculations
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // 3. String formatting (Ensuring we always have 2 digits, e.g. "05")
        const dStr = days.toString().padStart(2, '0');
        const hStr = hours.toString().padStart(2, '0');
        const mStr = minutes.toString().padStart(2, '0');
        const sStr = seconds.toString().padStart(2, '0');

        // 4. Update the specific boxes (Split Digits)
        
        // Days (Handle potential 3-digit days if necessary)
        // If days > 99, this grabs the last two digits. 
        // If you expect > 99 days, let me know and we can add a 3rd box!
        const d1Value = dStr.length > 2 ? dStr[dStr.length-2] : dStr[0];
        const d2Value = dStr[dStr.length-1];

        document.getElementById("d1").innerText = d1Value;
        document.getElementById("d2").innerText = d2Value;

        // Hours
        document.getElementById("h1").innerText = hStr[0];
        document.getElementById("h2").innerText = hStr[1];

        // Minutes
        document.getElementById("m1").innerText = mStr[0];
        document.getElementById("m2").innerText = mStr[1];

        // Seconds
        document.getElementById("s1").innerText = sStr[0];
        document.getElementById("s2").innerText = sStr[1];

    }, 1000);
}

// Start the engine
startCountdown();