document.addEventListener("DOMContentLoaded", () => {
    const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
    const navLinks = document.querySelector(".nav-links");
    const header = document.querySelector(".site-header");
    const navItems = document.querySelectorAll(".nav-list a");
    const lightbox = document.getElementById("lightbox");

    const closeMenu = () => {
        if (!navLinks || !mobileMenuBtn) return;
        navLinks.classList.remove("open");
        document.body.classList.remove("nav-open");
        mobileMenuBtn.setAttribute("aria-expanded", "false");
        mobileMenuBtn.setAttribute("aria-label", "Open menu");
        mobileMenuBtn.querySelectorAll("span").forEach((span) => {
            span.style.transform = "none";
            span.style.opacity = "1";
        });
    };

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener("click", () => {
            const open = navLinks.classList.toggle("open");
            document.body.classList.toggle("nav-open", open);
            mobileMenuBtn.setAttribute("aria-expanded", String(open));
            mobileMenuBtn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
            const spans = mobileMenuBtn.querySelectorAll("span");
            spans[0].style.transform = open ? "rotate(45deg) translate(5px, 5px)" : "none";
            spans[1].style.opacity = open ? "0" : "1";
            spans[2].style.transform = open ? "rotate(-45deg) translate(6px, -6px)" : "none";
        });
    }

    navItems.forEach((item) => {
        item.addEventListener("click", closeMenu);
    });

    window.addEventListener("scroll", () => {
        if (header) header.classList.toggle("scrolled", window.scrollY > 40);
        let current = "home";
        document.querySelectorAll("main section[id]").forEach((section) => {
            if (window.scrollY >= section.offsetTop - 180) current = section.id;
        });
        navItems.forEach((item) => {
            const href = item.getAttribute("href") || "";
            item.classList.toggle("active", href === `#${current}` || href.endsWith(`#${current}`));
        });
    }, { passive: true });

    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", (event) => {
            const targetId = anchor.getAttribute("href");
            if (!targetId || targetId === "#") return;
            const target = document.querySelector(targetId);
            if (!target) return;
            event.preventDefault();
            closeMenu();
            const offset = target.getBoundingClientRect().top + window.pageYOffset - 90;
            window.scrollTo({ top: offset, behavior: "smooth" });
        });
    });

    if (lightbox) {
        const lightboxImg = lightbox.querySelector("img");
        const lightboxCaption = lightbox.querySelector("p");
        const closeLightbox = () => {
            lightbox.hidden = true;
            lightboxImg.src = "";
            lightboxImg.alt = "";
        };
        document.querySelectorAll(".gallery-item").forEach((item) => {
            item.addEventListener("click", () => {
                lightboxImg.src = item.dataset.src;
                lightboxImg.alt = item.querySelector("img").alt;
                lightboxCaption.textContent = item.dataset.caption || "";
                lightbox.hidden = false;
            });
        });
        lightbox.querySelector(".lightbox-close").addEventListener("click", closeLightbox);
        lightbox.addEventListener("click", (event) => {
            if (event.target === lightbox) closeLightbox();
        });
        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                if (!lightbox.hidden) closeLightbox();
                closeMenu();
            }
        });
    }

    initWizard();
});

function initWizard() {
    const form = document.getElementById("quote-form");
    if (!form || !form.classList.contains("wizard")) return;

    const steps = [...form.querySelectorAll(".wizard-step")];
    const dots = [...form.querySelectorAll("[data-step-dot]")];
    const brief = document.getElementById("brief-text");
    const errorBox = document.getElementById("form-error");
    let current = 1;

    const showStep = (n) => {
        current = n;
        steps.forEach((step) => {
            const active = Number(step.dataset.step) === n;
            step.hidden = !active;
            step.classList.toggle("is-active", active);
        });
        dots.forEach((dot) => {
            const value = Number(dot.dataset.stepDot);
            dot.classList.toggle("is-active", value === n);
            dot.classList.toggle("is-done", value < n);
        });
        updateBrief();
        updateConditional();
        const legend = steps[n - 1].querySelector("legend");
        if (legend) legend.focus?.();
        steps[n - 1].scrollIntoView({ block: "nearest", behavior: "smooth" });
    };

    const field = (name) => form.elements[name];

    const updateBrief = () => {
        if (!brief) return;
        const suburb = (field("location")?.value || "").trim();
        const service = form.querySelector('input[name="service"]:checked')?.value || "";
        const hours = field("hours")?.value || "";
        const date = field("start_date")?.value || "";
        if (!suburb && !service) {
            brief.textContent = "Pick a suburb and a service to start the brief.";
            return;
        }
        const bits = [];
        bits.push(service ? service : "Licensed security");
        bits.push(suburb ? `in ${suburb}` : "in your suburb");
        if (date) bits.push(`from ${date}`);
        if (hours) bits.push(`(${hours})`);
        bits.push("— SLED ML 000110094. Same-day reply on most briefs.");
        brief.textContent = bits.join(" ");
    };

    const updateConditional = () => {
        const service = form.querySelector('input[name="service"]:checked')?.value || "";
        form.querySelectorAll(".cond").forEach((row) => {
            const keys = (row.dataset.for || "").split(",");
            const match = keys.some((key) => service.toLowerCase().includes(key.trim().toLowerCase()));
            row.hidden = !match;
        });
    };

    const validateStep = (n) => {
        if (errorBox) {
            errorBox.hidden = true;
            errorBox.textContent = "";
        }
        if (n === 1 && !(field("location")?.value || "").trim()) {
            return "Tell us the suburb or site.";
        }
        if (n === 2 && !form.querySelector('input[name="service"]:checked')) {
            return "Pick the type of security you need.";
        }
        if (n === 3 && !(field("message")?.value || "").trim()) {
            return "Give us a one-line brief so we can roster the right people.";
        }
        if (n === 4) {
            if (!(field("name")?.value || "").trim()) return "We need a name.";
            if (!(field("phone")?.value || "").trim()) return "We need a phone number.";
            if (!(field("email")?.value || "").trim()) return "We need an email.";
        }
        return "";
    };

    form.querySelectorAll(".wizard-next").forEach((btn) => {
        btn.addEventListener("click", () => {
            const message = validateStep(current);
            if (message) {
                if (errorBox) {
                    errorBox.hidden = false;
                    errorBox.textContent = message;
                }
                return;
            }
            showStep(Math.min(4, current + 1));
        });
    });

    form.querySelectorAll(".wizard-back").forEach((btn) => {
        btn.addEventListener("click", () => showStep(Math.max(1, current - 1)));
    });

    form.addEventListener("input", updateBrief);
    form.addEventListener("change", () => {
        updateBrief();
        updateConditional();
    });

    form.addEventListener("submit", (event) => {
        const message = validateStep(4);
        if (message) {
            event.preventDefault();
            if (errorBox) {
                errorBox.hidden = false;
                errorBox.textContent = message;
            }
            showStep(4);
        }
    });

    showStep(1);
    updateConditional();
    updateBrief();
}
