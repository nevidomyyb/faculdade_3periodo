    const gulp = require('gulp');
    const sass = require('gulp-sass')(require('sass'));

    function compilaSass(){
        return gulp.src('./editor_main/src/styles/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('./main_site/static/main_site/css/'))
    }
    exports.default = gulp
    exports.watch = function(){
        gulp.watch('./editor_main/src/styles/*.scss', gulp.series(compilaSass));
    }