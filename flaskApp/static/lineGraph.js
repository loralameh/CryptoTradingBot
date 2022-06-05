window.onload = function () {
  let data = [
    { Date: 1653782400000, Close: 0.9725 },
    { Date: 1653868800000, Close: 1.084 },
    { Date: 1653955200000, Close: 1.087 },
    { Date: 1654041600000, Close: 0.9818 },
    { Date: 1654128000000, Close: 1.036 },
    { Date: 1654214400000, Close: 0.9783 },
    { Date: 1654300800000, Close: 0.9807 },
  ];

  data.forEach((entry) => {
    (entry.Date = new Date(entry.Date)), (entry.Close = entry.Close);
  });

  const newdata = data.map(({ Date, Close }) => ({
    x: Date,
    y: Close,
  }));

  var chart = new CanvasJS.Chart('chartContainer', {
    title: {
      text: 'MANA coin Prices - per day',
    },
    data: [
      {
        type: 'line',

        dataPoints: newdata,
      },
    ],
  });

  chart.render();
};
