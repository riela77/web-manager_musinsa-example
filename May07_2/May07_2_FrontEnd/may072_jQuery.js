function connectMachineRegEvent() {
    $("button").click(function () {
        var c = $("#colorInput").val();
        var s = $("#statusInput").val();

        var url = "http://195.168.9.201:5698/machine.reg?color=" + c + "&status=" + s;
        $.getJSON(url, function (json) {
            alert(json.result);
            getMachineData();
        });

        $("input").val("");
        $("textarea").val("");
    });
}

function getMachineData() {
    $.getJSON("http://195.168.9.201:5698/machine.get", function (json) {
        $("ul").empty();
        $.each(json, function(i, m){
            var br1 = $("<br>");
            var br2 = $("<br>");
            var li = $("<li><li>").append(m.color, br1, m.status, br2, m.checkDate);
            $("ul").append(li);
        });
        $("ul").listview("refresh");
    });
}

$(function () {
    connectMachineRegEvent();
    getMachineData();
});