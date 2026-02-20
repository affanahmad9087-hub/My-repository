function updateCountdown() {
    // 1. Set the target date (Ramadan 2026 is expected around Feb 18)
    const targetDate = new Date("February 18, 2026 00:00:00").getTime();
    const now = new Date().getTime();
    const gap = targetDate - now;

    // 2. Check if the time has reached zero
    if (gap <= 0) {
    const topSection = document.querySelector(".p1-container");
    if (topSection) topSection.style.display = "none";

    const endMsg = document.getElementById("end-msg");
    if (endMsg) endMsg.style.display = "block";

    document.body.classList.add("celebration-bg");

    return; 
}

    // 3. Math calculations for Days, Hours, Minutes, Seconds
    const second = 1000;
    const minute = second * 60;
    const hour = minute * 60;
    const day = hour * 24;

    const d = Math.floor(gap / day);
    const h = Math.floor((gap % day) / hour);
    const m = Math.floor((gap % hour) / minute);
    const s = Math.floor((gap % minute) / second);

    // 4. Helper to split numbers into two digits (e.g., 9 becomes "0" and "9")
    const format = (num) => String(num).padStart(2, '0').split('');

    // 5. Update the HTML elements
    const [d1, d2] = format(d);
    const [h1, h2] = format(h);
    const [m1, m2] = format(m);
    const [s1, s2] = format(s);

    document.getElementById("d1").innerText = d1;
    document.getElementById("d2").innerText = d2;
    document.getElementById("h1").innerText = h1;
    document.getElementById("h2").innerText = h2;
    document.getElementById("m1").innerText = m1;
    document.getElementById("m2").innerText = m2;
    document.getElementById("s1").innerText = s1;
    document.getElementById("s2").innerText = s2;
}

// Update every second
setInterval(updateCountdown, 1000);
updateCountdown(); // Run immediately on load