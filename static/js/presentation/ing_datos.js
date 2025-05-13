window.addEventListener('load', () => {
    document
    .querySelectorAll('#limpieza .flip-card')
    .forEach(card => {
        const front = card.querySelector('.flip-card-front');
        const back  = card.querySelector('.flip-card-back');
        const h = Math.max(front.scrollHeight, back.scrollHeight);
        card.style.minHeight = h + 'px';
        card.querySelector('.flip-card-inner').style.minHeight = h + 'px';
    });
});
  