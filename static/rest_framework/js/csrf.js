/*
  Bu dosya, AJAX isteklerinde CSRF (Cross-Site Request Forgery) koruması sağlamak için kullanılır.
  Django Rest Framework ile çalışan formlarda ve AJAX işlemlerinde, güvenlik amacıyla CSRF token'ının otomatik olarak gönderilmesini sağlar.
  Sadece aynı origin (kaynak) üzerinden yapılan ve CSRF koruması gerektiren HTTP isteklerinde token'ı ekler.
*/
// Belirtilen isimdeki çerezi (cookie) döndürür.
function getCookie(name) {
  var cookieValue = null;

  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');

   
   
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);

     // İlgili isimle başlayan çerezi bulursa değerini döndürür.
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
       
        break;
      }
    }
  }

  return cookieValue;
}
// CSRF koruması gerektirmeyen HTTP metodlarını kontrol eder (GET, HEAD, OPTIONS, TRACE).
function csrfSafeMethod(method) {
  // Bu HTTP metodları CSRF koruması gerektirmez.
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Verilen URL'nin aynı origin (kaynak) olup olmadığını kontrol eder.
function sameOrigin(url) {
  // URL'nin aynı origin olup olmadığını test eder.
  // URL göreli, şema göreli veya mutlak olabilir.
  var host = document.location.host; // host + port
  var protocol = document.location.protocol;
  var sr_origin = '//' + host;
  var origin = protocol + sr_origin;

   // Mutlak veya şema göreli URL'ler için aynı origin kontrolü
  return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
    //
    //  Diğer tüm göreli URL'ler de aynı origin kabul edilir.
    !(/^(\/\/|http:|https:).*/.test(url));
}

// Django tarafından sağlanan CSRF token'ı alınır.
var csrftoken = window.drf.csrfToken;

// Tüm AJAX istekleri için CSRF token'ı otomatik olarak eklenir.
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
     // Eğer istek CSRF koruması gerektiriyorsa ve aynı origin ise token eklenir.
    if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
      // Sadece aynı origin ve koruma gerektiren isteklerde token gönderilir.
      xhr.setRequestHeader(window.drf.csrfHeaderName, csrftoken);
    }
  }
});
