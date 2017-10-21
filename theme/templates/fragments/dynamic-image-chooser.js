    <script type="text/javascript">
      // array of possible images sizes built off config filename
      var imageSizes = [];
      {% for name, dim in THUMBNAIL_SIZES.iteritems() %}
      imageSizes[ {{ loop.index-1 }} ] = { name: "{{name}}", size:"{{ dim }}", width: parseInt("{{dim}}".replace(/x.+/, '')), height: parseInt("{{dim}}".replace(/.+x/, '')) }
      {% endfor %}
      // sorted largest to smallest so if two sizes match abs, it choses the smaller
      imageSizes.sort(function(a,b) {return (a.height > b.height) ? -1 : ((b.height > a.height) ? 1 : 0);} );

      function imgUrlByHeight(filename, height) {
        var chosenSize = imageSizes[0]; //start at smallest size
        for (var i = 0; i < imageSizes.length; i++){ // redo smallest to calculate abs
          var curSize = imageSizes[i];
          curSize.abs = Math.abs(height - curSize.height);
          if (curSize.abs <= chosenSize.abs) chosenSize = curSize;
        }
        return "url({{ SITEURL }}/{{ THUMBNAIL_DIR}}/" + chosenSize.name + "/" + filename;
      }
    </script>
