document.addEventListener("DOMContentLoaded", (event) => {
    gsap.registerPlugin(ScrollTrigger);

    // Snappier Hero Animation
    gsap.fromTo(".gs-hero", 
        { y: 30, opacity: 0 }, 
        { y: 0, opacity: 1, duration: 1, stagger: 0.15, ease: "power3.out" }
    );

    // Optimized Scroll Reveal (Less lag, triggers sooner)
    const revealElements = document.querySelectorAll(".gs-reveal");
    
    revealElements.forEach((el) => {
        gsap.fromTo(el,
            { y: 40, opacity: 0 },
            {
                y: 0,
                opacity: 1,
                duration: 0.7,
                ease: "power2.out",
                scrollTrigger: {
                    trigger: el,
                    start: "top 90%", // Triggers earlier so you don't wait
                    toggleActions: "play none none reverse"
                }
            }
        );
    });
});