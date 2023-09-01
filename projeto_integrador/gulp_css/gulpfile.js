    const gulp = require('gulp');
    const sass = require('gulp-sass')(require('sass'));

    function compilaSass(){
        return gulp.src('./src/styles/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('./dist/styles'))
    }
    exports.default = gulp
    exports.watch = function(){
        gulp.watch('./src/styles/*.scss', gulp.series(compilaSass));
    }