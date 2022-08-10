// https://velog.io/@seong-dodo/자바스크립트-라이브러리-없이-무한-스크롤-구현하기
const debounce = (event, delay) => {
  let timeoutId = null;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(event.bind(null, ...args), delay);
  };
};

// 게시글의 Quill JSON 데이터 가져오기
function getContent(id) {
  $.getJSON({
    url: "/board/api/" + id,
    success: function (result) {
      quill.setContents(result.content.ops);
      $(".quill-content-" + id).html(quill.root.innerHTML);
    },
  });
}

// 태그 통계 차트
function drawBarChart(result, tagList) {
  let keys = [];
  let values = [];
  for (let [key, value] of Object.entries(tagList)) {
    keys.push(key);
    values.push(value);
  }
  return new Chart(document.getElementById("bar-chart-" + result.next.substring(result.next.indexOf("=") + 1)), {
    type: "bar",
    data: {
      labels: keys,
      datasets: [
        {
          label: "Tag 빈도",
          // backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
          data: values,
        },
      ],
    },
    options: {
      responsive: false,
      legend: { display: false },
      title: {
        display: true,
        text: "<#> Tag 통계",
      },
    },
  });
}

const getTagCount = (result) => {
  let tagList = {};

  result.results.forEach((data) => {
    if (data.tags == null) {
      return;
    }
    data.tags.forEach((element, index, array) => {
      if (Object.keys(tagList).length <= 0) {
        tagList[element] = 1;
        return;
      }
      for (let [key, value] of Object.entries(tagList)) {
        if (key == element) {
          tagList[key] = Number(value) + 1;
        } else {
          tagList[element] = 1;
        }
      }
    });
  });
  return tagList;
};
