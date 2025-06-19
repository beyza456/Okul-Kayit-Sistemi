/*
  Bu dosya, Django Rest Framework arayüzünde kullanıcı deneyimini artırmak için çeşitli arayüz işlevleri sağlar.
  JSON kodlarını vurgular, Bootstrap tooltip ve sekme (tab) davranışlarını yönetir, kullanıcı sekme tercihlerini çerezde saklar
  ve hata modallarını otomatik olarak gösterir.
*/

$(document).ready(function() {
  // JSON highlighting: Sayfadaki JSON kodlarını okunabilir ve renklendirilmiş şekilde gösterir.
  prettyPrint();

   // Bootstrap tooltips: .js-tooltip sınıfına sahip öğelerde gecikmeli tooltip gösterimini etkinleştirir.
  $('.js-tooltip').tooltip({
  
    delay: 1000,
    container: 'body'
  });

  // Sekme tıklamalarında, ilk sekme aktifse .tabbable kapsayıcısına özel bir sınıf ekler.
  $('a[data-toggle="tab"]:first').on('shown', function(e) {
   
    $(e.target).parents('.tabbable').addClass('first-tab-active');
  });

 // İlk sekme dışında bir sekme aktifse, .tabbable kapsayıcısından özel sınıfı kaldırır.
  $('a[data-toggle="tab"]:not(:first)').on('shown', function(e) {
    $(e.target).parents('.tabbable').removeClass('first-tab-active');
  });

  // Sekme tıklandığında, kullanıcının sekme tercihinin adını çerezde saklar.
  $('a[data-toggle="tab"]').click(function() {
    document.cookie = "tabstyle=" + this.name + "; path=/";
  });

   // Sayfa yüklendiğinde, çerezde kayıtlı sekme tercihi varsa o sekmeyi gösterir.
  // Yoksa varsayılan olarak ilk sekmeyi gösterir.
  var selectedTab = null;
  var selectedTabName = getCookie('tabstyle');

  if (selectedTabName) {
    // Güvenlik için sekme adında sadece harf ve tire karakterlerine izin verilir.
    selectedTabName = selectedTabName.replace(/[^a-z-]/g, '');
  }

  if (selectedTabName) {
    selectedTab = $('.form-switcher a[name=' + selectedTabName + ']');
  }

  if (selectedTab && selectedTab.length > 0) {
    // Kayıtlı sekme tercihi varsa onu göster.
    selectedTab.tab('show');
  } else {
    // Kayıtlı tercih yoksa ilk sekmeyi göster.
    $('.form-switcher a:first').tab('show');
  }

// Sayfa tamamen yüklendiğinde varsa hata modalını otomatik olarak gösterir.
  $(window).on('load', function() {
    $('#errorModal').modal('show');
  });

});
