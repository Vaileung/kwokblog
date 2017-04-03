/**
 * Created by kwok on 17-3-31.
 */
$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() != 0) {
            $("#toTop").fadeIn();
        } else {
            $("#toTop").fadeOut();
        }
    });
    $("body").append("<div id=\"toTop\" style=\"border:1px solid #fbfdfd;" +
        "background:#a4749d;" +
        "color:#e9eacb;" +
        "text-align:center;" +
        "padding:10px;" +
        "position:fixed;" +
        "bottom:20px;" +
        "right:10px;" +
        "cursor:pointer;" +
        "display:none;" +
        "font-family:verdana;" +
        "height:28px;" +
        "border-radius: 14px" +
        "font-size:22px;\">^</div>");
    $("#toTop").click(function () {
        $("body,html").animate({scrollTop: 0}, 800);
    });
});
