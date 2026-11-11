const players = [...document.querySelectorAll('video')];

// Keep each film's place, while preventing overlapping audio.
for (const player of players) {
  player.addEventListener('play', () => {
    for (const other of players) if (other !== player) other.pause();
  });
}

for (const bookmark of document.querySelectorAll('[data-seek]')) {
  bookmark.addEventListener('click', event => {
    event.preventDefault();
    const player = document.getElementById(bookmark.dataset.player);
    const seek = () => {
      player.currentTime = Number(bookmark.dataset.seek);
      player.play().catch(() => {});
    };
    if (player.readyState >= 1) seek();
    else {
      player.addEventListener('loadedmetadata', seek, { once: true });
      player.load();
    }
    player.scrollIntoView({ block: 'center' });
  });
}

for (const button of document.querySelectorAll('[data-copy]')) {
  button.addEventListener('click', async () => {
    const source = document.getElementById(button.dataset.copy);
    const status = document.getElementById(button.dataset.status);
    try {
      await navigator.clipboard.writeText(source.value);
      status.textContent = button.dataset.success || 'Copied.';
    } catch {
      source.hidden = false;
      source.focus();
      source.select();
      status.textContent = 'Text selected. Use your usual copy command.';
    }
  });
}
