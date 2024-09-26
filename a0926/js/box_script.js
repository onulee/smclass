//제이쿼리 선언
let num=0;
let num2 = 0;
$(function(){

  //우측버튼
  $("#right").click(function(){
    //alert("우측버튼클릭");
    if(num>=900){
      alert("오른쪽 끝에 도달했습니다. 우측 이동은 불가합니다.");
      return false;
    }
    $("#box").stop();
    num += 100;
    num2 += 360;
    $("#box").animate({
      left:num,"rotate":num2+"deg"
    },1000);
  });

  //좌측버튼
  $("#left").click(function(){
    //alert("좌측버튼클릭");
    if(num<=0){
      alert("왼쪽 끝에 도달했습니다. 좌측 이동은 불가합니다.");
      return false;
    }
    $("#box").stop();
    num -= 100;
    num2 -= 360;
    $("#box").animate({
      left:num,"rotate":num2+"deg"
    },1000);
  });


});//제이쿼리