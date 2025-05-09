function connectProductRegEvent(){
    $("button").click(function(){
        var c=$("#p_idInput").val();
        var s=$("#p_nameInput").val();
        
        var url="http://195.168.9.208:9999/product.reg?p_id=" + c + "&p_name=" + s;
        $.getJSON(url,function(json){
            alert(json.result);
            getProductData();
        });
        $("input").val("");
        $("textarea").val("");
        
    });
}

function getProductData() {
    $.getJSON("http://195.168.9.208:9999/product.get", function(json) {
        $("#product-list").empty(); // 이제 특정 <ul>만 비움
        $.each(json, function(i, m) {
            var br1 = $("<br>");
            var br2 = $("<br>");
            var li = $("<li></li>").append(m.p_id, br1, m.p_name, br2);
            $("#product-list").append(li);
        });
        $ul.listview();           // listview 초기화
        $ul.listview("refresh");  // 이후에 refresh
    });
}

$(document).ready(function() {
    $("#regProductRN").click(function() {
        alert("snffla");
        var c = $("#IDInput").val();
        var f = $("#nameInput").val();
        var s = $("#brand_idInput").val();
        var a = $("#category_idInput").val();
        var b = $("#priceInput").val();
        var d = $("#p_imageInput").val();
        var e = $("#p_locationInput").val();
        
        var url = "http://195.168.9.208:9999/product.reg" +
            "?p_id=" + c +
            "?p_name=" + f+
            "&p_brand_id=" + s +
            "&p_category_id=" + a +
            "&p_price=" + b +
            "&p_image=" + d +
            "&p_location=" + e;
        
        alert("요청 URL: " + url);
        $.getJSON(url, function(json) {
            alert(json.result);
        });
    });
});

