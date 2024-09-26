//제이쿼리 선언
$(function(){

  $("#searchBtn").click(function(){
    alert("검색버튼 클릭");
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({
      url:surl,
      type:"get",
      data:"",
      dataType:"json",
      success:function(data){
        alert("성공");
        console.log(data);
        let datalist = data.response.body.items.item;
        var data = "";
        for(var i=0;i<10;i++){
          data += `<tr id='${datalist[i].galContentId}' >`;
          data += `<td class='num'>${datalist[i].galContentId}</td>`;
          data += `<td>${datalist[i].galTitle}</td>`;
          data += `<td>${datalist[i].galPhotographer}</td>`;
          data += `<td>${datalist[i].galModifiedtime}</td>`;
          data += `<td><img src="${datalist[i].galWebImageUrl}"></td>`;
          data += "</tr>";

        }
        document.getElementById("tbody").innerHTML = data;



      },
      error:function(){
        alert("실패");
      }
  
    });//ajax
  });//searchBtn



});//제이쿼리