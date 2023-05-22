const languageElements = document.querySelectorAll('[data-language]');

languageElements.forEach((element) => {
  element.addEventListener('click', () => {
    const language = element.dataset.language;
    switchLanguage(language);
  });
});

function switchLanguage(language) {
  const url = window.location.href;
  const languageParamRegex = /\/(en|ru)\//;
  const hasLanguageParam = languageParamRegex.test(url);
  let newUrl;

  if (hasLanguageParam) {
    newUrl = url.replace(languageParamRegex, `/${language}/`);
  } else {
    const hasQueryParams = url.includes('?');
    const separator = hasQueryParams ? '&' : '?';
    newUrl = `${url}${separator}${languageParamRegex.test(url) ? '' : `/${language}/`}`;
  }

  window.location.href = newUrl;
}


