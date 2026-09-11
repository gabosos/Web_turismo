const form = document.querySelector('#contact-form');
if (form) {
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const status = form.querySelector('.form-status');
        const submitButton = form.querySelector('button');
        submitButton.disabled = true;
        status.textContent = 'Enviando...';
        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(Object.fromEntries(new FormData(form))),
            });
            const result = await response.json();
            if (!response.ok) throw new Error(result.error);
            form.reset();
            status.textContent = result.message;
        } catch (error) {
            status.textContent = error.message || 'No pudimos enviar tu consulta.';
        } finally {
            submitButton.disabled = false;
        }
    });
}

const navBars = document.querySelectorAll('.section-nav');
const updateScrollState = () => navBars.forEach((bar) => bar.classList.toggle('is-scrolled', window.scrollY > 12));
window.addEventListener('scroll', updateScrollState, { passive: true });
updateScrollState();

const revealItems = document.querySelectorAll('.hero-copy, .hero-placeholder, .popular-card, .destination-row, .mission, .contact-grid');
revealItems.forEach((item) => item.classList.add('reveal-target'));
if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
        if (entry.isIntersecting) entry.target.classList.add('is-visible');
    }), { threshold: 0.12 });
    revealItems.forEach((item) => observer.observe(item));
} else {
    revealItems.forEach((item) => item.classList.add('is-visible'));
}
