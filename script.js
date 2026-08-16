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
        mobileMenuBtn.classList.remove("is-open");
    };

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener("click", () => {
            const open = navLinks.classList.toggle("open");
            document.body.classList.toggle("nav-open", open);
            mobileMenuBtn.setAttribute("aria-expanded", String(open));
            mobileMenuBtn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
            mobileMenuBtn.classList.toggle("is-open", open);
        });
    }

    navItems.forEach((item) => {
        item.addEventListener("click", closeMenu);
    });
    navLinks?.querySelectorAll(".nav-actions a")?.forEach((btn) => {
        btn.addEventListener("click", closeMenu);
    });

    const subToggles = document.querySelectorAll(".nav-sub-toggle");
    const closeSubs = () => {
        document.querySelectorAll(".has-sub.is-open").forEach((item) => {
            item.classList.remove("is-open");
            item.querySelector(".nav-sub-toggle")?.setAttribute("aria-expanded", "false");
        });
    };
    subToggles.forEach((btn) => {
        btn.addEventListener("click", (event) => {
            event.preventDefault();
            event.stopPropagation();
            const item = btn.closest(".has-sub");
            const open = !item.classList.contains("is-open");
            closeSubs();
            item.classList.toggle("is-open", open);
            btn.setAttribute("aria-expanded", String(open));
        });
    });
    document.addEventListener("click", (event) => {
        if (!event.target.closest(".has-sub")) closeSubs();
    });

    const sections = [...document.querySelectorAll("main section[id]")];
    let sectionTops = [];
    const measureSections = () => {
        sectionTops = sections.map((section) => ({
            id: section.id,
            top: section.offsetTop
        }));
    };
    measureSections();
    window.addEventListener("resize", measureSections, { passive: true });
    let ticking = false;
    const onScroll = () => {
        const y = window.scrollY;
        if (header) header.classList.toggle("scrolled", y > 40);
        let current = "home";
        for (const section of sectionTops) {
            if (y >= section.top - 180) current = section.id;
        }
        navItems.forEach((item) => {
            const href = item.getAttribute("href") || "";
            item.classList.toggle("active", href === `#${current}` || href.endsWith(`#${current}`));
        });
        ticking = false;
    };
    window.addEventListener("scroll", () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(onScroll);
    }, { passive: true });

    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", (event) => {
            const targetId = anchor.getAttribute("href");
            if (!targetId || targetId === "#") return;
            const target = document.querySelector(targetId);
            if (!target) return;
            event.preventDefault();
            closeMenu();
            const headerH = header ? header.offsetHeight : 72;
            const offset = target.getBoundingClientRect().top + window.pageYOffset - headerH - 8;
            window.scrollTo({ top: offset, behavior: "smooth" });
        });
    });

    if (lightbox) {
        const lightboxImg = lightbox.querySelector("img");
        const lightboxCaption = lightbox.querySelector("p");
        const closeBtn = lightbox.querySelector(".lightbox-close");
        const closeLightbox = () => {
            lightbox.hidden = true;
            document.body.classList.remove("lightbox-open");
            lightboxImg.src = "";
            lightboxImg.alt = "";
        };
        document.querySelectorAll(".gallery-item").forEach((item) => {
            item.addEventListener("click", () => {
                lightboxImg.src = item.dataset.src;
                lightboxImg.alt = item.querySelector("img")?.alt || "";
                lightboxCaption.textContent = item.dataset.caption || "";
                lightbox.hidden = false;
                document.body.classList.add("lightbox-open");
                closeBtn?.focus();
            });
        });
        closeBtn?.addEventListener("click", closeLightbox);
        lightbox.addEventListener("click", (event) => {
            if (event.target === lightbox) closeLightbox();
        });
        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                if (!lightbox.hidden) closeLightbox();
                closeMenu();
                closeSubs();
            }
        });
    } else {
        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                closeMenu();
                closeSubs();
            }
        });
    }

    initWizard();
    initReveals();
    initCountUp();
});

function initReveals() {
    const items = document.querySelectorAll(".reveal");
    if (!items.length) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        items.forEach((el) => el.classList.add("is-in"));
        return;
    }
    const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
        });
    }, { threshold: 0.14, rootMargin: "0px 0px -8% 0px" });
    items.forEach((el) => io.observe(el));
}

function initCountUp() {
    const nums = document.querySelectorAll("[data-count]");
    if (!nums.length) return;
    const run = (el) => {
        const end = Number(el.dataset.count);
        if (!end) return;
        const suffix = el.dataset.suffix || "";
        const start = performance.now();
        const tick = (now) => {
            const t = Math.min(1, (now - start) / 900);
            const eased = 1 - Math.pow(1 - t, 3);
            el.textContent = Math.round(end * eased) + suffix;
            if (t < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
    };
    const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            run(entry.target);
            io.unobserve(entry.target);
        });
    }, { threshold: 0.6 });
    nums.forEach((el) => io.observe(el));
}

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
    };

    const goTo = (n) => {
        showStep(n);
        const headerH = document.querySelector(".site-header")?.offsetHeight || 72;
        const top = form.getBoundingClientRect().top + window.pageYOffset - headerH - 12;
        window.scrollTo({ top, behavior: "smooth" });
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
            const email = (field("email")?.value || "").trim();
            if (!email) return "We need an email.";
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return "That email does not look right.";
        }
        return "";
    };

    const showError = (message) => {
        if (!errorBox) return;
        errorBox.hidden = !message;
        errorBox.textContent = message || "";
    };

    form.querySelectorAll(".wizard-next").forEach((btn) => {
        btn.addEventListener("click", () => {
            const message = validateStep(current);
            if (message) {
                showError(message);
                return;
            }
            showError("");
            goTo(Math.min(4, current + 1));
        });
    });

    form.querySelectorAll(".wizard-back").forEach((btn) => {
        btn.addEventListener("click", () => {
            showError("");
            goTo(Math.max(1, current - 1));
        });
    });

    dots.forEach((dot) => {
        dot.addEventListener("click", () => {
            const target = Number(dot.dataset.stepDot);
            if (target < current) {
                showError("");
                goTo(target);
            }
        });
    });

    form.addEventListener("keydown", (event) => {
        if (event.key !== "Enter") return;
        const tag = (event.target.tagName || "").toLowerCase();
        if (tag === "textarea" || tag === "button") return;
        event.preventDefault();
        if (current < 4) {
            const message = validateStep(current);
            if (message) {
                showError(message);
                return;
            }
            showError("");
            goTo(current + 1);
        }
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
