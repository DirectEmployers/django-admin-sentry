$(document).ready(function () {
  $("li.row").click(function () {
    var model = this.getAttribute("model_id");
    var obj_id = this.getAttribute("obj_id");
    window.location.href = "/sawmill/activity?&model=" + model + "&obj=" + obj_id;
  });
  
  $("li.row").hover(
    function () {
      $("body").css("cursor", "pointer");
    },
    
    function () {
      $("body").css("cursor", "default");
    });

  $(".chartswitch").hover(
    function () {
      $("body").css("cursor", "pointer");
    },
    
    function () {
      $("body").css("cursor", "default");
    });
  
  $(".sidebar-module").delegate("select#id_content_type","change",function () {
    console.log(this.value);
    window.location.href = "/sawmill/activity?&model=" + this.value + "&obj=";
  });
});

