// https://velog.io/@seong-dodo/자바스크립트-라이브러리-없이-무한-스크롤-구현하기
const debounce = (event, delay) => {
  let timeoutId = null;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(event.bind(null, ...args), delay);
  };
};
