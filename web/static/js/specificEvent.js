$(document).ready(function(){
    var el = $('.specific-description')[0].firstElementChild;
    var str = el.innerHTML;
    str = str.replace(/(?:\r\n|\r|\n)/g, '<br>');
    // console.log(str);
    el.innerHTML = str;
  });