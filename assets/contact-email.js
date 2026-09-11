/* Compose locally. No request, analytics or storage receives the form contents. */
(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;
  const message = document.getElementById('contact-message');
  const name = document.getElementById('contact-name');
  const status = document.getElementById('contact-status');

  message.addEventListener('input', () => {
    message.setCustomValidity('');
    status.textContent = '';
  });

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!message.value.trim()) {
      message.setCustomValidity('Please write a message.');
      message.reportValidity();
      return;
    }
    if (!form.reportValidity()) return;
    const signature = name.value.trim();
    const body = message.value.trim() + (signature ? '\n\n' + signature : '');
    const url = 'mailto:thefieldwitnesssociety@gmail.com'
      + '?subject=' + encodeURIComponent('Enquiry — The Field Witness Society')
      + '&body=' + encodeURIComponent(body.replace(/\r?\n/g, '\r\n'));
    status.textContent = 'Your email app should open. Your message has not been sent by this website. If no app opens, use your usual email service and copy the message above.';
    // Keep all fields intact: opening a mail handler does not confirm delivery.
    window.location.assign(url);
  });
})();
