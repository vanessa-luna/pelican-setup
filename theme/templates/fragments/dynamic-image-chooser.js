    <script type="text/javascript">
      function gh(s) { return parseInt(s.replace(/.+x/, '')) }
      var imageSizes = [{% for name, dim in THUMBNAIL_SIZES.iteritems() %}{name:"{{name}}", h:gh("{{dim}}")}{% if not loop.last %}, {% endif %}{% endfor %}]
      imageSizes.sort(function(a,b) {return (a.h > b.h) ? -1 : ((b.h > a.h) ? 1 : 0);} );

      function imgUrlByHeight(filename, h) {
        var chosenSize = imageSizes[0]; //start at smallest size
        for (var i = 0; i < imageSizes.length; i++){ // redo smallest to calculate abs
          var curSize = imageSizes[i];
          curSize.abs = Math.abs(h - curSize.h);
          if (curSize.abs <= chosenSize.abs) chosenSize = curSize;
        }
        return "url({{ SITEURL }}/{{ THUMBNAIL_DIR}}/" + chosenSize.name + "/" + filename;
      }
    </script>
