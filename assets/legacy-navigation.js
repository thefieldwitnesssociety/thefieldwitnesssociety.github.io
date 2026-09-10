// Preserve links shared before the main sections became separate pages.
const previousSections = {
  '/#field-notes': '/field-notes/',
  '/#about': '/about/',
  '/#principles': '/about/#principles',
  '/#practice': '/about/#practice',
  '/about/#contact': '/contacts/',
};
function redirectPreviousSection() {
  const currentSection = window.location.pathname + window.location.hash;
  if (Object.hasOwn(previousSections, currentSection)) {
    window.location.replace(previousSections[currentSection]);
  }
}
window.addEventListener('hashchange', redirectPreviousSection);
redirectPreviousSection();
