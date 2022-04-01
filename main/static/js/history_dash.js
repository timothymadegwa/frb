if (document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
} else{
    ready()
}

function ready(){
    let lender1 = 3564;
    let lender2 = 783;
    let lender3 = 8392;
    let lender4 = 988;
    let total = lender1 + lender2 + lender3 + lender4;
    var xValues = ["Lender 1", "Lender 2", "Lender 3", "Lender 4"];
    var yBar = [lender1, lender2, lender3, lender4];
    var yDoughnut = [lender1/total, lender2/total, lender3/total, lender4/total].map(function(x) { return x * 100; })
    var colors = ["black", "red","green","orange"];

    new Chart("bar", {
    type: "bar",
    data: {
        label: "Monetary values of services on S-BOB",
        labels: xValues,
        datasets: [{
        backgroundColor: colors,
        data: yBar
        }]
    },
    options: {
        legend: {display: true},
        title: {
        display: true,
        text: "Monetary values of services on S-BOB"
        }
    }
    });
    new Chart("doughnut", {
        type: "doughnut",
        data: {
            label: "Monetary values of services on S-BOB",
            labels: xValues,
            datasets: [{
            backgroundColor: colors,
            data: yDoughnut
            }]
        },
        options: {
            legend: {display: true},
            title: {
            display: true,
            text: "Distribution of funds as a Percentage"
            }
        }
        });

}