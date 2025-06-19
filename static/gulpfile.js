/*
  Bu dosya, projenin derleme ve geliştirme süreçlerini otomatikleştirmek için Gulp görevlerini tanımlar.
  SCSS dosyalarını CSS'e derler, CSS'i minify eder, vendor dosyalarını yönetir ve geliştirme sırasında tarayıcıyı otomatik olarak yeniler.
  Projede, stil dosyalarının derlenmesi, otomatik prefix eklenmesi, canlı önizleme ve dağıtım işlemlerinin kolaylaştırılması için kullanılır.
*/


'use strict'
// Gerekli modüller yükleniyor
var gulp = require('gulp');
var browserSync = require('browser-sync').create(); // Canlı önizleme ve otomatik yenileme
var sass = require('gulp-sass'); // SCSS derleyici

var autoprefixer = require('gulp-autoprefixer'); // CSS için otomatik prefix ekleyici
var cssmin = require('gulp-cssmin') // CSS minify edici
var rename = require('gulp-rename'); // Dosya yeniden adlandırma aracı
var runSequence = require('run-sequence'); // Görevlerin sırayla çalıştırılmasını sağlar

// Yol ayarları tanımlanıyor
gulp.paths = { 
  dist: 'dist/', // Dağıtım klasörü
  
  src: 'src/', // Kaynak dosyaların bulunduğu klasör
  vendors: 'dist/vendors/' // Üçüncü parti kütüphanelerin bulunduğu klasör
};

var paths = gulp.paths; 
//Gulp görevleri için alt klasörler yükleniyor
require('require-dir')('./gulp-tasks');

// SCSS ve HTML dosyalarını izleyerek canlı sunucu başlatır
gulp.task('serve', ['sass'], function() {

  browserSync.init({
    server: ['./', './src']
  });

  gulp.watch(paths.src + 'scss/**/*.scss', ['sass']);
  gulp.watch(paths.src + '**/*.html').on('change', browserSync.reload);
  gulp.watch(paths.src + 'js/**/*.js').on('change', browserSync.reload);

});

// Sadece CSS, HTML ve JS dosyalarını izleyerek canlı sunucu başlatır (SCSS izlemez)
gulp.task('serve:lite', function() {

  browserSync.init({
    server: ['./', './src']
  });

  gulp.watch(paths.src + '**/*.css').on('change', browserSync.reload);
  gulp.watch(paths.src + '**/*.html').on('change', browserSync.reload);
  gulp.watch(paths.src + 'js/**/*.js').on('change', browserSync.reload);

});

// Derlenmiş dağıtım klasörünü sunar
gulp.task('serve:dist', function() {
  browserSync.init({
    server: ['./dist']
  });
});

// SCSS dosyalarını derler, autoprefix ekler, minify yapar ve çıktı olarak CSS üretir
gulp.task('sass', ['compile-vendors'], function() {
  return gulp.src(paths.src + '/scss/style.scss')
  .pipe(sass())
  .pipe(autoprefixer())
  .pipe(gulp.dest(paths.src + 'css'))
  .pipe(cssmin())
  .pipe(rename({suffix: '.min'}))
  .pipe(gulp.dest(paths.src + 'css'))
  .pipe(browserSync.stream());
});
// SCSS dosyalarını izleyip değişiklikte otomatik derler
gulp.task('sass:watch', function() {
  gulp.watch(paths.src + 'scss/**/*.scss', ['sass']);
});
// Varsayılan görev: geliştirme sunucusunu başlatır
gulp.task('default', ['serve']);
